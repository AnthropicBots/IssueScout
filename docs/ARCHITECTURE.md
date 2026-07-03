# IssueScout Architecture

**Version:** 1.0.0

**Status:** Stable

**Last Updated:** July 2026

---

# Table of Contents

1. Introduction
2. Architecture Goals
3. High-Level Architecture
4. Project Structure
5. Backend Architecture
6. Frontend Architecture
7. Scanner Engine
8. Analysis Pipeline
9. Confidence Calculation
10. REST API Layer
11. Data Flow
12. Dependency Injection
13. Security
14. Scalability
15. Testing Strategy
16. Design Decisions
17. Future Architecture
18. Conclusion

---

# 1. Introduction

IssueScout is a production-ready full-stack application that helps developers discover meaningful GitHub contribution opportunities through automated repository analysis.

The project combines a modern React frontend with a FastAPI backend to analyze GitHub repositories, identify contributor-friendly issues, and rank them using an evidence-driven confidence scoring system.

The architecture emphasizes:

- Modularity
- Maintainability
- Scalability
- Testability
- Strong typing
- Separation of concerns

Each subsystem has a clearly defined responsibility and communicates through well-defined models.

---

# 2. Architecture Goals

The architecture has been designed around the following goals.

## Modularity

Each package is responsible for one well-defined task.

Examples include:

- Repository scanning
- GitHub communication
- API routing
- Confidence scoring
- Frontend presentation

This allows components to evolve independently.

---

## Separation of Concerns

Business logic remains inside backend services.

API routes handle:

- Request validation
- Dependency injection
- Response serialization

The frontend focuses solely on presenting information to users.

---

## Extensibility

The architecture makes it easy to add:

- New analyzers
- Additional API endpoints
- New confidence strategies
- Frontend pages
- Future GitHub integrations

without affecting existing functionality.

---

## Testability

Every major subsystem can be tested independently.

The project includes:

- Unit tests
- Integration tests
- API tests
- Scanner tests
- Static type checking

---

## Maintainability

The codebase follows a layered architecture with clearly defined package boundaries, reducing coupling and improving long-term maintainability.

---

# 3. High-Level Architecture

IssueScout consists of two primary applications communicating through a REST API.

```text
                React Frontend
                       │
                       ▼
                FastAPI Backend
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
 RepositoryService  IssueService  ScannerEngine
         │             │             │
         └─────────────┼─────────────┘
                       ▼
                GitHub Services
                       │
                       ▼
                GitHub REST API
```

The frontend communicates only with the REST API.

The backend coordinates repository scanning and GitHub communication while remaining independent from the presentation layer.

---

# 4. Project Structure

The project is organized into two primary applications.

```text
IssueScout/
│
├── backend/
│   ├── issuescout/
│   └── tests/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── docs/
│
├── .github/
│
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── ROADMAP.md
├── CHANGELOG.md
└── LICENSE
```

Each directory has a clearly defined responsibility.

---

# 5. Backend Architecture

The backend is responsible for all repository analysis and GitHub communication.

Its responsibilities include:

- Repository scanning
- GitHub API integration
- Issue filtering
- Confidence scoring
- REST API
- Response serialization

The backend follows a layered architecture.

```text
               FastAPI Routes
                      │
                      ▼
                Service Layer
                      │
                      ▼
               Scanner Engine
                      │
                      ▼
             Analysis Pipeline
                      │
                      ▼
         Confidence Calculator
                      │
                      ▼
             GitHub REST API
```

Each layer communicates using strongly typed models.

---

# 6. Frontend Architecture

The frontend is a modern React application built with TypeScript and Vite.

Its primary responsibilities include:

- Repository search
- Scan progress visualization
- Displaying scan results
- Error handling
- Responsive user interface

High-level frontend architecture:

```text
React Application
        │
        ▼
Pages
        │
        ▼
Reusable Components
        │
        ▼
Custom Hooks
        │
        ▼
REST API Client
        │
        ▼
FastAPI Backend
```

The frontend contains no repository analysis logic.

All business logic remains inside the backend.

---

# 7. Scanner Engine

The Scanner Engine is the core component responsible for repository analysis.

Its responsibilities include:

- Fetching repository information
- Loading open issues
- Detecting linked pull requests
- Executing analyzers
- Calculating confidence
- Producing contributor-friendly issue summaries

High-level workflow:

```text
Repository
      │
      ▼
Fetcher
      │
      ▼
Repository Context
      │
      ▼
Linked PR Detection
      │
      ▼
Analysis Pipeline
      │
      ▼
Confidence Calculator
      │
      ▼
Scan Result
```

The scanner remains independent from the REST API and frontend.

---

# 8. Analysis Pipeline

The Analysis Pipeline coordinates multiple independent analyzers.

Each analyzer evaluates a specific characteristic of an issue.

Current analyzers include:

