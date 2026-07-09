import {
  AlertTriangle,
  RefreshCw,
  ShieldAlert,
} from "lucide-react";

interface ErrorStateProps {
  title?: string;
  message: string;
}

export default function ErrorState({
  title = "Something Went Wrong",
  message,
}: ErrorStateProps) {
  return (
    <div className="overflow-hidden rounded-[2rem] border border-red-200 bg-white shadow-lg">
      {/* Header */}

      <div className="border-b border-red-100 bg-gradient-to-r from-red-50 to-rose-50 p-6">
        <div className="flex items-center gap-4">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-red-100">
            <ShieldAlert
              size={28}
              className="text-red-600"
            />
          </div>

          <div>
            <h3 className="text-2xl font-bold text-red-700">
              {title}
            </h3>

            <p className="mt-1 text-sm text-red-600">
              The requested operation could not be completed.
            </p>
          </div>
        </div>
      </div>

      {/* Body */}

      <div className="space-y-6 p-8">
        <div className="rounded-2xl border border-red-200 bg-red-50 p-5">
          <div className="flex items-start gap-3">
            <AlertTriangle
              size={22}
              className="mt-0.5 shrink-0 text-red-600"
            />

            <div>
              <h4 className="font-semibold text-red-700">
                Error Details
              </h4>

              <p className="mt-2 leading-7 text-red-600">
                {message}
              </p>
            </div>
          </div>
        </div>

        {/* Suggestions */}

        <div className="grid gap-4 md:grid-cols-3">
          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <h5 className="font-semibold text-slate-900">
              Check Repository
            </h5>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Verify the repository owner and repository
              name are correct.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <h5 className="font-semibold text-slate-900">
              Verify Access
            </h5>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Make sure the repository exists and is
              publicly accessible.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <h5 className="font-semibold text-slate-900">
              Try Again
            </h5>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Temporary GitHub API or network issues may
              resolve after a few moments.
            </p>
          </div>
        </div>

        {/* Footer */}

        <div className="flex items-center justify-center rounded-2xl bg-slate-100 p-4">
          <div className="flex items-center gap-2 text-sm font-medium text-slate-700">
            <RefreshCw
              size={16}
              className="text-blue-600"
            />

            Refresh or scan the repository again after
            verifying the details.
          </div>
        </div>
      </div>
    </div>
  );
}
