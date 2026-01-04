## 🚀 Cloud Migration, CI/CD & Chaos Engineering on Azure (AKS)

Production-grade DevOps project demonstrating re-platform migration, CI/CD automation, Kubernetes resilience, monitoring, and chaos engineering on Microsoft Azure.

🔑 Keywords 

Azure AKS, DevOps, CI/CD, Jenkins, Docker, Kubernetes, Terraform, Azure Monitor, Prometheus, Grafana, Cloud Migration, Re-platforming, Chaos Engineering, FastAPI, Microservices, Containerization, Infrastructure as Code, SRE

📌 Project Summary

This project demonstrates an end-to-end cloud migration and DevOps lifecycle by re-platforming a locally developed FastAPI microservice to Azure Kubernetes Service (AKS) using Terraform (IaC) and Jenkins CI/CD.

The system was validated for production readiness using monitoring and chaos engineering, ensuring self-healing and resilience under failure scenarios.

🎯 Business & Engineering Objectives

Migrate an application to Azure using Re-platform (Lift-Tinker-Shift) strategy

Automate build, test, and deployment using CI/CD

Provision cloud infrastructure using Terraform

Deploy containerized workloads on AKS

Validate resilience using Chaos Engineering

Monitor system health using Azure Monitor

Ensure cost hygiene via full resource teardown

🏗️ Architecture Overview
Developer
   ↓
GitHub (Source Code)
   ↓
Jenkins CI Pipeline
   ↓
Docker Image Build & Test
   ↓
Azure Container Registry (ACR)
   ↓
Azure Kubernetes Service (AKS)
   ↓
Azure Monitor (Observability)
   ↓
Chaos Engineering (Pod Failure Simulation)

🔁 Cloud Migration Strategy — Re-platform

Why Re-platform?

No application rewrite

Minimal risk

Faster migration

Leverages managed Azure services

Area	Before	After
Runtime	Local Docker	AKS
Registry	Local	Azure ACR
Deployment	Manual	Jenkins CI/CD
Resilience	None	Kubernetes self-healing
Monitoring	Logs only	Azure Monitor
🧰 Technology Stack
Application

FastAPI (Python)

REST APIs (/health, /version)

DevOps & Cloud

Docker

Jenkins (CI/CD)

Terraform (IaC)

Azure Kubernetes Service (AKS)

Azure Container Registry (ACR)

Reliability & Observability

Azure Monitor (Container Insights)

Chaos Engineering (Pod Failure Testing)

⚙️ CI/CD Pipeline (Jenkins)

Pipeline Stages

GitHub checkout

Docker image build

Smoke testing (/health)

Push image to ACR

Deploy to AKS

Rolling update

CI/CD Validation

A new endpoint was added to verify deployments:

GET /version

{
  "service": "fastapi-app",
  "version": "v2.0.0",
  "status": "running"
}


Seeing this response live confirmed successful CI → CD → AKS deployment.

🧪 Chaos Engineering & Resilience Validation

Failure Injected

kubectl delete pod -l app=fastapi-app


Observed Results

Pod terminated intentionally

Kubernetes recreated pod automatically

Application recovered without manual intervention

Outcome

✔ Self-healing validated

✔ High availability confirmed

✔ Production resilience proven

📊 Monitoring & Observability

Monitoring was implemented using Azure Monitor (Container Insights) to observe:

Pod CPU & memory usage

Pod restart count

Container lifecycle

Recovery behavior during chaos tests

This ensured real-time visibility into system behavior under failure.

🧹 Cost & Resource Cleanup

All cloud resources were deleted after completion to avoid charges.

az group delete --name rg-fastapi-chaos --yes --no-wait


✔ No AKS
✔ No ACR
✔ No monitoring costs
✔ Zero ongoing billing

🧠 Key Skills Demonstrated

Cloud migration (Re-platform strategy)

Kubernetes & container orchestration

CI/CD pipeline design

Infrastructure as Code (Terraform)

Chaos engineering principles

Observability & monitoring

Cost optimization & teardown

Production-grade DevOps thinking

🏁 Final Outcome

This project demonstrates real-world DevOps and Cloud Engineering practices, focusing on automation, reliability, resilience, and observability rather than basic deployment.

👤 Author

Sahil Gupta
Cloud • DevOps • Kubernetes • Azure
