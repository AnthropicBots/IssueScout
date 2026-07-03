import type { InputHTMLAttributes, ReactNode } from "react";

import clsx from "clsx";

type InputSize = "sm" | "md" | "lg";

interface InputProps
  extends InputHTMLAttributes<HTMLInputElement> {
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  error?: boolean;
  inputSize?: InputSize;
}

export default function Input({
  className,
  leftIcon,
  rightIcon,
  error = false,
  inputSize = "md",
  disabled,
  ...props
}: InputProps) {
  return (
    <div className="relative w-full">

      {leftIcon && (
        <div className="pointer-events-none absolute inset-y-0 left-4 flex items-center text-slate-400">
          {leftIcon}
        </div>
      )}

      <input
        disabled={disabled}
        className={clsx(
          "w-full rounded-xl border bg-white text-slate-900 caret-blue-600 transition-all duration-200",
          "placeholder:text-slate-400",
          "focus:outline-none focus:ring-2 focus:ring-blue-500/20",
          "disabled:cursor-not-allowed disabled:bg-slate-100 disabled:text-slate-400",

          {
            "border-red-400 focus:border-red-500 focus:ring-red-200":
              error,

            "border-slate-300 focus:border-blue-500":
              !error,

            "pl-12": leftIcon,

            "pr-12": rightIcon,

            "px-3 py-2 text-sm":
              inputSize === "sm",

            "px-4 py-3 text-base":
              inputSize === "md",

            "px-5 py-4 text-lg":
              inputSize === "lg",
          },

          className,
        )}
        {...props}
      />

      {rightIcon && (
        <div className="absolute inset-y-0 right-4 flex items-center text-slate-400">
          {rightIcon}
        </div>
      )}

    </div>
  );
}
