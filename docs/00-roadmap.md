## Repository Structure
| Folder / File                | Notes                                   |
|------------------------------|-----------------------------------------|
| cloud-ops/                   | Root folder                             |
| ├─ Python/                   |                                         |
| ├─ cloud-serverless-app/     | Under development                       |
| ├─ docs/                     | Documentation folder                    |
| │ ├─ 00-roadmap.md           | Azure / DevOps learning roadmap         |
| │ ├─ 01-setup.md             | Local environment, PATH, CLI, Terraform |
| │ ├─ 02-cloud.md             |Cloud platform reference                 |
| │ ├─ 03-terraform.md         |                                         |
| │ ├─ 04-cicd.md              |                                         |
| │ ├─ 05-containers-k8s.md    |                                         |
| │ ├─ 06-sre-observability.md | Monitoring, logging, SLIs/SLOs          |
| │ ├─ 07-devsecops.md         |                                         |
| │ ├─ 08-networking.md        | Networking concepts                     |
| │ ├─ 09-system-design.md     |                                         |
| │ └─ resources.md            | Reference links and resources           |
| ├─ projects/                 |                                         |
| │ ├─ terraform-aws-vpc/      |                                         |
| │ ├─ terraform-aws-eks/      |                                         |
| │ ├─ cicd-github-actions/    |                                         |
| │ └─ k8s-microservice-demo/  |                                         |
| ├─ scripts/                  | Scripts folder                          |
| │ ├─ python/                 | Python scripts                          |
| │ └─ shell/                  | Shell automation scripts                |
| ├─ diagrams/                 |                                         |
| │ └─ architecture/           |                                         |
| └─ README.md                 | Root readme                             |

## Status Check
- Core competencies reflected in CV, LinkedIn, and applications
- Python and Shell automation scripts uploaded
- Production operations and incident response experience
- Resume and LinkedIn groundwork completed
- Mag7-ready Cloud/DevOps Engineer

## Azure Learning Roadmap
### Foundation & Story Inventory
- Align cloud knowledge to Azure concepts
- Build 8 core behavioral stories using STAR framework:
 - Major incident, automation improvement, difficult stakeholder, mistake, tight deadline, cross-team collaboration, security issue, customer escalation
- Translate AWS experience into Azure terminology
- Refine 1 story for customer focus

### Commerce, Advanced Troubleshooting & Competencies
- Deep dive into Azure billing and commerce scenarios
- Build 2 additional behavioral stories: adaptability, influence
- Practice production support scenarios and inclusive collaboration stories
- Add measurable impact to all stories
- Rapid-fire behavioral Q&A
- Full mock interview simulation (technical + behavioral)

### Polish & Pressure Simulation
- Deep technical clarity: subscription lifecycle, billing troubleshooting, shared responsibility, cloud vs on-prem
- Behavioral compression: concise (60–90s) and detailed (2–3 min) story versions
- Hard questions practice: failure, conflict, disagreement with manager
- Customer communication drills & case simulation
- Final mock interview with review

#### Learning Resources & Daily Routines
- [THE 2028 GLOBAL INTELLIGENCE CRISIS](https://www.citriniresearch.com/p/2028gic/)
- [LeetCode](https://leetcode.com/studyplan/)
- [Microsoft Learn](https://learn.microsoft.com/)
- [Microsoft Careers](https://apply.careers.microsoft.com/careers/dashboard/)
- [Google Careers](https://www.google.com/about/careers/applications/jobs/recommendations/)
- [Amazon Jobs](https://www.amazon.jobs/en-GB/user/recommendations/)

## DevOps & CloudOps Master Roadmap
### Core Cloud
- VPC, subnets, compute, load balancers, IAM
- Infrastructure as Code: Terraform providers, modules, dev/stage/prod environments
- GitHub hygiene: clean profile, meaningful commits, pin top repositories

### CI/CD & Containers
- GitHub Actions pipelines: build → test → deploy, secrets management
- Docker: multi-stage builds, image optimization
- Kubernetes: EKS/GKE, deployments, services, ConfigMaps, secrets, Helm basics

### SRE, Automation & Security
- Configuration management & automation: Ansible, Bash/Python scripts
- Observability: Prometheus, Grafana, logging, SLIs/SLOs
- DevSecOps: secrets management, IAM policies, container scanning
- Networking: DNS, load balancing, VPC peering

### Interview-Grade Polish
- Source control & collaboration: advanced Git, PR workflows, code review
- System design: scalable infrastructure, CI/CD architecture, failure scenarios, cost tradeoffs
- Resume, STAR stories, mock interviews

## Portfolio & Projects
### CloudOps & DevOps Projects
- Data pipeline with failure detection
- Linux service outage simulator
- Cloud-serverless app: Lambda / Cloud Functions, API Gateway, S3/GCS hosting, DynamoDB/Firestore, IAM access control

### AWS DB AI Platform
- Terraform-based scalable AI-enabled infrastructure
- Modules: VPC, ECS, RDS, IAM, CloudWatch, ALB
- Security: least-privilege IAM, private subnets, KMS encryption, S3 backend with locking
- Deployment: terraform init → plan → apply → verify → destroy

### Local Environment Setup
- Tools: Git, GitHub CLI, Terraform, kubectl, Helm, AWS CLI
- PATH setup for Dev tools and system binaries

---

### Notes
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

### User PATH (Dev tools)
C:\Users\SOTA\AppData\Local\Programs\
C:\Users\SOTA\bin\  # Add only this

### System PATH (Sys tools)
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
