import {
  Activity,
  Brain,
  GitBranch,
  ShieldCheck,
} from "lucide-react";

export default function TrustSection() {
  const features = [
    {
      icon: <Brain size={28} />,
      title: "AI Predictions",
      description:
        "Predict issue-to-pull-request relationships with confidence scoring.",
    },
    {
      icon: <GitBranch size={28} />,
      title: "Repository Analysis",
      description:
        "Analyze GitHub repositories in real time using your backend engine.",
    },
    {
      icon: <Activity size={28} />,
      title: "Contribution Insights",
      description:
        "Instantly identify issues ready for contributors.",
    },
    {
      icon: <ShieldCheck size={28} />,
      title: "Production Ready",
      description:
        "Built with React, TypeScript, FastAPI and modern architecture.",
    },
  ];

  return (
    <section className="my-16">

      <div className="mb-10 text-center">

        <h2 className="text-3xl font-bold">
          Why IssueScout?
        </h2>

        <p className="mt-3 text-slate-600">
          Everything you need to discover, analyze and contribute to GitHub projects.
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        {features.map((feature) => (
          <div
            key={feature.title}
            className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg"
          >
            <div className="mb-4 inline-flex rounded-xl bg-blue-100 p-3 text-blue-600">
              {feature.icon}
            </div>

            <h3 className="text-lg font-semibold">
              {feature.title}
            </h3>

            <p className="mt-3 text-sm leading-6 text-slate-600">
              {feature.description}
            </p>
          </div>
        ))}

      </div>

    </section>
  );
}
