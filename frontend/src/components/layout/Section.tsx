import type { ReactNode } from "react";

interface SectionProps {
  title?: string;
  subtitle?: string;
  children: ReactNode;
  className?: string;
}

export default function Section({
  title,
  subtitle,
  children,
  className = "",
}: SectionProps) {
  return (
    <section className={`space-y-6 ${className}`}>
      {(title || subtitle) && (
        <div>
          {title && (
            <h2 className="text-2xl font-bold tracking-tight text-slate-900">
              {title}
            </h2>
          )}

          {subtitle && (
            <p className="mt-2 text-slate-600">
              {subtitle}
            </p>
          )}
        </div>
      )}

      {children}
    </section>
  );
}
