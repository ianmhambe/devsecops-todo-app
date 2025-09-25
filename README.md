## DevSecOps To-Do App
A simple Flask to-do app demonstrating DevSecOps practices.

### CI/CD Pipeline
- **Tool**: GitHub Actions
- **Steps**:
  - SAST with Bandit to scan for code vulnerabilities.
  - Docker image build and scanning with Trivy for OS/library vulnerabilities.
  - DAST with OWASP ZAP to scan the running app.
- Artifacts: Bandit and ZAP reports are generated and uploaded for review.
### Deployment
- **Platform**: Render
- **URL**: https://todo-app-55yb.onrender.com/todos
- **Security**: HTTPS enabled, automated deployments via GitHub Actions.
