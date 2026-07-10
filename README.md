# 🚀 IssueScout

<div align="center">

# Intelligent GitHub Contribution Assistant

### Discover meaningful open-source contribution opportunities through explainable repository analysis, intelligent issue ranking, confidence scoring, and pull request prediction.

<p>

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)
![Vite](https://img.shields.io/badge/Vite-8-646CFF?logo=vite)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-4-38BDF8?logo=tailwindcss)
![License](https://img.shields.io/badge/License-MIT-green)
![Backend](https://img.shields.io/badge/Backend-Production_Ready-success)
![Frontend](https://img.shields.io/badge/Frontend-Production_Ready-success)
![Tests](https://img.shields.io/badge/Tests-620_Passing-success)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen)
![MyPy](https://img.shields.io/badge/MyPy-Passing-blue)
![Ruff](https://img.shields.io/badge/Ruff-Passing-orange)
![Build](https://img.shields.io/badge/Build-Passing-success)

</p>

### 🚀 Production Ready • 🧠 AI Powered • ⚡ FastAPI • ⚛️ React • 📊 Explainable Predictions

---

IssueScout is an intelligent GitHub repository analysis platform that helps contributors discover high-quality contribution opportunities by analyzing repository activity, issue discussions, pull requests, commit history, repository intelligence, and multiple relationship signals.

Unlike traditional issue search tools, IssueScout explains **why** an issue is recommended through evidence-driven confidence scoring rather than relying only on labels such as **good first issue** or **help wanted**.

</div>

---

# 👥 Who Is IssueScout For?

IssueScout is designed for:

- **Open-source contributors** looking for meaningful issues beyond repository labels.
- **Project maintainers** who want better visibility into issue and pull request relationships.
- **Students and newcomers** exploring real-world open-source projects.
- **Engineering teams** interested in repository analytics and explainable contribution recommendations.

---

# ⚡ Quick Start

Get IssueScout running locally in just a few minutes.

## 1. Clone the Repository

```bash
git clone https://github.com/AnthropicBots/IssueScout.git

cd IssueScout
```

---

## Configure the Backend (Optional but Recommended)

Copy the example environment file and configure your GitHub Personal Access Token.

```bash
cd backend

cp .env.example .env
```

Then edit `.env` and set:

```text
GITHUB_TOKEN=your_personal_access_token
```

IssueScout works without a token, but authenticated requests provide significantly higher GitHub API rate limits.

---

## 2. Start the Backend

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -e .

uvicorn issuescout.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 3. Start the Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# 🎬 Demo

> **Repository → Analysis → Prediction → Confidence → Contribution**

<p align="center">

<img src="docs/assets/demo.gif" alt="IssueScout Demo" width="100%"/>

</p>

IssueScout performs the following workflow automatically:

```text
Repository
      │
      ▼
Fetch Repository Information
      │
      ▼
Fetch Issues
      │
      ▼
Fetch Pull Requests
      │
      ▼
Collect Repository Intelligence
      │
      ▼
Relationship Detection
      │
      ▼
Evidence Collection
      │
      ▼
Confidence Scoring
      │
      ▼
Issue Ranking
      │
      ▼
Interactive Dashboard
```

---

# 📸 Screenshots

## 🏠 Landing Page

<p align="center">

<img src="docs/assets/home.png" width="100%"/>

</p>

---

## 🔍 Repository Scanner

<p align="center">

<img src="docs/assets/scanner.png" width="100%"/>

</p>

---

## 📊 Repository Dashboard

<p align="center">

<img src="docs/assets/dashboard.png" width="100%"/>

</p>

---

## 📑 Issue Intelligence

<p align="center">

<img src="docs/assets/issue-detail.png" width="100%"/>

</p>

---

## 🎯 Key Highlights

- 🔍 Analyze any public GitHub repository
- 🧠 Multi-signal relationship detection engine
- 📈 Explainable confidence scoring
- 🎯 Pull request prediction
- 📊 Repository intelligence dashboard
- ⚡ High-performance FastAPI backend
- 🎨 Modern React + TypeScript frontend
- 📱 Fully responsive interface
- 🧪 620 automated backend tests
- 📈 94% backend test coverage
- ✅ Production-ready architecture
- 📚 Comprehensive documentation
- 🔄 Continuous integration support

---

# 🎯 Why IssueScout?

Finding meaningful issues in large open-source repositories is difficult.

Traditional issue discovery relies heavily on labels like:

- good first issue
- help wanted
- documentation
- enhancement

Unfortunately these labels often become outdated, incomplete, or inconsistent across repositories.

IssueScout instead analyzes actual repository activity.

It combines repository intelligence, issue discussions, commit history, pull requests, review activity, timelines, metadata, and relationship signals to determine which issues are genuinely active and most likely connected to ongoing development.

Instead of simply telling contributors **what** to work on, IssueScout explains **why** an issue is recommended.

---

# 📖 Overview

IssueScout is an intelligent GitHub contribution assistant designed to improve how contributors discover work in open-source projects.

The backend continuously gathers repository intelligence from the GitHub REST API and combines multiple independent analyzers to understand relationships between issues and pull requests.

Each recommendation is accompanied by confidence scores and detailed evidence, making the prediction process transparent and explainable rather than a black-box ranking system.

The frontend presents this information through a modern analytics dashboard that allows contributors to quickly evaluate repositories, inspect issues, understand prediction confidence, and review related pull requests.

IssueScout was designed with three primary goals:

- Help contributors find meaningful work faster.
- Reduce manual repository exploration.
- Provide explainable recommendations backed by evidence.

---

# ✨ Features

## 🎨 Modern Frontend

- React 19
- TypeScript
- Vite
- Tailwind CSS
- React Query
- React Router
- Premium responsive interface
- Interactive repository dashboard
- Issue detail analytics
- Confidence visualizations
- Loading, error, and empty states
- Mobile-friendly design

---

## ⚙️ FastAPI Backend

- High-performance REST API
- Asynchronous repository scanning
- Dependency injection architecture
- Repository intelligence collection
- Candidate pull request discovery
- Resolution analysis
- Confidence calculation
- Ranking engine
- CLI support
- Production-ready architecture

---

## 🧠 Intelligence Engine

IssueScout analyzes numerous repository signals including:

- Repository metadata
- Issue body
- Issue comments
- Timeline events
- Commit history
- Pull requests
- Pull request reviews
- Changed files
- Repository branches
- Labels
- Contributors
- Merge status
- Discussion intelligence

---

## 🔍 Relationship Detection

Multiple analyzers work together to detect issue ↔ pull request relationships.

Current analyzers include:

- Title similarity
- Body similarity
- Author similarity
- Comment references
- Timeline references
- Commit references
- Branch similarity
- Changed file similarity
- Label similarity
- Merge detection
- Review detection
- Repository intelligence

---

## 📈 Prediction Engine

IssueScout produces explainable predictions through:

- Candidate discovery
- Evidence collection
- Confidence scoring
- Issue ranking
- Prediction summaries
- Recommendation generation

Every prediction includes supporting evidence so contributors understand exactly why an issue received its score.

---

# 🏗️ System Architecture

```text
                     React Frontend
                            │
                            ▼
                 React Query + Router
                            │
                            ▼
                    FastAPI REST API
                            │
                            ▼
                 Application Services
                            │
                            ▼
                   Repository Scanner
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
 Repository Data      Pull Requests      GitHub Metadata
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                Repository Intelligence
                            │
                            ▼
                 Candidate Discovery
                            │
                            ▼
                 Relationship Engine
        ├── Title Analyzer
        ├── Body Analyzer
        ├── Timeline Analyzer
        ├── Commit Analyzer
        ├── Review Analyzer
        ├── Metadata Analyzer
        └── Discussion Analyzer
                            │
                            ▼
                  Evidence Collection
                            │
                            ▼
                  Confidence Calculator
                            │
                            ▼
                     Ranking Engine
                            │
                            ▼
                    Prediction Results
                            │
                            ▼
                Interactive Web Dashboard
```

---

# 📂 Project Structure

```text
IssueScout
│
├── backend
│   ├── issuescout
│   │   ├── api
│   │   ├── application
│   │   ├── cli
│   │   ├── github
│   │   ├── intelligence
│   │   ├── models
│   │   ├── prediction
│   │   ├── ranking
│   │   ├── scanner
│   │   ├── services
│   │   └── utils
│   │
│   └── tests
│
├── frontend
│   ├── src
│   ├── public
│   └── dist
│
├── docs
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── LICENSE
└── README.md
```

---

# 🔧 Advanced Setup

## Requirements

Before installing IssueScout, ensure your system has:

| Requirement | Version |
|------------|---------|
| Python | 3.12+ |
| Node.js | 20+ |
| npm | 10+ |
| Git | Latest |
| GitHub Personal Access Token | Recommended |

---

# 📦 Clone Repository

```bash
git clone https://github.com/AnthropicBots/IssueScout.git

cd IssueScout
```

---

# 🖥️ Backend Installation

Create a virtual environment.

```bash
cd backend

python -m venv .venv
```

---

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Backend

```bash
pip install -e .
```

---

## Install Development Tools

```bash
pip install \
pytest \
pytest-cov \
ruff \
mypy \
pre-commit
```

---

## Enable Git Hooks

```bash
pre-commit install
```

---

# 🌐 Frontend Installation

Open another terminal.

```bash
cd frontend

npm install
```

---

## Start Development Server

```bash
npm run dev
```

---

# ⚙️ Configuration

IssueScout works without authentication but using a GitHub Personal Access Token is strongly recommended to avoid GitHub rate limits.

Create a file named:

```text
backend/.env
```

Example:

```env
GITHUB_TOKEN=your_personal_access_token
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| GITHUB_TOKEN | Recommended | GitHub Personal Access Token |
| GITHUB_API | Optional | GitHub API endpoint |
| LOG_LEVEL | Optional | Logging level |

---

# ▶️ Running After Installation

## Backend

```bash
cd backend

uvicorn issuescout.main:app --reload
```

Available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Frontend

```bash
cd frontend

npm run dev
```

Available at:

```
http://localhost:5173
```

---

# 🚀 Production Build

## Backend

```bash
uvicorn issuescout.main:app
```

---

## Frontend

```bash
npm run build
```

Preview production build:

```bash
npm run preview
```

---

# 📁 Project Configuration

## Backend Structure

```text
backend/
    issuescout/
    tests/
    pyproject.toml
```

---

## Frontend Structure

```text
frontend/
    src/
    public/
    package.json
```

---

# 🧪 Development Commands

## Backend

Run tests

```bash
pytest
```

Coverage

```bash
pytest --cov=issuescout
```

Lint

```bash
ruff check .
```

Format

```bash
ruff format .
```

Type Checking

```bash
mypy issuescout
```

---

## Frontend

Development

```bash
npm run dev
```

Lint

```bash
npm run lint
```

Production Build

```bash
npm run build
```

Preview Build

```bash
npm run preview
```

---

# 💡 Typical Development Workflow

```text
Fork Repository
        │
        ▼
Clone Repository
        │
        ▼
Create Feature Branch
        │
        ▼
Implement Changes
        │
        ▼
Run Ruff
        │
        ▼
Run MyPy
        │
        ▼
Run Tests
        │
        ▼
Run Frontend Lint
        │
        ▼
Run Frontend Build
        │
        ▼
Commit Changes
        │
        ▼
Open Pull Request
```

---

# 📚 API Documentation

IssueScout exposes a modern REST API built with **FastAPI**.

Interactive documentation is generated automatically using the OpenAPI specification.

## Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## OpenAPI Schema

```
http://127.0.0.1:8000/openapi.json
```

---

# 🌐 REST API

## Repository

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/github/{owner}/{repo}` | Repository information |

---

## Issues

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/issues/{owner}/{repo}` | Fetch repository issues |

---

## Scanner

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/scan/{owner}/{repo}` | Scan repository |
| GET | `/scan/jobs` | Active scan jobs |
| GET | `/scan/jobs/stats` | Scanner statistics |

---

## Health

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Health status |

---

# 🖥️ Command Line Interface

IssueScout includes a command-line interface for development and repository analysis.

Available commands include:

```text
issuescout scan
issuescout evaluate
issuescout dataset
issuescout version
```

---

# 🧪 Testing

IssueScout includes a comprehensive automated backend test suite.

## Current Status

| Metric | Status |
|---------|--------|
| Backend Tests | ✅ 620 Passing |
| Backend Coverage | ✅ 94% |
| Ruff | ✅ Passing |
| MyPy | ✅ Passing |
| Frontend ESLint | ✅ Passing |
| Frontend Production Build | ✅ Passing |

---

## Run All Tests

```bash
pytest
```

---

## Coverage Report

```bash
pytest --cov=issuescout
```

---

## Specific Test

```bash
pytest tests/scanner/test_engine.py
```

---

## Entire Test Directory

```bash
pytest tests
```

---

# 📈 Test Coverage

Current backend coverage:

```text
94%
```

Coverage includes:

- API
- Scanner
- Repository Fetcher
- Prediction Engine
- Confidence Calculator
- Candidate Discovery
- Resolution Analysis
- Evidence Collection
- Intelligence Collectors
- Ranking
- CLI
- Application Services

---

# 🧹 Code Quality

IssueScout follows strict quality standards.

## Ruff

Lint the backend:

```bash
ruff check .
```

Format the backend:

```bash
ruff format .
```

---

## MyPy

Static type checking:

```bash
mypy issuescout
```

---

## Frontend

Lint:

```bash
npm run lint
```

Build:

```bash
npm run build
```

---

# 🔄 Continuous Integration

Every pull request is automatically validated.

Backend validation includes:

- Ruff
- Ruff Formatting
- MyPy
- Pytest
- Coverage

Frontend validation includes:

- ESLint
- TypeScript Compilation
- Production Build

This ensures every change merged into the project satisfies the same quality standards as the main branch.

---

# 🛠️ Technology Stack

## Backend

- Python 3.12
- FastAPI
- Pydantic
- HTTPX
- AsyncIO

---

## Frontend

- React 19
- TypeScript
- Vite
- Tailwind CSS
- React Query
- React Router
- Lucide React

---

## Testing

- Pytest
- Pytest-Cov

---

## Code Quality

- Ruff
- MyPy
- ESLint

---

## Automation

- GitHub Actions
- Dependabot
- Pre-commit

---

## Development Tools

- Pre-commit
- GitHub Actions
- MyPy
- Ruff
- ESLint

---

## External APIs

- GitHub REST API

---

# 📊 Project Statistics

| Category | Value |
|----------|------:|
| Backend Tests | **620** |
| Backend Coverage | **94%** |
| Python Version | **3.12** |
| Frontend | **React 19** |
| Backend | **FastAPI** |
| Build Status | **Passing** |
| Type Checking | **Passing** |
| Production Build | **Passing** |

---

# 🏆 Quality Assurance

IssueScout has completed the following quality verification:

- ✅ Backend feature complete
- ✅ Frontend feature complete
- ✅ Production-ready architecture
- ✅ 620 automated backend tests
- ✅ 94% backend test coverage
- ✅ Ruff clean
- ✅ Ruff formatted
- ✅ MyPy clean
- ✅ Frontend ESLint passing
- ✅ Frontend production build passing
- ✅ Comprehensive documentation
- ✅ Production-ready release

---

# 🌟 Why IssueScout?

Most GitHub contribution tools focus on filtering issues using labels such as **good first issue** or **help wanted**.

IssueScout goes much further.

Instead of relying on labels alone, it analyzes real repository activity to understand the relationship between issues and ongoing development.

Every recommendation is supported by evidence and confidence scoring, helping contributors make informed decisions before starting work.

---

## 🚀 Core Capabilities

- 🔍 Intelligent repository scanning
- 🧠 Multi-signal relationship detection
- 📈 Explainable confidence scoring
- 🎯 Pull request prediction
- 📊 Repository intelligence
- ⚡ High-performance asynchronous scanning
- 📱 Modern responsive dashboard
- 🧪 Extensive automated testing
- 🏗️ Clean modular architecture
- 📚 Comprehensive documentation

---

# 📈 Project Status

IssueScout is feature complete for its planned v1.0 release and is undergoing final quality polishing before release.

| Component | Status |
|-----------|--------|
| Backend | ✅ Production Ready |
| Frontend | ✅ Production Ready |
| REST API | ✅ Stable |
| CLI | ✅ Stable |
| Repository Scanner | ✅ Stable |
| Candidate Discovery | ✅ Stable |
| Relationship Engine | ✅ Stable |
| Prediction Engine | ✅ Stable |
| Confidence Calculator | ✅ Stable |
| Ranking Engine | ✅ Stable |
| Documentation | ✅ Complete |
| Backend Tests | ✅ 620 Passing |
| Backend Coverage | ✅ 94% |
| Ruff | ✅ Passing |
| MyPy | ✅ Passing |
| ESLint | ✅ Passing |
| Production Build | ✅ Passing |

---

# 🗺️ Roadmap

IssueScout v1.0.0 is feature complete.

Future releases will focus on expanding functionality rather than completing existing features.

## v1.1

- Repository comparison
- Saved scans
- Repository bookmarking
- Better filtering
- Export scan results
- Dark mode
- Keyboard shortcuts

---

## v1.2

- GitHub GraphQL integration
- Incremental repository scanning
- Historical repository analytics
- Improved recommendation engine
- Performance optimizations

---

## v2.0

- User authentication
- Organization dashboards
- Scan history
- Team workspaces
- Notifications
- AI-assisted recommendations
- Docker deployment
- Cloud-hosted IssueScout

---

# 🤝 Contributing

Contributions of every size are welcome.

Whether you're fixing bugs, improving documentation, adding tests, enhancing the frontend, or implementing new features, we'd love your help.

Please read **CONTRIBUTING.md** before opening a pull request.

## Typical Workflow

```text
Fork Repository
      │
      ▼
Create Feature Branch
      │
      ▼
Implement Changes
      │
      ▼
Run Backend Checks
      │
      ▼
Run Frontend Checks
      │
      ▼
Commit Changes
      │
      ▼
Open Pull Request
```

---

# 🧪 Development Checklist

Before submitting a pull request, verify the following.

## Backend

```bash
ruff check .

ruff format .

mypy issuescout

pytest
```

---

## Frontend

```bash
npm run lint

npm run build
```

---

All checks should pass before opening a pull request.

---

# 📚 Documentation

The following documents provide a deeper understanding of IssueScout's architecture and implementation:

- `docs/API.md` — REST API reference.
- `docs/ARCHITECTURE.md` — Overall system architecture.
- `docs/BACKEND.md` — Backend implementation details.
- `docs/SCANNER.md` — Scanner pipeline and relation engine.

Additional project resources include:

- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `ROADMAP.md`

---

# 📄 License

IssueScout is licensed under the **MIT License**.

See the **LICENSE** file for complete license information.

---

# 🙏 Acknowledgements

IssueScout would not have been possible without the incredible open-source ecosystem.

Special thanks to the communities behind:

- Python
- FastAPI
- React
- TypeScript
- Tailwind CSS
- Vite
- Pydantic
- HTTPX
- Pytest
- Ruff
- GitHub REST API
- GitHub Actions

Thank you to everyone who contributes to open source.

---

# 👨‍💻 Maintainers

IssueScout is maintained by the **AnthropicBots** organization.

Project Lead

**Bhuvansh Kataria**

GitHub: https://github.com/BHUVANSH855

Organization: https://github.com/AnthropicBots

---

# ❤️ Support

If you find IssueScout useful, consider supporting the project.

You can help by:

- ⭐ Starring the repository
- 🍴 Forking the project
- 🐛 Reporting bugs
- 💡 Suggesting features
- 📖 Improving documentation
- 🧪 Adding tests
- 🚀 Opening pull requests
- 📢 Sharing the project

Every contribution helps make IssueScout better for the entire open-source community.

---

<div align="center">

# 🚀 IssueScout v1.0.0

### Intelligent GitHub Repository Analysis

**Explainable • Evidence Driven • Production Ready**

Made with ❤️ for the Open Source Community.

If this project helped you, consider leaving a ⭐ on GitHub.

</div>
