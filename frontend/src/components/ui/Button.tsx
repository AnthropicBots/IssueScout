import type {
  ButtonHTMLAttributes,
  ReactNode,
} from "react";
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
        "inline-flex items-center justify-center gap-2 rounded-2xl font-semibold",
        "transition-all duration-300 ease-out",
        "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2",
        "disabled:cursor-not-allowed disabled:opacity-60",
        "active:scale-[0.98]",

        {
          "w-full": fullWidth,

          "px-4 py-2.5 text-sm":
            size === "sm",

          "px-6 py-3.5 text-base":
            size === "md",

          "px-8 py-4 text-lg":
            size === "lg",

          // Primary

          "bg-gradient-to-r from-blue-600 to-cyan-500 text-white shadow-lg hover:-translate-y-0.5 hover:shadow-xl":
            variant === "primary",

          // Secondary

          "bg-slate-900 text-white shadow-lg hover:-translate-y-0.5 hover:bg-slate-800 hover:shadow-xl":
            variant === "secondary",

          // Outline

          "border border-slate-300 bg-white text-slate-700 shadow-sm hover:-translate-y-0.5 hover:border-blue-300 hover:bg-slate-50 hover:shadow-md":
            variant === "outline",

          // Danger

          "bg-gradient-to-r from-red-600 to-rose-600 text-white shadow-lg hover:-translate-y-0.5 hover:shadow-xl":
            variant === "danger",
        },

        className,
      )}
      {...props}
    >
      {loading ? (
        <>
          <span className="h-5 w-5 animate-spin rounded-full border-2 border-white border-t-transparent" />

          Loading...
        </>
      ) : (
        <>
          {leftIcon && (
            <span className="flex items-center">
              {leftIcon}
            </span>
          )}

          <span>{children}</span>

          {rightIcon && (
            <span className="flex items-center">
              {rightIcon}
            </span>
          )}
        </>
      )}
    </button>
  );
}
