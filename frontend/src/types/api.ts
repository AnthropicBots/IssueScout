export interface IssueSummary {
  number: number;
  title: string;
  assigned: boolean;
  assignee: string | null;
  confidence: number;
  linked_pr_number: number | null;
  linked_pr_title: string | null;
  github_url?: string;
}

export interface ScanResult {
  repository: string;
  total_issues: number;
  available_issues: number;
  issues: IssueSummary[];
}
