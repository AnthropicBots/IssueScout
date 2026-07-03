import { GitPullRequest } from "lucide-react";

import Card from "../ui/Card";

interface PullRequestCardProps {
  number?: number | null;
  title?: string | null;
}

export default function PullRequestCard({
  number,
  title,
}: PullRequestCardProps) {
  return (
    <Card>

      <div className="space-y-4">

        <div className="flex items-center gap-2">

          <GitPullRequest
            size={20}
            className="text-green-600"
          />

          <h3 className="text-lg font-semibold">
            Linked Pull Request
          </h3>

        </div>

        {number ? (
          <>
            <p>

              <strong>PR:</strong>

              {" "}

              #{number}

            </p>

            {title && (
              <p className="text-slate-600">
                {title}
              </p>
            )}

          </>
        ) : (
          <p className="text-slate-500">
            No linked pull request found.
          </p>
        )}

      </div>

    </Card>
  );
}
