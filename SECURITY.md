# 🔒 Security Policy

Thank you for helping keep **IssueScout** secure.

The security of our users, contributors, and the open-source community is a top priority. We greatly appreciate responsible disclosure of security vulnerabilities and work to address valid reports as quickly as possible.

---

# 📦 Supported Versions

Security updates are provided only for actively supported releases.

| Version | Supported |
|----------|-----------|
| 1.x | ✅ Yes |
| < 1.0 | ❌ No |

Only the latest stable **1.x** release receives security fixes.

---

# 🚨 Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues or pull requests.**

Instead, report them privately to the project maintainers.

Include as much information as possible:

- Description of the vulnerability
- Steps to reproduce
- Expected behavior
- Actual behavior
- Proof of concept (if available)
- Potential impact
- Suggested mitigation (optional)
- Environment details
  - Operating System
  - Python version
  - Node.js version
  - Browser (if applicable)

Reports containing reproducible information can generally be investigated much more quickly.

---

# 🔄 Response Process

When a security report is received, the maintainers will:

1. Acknowledge receipt.
2. Validate the report.
3. Assess severity and impact.
4. Develop and test a fix.
5. Prepare a security release if required.
6. Coordinate responsible disclosure.
7. Credit the reporter unless anonymity is requested.

While response times may vary depending on complexity, every report will be reviewed.

---

# 🛡️ Security Scope

This policy applies to all official IssueScout components.

## Backend

- FastAPI REST API
- Repository scanner
- GitHub client
- Evidence collection
- Relationship detection engine
- Confidence calculator
- Ranking engine
- Prediction services

---

## Frontend

- React application
- Client-side API communication
- Repository dashboard
- Issue detail pages

---

## Infrastructure

- GitHub Actions
- CI workflows
- Dependency management
- Configuration files
- Documentation

---

# ❌ Out of Scope

The following are outside the scope of this security policy:

- GitHub platform vulnerabilities
- Vulnerabilities in third-party services
- User-owned GitHub repositories
- Local development environment misconfiguration
- Self-hosted deployments modified by third parties
- Social engineering attacks

---

# 🔐 Security Best Practices

When deploying or contributing to IssueScout:

- Keep dependencies up to date.
- Use the latest supported release.
- Store GitHub Personal Access Tokens securely.
- Never commit secrets or credentials.
- Use environment variables for sensitive configuration.
- Rotate compromised credentials immediately.
- Enable GitHub Secret Scanning.
- Enable Dependabot security updates.
- Review dependency updates before merging.
- Follow the principle of least privilege when creating GitHub tokens.

---

# 📦 Dependency Security

IssueScout uses several tools to improve software security and code quality.

These include:

- GitHub Dependabot
- GitHub Security Advisories
- GitHub Actions
- Ruff
- MyPy
- Pytest
- Automated CI validation

Every pull request should pass all automated quality checks before merging.

---

# 🔍 Supported Reporting Language

Security reports are accepted in:

- English

---

# 🤝 Responsible Disclosure

Please allow reasonable time for investigation, remediation, testing, and coordinated disclosure before making any vulnerability public.

Responsible disclosure helps protect the project's users and the broader open-source ecosystem.

---

# 🏆 Security Acknowledgements

We sincerely appreciate security researchers and community members who responsibly disclose vulnerabilities.

Contributors who help improve the security of IssueScout may be acknowledged in future release notes unless anonymity is requested.

---

# 📬 Contact

If a dedicated security email or private reporting channel becomes available in the future, this document will be updated.

Until then, please use the project's private maintainer communication channels for responsible disclosure.

---

# ❤️ Thank You

Security is a shared responsibility.

Thank you for helping keep **IssueScout** reliable, secure, and trustworthy for the entire open-source community.
