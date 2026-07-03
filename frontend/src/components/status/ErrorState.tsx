import { AlertTriangle } from "lucide-react";

interface ErrorStateProps {
  title?: string;
  message: string;
}

export default function ErrorState({
  title = "Something went wrong",
  message,
}: ErrorStateProps) {
  return (
    <div className="rounded-2xl border border-red-200 bg-red-50 p-8">

      <div className="flex items-start gap-4">

        <AlertTriangle
          className="text-red-600"
          size={28}
        />

        <div>

          <h3 className="font-semibold text-red-700">
            {title}
          </h3>

          <p className="mt-2 text-red-600">
            {message}
          </p>

        </div>

      </div>

    </div>
  );
}
