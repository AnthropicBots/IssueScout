import type { ReactNode } from "react";

interface StatisticsGridProps {
  children: ReactNode;
}

export default function StatisticsGrid({
  children,
}: StatisticsGridProps) {
  return (
    <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-3">
      {children}
    </div>
  );
}
