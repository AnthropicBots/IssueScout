import type { ReactNode } from "react";

interface StatisticsGridProps {
  children: ReactNode;
}

export default function StatisticsGrid({
  children,
}: StatisticsGridProps) {
  return (
    <section
      aria-label="Repository Statistics"
      className="
        grid
        gap-4
        sm:grid-cols-2
        xl:grid-cols-3
        2xl:grid-cols-6
        auto-rows-fr
        items-stretch
      "
    >
      {children}
    </section>
  );
}
