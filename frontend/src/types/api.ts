export interface EvidenceItem {
  analyzer: string;
  score: number;
  confidence: number;
  reason: string;
  evidence_type: string;
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
