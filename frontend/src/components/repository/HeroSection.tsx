import { SearchCheck } from "lucide-react";

export default function HeroSection() {
  return (
    <section className="mb-12 text-center">
      <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-blue-100">
        <SearchCheck
          size={40}
          className="text-blue-600"
        />
      </div>

      <h1 className="mt-6 text-5xl font-bold tracking-tight">
        IssueScout
      </h1>

      <p className="mx-auto mt-5 max-w-2xl text-lg text-slate-600">
        Find GitHub issues that are suitable for contributors using
        intelligent repository analysis, assignment detection,
        linked pull request tracking and confidence scoring.
      </p>
    </section>
  );
}
