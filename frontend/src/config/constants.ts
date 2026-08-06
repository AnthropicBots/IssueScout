/**
 * App-wide constants.
 *
 * This file was empty. Values below were previously hardcoded inline in
 * various components (RepositorySearchForm, SearchToolbar, etc). Nothing
 * currently imports from here yet - it's safe to paste as-is, and you can
 * gradually point existing components at these exports instead of their
 * local literals so there's a single source of truth.
 */

export const APP_NAME = "IssueScout";

export const API_BASE_URL =
  import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000/api/v1";

/** sessionStorage keys used to persist the last search/result (see RepositorySearchForm.tsx) */
export const STORAGE_KEYS = {
  OWNER: "issuescout-owner",
  REPOSITORY: "issuescout-repository",
  LAST_RESULT: "issuescout-last-result",
} as const;

/** Suggested repositories shown on the scanner form. */
export const POPULAR_REPOSITORIES = [
  "microsoft/vscode",
  "angular/angular",
  "facebook/react",
  "pallets/flask",
  "fastapi/fastapi",
] as const;

/** Options for SearchToolbar's "Sort By" select. */
export const SORT_OPTIONS = [
  { value: "confidence-desc", label: "Highest Confidence" },
  { value: "confidence-asc", label: "Lowest Confidence" },
  { value: "issue-desc", label: "Newest Issue" },
  { value: "issue-asc", label: "Oldest Issue" },
  { value: "title", label: "Alphabetical" },
] as const;

/** Options for SearchToolbar's "Filter" select. */
export const FILTER_OPTIONS = [
  { value: "all", label: "All Issues" },
  { value: "assigned", label: "Assigned" },
  { value: "unassigned", label: "Unassigned" },
  { value: "linked", label: "Linked Pull Request" },
  { value: "unlinked", label: "No Linked Pull Request" },
] as const;

/** Confidence-tier thresholds (see utils/formatters/formatConfidence.ts). */
export const CONFIDENCE_THRESHOLDS = {
  EXCELLENT: 90,
  HIGH: 70,
  MEDIUM: 50,
} as const;
