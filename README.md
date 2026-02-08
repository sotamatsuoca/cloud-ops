# Master Schedule - DevOps & CloudOps Roadmap

## Overview
This repository contains a comprehensive roadmap for learning and executing DevOps and CloudOps projects, along with production-ready Terraform infrastructure code for cloud platforms. The goal is to prepare for DevOps / Cloud Engineer roles.

### Purpose
- Demonstrate production-minded cloud engineering skills
- Focus on reliability, data integrity, and incident handling
- Build a portfolio of infrastructure, automation, and SRE projects

### Target Roles
- Cloud Engineer
- Cloud Technical Solutions Engineer
- DevOps Engineer

---

## About Me
- Background in enterprise system operation and data systems
- Experience with Linux, SQL, automation, incident response
 - Bachelor’s degree in Finance, with equivalent practical experience in IT.
 - 5.5 years of experience in troubleshooting and advocating for customer needs, and triaging technical issues (hardware, software, application, operational, process).
 - 3.5 years of experience with computer networking and web technologies (HTTP, HTML, DNS)
 - Experience in system administration with Linux
 - Experience with core programming and scripting languages (Python, JavaScript, PowerShell, Bash/Shell)

---
## Repository Structure

| Folder / File                  | Notes                               |
|--------------------------------|------------------------------------|
| master-schedule/               | Root folder                        |
| ├─ docs/                       | Documentation folder               |
| │ ├─ 00-status.md               | Markdown doc                        |
| │ ├─ 01-roadmap.md              | Markdown doc                        |
| │ ├─ 02-cloud.md                | Markdown doc                        |
| │ ├─ 03-terraform.md            | Markdown doc                        |
| │ ├─ 04-cicd.md                 | Markdown doc                        |
| │ ├─ 05-containers-k8s.md       | Markdown doc                        |
| │ ├─ 06-sre-observability.md    | Markdown doc                        |
| │ ├─ 07-devsecops.md            | Markdown doc                        |
| │ ├─ 08-networking.md           | Markdown doc                        |
| │ ├─ 09-system-design.md        | Markdown doc                        |
| │ └─ resources.md               | Markdown doc                        |
| ├─ projects/                    | Project implementations            |
| │ ├─ terraform-aws-vpc/         | Terraform AWS VPC project           |
| │ ├─ terraform-aws-eks/         | Terraform AWS EKS project           |
| │ ├─ cicd-github-actions/       | CI/CD GitHub Actions project        |
| │ └─ k8s-microservice-demo/     | Kubernetes microservice demo        |
| ├─ scripts/                     | Scripts folder                     |
| │ ├─ python/                     | Python scripts                      |
| │ └─ shell/                      | Shell scripts                        |
| ├─ diagrams/                     | Diagrams folder                     |
| │ └─ architecture/               | Architecture diagrams               |
| └─ README.md                     | Root readme                         |
---

## Status Check
- Amazon Leadership Principles reflected in CV, LinkedIn, and applications
- Python and Shell automation scripts uploaded to GitHub
- Production operations and incident response experience
- Resume and LinkedIn groundwork completed
- Goal: Big Tech–ready DevOps Engineer

---

## Phase 1 — Core Cloud

### Cloud Platforms
- VPC & subnets
- Compute & load balancers
- IAM (roles, least privilege)

**Deliverables**
- `cloud-basics/` repository
- Architecture diagram in README

### GitHub Hygiene
- Clean profile, proper READMEs, meaningful commits
- Pin 2–3 repositories
- Signal understanding of architecture, not just services

### Infrastructure as Code (Terraform)
- Providers, modules, remote state
- Environments: dev / stage / prod

**Deliverables**
- `terraform-aws-vpc/`
- `terraform-aws-ecs-or-eks/`
- Key concepts: Terraform, reusable modules, IaC best practices

---

## Phase 2 — CI/CD & Containers

### CI/CD Pipelines (GitHub Actions)
- Build → Test → Deploy
- Secrets handling
- Terraform plan & apply in pipeline

**Deliverables**
- `.github/workflows/ci.yml`
- Automated infrastructure or application deployment

### Containers & Kubernetes
- **Docker:** Multi-stage builds, image optimization
- **Kubernetes:** EKS / GKE, Deployments, Services, ConfigMaps, Secrets, Helm basics

**Deliverables**
- `k8s-microservice-demo/`
- `helm-chart/`

---

## Phase 3 — SRE, Automation & Security

### Configuration & Automation
- Ansible basics
- Infrastructure & application configuration
- Bash & Python glue scripts

### Observability & SRE
- Prometheus, Grafana
- Logging, alerts
- SLIs / SLOs

**Deliverables**
- Monitoring dashboard screenshots
- Incident simulation write-ups

### DevSecOps & Networking
- **DevSecOps:** Secrets management, IAM policies, container scanning, policy-as-code
- **Networking:** DNS, load balancing, TCP basics, VPC peering

---

## Phase 4 — Interview-Grade Polish

