import { ArrowLeft } from "lucide-react";
import { Link } from "react-router-dom";

interface IssueHeaderProps {
  issueNumber: number;
  title: string;
}

export default function IssueHeader({
  issueNumber,
  title,
}: IssueHeaderProps) {
  return (
    <>
      <Link
        to="/"
        className="mb-8 inline-flex items-center gap-2 text-blue-600 hover:underline"
      >
        <ArrowLeft size={18} />
        Back to Repository
      </Link>

      <div className="mb-8">

        <h1 className="text-4xl font-bold">
          Issue #{issueNumber}
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          {title}
        </p>

      </div>
    </>
  );
}
