import { SearchCode, GitBranch } from "lucide-react";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 border-b bg-white/90 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <SearchCode
            className="text-blue-600"
            size={28}
          />

          <div>
            <h1 className="text-lg font-bold">
              IssueScout
            </h1>

            <p className="text-xs text-slate-500">
              Intelligent GitHub Issue Discovery
            </p>
          </div>
        </div>

        <GitBranch
          className="text-slate-500"
          size={22}
        />
      </div>
    </header>
  );
}