### Source Control & Collaboration
- Advanced Git, PR workflows, trunk-based development, code review mindset

### System Design
- CI/CD system design
- Scalable infrastructure
- Failure scenarios
- Cost tradeoffs

### Finalization & Applications
- Resume final pass
- STAR stories for leadership & incidents
- Mock interviews and active applications

---

## Final Portfolio Checklist
- Terraform infrastructure repository
- GitHub Actions CI/CD pipeline
- Kubernetes deployment
- Monitoring & alerting setup
- Python automation
- Clear READMEs & architecture diagrams

---

## Projects

### CloudOps Projects
1. Data Pipeline with Failure Detection
2. Linux Service Outage Simulator

### Cloud-Serverless App
- Event-driven serverless architecture using Lambda / Cloud Functions
- API Gateway / Cloud Run for HTTP endpoints
- S3 / GCS for static hosting
- DynamoDB / Firestore for serverless database
- IAM roles / Service accounts for access control

---

## AWS DB AI Platform
**Terraform IaC for AWS scalable, AI-enabled platform**

**Modules**
- VPC: Isolated public/private subnets
- ECS: Container orchestration
- RDS PostgreSQL: Multi-AZ with automated backups
- IAM: Role-based access control
- CloudWatch: Monitoring & alerting
- ALB: Application load balancer

**Deployment Steps**
1. Terraform validation (`terraform init`, `terraform validate`, `terraform plan`)
2. Configure AWS account and environment variables
3. Apply Terraform (`terraform apply tfplan`)
4. Verify deployment (ECS, RDS, CloudWatch)
5. Optional destroy (`terraform destroy`)

**Security Best Practices**
- Never commit secrets; use `.gitignore` and Secrets Manager
- Least-privilege IAM roles
- S3 backend with DynamoDB locking and KMS encryption
- Network segregation: private subnets for RDS, ALB in public subnets

---

## Local Environment Notes

**Git / GitHub CLI**
```powershell
git clone <url>
git status
git add .
git commit -m 'message'
git push
gh auth login
```

**Terraform**
```powershell
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

**Scripts & Tools**
- Python: `scripts/python/`  
- Shell: `scripts/shell/`  
- Other tools: Terraform, kubectl, helm, aws, gh located in `C:\Users\SOTA\bin\`

---

## Learning Resources

| Topic | Resource |
|-------|----------|
| Terraform | [https://www.terraform.io/docs](https://www.terraform.io/docs) |
| AWS | [https://docs.aws.amazon.com](https://docs.aws.amazon.com) |
| ECS Best Practices | [AWS ECS Guide](https://docs.aws.amazon.com/ecs/) |
| Terraform State | [State Management](https://www.terraform.io/language/state) |

---

## Roadmap

- **Phase 1:** Subnets, NAT, ALB, SGs  
- **Phase 2:** Secrets Manager, parameter groups  
- **Phase 3:** AWS account + first deploy  
- **Phase 4:** CI/CD pipeline (GitHub Actions → ECR → ECS)  
- **Phase 5:** Auto-scaling groups + Spot instances  
- **Phase 6:** Multi-region failover  

---

## Interview Talking Points

- **Modularity:** Why each resource is in its own module  
- **State management:** Why S3 + DynamoDB is better than local state  
- **IAM design:** Least-privilege across services  
- **Cost optimization:** t3.micro RDS, spot instances, data transfer zones  
- **Disaster recovery:** Multi-AZ, backups, destroy/recreate workflow  

---

## Contributing

- Validate syntax: `terraform validate`  
- Format code: `terraform fmt -recursive .`  
- Plan before apply: `terraform plan -out=tfplan`  
- Use meaningful commit messages  

---

### Git
- C:\Program Files\Git\cmd
- C:\Program Files\Git\bin
- git.exe

### GitHub CLI (`where gh`)
- C:\Program Files\GitHub CLI\
- gh.exe
- C:\Users\<USERNAME>\AppData\Local\Programs\GitHub CLI\

### Terraform
- C:\Program Files\Terraform\
- C:\HashiCorp\Terraform\
- C:\Users\SOTA\bin\
- terraform.exe

## User PATH (Dev tools)
C:\Users\SOTA\AppData\Local\Programs\
C:\Users\SOTA\bin\  # Add only this

## System PATH (Sys tools)
C:\Program Files\
C:\Program Files\Git\cmd\
C:\Program Files\GitHub CLI\

C:\Users\SOTA\bin\
| Binary         | Notes                   |
|----------------|------------------------|
| terraform.exe  | Terraform CLI           |
| kubectl.exe    | Kubernetes CLI          |
| helm.exe       | Helm package manager    |
| aws.exe        | AWS CLI                 |
| gh.exe         | GitHub CLI              |

### Sanity chk
`$env:PATH -split ";"`

---

## License

[e.g., MIT, Apache 2.0]

---

## Author

S. M. / DevOps

**Last Updated:** February 2026