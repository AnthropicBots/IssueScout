# 🚀 IssueScout

> An intelligent GitHub contribution assistant that helps contributors discover high-quality issues by analyzing repositories, issue metadata, and pull request relationships.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Tests](https://img.shields.io/badge/Tests-231%2B-success)
![Coverage](https://img.shields.io/badge/Coverage-97%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Overview

IssueScout helps developers identify GitHub issues that are suitable for contribution.

Instead of relying solely on labels like **good first issue**, IssueScout analyzes repository data, issue metadata, comments, timelines, commits, pull requests, and multiple similarity signals to predict whether an issue is already associated with a pull request and to surface actionable information.

---

## ✨ Features

* 🔍 Repository scanning
* 📋 Open issue discovery
* 🔗 Intelligent pull request prediction
* 🧠 Multi-factor relation engine
* 📊 Confidence scoring
* 📝 Human-readable explanations
* 📦 JSON output formatter
* 💻 Console reporting
* ⚡ FastAPI REST API
* ✅ Extensive automated test suite
* 🚀 GitHub Actions CI
* 🧹 Ruff linting

---

## 🏗️ Architecture

```
GitHub Repository
        │
        ▼
 GitHub API Clients
        │
        ▼
 Evidence Collection
 ├── Timeline
 ├── Comments
 ├── Commits
 └── Reviews
        │
        ▼
 Relation Engine
 ├── Author Similarity
 ├── Title Similarity
 ├── Body References
 ├── Timeline References
 ├── Commit References
 ├── Branch Similarity
 ├── Metadata Similarity
 ├── Reviewer Similarity
 ├── File Similarity
 └── Label Similarity
        │
        ▼
 Prediction Engine
        │
        ▼
 Scanner Engine
        │
        ▼
 FastAPI REST API
```

---

## 📁 Project Structure

```
backend/
│
├── issuescout/
│   ├── api/
│   ├── core/
│   ├── evidence/
│   ├── github/
│   ├── models/
│   ├── output/
│   ├── prediction/
│   ├── presentation/
│   ├── ranking/
│   ├── scanner/
│   ├── services/
│   └── utils/
│
├── tests/
│
└── pyproject.toml
```

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/BHUVANSH855/IssueScout.git

cd IssueScout/backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

---

## ⚙️ Environment Variables

Create a `.env` file inside the `backend` directory.

```env
GITHUB_TOKEN=your_personal_access_token
```

---

## ▶️ Running the API

```bash
uvicorn issuescout.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

| Method | Endpoint               | Description            |
| ------ | ---------------------- | ---------------------- |
| GET    | `/`                    | Welcome message        |
| GET    | `/health`              | Health check           |
| GET    | `/github`              | Repository information |
| GET    | `/issues`              | List open issues       |
| GET    | `/scan/{owner}/{repo}` | Scan a repository      |

---

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=issuescout
```

Run Ruff:

```bash
ruff check .
```

---

## 🛠️ Technology Stack

* Python 3.12
* FastAPI
* Pydantic
* HTTPX
* Pytest
* Ruff
* GitHub REST API
* GitHub Actions

---

## 📈 Current Status

* ✅ 231+ automated tests
* ✅ High test coverage (~97%)
* ✅ GitHub Actions CI
* ✅ Ruff lint checks
* ✅ Editable Python package
* ✅ REST API
* ✅ Modular architecture

---

## 🗺️ Roadmap

* [x] GitHub API integration
* [x] Relation engine
* [x] Prediction engine
* [x] Confidence scoring
* [x] Evidence collection
* [x] Scanner engine
* [x] FastAPI API
* [x] Comprehensive testing
* [x] GitHub Actions
* [x] Ruff linting
* [ ] Docker support
* [ ] Web dashboard
* [ ] Database support
* [ ] Machine learning ranking
* [ ] Release v1.0.0

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Add or update tests.
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Bhuvansh Kataria**

GitHub: https://github.com/BHUVANSH855

---

⭐ If you find this project useful, consider giving it a star!
