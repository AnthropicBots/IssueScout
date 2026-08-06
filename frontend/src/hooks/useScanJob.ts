import { useCallback, useEffect, useRef, useState } from "react";

import {
  cancelScanJob,
  createScanJob,
  getScanJobResult,
  getScanJobStatus,
} from "../api/scan";

import type {
  ScanJobStatus,
  ScanResult,
} from "../types/api";

const TERMINAL_STATUSES: ScanJobStatus[] = [
  "completed",
  "failed",
  "cancelled",
];

const POLL_INTERVAL_MS = 1500;

interface UseScanJobState {
  jobId: string | null;
  status: ScanJobStatus | null;
  progress: number;
  processedIssues: number;
  totalIssues: number;
  data: ScanResult | null;
  error: Error | null;
  isRunning: boolean;
}

const INITIAL_STATE: UseScanJobState = {
  jobId: null,
  status: null,
  progress: 0,
  processedIssues: 0,
  totalIssues: 0,
  data: null,
  error: null,
  isRunning: false,
};

/**
 * Drives the backend's async scan-job flow end to end:
 *
 *   POST /scan/{owner}/{repo}       -> job_id
 *   GET  /scan/jobs/{job_id}        -> poll until terminal status
 *   GET  /scan/jobs/{job_id}/result -> ScanResult
 *
 * Unlike `useRepositoryScan` (which calls the synchronous endpoint and
 * blocks until the whole scan finishes with no progress feedback), this
 * hook exposes live `progress` / `processedIssues` / `totalIssues` values
 * you can feed straight into `LoadingState`.
 */
export function useScanJob() {
  const [state, setState] = useState<UseScanJobState>(INITIAL_STATE);

  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const clearPoll = useCallback(() => {
    if (pollRef.current !== null) {
      clearInterval(pollRef.current);
      pollRef.current = null;
    }
  }, []);

  useEffect(() => clearPoll, [clearPoll]);

  const start = useCallback(
    async (owner: string, repository: string) => {
      clearPoll();

      setState({
        ...INITIAL_STATE,
        isRunning: true,
      });

      try {
        const job = await createScanJob(owner, repository);

        setState((prev) => ({
          ...prev,
          jobId: job.job_id,
          status: job.status,
        }));

        pollRef.current = setInterval(async () => {
          try {
            const jobId = job.job_id;

            const statusResponse = await getScanJobStatus(jobId);

            setState((prev) => ({
              ...prev,
              status: statusResponse.status,
              progress: statusResponse.progress,
              processedIssues: statusResponse.processed_issues,
              totalIssues: statusResponse.total_issues,
            }));

            if (!TERMINAL_STATUSES.includes(statusResponse.status)) {
              return;
            }

            clearPoll();

            if (statusResponse.status !== "completed") {
              setState((prev) => ({
                ...prev,
                isRunning: false,
                error: new Error(
                  statusResponse.status === "cancelled"
                    ? "Scan was cancelled."
                    : "Scan failed while processing the repository.",
                ),
              }));

              return;
            }

            const result = await getScanJobResult(jobId);

            setState((prev) => ({
              ...prev,
              data: result,
              isRunning: false,
            }));
          } catch (pollError) {
            clearPoll();

            setState((prev) => ({
              ...prev,
              isRunning: false,
              error:
                pollError instanceof Error
                  ? pollError
                  : new Error("Failed to check scan job status."),
            }));
          }
        }, POLL_INTERVAL_MS);
      } catch (startError) {
        setState((prev) => ({
          ...prev,
          isRunning: false,
          error:
            startError instanceof Error
              ? startError
              : new Error("Failed to start repository scan."),
        }));
      }
    },
    [clearPoll],
  );

  const cancel = useCallback(async () => {
    clearPoll();

    if (state.jobId) {
      try {
        await cancelScanJob(state.jobId);
      } catch {
        // Best-effort - the poll loop is already stopped locally either way.
      }
    }

    setState((prev) => ({ ...prev, isRunning: false }));
  }, [clearPoll, state.jobId]);

  const reset = useCallback(() => {
    clearPoll();
    setState(INITIAL_STATE);
  }, [clearPoll]);

  return { ...state, start, cancel, reset };
}
