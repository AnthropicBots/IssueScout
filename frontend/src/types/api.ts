export interface EvidenceItem {
  type: string;
  label: string;
  description: string;
  weight: number;
  passed: boolean;
  details: Record<string, unknown>;
}

export interface CandidatePullRequestSummary {
  number: number;
  title: string;
  confidence: number;
  url: string;
  sources: string[];
  reasons: string[];
  evidence: EvidenceItem[];
}

export interface IssueSummary {
  number: number;
  title: string;
  assigned: boolean;
  assignee: string | null;
  confidence: number;
  /** ISO 8601 datetime strings, as serialized by the FastAPI backend. */
  author?: string | null;
  created_at?: string | null;
  updated_at?: string | null;
  linked_pr_number: number | null;
  linked_pr_title: string | null;
  candidate_count: number;
  candidate_pull_requests: CandidatePullRequestSummary[];
  github_url?: string;
}

export interface ScanResult {
  repository: string;
  total_issues: number;
  available_issues: number;
  issues: IssueSummary[];
}

// ---------------------------------------------------------------------------
// Scan job types (async flow: POST /scan/{owner}/{repository} -> poll ->
// GET /scan/jobs/{job_id}/result). Mirrors backend/issuescout/models/responses.
// Used by api/scan.ts and hooks/useScanJob.ts.
// ---------------------------------------------------------------------------

export type ScanJobStatus =
  | "queued"
  | "running"
  | "completed"
  | "failed"
  | "cancelled";

export interface ScanJobResponse {
  job_id: string;
  status: ScanJobStatus;
}

export interface ScanJobStatusResponse {
  job_id: string;
  status: ScanJobStatus;
  progress: number;
  processed_issues: number;
  total_issues: number;
}

export interface ScanJobSummaryResponse {
  job_id: string;
  owner: string;
  repository: string;
  status: ScanJobStatus;
  progress: number;
  processed_issues: number;
  total_issues: number;
}

export interface ScanJobStatsResponse {
  total_jobs: number;
  queued_jobs: number;
  running_jobs: number;
  completed_jobs: number;
  failed_jobs: number;
}
