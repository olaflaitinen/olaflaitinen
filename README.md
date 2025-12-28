# Olaf Yunus Laitinen-Imanov

CTO & Co-Founder, Skolyn AB · Postdoctoral Research Fellow, Uppsala University · Seconded National Expert, European Research Council Executive Agency  
Clinical Bioinformatician, Linköping University Hospital · Data Science Specialist, DTU Bioengineering  
Location: Greater Linköping Metropolitan Area, Sweden (also Baku, Azerbaijan)

Links: [LinkedIn](https://www.linkedin.com/in/olafylimanov) · [ORCID](https://orcid.org/0009-0006-5184-0810) · [Google Scholar](https://scholar.google.com/citations?hl=en&user=WSqps1YAAAAJ) · [ResearchGate](https://www.researchgate.net/profile/Olaf-Laitinen)  
Contact: olafylimanov@skolyn.se · olaf.imanov@it.uu.se · +46 76 236 80 88

---

## Index

- [Overview](#overview)
- [Now / Roadmap](#now--roadmap)
- [Appointments](#appointments)
- [Research and Engineering Themes](#research-and-engineering-themes)
- [Selected Publications](#selected-publications-20232025)
- [Selected Artifacts](#selected-artifacts)
- [Technical Stack](#technical-stack-representative)
- [Talks, Teaching, Service](#talks-teaching-service)
- [Citation and Archiving](#citation-and-archiving)
- [Disclaimer](#disclaimer)

---

## Overview

I build clinically deployable machine learning systems at the intersection of medical imaging, clinical genomics, and multi-omics.  
My work spans research and engineering: problem formulation → reproducible pipelines → interpretable modeling → multi-site validation → deployment in regulated settings.

Core priorities:
- Interpretability and auditability as first-class requirements (not post-hoc add-ons)
- Privacy-preserving evaluation across institutions under real heterogeneity
- Reproducible computational biology pipelines aligned with clinical operations
- Interoperability boundaries (DICOM/NIfTI, HL7/FHIR) and traceable system behavior

---

## Now / Roadmap

### Current (Q4 2025–H1 2026)
- Clinical decision support: strengthen traceability, structured explanations, and audit logs suitable for clinical stakeholders.
- Federated benchmarking: finalize multi-site evaluation protocols, site-effect analysis, and reporting conventions.
- Clinical genomics: harden Nextflow/nf-core execution patterns (provenance, version pinning, reproducible environments) for routine diagnostics.
- Publications: complete and submit pending manuscripts in medical imaging, sonography interpretability, and multi-omics biomarker discovery.

### Next (H2 2026)
- Deployment engineering: improve model monitoring, dataset shift detection, and calibration strategies in real operational constraints.
- Open-source artifacts: extract and publish reusable components (evaluation harnesses, reference implementations, reproducibility scaffolding).
- Human-AI collaboration: formalize reader-study and interaction evaluation packages for clinical workflows.

### Longer horizon (2027+)
- Multi-modal and multi-omics integration at scale with clinically meaningful interpretability (concept-level and pathway-level reporting).
- Federated learning beyond training: federated evaluation and governance patterns with auditable compliance-friendly reporting.

---

## Appointments

- Skolyn AB (CTO & Co-Founder) — AI-driven clinical decision support; interoperable deployment (HL7/FHIR); scalable inference (Python/PyTorch; Docker/Kubernetes)
- European Research Council Executive Agency (Seconded National Expert) — evaluation workflows and strategic analysis for large-scale research portfolios
- Uppsala University (Postdoctoral Research Fellow) — medical imaging, neuroradiology, explainability; federated learning benchmarking across Swedish hospitals
- Linköping University Hospital (Clinical Bioinformatician) — clinical genomics operations; rare disease diagnosis; nf-core/Nextflow workflows
- DTU Bioengineering (Data Science Specialist) — proteomics and systems biology; graph learning for protein interactions

Previously: Google Health (Research Scientist; Technical Program Manager II) · Finnish Center for Artificial Intelligence (Senior Research Scientist)

---

## Research and Engineering Themes

### Trustworthy Medical AI
- Interpretability: SHAP, Integrated Gradients, attention-based analyses; structured explanation reporting
- Reliability: calibration, uncertainty estimation, OOD behavior, subgroup and shift analysis
- Human-AI collaboration: evaluation protocols, reader studies, interaction design constraints

### Federated Learning in Healthcare
- Robust training under institutional heterogeneity (site effects, device/protocol variation)
- Privacy-preserving evaluation design and reporting (reproducible metrics across sites)
- Operational constraints: governance, logging, monitoring, update strategies

### Clinical Genomics and Multi-Omics
- Rare disease workflows: variant calling/annotation/interpretation and reporting practices
- Multi-omics integration: network analysis, graph neural networks, latent factor models
- Reproducibility: Nextflow/nf-core conventions; provenance, parameterization, environment pinning

### Interoperability and Standards
- Imaging: DICOM, NIfTI; reproducible pre-processing and annotation practices
- Health data: HL7/FHIR integration patterns; system boundaries and audit trails

---

## Selected Publications (2023–2025)

1. Imanov, O.Y.L., Schmidt, M., Andersson, L. (2025). Integrative machine learning framework for early-stage neurodegeneration biomarkers from multi-omics profiles. Journal of Proteome Research (forthcoming).
2. Imanov, O.Y.L., Chen, E., Kumar, R. (2025). Explainable AI in sonography: transferring interpretability from proteomics to medical imaging. JAMIA (forthcoming).
3. Imanov, O.Y.L., Christensen, A.N., Nielsen, M. (2025). Designing adaptive human-AI systems for collaborative problem solving in fetal ultrasound diagnostics. Medical Image Analysis, 85:102745.
4. Imanov, O.Y.L., Kaski, S., Virtanen, P. (2024). Adaptive federated ensembles for heterogeneous medical imaging datasets. IEEE Transactions on Medical Imaging, 43(12):4234–4247.
5. Chen, E., Imanov, O.Y.L., Zhang, W. (2024). Human-in-the-loop evaluation of large language models for medical question answering. Nature Digital Medicine, 7(1):245.
6. Imanov, O.Y.L., Bergström, S., Andersson, J. (2023). Trustworthy reinforcement learning with human-in-the-loop feedback for medical imaging. Medical Image Analysis, 89:102876.

Full list: https://scholar.google.com/citations?hl=en&user=WSqps1YAAAAJ

---

## Selected Artifacts

The sections below follow a consistent structure: Scope, Non-goals, Reproducibility, and Citation.  
For clinical or medically adjacent code, explicit boundaries are stated to reduce misuse risk and to clarify intended usage.

### SkolynAI (clinical co-pilot platform foundations)
Repository: https://github.com/skolyn/skolyn-ai

Scope
- Reference implementations and platform foundations for explainable clinical decision support workflows.
- System engineering patterns for low-latency inference, traceable outputs, and integration boundaries.

Non-goals
- Not a substitute for professional medical judgment.
- Not a standalone EHR system and not a comprehensive clinical workflow product by itself.
- Not a claim of regulatory clearance; regulatory readiness work is handled as a separate governance track.

Reproducibility
- Prefer containerized execution for deterministic environments.
- Where applicable: explicit data splits, pinned dependencies, and evaluation scripts producing stable metrics.

Citation
- Add a CITATION.cff file at repository root (recommended).
- If archival is enabled, attach a DOI to releases and reference it in the repository documentation.

---

### FedMed (federated learning framework for healthcare settings)
Repository: https://github.com/fcai/fedmed · PyPI: https://pypi.org/project/fedmed/

Scope
- Federated learning baselines and evaluation harnesses for heterogeneous clinical datasets.
- Utility modules for reporting, aggregation experiments, and reproducible comparisons.

Non-goals
- Not a production-grade FL orchestrator; focuses on research-grade baselines and benchmarking.
- Not a privacy guarantee by default; privacy claims must be explicit, threat-modelled, and tested.

Reproducibility
- Run scripts should produce (a) metrics tables, (b) calibration and error analyses, and (c) a manifest of configs.
- Prefer: fixed seeds, version pinning, and explicit dataset provenance statements.

Citation
- Provide CITATION.cff and versioned release tags; archive key releases to obtain a DOI when appropriate.

---

### nf-core/clinicalgenomics (upstream contributions)
Repository: https://github.com/nf-core/clinicalgenomics

Scope
- Community pipeline ecosystem for clinical genomics workflows (Nextflow).
- Contributions typically focus on: robustness, portability, and reproducible execution in clinical operations.

Non-goals
- Not a single-institution bespoke pipeline; aims to be generalizable and configurable.
- Not a substitute for local clinical validation requirements.

Reproducibility
- Follow nf-core guidelines: parameterized execution, container profiles, and consistent provenance outputs.

Citation
- Use the project’s recommended citation entry and add local documentation for clinical validation context.

---

## Technical Stack (representative)

Languages: Python, R, SQL  
ML: PyTorch, TensorFlow; CNNs, Transformers, GNNs; evaluation and calibration  
MLOps/Infra: Docker, Kubernetes; containerized training/inference; reproducible environments  
Pipelines: Nextflow, nf-core; CI-ready workflow patterns  
Standards: HL7/FHIR, DICOM, NIfTI

---

## Talks, Teaching, Service

Talks (2023–2025): ECR · MICCAI · ICML · NeurIPS Workshops · Nordic AI in Medicine Summit · Google Health AI Symposium  
Teaching (2025, Linköping University): data analysis with Python; regression/statistical modeling; probability and statistics; multivariate methods  
Review/service: MICCAI, NeurIPS, ICML, ICLR; Nature Digital Medicine, Medical Image Analysis, IEEE TMI, Bioinformatics, PLOS Computational Biology

---

## Citation and Archiving

Recommended for research software:
- Add a CITATION.cff file to repositories to provide machine-readable citation metadata.
- For long-lived releases, archive versions and issue DOIs (e.g., via Zenodo GitHub integration).
- Document how to reproduce key results (configs, seeds, environment, and evaluation entrypoints).

---

## Disclaimer

This profile reflects personal work and research. It is not an official product statement.  
Last updated: December 2025