- Assignment Analyzer
- Linked Pull Request Analyzer

Each analyzer returns an independent analysis result.

```text
Issue
   │
   ▼
Assignment Analyzer
   │
   ▼
Linked PR Analyzer
   │
   ▼
Analysis Results
```

The pipeline determines whether an issue is suitable for contributors before confidence is calculated.

---

# 9. Confidence Calculation

IssueScout ranks contributor-friendly issues using a confidence scoring system.

The confidence score combines multiple signals gathered during repository analysis, helping contributors prioritize issues that are more likely to be suitable.

Current scoring factors include:

- Assignment status
- Linked pull request detection
- Repository labels
- Milestone presence
- Recent repository activity

High-level workflow:

```text
Analysis Results
        │
        ▼
Confidence Calculator
        │
        ▼
Confidence Score
        │
        ▼
Issue Summary
```

Confidence calculation remains independent from the analysis pipeline, allowing future scoring strategies to be introduced without modifying analyzers.

---

# 10. REST API Layer

The REST API provides the public interface to the backend.

Its responsibilities include:

- Request validation
- Dependency injection
- Service orchestration
- Response serialization
- Error handling

High-level architecture:

```text
HTTP Request
      │
      ▼
FastAPI Router
      │
      ▼
Service Layer
      │
      ▼
Scanner Engine
      │
      ▼
Response Models
      │
      ▼
JSON Response
```

The API layer intentionally contains no repository analysis logic.

---

# 11. Data Flow

A repository scan follows the workflow below.

```text
User
   │
   ▼
React Frontend
   │
   ▼
REST API
   │
   ▼
Scanner Engine
   │
   ▼
GitHub REST API
   │
   ▼
Repository Context
   │
   ▼
Analysis Pipeline
   │
   ▼
Confidence Calculator
   │
   ▼
Issue Summaries
   │
   ▼
REST API Response
   │
   ▼
Frontend Results
```

This architecture keeps presentation, business logic, and external integrations clearly separated.

---

# 12. Dependency Injection

IssueScout uses dependency injection throughout the backend to reduce coupling and simplify testing.

Major injected components include:

- RepositoryService
- IssueService
- ScannerEngine
- Fetcher
- Linked Pull Request Detector
- ConfidenceCalculator

Benefits include:

- Easier testing
- Better maintainability
- Clear dependencies
- Simplified mocking

---

# 13. Security

IssueScout follows several security principles.

## Configuration

Sensitive values such as GitHub Personal Access Tokens are supplied through environment variables.

No credentials are stored in source code.

---

## Input Validation

Incoming API requests are validated before processing.

---

## Error Isolation

Failures affecting one repository or issue should not terminate unrelated analyses whenever possible.

---

## Least Privilege

IssueScout only requires read access to GitHub repositories.

Future integrations should continue following the principle of least privilege.

---

# 14. Scalability

The architecture is designed to scale as the project grows.

Current design supports:

- Asynchronous GitHub requests
- Independent repository scans
- Modular analyzers
- Extensible confidence scoring
- Independent frontend and backend deployment

Future improvements may include:

- Response caching
- Background jobs
- Distributed workers
- WebSocket progress updates

---

# 15. Testing Strategy

Reliability is ensured through automated testing and static analysis.

Current quality checks include:

- Unit tests
- Integration tests
- API tests
- Scanner tests
- Ruff linting
- MyPy static type checking

These checks help maintain architectural stability as the project evolves.

---

# 16. Design Decisions

Several important design decisions shaped IssueScout.

## Why FastAPI?

- Excellent asynchronous support
- Automatic OpenAPI documentation
- Strong typing
- High performance

---

## Why React?

- Component-based architecture
- TypeScript support
- Excellent developer experience
- Large ecosystem

---

## Why a Layered Architecture?

Separating presentation, services, scanning, and GitHub communication improves maintainability and keeps responsibilities clearly defined.

---

## Why Strong Typing?

Typed models improve:

- Reliability
- Validation
- Documentation
- Refactoring
- IDE support

---

# 17. Future Architecture

Future releases may expand the architecture with:

- GitHub GraphQL integration
- Repository analytics
- AI-assisted recommendations
- Export services
- Saved repository history
- Browser extension
- Docker deployment
- Plugin architecture

These additions are intended to extend the existing architecture rather than replace it.

---

# 18. Conclusion

IssueScout follows a modular, layered architecture that separates frontend presentation, backend services, repository analysis, and GitHub integration into independent components.

This design provides:

- Clear separation of concerns
- High maintainability
- Excellent testability
- Strong type safety
- Extensibility for future features

By combining a modern React frontend with a FastAPI backend and an evidence-driven scanning engine, IssueScout delivers a scalable and maintainable platform for discovering meaningful open-source contribution opportunities while remaining easy to extend as the project evolves.

---

**End of Document**
