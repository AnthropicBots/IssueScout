import Input from "../ui/Input";

export default function SearchToolbar() {
  return (
    <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
      <div className="w-full md:max-w-md">
        <Input
          placeholder="Search issues..."
        />
      </div>

      <div className="flex gap-3">
        <select className="rounded-lg border border-slate-300 bg-white px-4 py-3">
          <option>
            Highest Confidence
          </option>

          <option>
            Lowest Confidence
          </option>

          <option>
            Issue Number
          </option>
        </select>

        <select className="rounded-lg border border-slate-300 bg-white px-4 py-3">
          <option>
            All Issues
          </option>

          <option>
            Assigned
          </option>

          <option>
            Unassigned
          </option>
        </select>
      </div>
    </div>
  );
}
