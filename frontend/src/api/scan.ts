import { api } from "./client";
import type {
  ScanJobResponse,
  ScanJobStatsResponse,
  ScanJobStatusResponse,
  ScanJobSummaryResponse,
} from "../types/api";

/**
 * Async (job-based) scan API.
 *
 * `api/repository.ts` calls the SYNCHRONOUS endpoint
 * (`GET /scan/repository/{owner}/{repository}`), which blocks the request
 * until the whole scan finishes. That's fine for small repositories, but
 * the backend also exposes a JOB-based flow (create -> poll status ->
 * fetch result) that lets the UI show real progress and avoid long-lived
 * HTTP requests timing out on large repositories. This file wraps that
 * job-based flow. It currently isn't wired into any component - use
 * `useRepositoryScan`/`useRepositoryQuery` as a reference for how to turn
 * these into React Query hooks (e.g. `useMutation` for `createScanJob`,
 * then `useQuery` with `refetchInterval` for `getScanJobStatus` until the
 * job is `completed`/`failed`/`cancelled`, then `getScanJobResult`).
 */

export async function createScanJob(
  owner: string,
  repository: string,
): Promise<ScanJobResponse> {
  const response = await api.post<ScanJobResponse>(
    `/scan/${owner}/${repository}`,
  );

  return response.data;
}

export async function listScanJobs(params?: {
  status?: string;
  owner?: string;
  repository?: string;
  limit?: number;
  offset?: number;
}): Promise<ScanJobSummaryResponse[]> {
  const response = await api.get<ScanJobSummaryResponse[]>(
    "/scan/jobs",
    { params },
  );

  return response.data;
}

export async function getScanJobStats(): Promise<ScanJobStatsResponse> {
  const response = await api.get<ScanJobStatsResponse>(
    "/scan/jobs/stats",
  );

  return response.data;
}

export async function getScanJobStatus(
  jobId: string,
): Promise<ScanJobStatusResponse> {
  const response = await api.get<ScanJobStatusResponse>(
    `/scan/jobs/${jobId}`,
  );

  return response.data;
}

export async function getScanJobResult(
  jobId: string,
): Promise<import("../types/api").ScanResult> {
  const response = await api.get<import("../types/api").ScanResult>(
    `/scan/jobs/${jobId}/result`,
  );

  return response.data;
}

export async function cancelScanJob(
  jobId: string,
): Promise<ScanJobStatusResponse> {
  const response = await api.post<ScanJobStatusResponse>(
    `/scan/jobs/${jobId}/cancel`,
  );

  return response.data;
}

export async function deleteScanJob(jobId: string): Promise<void> {
  await api.delete(`/scan/jobs/${jobId}`);
}
