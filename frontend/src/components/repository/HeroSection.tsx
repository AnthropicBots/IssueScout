import {
  ArrowRight,
  CheckCircle2,
  GitBranch,
  SearchCheck,
  Sparkles,
  Target,
} from "lucide-react";

import heroImage from "../../assets/hero.png";

import Button from "../ui/Button";

export default function HeroSection() {
  const scrollToScanner = () => {
    document.getElementById("repository-scanner")?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  };

  const scrollToAbout = () => {
    document.getElementById("about-issuescout")?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  };

  return (
    <section
      className="
        relative
        overflow-hidden
        rounded-[2rem]
        border
        border-white/10
        bg-gradient-to-br
        from-slate-950
        via-slate-900
        to-blue-950
        px-6
        py-16
        text-white
        shadow-[0_30px_80px_rgba(15,23,42,0.35)]
        sm:px-8
        lg:px-16
        lg:py-20
      "
    >
      {/* Background Effects */}
      <div className="absolute -left-24 -top-24 h-72 w-72 rounded-full bg-blue-500/20 blur-3xl" />
      <div className="absolute -bottom-24 -right-24 h-80 w-80 rounded-full bg-cyan-400/20 blur-3xl" />

      <div className="relative grid items-center gap-16 lg:grid-cols-2">
        {/* Left Content */}
        <div>
          <div className="mb-8 inline-flex items-center gap-2 rounded-full border border-cyan-400/20 bg-white/5 px-4 py-2 text-sm font-medium text-cyan-100 backdrop-blur-xl">
            <Sparkles size={16} className="text-cyan-300" />
            AI-Powered GitHub Repository Intelligence
          </div>

          <h1 className="max-w-3xl text-5xl font-black leading-tight tracking-tight lg:text-6xl">
            Discover
            <span className="block bg-gradient-to-r from-cyan-300 via-sky-300 to-indigo-300 bg-clip-text text-transparent">
              High-Quality GitHub Issues
            </span>

            <span className="block text-slate-200">
              Faster Than Ever
            </span>
          </h1>

          <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-300">
            Analyze repositories with AI, discover contributor-friendly
            issues, predict pull request relationships, evaluate confidence
            scores, and identify the best opportunities for meaningful
            open-source contributions—all in one place.
          </p>

          <div className="mt-10 flex flex-wrap gap-4">
            <Button
              variant="primary"
              size="lg"
              rightIcon={<ArrowRight size={18} />}
              onClick={scrollToScanner}
            >
              Start Scanning
            </Button>

            <Button
              variant="outline"
              size="lg"
              className="border-white/30 bg-white/10 text-white hover:bg-white/20"
              onClick={scrollToAbout}
            >
              Learn More
            </Button>
          </div>

          <div className="mt-12 grid gap-5 sm:grid-cols-2">
            <div className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/5 px-4 py-3 backdrop-blur-sm transition-all duration-200 hover:border-cyan-400/20 hover:bg-white/10">
              <CheckCircle2 className="text-green-400" />
              <span>Repository Analysis</span>
            </div>

            <div className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/5 px-4 py-3 backdrop-blur-sm transition-all duration-200 hover:border-cyan-400/20 hover:bg-white/10">
              <Target className="text-cyan-300" />
              <span>Confidence Scoring</span>
            </div>

            <div className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/5 px-4 py-3 backdrop-blur-sm transition-all duration-200 hover:border-cyan-400/20 hover:bg-white/10">
              <GitBranch className="text-blue-300" />
              <span>PR Relationship Detection</span>
            </div>

            <div className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/5 px-4 py-3 backdrop-blur-sm transition-all duration-200 hover:border-cyan-400/20 hover:bg-white/10">
              <SearchCheck className="text-amber-300" />
              <span>Contribution Insights</span>
            </div>
          </div>
        </div>

        {/* Right Content */}
        <div className="relative flex items-center justify-center">
          <div className="absolute h-80 w-80 rounded-full bg-blue-500/20 blur-3xl" />

          <img
            src={heroImage}
            alt="IssueScout Dashboard Preview"
            className="relative z-10 w-[90%] max-w-md object-contain drop-shadow-[0_40px_80px_rgba(37,99,235,0.35)] transition-transform duration-500 hover:scale-[1.02] lg:max-w-xl"
          />
        </div>
      </div>
    </section>
  );
}
