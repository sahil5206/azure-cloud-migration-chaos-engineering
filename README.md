# 🚀 Cloud Migration, CI/CD & Chaos Engineering on Azure (AKS)

[![Azure](https://img.shields.io/badge/Azure-AKS-blue?style=flat-square&logo=microsoft-azure)](https://azure.microsoft.com/en-us/products/kubernetes-service/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4?style=flat-square&logo=terraform)](https://www.terraform.io/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=flat-square&logo=jenkins)](https://www.jenkins.io/)
[![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Python-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)

> Production-grade DevOps project demonstrating re-platform migration, CI/CD automation, Kubernetes resilience, monitoring, and chaos engineering on Microsoft Azure.

---

## 📋 Table of Contents

- [🔑 Keywords](#-keywords)
- [📌 Project Summary](#-project-summary)
- [🎯 Objectives](#-objectives)
- [🏗️ Architecture](#️-architecture)
- [🔁 Migration Strategy](#-migration-strategy)
- [🛠️ Technology Stack]((#️-technology-stack)
- [⚙️ CI/CD Pipeline](#️-cicd-pipeline)
- [🧪 Chaos Engineering](#-chaos-engineering)
- [📊 Monitoring](#-monitoring)
- [🧹 Resource Cleanup](#-resource-cleanup)
- [🧠 Key Skills](#-key-skills)
- [🏁 Outcome](#-outcome)
- [👤 Author](#-author)

---

## 🔑 Keywords

`Azure AKS` `DevOps` `CI/CD` `Jenkins` `Docker` `Kubernetes` `Terraform` `Azure Monitor` `Prometheus` `Grafana` `Cloud Migration` `Re-platforming` `Chaos Engineering` `FastAPI` `Microservices` `Containerization` `Infrastructure as Code` `SRE`

---

## 📌 Project Summary

This project demonstrates an **end-to-end cloud migration and DevOps lifecycle** by re-platforming a locally developed FastAPI microservice to Azure Kubernetes Service (AKS) using Terraform (IaC) and Jenkins CI/CD.

The system was validated for **production readiness** using monitoring and chaos engineering, ensuring self-healing and resilience under failure scenarios.

---

## 🎯 Objectives

### Business & Engineering Goals

- ✅ **Migrate** an application to Azure using Re-platform (Lift-Tinker-Shift) strategy
- ✅ **Automate** build, test, and deployment using CI/CD
- ✅ **Provision** cloud infrastructure using Terraform
- ✅ **Deploy** containerized workloads on AKS
- ✅ **Validate** resilience using Chaos Engineering
- ✅ **Monitor** system health using Azure Monitor
- ✅ **Ensure** cost hygiene via full resource teardown

---

## 🏗️ Architecture

```mermaid
graph TD
    A[Developer] --> B[GitHub<br/>Source Code]
    B --> C[Jenkins CI Pipeline]
    C --> D[Docker Image<br/>Build & Test]
    D --> E[Azure Container Registry<br/>(ACR)]
    E --> F[Azure Kubernetes Service<br/>(AKS)]
    F --> G[Azure Monitor<br/>Observability]
    G --> H[Chaos Engineering<br/>Pod Failure Simulation]
```

---

## 🔁 Migration Strategy — Re-platform

### Why Re-platform?

- 🔄 **No application rewrite**
- ⚡ **Minimal risk**
- 🚀 **Faster migration**
- ☁️ **Leverages managed Azure services**

### Migration Comparison

| Area | Before | After |
|------|--------|-------|
| **Runtime** | Local Docker | AKS |
| **Registry** | Local | Azure ACR |
| **Deployment** | Manual | Jenkins CI/CD |
| **Resilience** | None | Kubernetes self-healing |
| **Monitoring** | Logs only | Azure Monitor |

---

## 🛠️ Technology Stack

### 🎯 Application
- **FastAPI** (Python)
- REST APIs (`/health`, `/version`)

### ☁️ DevOps & Cloud
- **Docker**
- **Jenkins** (CI/CD)
- **Terraform** (IaC)
- **Azure Kubernetes Service** (AKS)
- **Azure Container Registry** (ACR)

### 📊 Reliability & Observability
- **Azure Monitor** (Container Insights)
- **Chaos Engineering** (Pod Failure Testing)

---

## ⚙️ CI/CD Pipeline (Jenkins)

### Pipeline Stages

1. 📥 GitHub checkout
2. 🏗️ Docker image build
3. 🧪 Smoke testing (`/health`)
4. 📤 Push image to ACR
5. 🚀 Deploy to AKS
6. 🔄 Rolling update

### CI/CD Validation

A new endpoint was added to verify deployments:

```http
GET /version
```

```json
{
  "service": "fastapi-app",
  "version": "v2.0.0",
  "status": "running"
}
```

> ✅ **Seeing this response live confirmed successful CI → CD → AKS deployment**

---

## 🧪 Chaos Engineering & Resilience Validation

### Failure Injection

```bash
kubectl delete pod -l app=fastapi-app
```

### Observed Results

- 🎯 Pod terminated intentionally
- 🔄 Kubernetes recreated pod automatically
- ✅ Application recovered without manual intervention

### Outcome

- ✔ Self-healing validated
- ✔ High availability confirmed
- ✔ Production resilience proven

---

## 📊 Monitoring & Observability

Monitoring was implemented using **Azure Monitor (Container Insights)** to observe:

- 📈 Pod CPU & memory usage
- 🔄 Pod restart count
- 📦 Container lifecycle
- 🛡️ Recovery behavior during chaos tests

This ensured **real-time visibility** into system behavior under failure.

---

## 🧹 Resource Cleanup

All cloud resources were deleted after completion to avoid charges.

```bash
az group delete --name rg-fastapi-chaos --yes --no-wait
```

### ✅ Cleanup Verification

- ❌ No AKS
- ❌ No ACR  
- ❌ No monitoring costs
- 💰 Zero ongoing billing

---

## 🧠 Key Skills Demonstrated

- ☁️ **Cloud migration** (Re-platform strategy)
- ⚙️ **Kubernetes & container orchestration**
- 🔄 **CI/CD pipeline design**
- 🏗️ **Infrastructure as Code** (Terraform)
- 🧪 **Chaos engineering principles**
- 📊 **Observability & monitoring**
- 💰 **Cost optimization & teardown**
- 🎯 **Production-grade DevOps thinking**

---

## 🏁 Final Outcome

This project demonstrates **real-world DevOps and Cloud Engineering practices**, focusing on automation, reliability, resilience, and observability rather than basic deployment.

---

## 👤 Author

**Sahil Gupta**  
Cloud • DevOps • Kubernetes • Azure

---

<div align="center">

**⭐ If you found this project helpful, consider giving it a star!**

</div>
