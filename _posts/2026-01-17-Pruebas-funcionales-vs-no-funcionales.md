---
layout: post
title: Functional vs. Non-Functional Testing
date: 2026-01-17 13:01:35 +0300
last_modified_at: 2026-01-26
categories: [Quality Assurance]
---

A few time ago, I landed a job at Banorte, a fairly large bank here in Mexico, and it wasn't by chance or magic. It was the result of constant preparation, which was full of lessons, mistakes, and a compelling backstory. While I could tell you the whole story, I'd like to focus on the final piece that led to this job. I'm talking about Esteban Balvin's "Software Testing from Scratch: All-in-One MasterClass (2025)" course on Udemy. Specifically, the video "Functional vs. Non-Functional Testing."

I mention this because everything in the video was covered in the theoretical interview, which was the deciding factor in getting the job.

#### Types of Testing
There are two types of testing: **Functional Testing** and **Non-Functional Testing**. Functional testing is the most common; it's the traditional kind. Functional testing ensures that the software's features and functionalities behave as expected. Non-functional testing focuses on other aspects such as security, stability, accessibility, etc.


<div class="mermaid">
graph TD
  %% Estilos para el nodo principal (Cuadrado y grande)
  root[Software testing Types]:::principal
  
  %% Ramas Principales
  root --> Func[Functional]
  root --> NoFunc[Non-Functional]

  %% Desglose Funcionales
  Func --> Unit[Unit]
  Func --> Int[Integration]
  Func --> Sis[System]
  Func --> Acep[Acceptance]
  Func --> San[Sanity]

  %% Desglose No Funcionales
  NoFunc --> Rend[Perfomance]
  NoFunc --> Seg[Segurity]
  NoFunc --> Usab[Usability]
  NoFunc --> Comp[Compatibility]

  %% Sub-rama Rendimiento
  Rend --> Carga[Load]
  Rend --> Estres[Stress]

  %% AQUI ESTA EL CAMBIO: Cambié #f9f (rosa) por #e5e5e5 (gris claro)
  classDef principal fill:#e5e5e5,stroke:#333,stroke-width:2px,font-size:18px;
</div>

#### Let's delve a little deeper into functional testing:
- **Unit Testing:** Verifies that each individual component or unit of the source code functions correctly in isolation.

- **Integration Testing:** Evaluates how the different modules or components of a system interact and communicate with each other.

- **Smoke Testing:** A set of quick tests that ensure the most basic and critical functionalities of a new version operate without blocking errors.

- **Regression Testing:** Consists of retesting a previously analyzed system to ensure that recent changes have not introduced new defects.

- **Acceptance Testing:** Final validation performed by the user or client to determine if the software meets business requirements and can be accepted.

#### Now we'll talk about non-functional testing
- **Performance Testing:** Determines the stability, speed, and scalability of an application under a specific workload.

- **Load Testing:** A type of performance test that measures system behavior when increasing the load of users or transactions to its expected limit.

- **Stress Testing:** Evaluates the robustness and breaking points of software by subjecting it to extreme conditions beyond its normal capacity.

- **Security Testing:** Activities focused on finding vulnerabilities to prevent attacks and protect the integrity of important information.

The above are notes I took while taking the aforementioned course. I would like to thank Professor Esteban Balvin.
