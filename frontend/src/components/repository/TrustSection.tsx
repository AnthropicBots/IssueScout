import {
  Activity,
  Brain,
  GitBranch,
  ShieldCheck,
} from "lucide-react";

export default function TrustSection() {
  const features = [
    {
      icon: <Brain size={30} />,
      title: "AI-Powered Predictions",
      description:
        "Leverage intelligent analysis to predict issue-to-pull-request relationships with confidence scoring.",
      color: "from-cyan-500 to-blue-600",
    },
    {
      icon: <GitBranch size={30} />,
      title: "Repository Intelligence",
      description:
        "Analyze GitHub repositories in real time using IssueScout's advanced backend analysis engine.",
      color: "from-indigo-500 to-violet-600",
    },
    {
      icon: <Activity size={30} />,
      title: "Contributor Insights",
      description:
        "Instantly identify high-quality issues that are ready for new contributors and open-source collaboration.",
      color: "from-emerald-500 to-green-600",
    },
    {
      icon: <ShieldCheck size={30} />,
      title: "Production Ready",
      description:
        "Built with React, TypeScript, FastAPI, modern architecture, and a scalable AI-powered analysis pipeline.",
      color: "from-orange-500 to-red-500",
    },
  ];

  return (
    <section
      id="about-issuescout"
      className="my-20"
    >
      {/* Section Header */}

      <div className="mx-auto mb-14 max-w-3xl text-center">
        <span className="inline-flex rounded-full border border-blue-200 bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
          Why Choose IssueScout?
        </span>

        <h2 className="mt-6 text-4xl font-extrabold tracking-tight text-slate-900 lg:text-5xl">
          Built for Modern Open Source Contributors
        </h2>

        <p className="mt-5 text-lg leading-8 text-slate-600">
          IssueScout combines intelligent repository analysis,
          prediction models, and contributor insights to help
          developers discover the right issues faster and make
          meaningful open-source contributions.
        </p>
      </div>

      {/* Feature Cards */}

      <div className="grid gap-8 md:grid-cols-2 xl:grid-cols-4">
        {features.map((feature) => (
          <div
            key={feature.title}
            className="group relative overflow-hidden rounded-[1.75rem] border border-slate-200 bg-white p-8 shadow-sm transition-all duration-300 hover:-translate-y-2 hover:border-blue-200 hover:shadow-2xl"
          >
            {/* Background Accent */}

            <div className="absolute inset-x-0 top-0 h-1 bg-gradient-to-r opacity-0 transition-opacity duration-300 group-hover:opacity-100">
              <div
                className={`h-full w-full bg-gradient-to-r ${feature.color}`}
              />
            </div>

            {/* Icon */}

            <div
              className={`mb-6 inline-flex rounded-2xl bg-gradient-to-br ${feature.color} p-4 text-white shadow-lg transition-transform duration-300 group-hover:scale-110`}
            >
              {feature.icon}
            </div>

            {/* Content */}

            <h3 className="text-xl font-bold text-slate-900 transition-colors group-hover:text-blue-700">
              {feature.title}
            </h3>

            <p className="mt-4 leading-7 text-slate-600">
              {feature.description}
            </p>

            {/* Bottom Accent */}

            <div className="mt-8 flex items-center text-sm font-semibold text-blue-600 opacity-0 transition-all duration-300 group-hover:opacity-100">
              Learn More →
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
