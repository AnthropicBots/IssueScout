import { Loader2 } from "lucide-react";

interface LoadingSpinnerProps {
  size?: "sm" | "md" | "lg";
  text?: string;
  fullScreen?: boolean;
}

export default function LoadingSpinner({
  size = "md",
  text,
  fullScreen = false,
}: LoadingSpinnerProps) {
  const iconSize =
    size === "sm"
      ? 18
      : size === "lg"
      ? 42
      : 28;

  const containerClass = fullScreen
    ? "flex min-h-[50vh] flex-col items-center justify-center gap-4"
    : "flex flex-col items-center justify-center gap-3 py-6";

  return (
    <div className={containerClass}>
      <div className="flex items-center justify-center rounded-full bg-blue-50 p-4 shadow-sm">
        <Loader2
          size={iconSize}
          className="animate-spin text-blue-600"
        />
      </div>

      {text && (
        <p className="text-sm font-medium text-slate-600">
          {text}
        </p>
      )}
    </div>
  );
}
