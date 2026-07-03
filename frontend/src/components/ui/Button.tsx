import type { ButtonHTMLAttributes, ReactNode } from "react";
import clsx from "clsx";

type ButtonVariant =
  | "primary"
  | "secondary"
  | "outline"
  | "danger";

type ButtonSize =
  | "sm"
  | "md"
  | "lg";

interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  fullWidth?: boolean;
  loading?: boolean;
}

export default function Button({
  children,
  className,
  variant = "primary",
  size = "md",
  leftIcon,
  rightIcon,
  fullWidth = false,
  loading = false,
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      disabled={disabled || loading}
      className={clsx(
        "inline-flex items-center justify-center gap-2 rounded-xl font-medium",
        "transition-all duration-200",
        "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2",
        "disabled:cursor-not-allowed disabled:opacity-60",
        "active:scale-[0.98]",

        {
          "w-full": fullWidth,

          "px-3 py-2 text-sm": size === "sm",

          "px-5 py-3 text-base": size === "md",

          "px-6 py-4 text-lg": size === "lg",

          "bg-blue-600 text-white hover:bg-blue-700 shadow-md hover:shadow-lg":
            variant === "primary",

          "bg-slate-900 text-white hover:bg-slate-800 shadow-md hover:shadow-lg":
            variant === "secondary",

          "border border-slate-300 bg-white text-slate-700 hover:bg-slate-100":
            variant === "outline",

          "bg-red-600 text-white hover:bg-red-700":
            variant === "danger",
        },

        className,
      )}
      {...props}
    >
      {loading ? (
        <>
          <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />

          Loading...
        </>
      ) : (
        <>
          {leftIcon}

          {children}

          {rightIcon}
        </>
      )}
    </button>
  );
}
