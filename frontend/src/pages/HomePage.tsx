import HeroSection from "../components/repository/HeroSection";
import RepositorySearchForm from "../components/repository/RepositorySearchForm";
import TrustSection from "../components/repository/TrustSection";

export default function HomePage() {
  return (
    <main className="relative overflow-hidden pb-24">
      {/* Background */}

      <div className="pointer-events-none absolute inset-0 -z-10">
        <div className="absolute left-0 top-0 h-96 w-96 rounded-full bg-blue-500/10 blur-3xl" />

        <div className="absolute right-0 top-1/3 h-[30rem] w-[30rem] rounded-full bg-cyan-400/10 blur-3xl" />

        <div className="absolute bottom-0 left-1/3 h-[26rem] w-[26rem] rounded-full bg-indigo-400/10 blur-3xl" />
      </div>

      <div className="space-y-24">
        {/* Hero */}

        <HeroSection />

        {/* About */}

        <section
          id="about-issuescout"
          className="scroll-mt-24"
        >
          <div className="mb-12 text-center">
            <div className="inline-flex items-center rounded-full border border-blue-200 bg-blue-50 px-4 py-2 text-sm font-semibold text-blue-700">
              Why Developers Choose IssueScout
            </div>

            <h2 className="mt-6 text-4xl font-black tracking-tight text-slate-900">
              Built for Open Source Contributors
            </h2>

            <p className="mx-auto mt-5 max-w-3xl text-lg leading-8 text-slate-600">
              Discover contribution opportunities using
              intelligent repository analysis, pull request
              prediction, confidence scoring, and repository
              intelligence—all in one modern dashboard.
            </p>
          </div>

          <TrustSection />
        </section>

        {/* Scanner */}

        <section
          id="repository-scanner"
          className="scroll-mt-24"
        >
          <div className="mx-auto mb-12 max-w-4xl text-center">
            <div className="inline-flex items-center rounded-full border border-cyan-200 bg-cyan-50 px-4 py-2 text-sm font-semibold text-cyan-700">
              AI Repository Scanner
            </div>

            <h2 className="mt-6 text-4xl font-black tracking-tight text-slate-900">
              Analyze Any GitHub Repository
            </h2>

            <p className="mx-auto mt-5 max-w-3xl text-lg leading-8 text-slate-600">
              Enter a GitHub repository to generate issue
              intelligence, contributor insights, confidence
              scores, and linked pull request predictions
              within seconds.
            </p>
          </div>

          <RepositorySearchForm />
        </section>
      </div>
    </main>
  );
}
