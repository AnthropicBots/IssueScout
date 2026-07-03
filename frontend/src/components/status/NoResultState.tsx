import { SearchX } from "lucide-react";

interface NoResultStateProps {
  title?: string;
  description?: string;
}

export default function NoResultState({
  title = "No matching issues found",
  description = "Try changing the search term or filters.",
}: NoResultStateProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-10 text-center shadow-sm">

      <SearchX
        className="mx-auto mb-4 text-slate-400"
        size={48}
      />

      <h3 className="text-xl font-semibold">
        {title}
      </h3>

      <p className="mt-3 text-slate-500">
        {description}
      </p>

    </div>
  );
}
