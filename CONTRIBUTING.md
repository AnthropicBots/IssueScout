# Contributing to IssueScout

First off, thank you for your interest in contributing to **IssueScout**! 🎉

IssueScout is an open-source platform for intelligent GitHub repository analysis and contribution discovery. We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, tests, UI enhancements, and performance optimizations.

---

# 📋 Before You Start

Before opening an issue or pull request, please:

- Search existing issues and pull requests.
- Read this guide completely.
- Keep pull requests focused on a single change.
- Discuss large features in an issue before implementation.

---

# 🚀 Development Setup

## 1. Fork the Repository

Fork the repository on GitHub.

---

## 2. Clone Your Fork

```bash
git clone https://github.com/<your-username>/IssueScout.git

cd IssueScout
```

---

## 3. Add the Upstream Repository

```bash
git remote add upstream https://github.com/AnthropicBots/IssueScout.git
```

Verify remotes:

```bash
git remote -v
```

---

# ⚙️ Backend Setup

## Create a Virtual Environment

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Backend

```bash
cd backend

pip install -e .
```

---

## Install Development Dependencies

```bash
pip install pytest pytest-cov ruff mypy pre-commit
```

---

# 🎨 Frontend Setup

```bash
cd frontend

npm install
```

Run the development server:

```bash
npm run dev
```

---

# 🌿 Creating a Branch

Always create a new branch before making changes.

Examples:

```text
feature/repository-comparison

fix/scanner-timeout

docs/update-readme

test/repository-intelligence

refactor/evidence-builder
```

---

# 🧪 Backend Validation

Run these commands before opening a pull request.

Run tests:

```bash
pytest
```

Run coverage:

```bash
pytest --cov=issuescout
```

Lint:

```bash
ruff check .
```

Format:

```bash
ruff format .
```

Type checking:

```bash
mypy issuescout
```

---

# 🖥️ Frontend Validation

Lint:

```bash
npm run lint
```

Production build:

```bash
npm run build
```

---

# 🔄 Pre-commit

Install hooks:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

---

# 💬 Commit Messages

IssueScout follows the **Conventional Commits** specification.

Examples:

```text
feat: add repository comparison

fix: prevent scanner timeout

docs: update API documentation

test: improve evidence collector coverage

refactor: simplify repository fetcher
```

---

# 🔀 Pull Requests

Before submitting a pull request, ensure that:

- Backend tests pass.
- Ruff passes.
- MyPy passes.
- Frontend lint passes.
- Frontend production build succeeds.
- New functionality includes appropriate tests.
- Documentation has been updated if necessary.
- Your branch is up to date with the latest default branch.

---

# 📝 Development Workflow

A typical contribution follows this workflow:

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
Run Backend Checks
        │
        ▼
Run Frontend Checks
        │
        ▼
Commit Changes
        │
        ▼
Push Branch
        │
        ▼
Open Pull Request
```

---

# 🐞 Reporting Bugs

When opening a bug report, please include:

- Operating system
- Python version
- Node.js version
- Browser (if frontend-related)
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages or logs
- Screenshots (if applicable)

---

# 💡 Feature Requests

Feature requests are welcome.

Please describe:

- The problem you're trying to solve.
- Your proposed solution.
- Alternative approaches you've considered.
- Any additional context or examples.

---

# 📚 Documentation

Documentation improvements are always appreciated.

Useful areas include:

- README
- API documentation
- Architecture
- Backend
- Scanner
- Tutorials
- Code comments

---

# 🤝 Code of Conduct

Please follow our **Code of Conduct** and maintain a welcoming, respectful, and collaborative environment for everyone.

---

# ❤️ Thank You

Every contribution—whether it's code, documentation, testing, or feedback—helps make IssueScout better for the entire open-source community.

Happy contributing! 🚀
