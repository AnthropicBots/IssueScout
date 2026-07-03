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
    <div className="mb-8 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
        <div className="w-full lg:max-w-md">
          <Input
            placeholder="Search issues by title or number..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
          />
        </div>

        <div className="flex flex-col gap-3 sm:flex-row">
          <select
            value={sortBy}
            onChange={(e) => onSortChange(e.target.value)}
            className="rounded-xl border border-slate-300 bg-white px-4 py-3"
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

          <select
            value={filterBy}
            onChange={(e) => onFilterChange(e.target.value)}
            className="rounded-xl border border-slate-300 bg-white px-4 py-3"
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
              Linked PR
            </option>

            <option value="unlinked">
              No Linked PR
            </option>
          </select>
        </div>
      </div>
    </div>
  );
}
