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
  return (
    <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 px-8 py-16 text-white shadow-2xl lg:px-16">

      {/* Background Blur */}

      <div className="absolute -left-24 -top-24 h-72 w-72 rounded-full bg-blue-500/20 blur-3xl" />

      <div className="absolute -bottom-24 -right-24 h-80 w-80 rounded-full bg-cyan-400/20 blur-3xl" />

      <div className="relative grid items-center gap-12 lg:grid-cols-2">

        {/* Left */}

        <div>

          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-blue-400/30 bg-white/10 px-4 py-2 text-sm backdrop-blur">

            <Sparkles size={16} />

            AI Powered GitHub Analysis

          </div>

          <h1 className="text-5xl font-extrabold leading-tight lg:text-6xl">

            Discover the
            <span className="block bg-gradient-to-r from-cyan-300 to-blue-300 bg-clip-text text-transparent">
              Right GitHub Issues
            </span>

          </h1>

          <p className="mt-6 max-w-xl text-lg leading-8 text-slate-300">

            IssueScout intelligently analyzes GitHub repositories,
            predicts pull request relationships, identifies assignment
            status, and helps contributors discover the best issues
            to work on.

          </p>

          <div className="mt-8 flex flex-wrap gap-4">

            <Button
              variant="primary"
              size="lg"
              rightIcon={<ArrowRight size={18} />}
            >
              Start Scanning
            </Button>

            <Button
              variant="outline"
              size="lg"
              className="border-white/30 bg-white/10 text-white hover:bg-white/20"
            >
              Learn More
            </Button>

          </div>

          <div className="mt-10 grid gap-4 sm:grid-cols-2">

            <div className="flex items-center gap-3">

              <CheckCircle2 className="text-green-400" />

              <span>Repository Analysis</span>

            </div>

            <div className="flex items-center gap-3">

              <Target className="text-cyan-300" />

              <span>Confidence Scoring</span>

            </div>

            <div className="flex items-center gap-3">

              <GitBranch className="text-blue-300" />

              <span>PR Relationship Detection</span>

            </div>

            <div className="flex items-center gap-3">

              <SearchCheck className="text-amber-300" />

              <span>Contribution Insights</span>

            </div>

          </div>

        </div>

        {/* Right */}

        <div className="relative flex justify-center">

          <div className="absolute h-72 w-72 rounded-full bg-blue-500/20 blur-3xl" />

          <img
            src={heroImage}
            alt="IssueScout Dashboard Preview"
            className="relative w-full max-w-lg drop-shadow-2xl"
          />

        </div>

      </div>

    </section>
  );
}
