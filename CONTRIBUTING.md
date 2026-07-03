# Contributing to IssueScout

Thank you for your interest in contributing to IssueScout! 🚀

We welcome bug reports, feature requests, documentation improvements, and code contributions.

---

## Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/AnthropicBots/IssueScout.git

cd IssueScout
```

## Backend Setup

### 2. Create a virtual environment

Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the backend

```bash
cd backend

pip install -e .
```

### 4. Install development tools

```bash
pip install pytest pytest-cov ruff mypy pre-commit
```

---

## Frontend Setup

From the project root:

```bash
cd frontend

npm install
```

Run the frontend development server:

```bash
npm run dev
```

---

## Running Tests

Contributors should run the following checks before opening a pull request:

- Ruff (linting)
- MyPy (static type checking)
- Pytest (test suite)

All three checks are required for contributions to be accepted.

Run the full test suite:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=issuescout --cov-report=term-missing
```

---

## Code Quality

Lint the project:

```bash
ruff check .
```

Automatically fix issues:

```bash
ruff check . --fix
```

Format the project:

```bash
ruff format .
```

Run static type checking:

```bash
mypy issuescout
```

---

## Pre-commit

Install hooks:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

---

## Branch Naming

Examples:

```
feature/github-pagination
fix/client-timeout
docs/update-readme
test/metadata-similarity
refactor/github-client
```

---

## Commit Messages

Follow Conventional Commits.

Examples:

```
feat: add GitHub pagination helper

fix: handle missing repository metadata

docs: update README

test: improve GitHub client coverage

refactor: simplify scanner pipeline
```

---

## Development Workflow

Typical development workflow:

1. Create a feature branch.
2. Implement your changes.
3. Run linting, formatting, type checking, and tests.
4. Commit using Conventional Commits.
5. Push your branch.
6. Open a Pull Request against the default branch.

---

## Pull Requests

Before submitting a pull request, ensure:

- All tests pass (`python -m pytest`)
- Ruff passes without errors (`ruff check .`)
- MyPy passes without errors (`mypy issuescout`)
- New functionality includes appropriate tests
- Documentation is updated when necessary
- Both backend and frontend build successfully

---

## Reporting Issues

When opening an issue, include:

- Operating System
- Python version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Logs or screenshots (if applicable)

---

## Questions

If you have questions about the project, feel free to open a GitHub Discussion or create an issue describing your question.

---

Thank you for helping improve **IssueScout** and supporting the open-source community! 🚀
