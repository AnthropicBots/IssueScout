import HeroSection from "../components/repository/HeroSection";
import RepositorySearchForm from "../components/repository/RepositorySearchForm";
import TrustSection from "../components/repository/TrustSection";

export default function HomePage() {
  return (
    <main className="space-y-16 pb-20">

      {/* Hero */}

      <HeroSection />

      {/* Why IssueScout */}

      <section id="about-issuescout">
        <TrustSection />
      </section>

      {/* Repository Scanner */}

      <section id="repository-scanner">

        <div className="mb-8 text-center">

          <h2 className="text-3xl font-bold text-slate-900">
            Analyze a GitHub Repository
          </h2>

          <p className="mt-3 text-lg text-slate-600">
            Enter a repository owner and name to discover contribution
            opportunities, confidence scores, and linked pull requests.
          </p>

        </div>

        <RepositorySearchForm />

      </section>

    </main>
  );
}
