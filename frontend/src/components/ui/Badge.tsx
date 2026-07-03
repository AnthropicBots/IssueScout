import type { HTMLAttributes, ReactNode } from "react";

import clsx from "clsx";

type BadgeColor =
  | "blue"
  | "green"
  | "yellow"
  | "red"
  | "gray";

type BadgeSize =
  | "sm"
  | "md";

interface BadgeProps
  extends HTMLAttributes<HTMLSpanElement> {
  color?: BadgeColor;
  size?: BadgeSize;
  icon?: ReactNode;
}

export default function Badge({
  children,
  color = "gray",
  size = "md",
  icon,
  className,
  ...props
}: BadgeProps) {
  return (
    <span
      className={clsx(
        "inline-flex items-center gap-2 rounded-full font-medium transition-colors",

        {
          "px-2.5 py-1 text-xs": size === "sm",

          "px-3 py-1.5 text-sm": size === "md",

          "bg-blue-100 text-blue-700":
            color === "blue",

          "bg-green-100 text-green-700":
            color === "green",

          "bg-yellow-100 text-yellow-700":
            color === "yellow",

          "bg-red-100 text-red-700":
            color === "red",

          "bg-slate-100 text-slate-700":
            color === "gray",
        },

        className,
      )}
      {...props}
    >
      {icon}

      {children}
    </span>
  );
}
