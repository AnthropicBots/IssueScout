import { SearchX } from "lucide-react";

export default function EmptyState() {
  return (
    <div className="rounded-xl border border-dashed bg-white py-16 text-center">
      <SearchX
        className="mx-auto text-slate-400"
        size={48}
      />

      <h3 className="mt-6 text-xl font-semibold">
        No Issues Found
      </h3>

      <p className="mt-2 text-slate-500">
        Try scanning another repository.
      </p>
    </div>
  );
}
