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
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-slate-500">
            {title}
          </p>

          <h3 className="mt-2 text-3xl font-bold text-slate-900">
            {value}
          </h3>

          {subtitle && (
            <p className="mt-2 text-sm text-slate-500">
              {subtitle}
            </p>
          )}
        </div>

        {icon && (
          <div className={`rounded-xl p-3 ${color}`}>
            {icon}
          </div>
        )}
      </div>
    </div>
  );
}
