import type {
  HTMLAttributes,
  ReactNode,
} from "react";

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
        "inline-flex items-center justify-center gap-2 rounded-full border font-semibold shadow-sm transition-all duration-200",

        {
          "px-3 py-1 text-xs":
            size === "sm",

          "px-4 py-2 text-sm":
            size === "md",

          "border-blue-200 bg-blue-50 text-blue-700":
            color === "blue",

          "border-green-200 bg-green-50 text-green-700":
            color === "green",

          "border-yellow-200 bg-yellow-50 text-yellow-700":
            color === "yellow",

          "border-red-200 bg-red-50 text-red-700":
            color === "red",

          "border-slate-200 bg-slate-100 text-slate-700":
            color === "gray",
        },

        className,
      )}
      {...props}
    >
      {icon && (
        <span className="flex items-center">
          {icon}
        </span>
      )}

      <span>{children}</span>
    </span>
  );
}
