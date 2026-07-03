# 🔒 Security Policy

Thank you for helping keep **IssueScout** and its users safe.

Security is a top priority for the project, and we appreciate the efforts of researchers and community members who responsibly disclose vulnerabilities.

---

# Supported Versions

The following versions currently receive security updates.

| Version | Supported |
|----------|-----------|
| 1.x | ✅ Yes |
| < 1.0 | ❌ No |

---

# Reporting a Vulnerability

If you discover a security vulnerability in IssueScout, **please do not disclose it publicly** until it has been reviewed and addressed.

Instead, report it privately to the project maintainers.

Please include as much information as possible:

- Description of the vulnerability
- Steps to reproduce
- Expected behavior
- Actual behavior
- Proof of concept (if available)
- Potential impact
- Suggested mitigation (optional)
- Environment details (OS, Python version, browser if applicable)

---

# Response Process

After receiving a security report, the maintainers will:

1. Acknowledge receipt of the report.
2. Reproduce and validate the issue.
3. Assess severity and impact.
4. Develop and test a fix.
5. Release a security update when appropriate.
6. Coordinate public disclosure.
7. Credit the reporter (unless anonymity is requested).

---

# Security Scope

This policy applies to all official IssueScout components, including:

## Backend

- FastAPI REST API
- Repository scanner
- Evidence collection pipeline
- Prediction engine
- Confidence scoring
- GitHub API client

## Frontend

- React application
- Client-side API communication
- Authentication-related components (future releases)

## Infrastructure

- GitHub Actions workflows
- Dependency management
- Documentation
- Configuration files

The following are **out of scope**:

- GitHub platform vulnerabilities
- Third-party services
- User-owned GitHub repositories
- Local development environment misconfiguration

---

# Security Best Practices

When deploying or contributing to IssueScout:

- Keep all dependencies up to date.
- Use the latest supported release.
- Store GitHub Personal Access Tokens securely.
- Never commit secrets or credentials.
- Use environment variables for sensitive configuration.
- Rotate compromised credentials immediately.
- Enable Dependabot security updates.
- Enable GitHub secret scanning when available.
- Review dependency updates before merging.

---

# Dependency Security

IssueScout uses automated tooling to improve dependency security, including:

- Dependabot
- GitHub Security Advisories
- GitHub Actions CI
- Ruff
- MyPy
- Automated test suite

Every pull request should pass all quality checks before merging.

---

# Supported Reporting Languages

Security reports are accepted in:

- English

---

# Responsible Disclosure

Please allow reasonable time for investigation, remediation, and release coordination before publicly disclosing a vulnerability.

Responsible disclosure helps protect the project's users and contributors.

---

# Security Acknowledgements

We sincerely appreciate security researchers and community members who responsibly disclose vulnerabilities.

Contributors who help improve the security of IssueScout may be acknowledged in future release notes unless anonymity is requested.

---

# Contact

If a dedicated security contact or security email becomes available in the future, this policy will be updated accordingly.

Until then, please use the project's private maintainer communication channels for responsible disclosure.

---

Thank you for helping keep **IssueScout** secure for the entire open-source community. 🚀
