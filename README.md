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

# 📖 Overview

> **Production-ready full-stack application** built to help developers identify high-quality GitHub contribution opportunities using evidence-driven analysis and explainable issue ranking.

> **IssueScout** helps developers quickly discover meaningful open-source contribution opportunities by combining repository analysis, evidence collection, intelligent ranking, and explainable issue evaluation in a modern full-stack application.

IssueScout is an intelligent GitHub contribution assistant designed to help developers discover meaningful open-source contribution opportunities.

Rather than relying solely on labels such as **good first issue** or **help wanted**, IssueScout analyzes multiple signals across a repository to identify relationships between issues and pull requests.

The project combines GitHub repository metadata, issue timelines, commits, comments, reviews, and multiple similarity algorithms to produce explainable predictions about issue activity.

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

# 🏗️ High-Level Architecture

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

# 💡 Why IssueScout?

Traditional GitHub searches depend heavily on repository labels and manual inspection.

IssueScout improves this process by combining evidence from multiple GitHub resources into a unified prediction engine that helps contributors understand:

- Which issues are likely already linked to pull requests.
- How issues relate to commits and discussions.
- The confidence of each prediction.
- Why a prediction was made.

This makes repository exploration faster, more transparent, and easier to understand.

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

# 📡 Available Endpoints

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

# 📦 Project Highlights

- Modular architecture
- Asynchronous GitHub client
- Evidence-based repository analysis
- Intelligent relation engine
- Explainable prediction system
- Structured logging
- Global exception handling
- Request logging middleware
- Response models
- Pagination utilities
- Automated testing
- Continuous integration
- Production-ready project structure

---

# 📈 Project Status

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

Originally created and developed by **Bhuvansh Kataria**.

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
