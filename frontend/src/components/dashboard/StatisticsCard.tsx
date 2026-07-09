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
    <div className="group relative overflow-hidden rounded-[1.75rem] border border-slate-200 bg-white shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-blue-200 hover:shadow-xl">
      {/* Top Accent */}

      <div className="absolute left-0 right-0 top-0 h-1 bg-gradient-to-r from-blue-500 via-cyan-500 to-indigo-500 opacity-0 transition-opacity duration-300 group-hover:opacity-100" />

      <div className="flex items-start justify-between p-7">
        <div className="min-w-0 flex-1">
          <p className="text-sm font-semibold uppercase tracking-wider text-slate-500">
            {title}
          </p>

          <h3 className="mt-3 break-words text-3xl font-black tracking-tight text-slate-900">
            {value}
          </h3>

          {subtitle && (
            <p className="mt-3 text-sm leading-6 text-slate-500">
              {subtitle}
            </p>
          )}
        </div>

        {icon && (
          <div
            className={`ml-5 flex h-14 w-14 items-center justify-center rounded-2xl shadow-sm transition-transform duration-300 group-hover:scale-110 ${color}`}
          >
            {icon}
          </div>
        )}
      </div>
    </div>
  );
}
