import {
  ArrowDownAZ,
  Filter,
  Search,
} from "lucide-react";

import Input from "../ui/Input";

type Props = {
  searchQuery: string;
  sortBy: string;
  filterBy: string;
  onSearchChange: (value: string) => void;
  onSortChange: (value: string) => void;
  onFilterChange: (value: string) => void;
};

export default function SearchToolbar({
  searchQuery,
  sortBy,
  filterBy,
  onSearchChange,
  onSortChange,
  onFilterChange,
}: Props) {
  return (
    <div className="overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-lg">
      <div className="border-b border-slate-100 px-8 py-6">
        <div className="flex flex-col gap-2 lg:flex-row lg:items-center lg:justify-between">
          <div>
            <h2 className="text-2xl font-bold tracking-tight text-slate-900">
              Search & Filter Results
            </h2>

            <p className="mt-1 text-slate-500">
              Quickly search, filter, and sort analyzed GitHub issues.
            </p>
          </div>
        </div>
      </div>

      <div className="grid gap-6 p-8 lg:grid-cols-[2fr_1fr_1fr]">
        {/* Search */}

        <div>
          <label className="mb-2 flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-600">
            <Search
              size={16}
              className="text-blue-600"
            />
            Search Issues
          </label>

          <Input
            placeholder="Search by issue title or issue number..."
            value={searchQuery}
            onChange={(e) =>
              onSearchChange(e.target.value)
            }
          />
        </div>

        {/* Sort */}

        <div>
          <label className="mb-2 flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-600">
            <ArrowDownAZ
              size={16}
              className="text-indigo-600"
            />
            Sort By
          </label>

          <select
            value={sortBy}
            onChange={(e) =>
              onSortChange(e.target.value)
            }
            className="w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 shadow-sm transition-all duration-200 outline-none hover:border-blue-300 focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
          >
            <option value="confidence-desc">
              Highest Confidence
            </option>

            <option value="confidence-asc">
              Lowest Confidence
            </option>

            <option value="issue-desc">
              Newest Issue
            </option>

            <option value="issue-asc">
              Oldest Issue
            </option>

            <option value="title">
              Alphabetical
            </option>
          </select>
        </div>

        {/* Filter */}

        <div>
          <label className="mb-2 flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-slate-600">
            <Filter
              size={16}
              className="text-emerald-600"
            />
            Filter
          </label>

          <select
            value={filterBy}
            onChange={(e) =>
              onFilterChange(e.target.value)
            }
            className="w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 shadow-sm transition-all duration-200 outline-none hover:border-blue-300 focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
          >
            <option value="all">
              All Issues
            </option>

            <option value="assigned">
              Assigned
            </option>

            <option value="unassigned">
              Unassigned
            </option>

            <option value="linked">
              Linked Pull Request
            </option>

            <option value="unlinked">
              No Linked Pull Request
            </option>
          </select>
        </div>
      </div>
    </div>
  );
}
