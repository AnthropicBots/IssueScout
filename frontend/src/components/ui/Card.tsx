import type {
  HTMLAttributes,
  ReactNode,
} from "react";

import clsx from "clsx";

type CardVariant =
  | "default"
  | "outlined"
  | "filled"
  | "glass";

interface CardProps
  extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  variant?: CardVariant;
  hover?: boolean;
  clickable?: boolean;
  padding?: "sm" | "md" | "lg";
}

export default function Card({
  children,
  className,
  variant = "default",
  hover = true,
  clickable = false,
  padding = "md",
  ...props
}: CardProps) {
  return (
    <div
      className={clsx(
        "rounded-2xl transition-all duration-300",

        {
          "border border-slate-200 bg-white shadow-sm":
            variant === "default",

          "border-2 border-slate-200 bg-white":
            variant === "outlined",

          "bg-slate-50":
            variant === "filled",

          "border border-white/20 bg-white/70 backdrop-blur":
            variant === "glass",

          "hover:-translate-y-1 hover:shadow-xl":
            hover,

          "cursor-pointer":
            clickable,

          "p-4":
            padding === "sm",

          "p-6":
            padding === "md",

          "p-8":
            padding === "lg",
        },

        className,
      )}
      {...props}
    >
      {children}
    </div>
  );
}
