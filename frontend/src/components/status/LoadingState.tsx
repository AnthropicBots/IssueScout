import { Loader2 } from "lucide-react";

interface LoadingStateProps {
  title?: string;
  description?: string;
}

export default function LoadingState({
  title = "Scanning Repository...",
  description = "IssueScout is analyzing issues and pull requests.",
}: LoadingStateProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-10 shadow-sm">
      <div className="flex flex-col items-center text-center">

        <Loader2
          className="mb-5 animate-spin text-blue-600"
          size={42}
        />

        <h3 className="text-xl font-semibold text-slate-900">
          {title}
        </h3>

        <p className="mt-2 max-w-md text-slate-500">
          {description}
        </p>

      </div>
    </div>
  );
}
