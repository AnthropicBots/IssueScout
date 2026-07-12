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
        "overflow-hidden rounded-3xl transition-all duration-300 ease-out",

        {
          // Default

          "border border-slate-200 bg-white shadow-sm":
            variant === "default",

          // Outlined

          "border-2 border-slate-200 bg-white shadow-sm":
            variant === "outlined",

          // Filled

          "bg-slate-50":
            variant === "filled",

          // Glass

          "border border-white/30 bg-white/70 shadow-lg backdrop-blur-xl":
            variant === "glass",

          // Hover

          "hover:-translate-y-0.5 hover:border-blue-100 hover:shadow-xl":
            hover,

          // Clickable

          "cursor-pointer active:scale-[0.99]":
            clickable,

          // Padding

          "p-4":
            padding === "sm",

          "p-5":
            padding === "md",

          "p-6":
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
