import type {
  InputHTMLAttributes,
  ReactNode,
} from "react";

import clsx from "clsx";

type InputSize =
  | "sm"
  | "md"
  | "lg";

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
        <div className="pointer-events-none absolute inset-y-0 left-5 flex items-center text-slate-400 transition-colors">
          {leftIcon}
        </div>
      )}

      <input
        disabled={disabled}
        className={clsx(
          "w-full rounded-2xl border bg-white text-slate-900 shadow-sm",
          "placeholder:text-slate-400",
          "transition-all duration-300",
          "caret-blue-600",
          "focus:border-blue-500 focus:outline-none focus:ring-4 focus:ring-blue-500/10 focus:shadow-md",
          "disabled:cursor-not-allowed disabled:border-slate-200 disabled:bg-slate-100 disabled:text-slate-400",

          {
            // Error

            "border-red-300 focus:border-red-500 focus:ring-red-500/10":
              error,

            // Normal

            "border-slate-300 hover:border-slate-400":
              !error,

            // Icons

            "pl-14": leftIcon,

            "pr-14": rightIcon,

            // Sizes

            "px-4 py-2.5 text-sm":
              inputSize === "sm",

            "px-5 py-3.5 text-base":
              inputSize === "md",

            "px-6 py-4.5 text-lg":
              inputSize === "lg",
          },

          className,
        )}
        {...props}
      />

      {rightIcon && (
        <div className="absolute inset-y-0 right-5 flex items-center text-slate-400 transition-colors">
          {rightIcon}
        </div>
      )}
    </div>
  );
}
