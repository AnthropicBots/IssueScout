import type { ReactNode } from "react";

interface StatisticsCardProps {
  title: string;
  value: string | number;
  icon?: ReactNode;
  color?: string;
  subtitle?: string;
}

export default function StatisticsCard({
  title,
  value,
  icon,
  color = "bg-blue-100 text-blue-600",
  subtitle,
}: StatisticsCardProps) {
  return (
    <div
      className="
        group
        overflow-hidden
        rounded-3xl
        border
        border-slate-200
        bg-white
        p-5
        shadow-sm
        transition-all
        duration-300
        hover:-translate-y-0.5
        hover:border-blue-200
        hover:shadow-lg
      "
    >
      <div className="flex items-start justify-between gap-4">

        <div className="min-w-0 flex-1">

          <p className="text-xs font-semibold uppercase tracking-widest text-slate-500">
            {title}
          </p>

          <h3 className="mt-2 break-words text-2xl font-black tracking-tight text-slate-900">
            {value}
          </h3>

          {subtitle && (
            <p className="mt-2 text-sm leading-5 text-slate-500">
              {subtitle}
            </p>
          )}

        </div>

        {icon && (
          <div
            className={`
              flex
              h-12
              w-12
              shrink-0
              items-center
              justify-center
              rounded-2xl
              ${color}
            `}
          >
            {icon}
          </div>
        )}

      </div>
    </div>
  );
}
