import {
  ArrowLeft,
  ExternalLink,
  User,
} from "lucide-react";

import { Link, useLocation } from "react-router-dom";

import IssueHeader from "../../components/issue/IssueHeader";
import IssueMetadata from "../../components/issue/IssueMetadata";
import PullRequestCard from "../../components/issue/PullRequestCard";
import PredictionSummary from "../../components/prediction/PredictionSummary";
import ConfidenceBar from "../../components/issue/ConfidenceBar";
import PageContainer from "../../components/layout/PageContainer";
import Section from "../../components/layout/Section";
import Card from "../../components/ui/Card";
import {
  issueUrl,
  pullRequestUrl,
} from "../../utils/formatters/formatRepository";

export default function IssueDetailPage() {
  const location = useLocation();

  const issue = location.state?.issue;
  const owner = location.state?.owner;
  const repo = location.state?.repo;

  if (!issue) {
    return (
      <PageContainer>
        <Card>
          <div className="space-y-4 py-8 text-center">
            <h2 className="text-2xl font-bold">
              Issue Not Found
            </h2>

            <p className="text-slate-500">
              Please go back and scan the repository again.
            </p>

            <Link
              to="/"
              className="inline-flex items-center gap-2 rounded-lg bg-blue-600 px-5 py-3 text-white transition hover:bg-blue-700"
            >
              <ArrowLeft size={18} />
              Back to Home
            </Link>
          </div>
        </Card>
      </PageContainer>
    );
  }

  return (
    <PageContainer>
      <IssueHeader
        issueNumber={issue.number}
        title={issue.title}
      />

      <Section>
        <Card>
          <div className="space-y-8">

            {/* Status */}

            <IssueMetadata
              confidence={issue.confidence}
              assigned={issue.assigned}
            />

            {/* Confidence */}

            <ConfidenceBar
              value={issue.confidence}
            />

            {/* Details */}

            <div className="grid gap-6 lg:grid-cols-2">

              <Card>
                <div className="space-y-4">

                  <div className="flex items-center gap-2">
                    <User
                      size={20}
                      className="text-blue-600"
                    />

                    <h3 className="text-lg font-semibold">
                      Assignment
                    </h3>
                  </div>

                  <div className="space-y-2 text-slate-600">

                    <p>

                      <strong>Status:</strong>{" "}

                      {issue.assigned
                        ? "Assigned"
                        : "Open"}

                    </p>

                    <p>

                      <strong>Assignee:</strong>{" "}

                      {issue.assignee ??
                        "Not Assigned"}

                    </p>

                  </div>

                </div>
              </Card>

              <PullRequestCard
                number={issue.linked_pr_number}
                title={issue.linked_pr_title}
              />

            </div>

            {/* Summary */}

            <PredictionSummary
              confidence={issue.confidence}
              assigned={issue.assigned}
              linkedPR={Boolean(issue.linked_pr_number)}
            />

            {/* Actions */}

            <div className="flex flex-wrap items-center gap-4 border-t pt-6">

              <a
                href={issueUrl(
                  owner,
                  repo,
                  issue.number,
                )}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-3 rounded-xl bg-gradient-to-r from-slate-900 to-slate-700 px-6 py-3 font-semibold text-white shadow-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-xl"
              >
                <ExternalLink size={18} />
                Open Issue on GitHub
              </a>
              {issue.linked_pr_number && (
                <a
                  href={pullRequestUrl(
                    owner,
                    repo,
                    issue.linked_pr_number,
                  )}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-3 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 px-6 py-3 font-semibold text-white shadow-lg transition-all duration-200 hover:-translate-y-0.5 hover:shadow-xl"
                >
                  <ExternalLink size={18} />
                  Open Linked Pull Request
                </a>
              )}
            </div>

          </div>
        </Card>
      </Section>
    </PageContainer>
  );
}
