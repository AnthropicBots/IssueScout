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
    <section
      className={`space-y-8 ${className}`}
    >
      {(title || subtitle) && (
        <div className="max-w-4xl">
          {title && (
            <h2 className="text-3xl font-black tracking-tight text-slate-900 lg:text-4xl">
              {title}
            </h2>
          )}

          {subtitle && (
            <p className="mt-4 text-lg leading-8 text-slate-600">
              {subtitle}
            </p>
          )}
        </div>
      )}

      {children}
    </section>
  );
}
