import {
  ArrowLeft,
  ExternalLink,
  GitPullRequest,
  User,
} from "lucide-react";

import {
  Link,
  useLocation,
} from "react-router-dom";

import ConfidenceBar from "../../components/issue/ConfidenceBar";
import IssueHeader from "../../components/issue/IssueHeader";
import IssueMetadata from "../../components/issue/IssueMetadata";
import PullRequestCard from "../../components/issue/PullRequestCard";
import PageContainer from "../../components/layout/PageContainer";
import Section from "../../components/layout/Section";
import PredictionSummary from "../../components/prediction/PredictionSummary";
import Card from "../../components/ui/Card";

import {
  issueUrl,
  pullRequestUrl,
} from "../../utils/formatters/formatRepository";

export default function IssueDetailPage() {
  const location = useLocation();

  const issue = location.state?.issue;

  const owner =
    location.state?.owner ??
    issue?.repository_owner ??
    issue?.owner ??
    "";

  const repo =
    location.state?.repo ??
    issue?.repository_name ??
    issue?.repository ??
    "";

  if (!issue || !owner || !repo) {
    return (
      <PageContainer>
        <div className="mx-auto max-w-2xl">
          <Card className="overflow-hidden">
            <div className="border-b border-slate-100 bg-gradient-to-r from-red-50 via-rose-50 to-red-50 p-8 text-center">
              <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-red-100">
                <GitPullRequest
                  size={36}
                  className="text-red-600"
                />
              </div>

              <h2 className="mt-6 text-3xl font-black text-slate-900">
                Issue Not Found
              </h2>

              <p className="mx-auto mt-4 max-w-lg text-lg leading-8 text-slate-600">
                This page doesn't contain an issue anymore.
                Scan the repository again to regenerate
                the analysis.
              </p>
            </div>

            <div className="p-8 text-center">
              <Link
                to="/"
                className="inline-flex items-center gap-3 rounded-2xl bg-gradient-to-r from-blue-600 to-cyan-500 px-7 py-4 font-semibold text-white shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
              >
                <ArrowLeft size={20} />

                Back to Repository Scanner
              </Link>
            </div>
          </Card>
        </div>
      </PageContainer>
    );
  }

  return (
    <PageContainer>
      <IssueHeader
        issueNumber={issue.number}
        title={issue.title}
        owner={owner}
        repository={repo}
        author={issue.author}
        createdAt={issue.created_at}
        updatedAt={issue.updated_at}
      />

      <div className="mb-8 grid gap-4 md:grid-cols-4">

        <Card
          padding="sm"
          hover={false}
        >
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Confidence
          </p>

          <h3 className="mt-2 text-3xl font-black text-blue-600">
            {issue.confidence}%
          </h3>

          <p className="mt-1 text-sm text-slate-500">
            AI Prediction
          </p>
        </Card>

        <Card
          padding="sm"
          hover={false}
        >
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Assignment
          </p>

          <h3 className="mt-2 text-xl font-bold text-slate-900">
            {issue.assigned
              ? "Assigned"
              : "Open"}
          </h3>

          <p className="mt-1 text-sm text-slate-500">
            Contributor Status
          </p>
        </Card>

        <Card
          padding="sm"
          hover={false}
        >
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Linked PR
          </p>

          <h3 className="mt-2 text-xl font-bold text-slate-900">
            {issue.linked_pr_number
              ? `#${issue.linked_pr_number}`
              : "None"}
          </h3>

          <p className="mt-1 text-sm text-slate-500">
            Relationship
          </p>
        </Card>

        <Card
          padding="sm"
          hover={false}
        >
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Repository
          </p>

          <h3 className="mt-2 text-xl font-bold text-slate-900 truncate">
            {repo}
          </h3>

          <p className="mt-1 text-sm text-slate-500">
            {owner}
          </p>
        </Card>

      </div>

      <Section>
        <Card>
          <div className="space-y-10">

            {/* Status */}

            <IssueMetadata
              confidence={issue.confidence}
              assigned={issue.assigned}
            />

            {/* Confidence */}

            <Card
              variant="filled"
              className="border border-slate-200"
            >
              <div className="space-y-6">
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="text-2xl font-bold text-slate-900">
                      Prediction Confidence
                    </h3>

                    <p className="mt-2 text-slate-500">
                      Overall confidence generated by
                      IssueScout's AI analysis.
                    </p>
                  </div>

                  <div className="rounded-2xl bg-blue-100 px-6 py-4 text-center">
                    <div className="text-3xl font-black text-blue-700">
                      {issue.confidence}%
                    </div>

                    <div className="text-xs font-semibold uppercase tracking-wide text-blue-600">
                      Confidence
                    </div>
                  </div>
                </div>

                <ConfidenceBar
                  value={issue.confidence}
                />
              </div>
            </Card>

            {/* Repository Information */}

            <div className="grid gap-8 xl:grid-cols-2">
              {/* Assignment */}

              <Card className="h-full">
                <div className="space-y-8">
                  <div className="flex items-center gap-4">
                    <div className="rounded-2xl bg-blue-100 p-4">
                      <User
                        size={24}
                        className="text-blue-600"
                      />
                    </div>

                    <div>
                      <h3 className="text-2xl font-bold text-slate-900">
                        Assignment
                      </h3>

                      <p className="mt-1 text-slate-500">
                        Current contributor assignment
                        information.
                      </p>
                    </div>
                  </div>

                  <div className="grid gap-5">
                    <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
                      <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
                        Status
                      </p>

                      <h4 className="mt-2 text-2xl font-bold text-slate-900">
                        {issue.assigned
                          ? "Assigned"
                          : "Open for Contribution"}
                      </h4>
                    </div>

                    <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
                      <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
                        Assignee
                      </p>

                      <h4 className="mt-2 text-2xl font-bold text-slate-900">
                        {issue.assignee ??
                          "No Assignee"}
                      </h4>
                    </div>
                  </div>

                  <div className="rounded-2xl bg-gradient-to-r from-blue-50 to-cyan-50 p-5">
                    <p className="text-sm leading-7 text-slate-700">
                      <span className="font-semibold">
                        Contributor Insight:
                      </span>{" "}
                      {issue.assigned
                        ? "This issue already has an assigned contributor. Review the repository discussion before starting work."
                        : "This issue is currently unassigned and may be a good opportunity for new contributors."}
                    </p>
                  </div>
                </div>
              </Card>

              {/* Pull Request */}

              <div className="h-full">
                <PullRequestCard
                  number={
                    issue.linked_pr_number
                  }
                  title={
                    issue.linked_pr_title
                  }
                />
              </div>
            </div>

            {/* Prediction Dashboard */}

            <PredictionSummary
              confidence={
                issue.confidence
              }
              assigned={
                issue.assigned
              }
              linkedPR={Boolean(
                issue.linked_pr_number,
              )}
            />

            {/* GitHub Resources */}

            <Card className="border border-slate-200">

              <div className="flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">

                <div>

                  <h3 className="text-2xl font-bold text-slate-900">
                    GitHub Resources
                  </h3>

                  <p className="mt-2 max-w-2xl text-slate-600">
                    Continue investigating this issue directly on GitHub,
                    inspect pull requests, repository activity and discussions.
                  </p>

                </div>

                <div className="rounded-2xl bg-slate-100 px-5 py-3">

                  <p className="text-xs uppercase tracking-wider text-slate-500">
                    Repository
                  </p>

                  <p className="mt-1 font-bold text-slate-900">
                    {owner}/{repo}
                  </p>

                </div>

              </div>

              <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4">

                {/* Open Issue */}

                <a
                  href={issueUrl(owner, repo, issue.number)}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-center gap-2 rounded-2xl bg-slate-900 px-6 py-4 font-semibold text-white transition hover:bg-slate-800"
                >
                  <ExternalLink size={18} />

                  Open Issue
                </a>

                {/* Pull Request */}

                {issue.linked_pr_number ? (

                  <a
                    href={pullRequestUrl(
                      owner,
                      repo,
                      issue.linked_pr_number,
                    )}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center justify-center gap-2 rounded-2xl bg-blue-600 px-6 py-4 font-semibold text-white transition hover:bg-blue-700"
                  >
                    <ExternalLink size={18} />

                    Open Pull Request
                  </a>

                ) : (

                  <button
                    disabled
                    className="cursor-not-allowed rounded-2xl bg-slate-200 px-6 py-4 font-semibold text-slate-500"
                  >
                    No Linked PR
                  </button>

                )}

                {/* Repository */}

                <a
                  href={`https://github.com/${owner}/${repo}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-center gap-2 rounded-2xl border border-slate-300 bg-white px-6 py-4 font-semibold text-slate-800 transition hover:border-blue-500 hover:text-blue-600"
                >
                  <ExternalLink size={18} />

                  Repository
                </a>

                {/* Back */}

                <Link
                  to="/"
                  className="flex items-center justify-center gap-2 rounded-2xl border border-slate-300 bg-white px-6 py-4 font-semibold text-slate-800 transition hover:border-blue-500 hover:text-blue-600"
                >
                  <ArrowLeft size={18} />

                  Back
                </Link>

              </div>

            </Card>

          </div>
        </Card>
      </Section>
    </PageContainer>
  );
}
