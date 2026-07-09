import {
  ArrowRight,
  SearchX,
} from "lucide-react";

interface NoResultStateProps {
  title?: string;
  description?: string;
}

export default function NoResultState({
  title = "No Matching Issues Found",
  description = "Try adjusting your search query or filters to discover more issues.",
}: NoResultStateProps) {
  return (
    <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-lg">
      <div className="flex flex-col items-center px-8 py-14 text-center">
        {/* Icon */}

        <div className="mb-8 flex h-24 w-24 items-center justify-center rounded-full bg-slate-100 ring-8 ring-slate-50">
          <SearchX
            size={46}
            className="text-slate-500"
          />
        </div>

        {/* Heading */}

        <h3 className="text-3xl font-bold tracking-tight text-slate-900">
          {title}
        </h3>

        {/* Description */}

        <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
          {description}
        </p>

        {/* Suggestions */}

        <div className="mt-10 grid w-full max-w-3xl gap-4 md:grid-cols-3">
          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <p className="font-semibold text-slate-900">
              Clear Filters
            </p>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Remove active filters to display more issues.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <p className="font-semibold text-slate-900">
              Search Again
            </p>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Try another keyword or issue number.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <p className="font-semibold text-slate-900">
              Scan Another Repository
            </p>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              Different repositories may contain suitable issues.
            </p>
          </div>
        </div>

        {/* Footer */}

        <div className="mt-10 inline-flex items-center gap-2 rounded-full border border-blue-200 bg-blue-50 px-5 py-3 text-sm font-semibold text-blue-700">
          <ArrowRight size={16} />
          Update your search to continue
        </div>
      </div>
    </div>
  );
}
