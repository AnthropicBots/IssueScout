# 🚀 IssueScout

<div align="center">

# Intelligent GitHub Contribution Assistant

**Discover meaningful GitHub contribution opportunities through evidence-driven repository analysis, intelligent issue ranking, and explainable pull request prediction.**

<p>

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)
![Vite](https://img.shields.io/badge/Vite-7-646CFF?logo=vite)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-484%20Passing-success)
![MyPy](https://img.shields.io/badge/MyPy-Passing-blue)
![Ruff](https://img.shields.io/badge/Ruff-Passing-orange)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=githubactions)

</p>

**Backend:** ✅ Production Ready &nbsp;&nbsp;|&nbsp;&nbsp;
**Frontend:** ✅ Complete &nbsp;&nbsp;|&nbsp;&nbsp;
**Documentation:** 🚧 Improving

</div>

---

## 🎬 Demo

> **See IssueScout in action**

<p align="center">

<img src="docs/assets/demo.gif" alt="IssueScout Demo" width="100%">

</p>

> **Demo workflow**
>
> Repository → Scan → Intelligent Analysis → Ranked Issues → PR Prediction → Confidence Score

---

## 📸 Screenshots

| Home | Repository Analysis |
|------|----------------------|
| ![](docs/assets/home.png) | ![](docs/assets/results.png) |

| Issue Details | Prediction View |
|---------------|-----------------|
| ![](docs/assets/issue-details.png) | ![](docs/assets/prediction.png) |

---

# ⚡ Quick Start

Get IssueScout running in under 5 minutes.

```bash
git clone https://github.com/AnthropicBots/IssueScout.git

cd IssueScout/backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -e .

uvicorn issuescout.main:app --reload
```

Then start the frontend:

```bash
cd ../frontend

npm install

npm run dev
```

- 🌐 Frontend: http://localhost:5173
- 📖 API Docs: http://127.0.0.1:8000/docs

---

# 🎯 Why Use IssueScout?

Finding meaningful issues in large open-source repositories can be time-consuming.

IssueScout analyzes multiple repository signals to help contributors focus on the most promising opportunities.

| Traditional GitHub Search | IssueScout |
|---------------------------|------------|
| Manual issue browsing | ✅ Automated repository analysis |
| Depends on labels | ✅ Multi-signal ranking |
| No confidence estimation | ✅ Confidence scoring |
| Limited issue context | ✅ Explainable predictions |
| No PR relationship analysis | ✅ Issue ↔ Pull Request prediction |

---

# 🚀 Key Highlights

- 🔍 Analyze any public GitHub repository
- 🧠 Multi-signal issue and pull request relation engine
- 📊 Explainable confidence scoring
- ⚡ FastAPI backend with asynchronous scanning
- 🎨 Modern React + TypeScript frontend
- 🧪 484+ automated tests
- 🔄 GitHub Actions CI with Ruff & MyPy
- 📚 Comprehensive documentation
- 🏗️ Clean, modular, production-ready architecture

---

# 📖 Overview

IssueScout is an intelligent GitHub contribution assistant that helps developers discover meaningful open-source contribution opportunities through evidence-driven repository analysis.

Instead of relying solely on labels like **good first issue** or **help wanted**, IssueScout analyzes repository activity, issue discussions, commits, pull requests, reviews, timelines, and metadata to identify meaningful relationships between issues and development activity.

Its explainable ranking engine provides confidence scores and supporting evidence for every prediction, helping contributors understand *why* an issue is recommended rather than simply presenting a ranked list.

Built with a modern React frontend and a FastAPI backend, IssueScout is designed to work with any public GitHub repository while remaining fast, transparent, and extensible.

---

# ✨ Features

## 🎨 Frontend

- Modern React + TypeScript interface
- Repository search
- Live repository scan progress
- Responsive layout
- Result cards
- Error and loading states
- Fast Vite development experience

---

## ⚙️ Backend

- FastAPI REST API
- Asynchronous repository scanning
- Evidence collection pipeline
- Repository metadata analysis
- Issue filtering
- Confidence scoring
- JSON response models

---

## 🧠 Relation Engine

IssueScout combines multiple independent detectors including:

- Author similarity
- Title similarity
- Body references
- Timeline references
- Commit references
- Commit message references
- Branch similarity
- Reviewer similarity
- File similarity
- Label similarity
- Repository metadata similarity

---

## 📊 Prediction Engine

- Intelligent pull request prediction
- Explainable results
- Candidate ranking
- Confidence scoring

---

## 🛠️ Developer Experience

- Ruff
- MyPy
- Pytest
- GitHub Actions
- Pre-commit
- Dependabot
- Structured logging
- Modular architecture

---

# 📊 Example Repository Analysis

Repository:

```text
python/cpython
```

Issue Selected:

```text
#152997
Add an iconv-based codec engine to support all system locale encodings
```

IssueScout Analysis:

| Metric | Result |
|---------|--------|
| Repository Scan | ✅ Completed |
| Confidence Score | 94% |
| Related Pull Requests | 3 Candidates |
| Evidence Signals | 11 |
| Ranking | Top Recommendation |

Example Evidence

- ✅ Title similarity detected
- ✅ Commit reference found
- ✅ Timeline activity matched
- ✅ Author relationship detected
- ✅ Repository metadata similarity

> Every recommendation is accompanied by supporting evidence so contributors can understand **why** it was ranked.

# 🏗️ System Architecture

```text
                  React Frontend
                        │
                        ▼
                 FastAPI Backend
                        │
                        ▼
                Repository Scanner
                        │
                        ▼
              GitHub REST API Client
                        │
                        ▼
               Evidence Collection
        ├── Timeline Events
        ├── Issue Comments
        ├── Commit History
        ├── Pull Requests
        └── Repository Metadata
                        │
                        ▼
                 Relation Engine
        ├── Author Similarity
        ├── Title Similarity
        ├── Timeline References
        ├── Commit References
        ├── Branch Similarity
        ├── File Similarity
        └── Metadata Similarity
                        │
                        ▼
               Prediction Engine
                        │
                        ▼
                Confidence Scoring
                        │
                        ▼
                 Ranked Results API
```

---

# 📂 Project Structure

```text
IssueScout/
│
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── dependabot.yml
│
├── backend/
│   ├── issuescout/
│   │   ├── api/
│   │   ├── core/
│   │   ├── evidence/
│   │   ├── github/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── output/
│   │   ├── prediction/
│   │   ├── presentation/
│   │   ├── ranking/
│   │   ├── scanner/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── tests/
│   └── pyproject.toml
│
├── docs/
├── frontend/
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── LICENSE
└── README.md
```

---

# ⚡ Installation

## Prerequisites

Before getting started, ensure you have:

- Python 3.12 or later
- Git
- A GitHub Personal Access Token (recommended to avoid rate limits)

---

## Clone the Repository

```bash
git clone https://github.com/AnthropicBots/IssueScout.git

cd IssueScout
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv
```

---

## Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Backend Dependencies

Install IssueScout in editable mode:

```bash
pip install -e .
```

Install development dependencies:

```bash
pip install pytest pytest-cov ruff mypy pre-commit
```

Enable Git hooks:

```bash
pre-commit install
```

---

## Install Frontend Dependencies

Open another terminal.

```bash
cd ../frontend

npm install
```

---

# ⚙️ Configuration

Create a `.env` file inside the `backend` directory.

```env
GITHUB_TOKEN=your_github_personal_access_token
```

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GITHUB_TOKEN` | Recommended | GitHub Personal Access Token |
| `GITHUB_API` | Optional | GitHub REST API endpoint |

---

# ▶️ Running the Application

## Backend

```bash
cd backend

uvicorn issuescout.main:app --reload
```

Backend API:

```
http://127.0.0.1:8000
```

Interactive API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend

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

# 📚 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

OpenAPI Schema

```
http://127.0.0.1:8000/openapi.json
```

---

# 🌐 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Health check |
| GET | `/github` | Repository information |
| GET | `/issues` | List repository issues |
| GET | `/scan/{owner}/{repo}` | Scan a GitHub repository |

---

# 🧪 Testing

Run the complete test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=issuescout
```

Run a specific test:

```bash
pytest tests/github/test_client.py
```

Run all GitHub-related tests:

```bash
pytest tests/github
```

Current status:

- ✅ 484 automated tests passing
- ✅ Ruff linting passing
- ✅ MyPy static type checking passing
- ✅ High test coverage
- ✅ GitHub Actions CI
- ✅ Production-ready backend

---

# 🧹 Code Quality

Lint the project:

```bash
ruff check .
```

Automatically format code:

```bash
ruff format .
```

Run all pre-commit hooks:

```bash
pre-commit run --all-files
```

---

# 🔄 Continuous Integration

IssueScout uses GitHub Actions for continuous integration.

Every push and pull request automatically runs:

- Ruff linting
- Ruff formatting checks
- Complete test suite
- Coverage reporting

Dependabot automatically keeps:

- Python dependencies updated
- GitHub Actions updated

---

# 🛠️ Technology Stack

## Backend

- Python 3.12
- FastAPI
- Pydantic
- HTTPX
- AsyncIO

## Frontend

- React 19
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Lucide React

## Testing

- Pytest
- Pytest-Cov

## Code Quality

- Ruff
- Pre-commit

## Automation

- GitHub Actions
- Dependabot

## APIs

- GitHub REST API

---

# 📦 What Makes IssueScout Different?

Unlike traditional GitHub search tools, IssueScout focuses on understanding repository activity rather than simply filtering issues by labels.

### Core Capabilities

- 🔍 Repository-wide evidence collection
- 🧠 Multi-signal relation analysis
- 📈 Explainable issue ranking
- 🎯 Pull request prediction
- 📊 Confidence scoring
- ⚡ Asynchronous repository scanning
- 🏗️ Modular architecture
- 🧪 Extensive automated testing
- 🔄 Continuous integration
- 📚 Comprehensive documentation

IssueScout is designed to help contributors spend less time searching and more time contributing.

---

# 📈 Project Maturity

IssueScout is actively developed and maintained.

Current project status:

| Component | Status |
|-----------|--------|
| Frontend | ✅ Complete |
| Backend | ✅ Complete |
| REST API | ✅ Stable |
| Repository Scanner | ✅ Stable |
| Evidence Collection | ✅ Stable |
| Relation Engine | ✅ Stable |
| Prediction Engine | ✅ Stable |
| Ranking Engine | ✅ Stable |
| Automated Tests | ✅ 484 Passing |
| Ruff | ✅ Passing |
| MyPy | ✅ Passing |
| GitHub Actions | ✅ Enabled |
| Documentation | 🚧 Improving |

---

# 🗺️ Roadmap

## ✅ Completed

- Modern React frontend
- FastAPI backend
- Repository scanner
- Evidence collection pipeline
- Relation engine
- Confidence scoring
- Ranking engine
- REST API
- CLI support
- Comprehensive automated testing
- Ruff linting
- MyPy static type checking
- GitHub Actions CI

---

## 🚀 Future Enhancements

- GitHub GraphQL support
- AI-assisted issue recommendations
- Scan history
- Repository analytics dashboard
- Browser extension
- Plugin system
- Saved repositories
- User authentication
- Docker deployment

---

# 🤝 Contributing

Contributions are always welcome!

Whether you'd like to:

- Report a bug
- Suggest a feature
- Improve documentation
- Write tests
- Refactor existing code
- Improve performance

your contributions are appreciated.

Please read the project's **CONTRIBUTING.md** before opening a pull request.

Typical workflow:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Run Ruff and the test suite.
5. Commit your work.
6. Open a Pull Request.

---

# 🧪 Development Workflow

Install pre-commit hooks:

```bash
pre-commit install
```

Before committing:

```bash
ruff check .

ruff format .

python -m pytest

mypy issuescout
```

If all checks pass, commit your changes.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for details.

---

# 🙏 Acknowledgements

IssueScout is built using several excellent open-source projects.

Special thanks to the communities behind:

- Python
- FastAPI
- Pydantic
- HTTPX
- Pytest
- Ruff
- GitHub REST API
- GitHub Actions

Their work makes projects like IssueScout possible.

---

# 👨‍💻 Maintainers

**IssueScout** is maintained by the **AnthropicBots** organization.

Originally created and developed by [**Bhuvansh Kataria**](https://github.com/BHUVANSH855).

GitHub Organization:

**https://github.com/AnthropicBots**

---

# ⭐ Support the Project

If you find IssueScout useful, consider:

- ⭐ Starring the repository
- 🍴 Forking the project
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing code
- 📢 Sharing the project with others

Every contribution—big or small—helps improve IssueScout.

---

<div align="center">

## 🚀 Happy Contributing!

Made with ❤️ for the open-source community.

**IssueScout — Helping developers discover meaningful GitHub contributions.**

</div>
