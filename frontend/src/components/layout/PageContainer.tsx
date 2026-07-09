import type { ReactNode } from "react";

interface PageContainerProps {
  children: ReactNode;
  className?: string;
}

export default function PageContainer({
  children,
  className = "",
}: PageContainerProps) {
  return (
    <section
      className={`
        mx-auto
        w-full
        max-w-7xl
        px-5
        py-10
        sm:px-6
        lg:px-8
        xl:px-10
        ${className}
      `}
    >
      {children}
    </section>
  );
}
