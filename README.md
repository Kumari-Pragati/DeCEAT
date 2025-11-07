# 🧠 DeCEAT:  Decoding Carbon Emissions of AI-driven Testing

This repository contains the complete experimental framework, datasets, and metric resources developed for the paper  
**“Sustainable Prompt Engineering for Automated Test Generation with Small Language Models (AST 2026 Submission)”**.  

DeCEAT — *Decoding Carbon Emissions of AI-driven Testing* — is a sustainability-aware framework that quantifies the trade-offs between **energy efficiency**, **carbon emissions**, **test coverage quality**, and **execution time** in small language models (SLMs).  
It integrates structured prompt engineering, emission tracking via **CodeCarbon**, and unified sustainability metrics for transparent and reproducible analysis.

---

## 🔍 Overview

The foundation of this experimental evaluation is the **HumanEval benchmark**, a standardized dataset comprising **164 Python programming tasks** used to measure the coding capability of language models.  
You can access the dataset here: 👉 [Hugging Face – openai/openai_humaneval](https://huggingface.co/datasets/openai/openai_humaneval)

Each record in HumanEval includes:

| Field | Description |
|:--|:--|
| `task_id` | Unique identifier for each problem |
| `prompt` | Natural-language problem statement and required Python function signature |
| `canonical_solution` | Correct reference implementation |
| `test` | Human-written assertion-based unit tests |
| `entry_point` | Callable name of the function to be tested |

The **Test Script Generation** phase focuses on the systematic creation of unit tests by SLMs based on structured prompts and prepared data modules.  
All models are instantiated under various quantization schemes to maximize efficiency and minimize the computational footprint during inference.

---

## ⚙️ Experimental Setup

Experiments were conducted on **Google Colab** using an **NVIDIA T4 GPU (16 GB RAM)**.  
The setup employed the following libraries and tools:

- **Transformers**, **Accelerate**, **BitsAndBytes** → for model quantization and inference  
- **CodeCarbon** → for energy and emission tracking  
- **tqdm**, **pandas**, **coverage.py** → for runtime monitoring, data handling, and coverage computation  

**Carbon intensity factor (I)** represents the 12-month average value for *Alberta, Canada*, obtained from **ElectricityMaps**, ensuring realistic emission calculations.

---

### 🧮 Generation and Run Parameters

| **Parameter** | **Value** |
|:--|:--|
| Temperature | 0.2 |
| `max_new_tokens` | 1024 |
| Batch size | 5 code files per batch |
| Model quantization | 4-bit or 8-bit (as defined in framework) |
| Tracking tool | CodeCarbon |

**Quantization Scheme**  
- **8-bit Quantization** → *Phi-3.5-mini* and *Qwen 2.5-1.5B*  
- **4-bit Quantization** → *DeepSeek-Coder-7B*, *Mistral-7B*, *Llama-3-8B*

All models were executed under identical generation parameters to ensure fairness across all adaptive prompt variants (**APV₀ – APV₃**).

---

## 🧩 DeCEAT Workflow

The **DeCEAT** pipeline comprises five sequential stages that ensure reproducibility and uniformity:

1. **Batch Execution** – Each model generates test scripts under the four prompt variants (APV₀–APV₃), producing one CodeCarbon log per variant.  
2. **Data Consolidation** – The 20 CSV logs are merged into a unified dataset containing emission (kgCO₂), energy (kWh), execution time (s), and GPU metrics.  
3. **Coverage Measurement** – Unit-test coverage (%) is computed using `coverage.py` and averaged across all prompt variants.  
4. **Metric Input Extraction** – The dataset yields coverage, emission (gCO₂), energy (kWh), and time (s) inputs for all primary and derived metrics.  
5. **Evaluation Phases** – Computed inputs are used to derive both the **Primary Analysis metrics (SCI, SEI, CER)** and the **Trade-off Analysis metrics (GQI, SCV, SVI, GFβ)**.

This structured process ensures consistent emission factors and reproducible sustainability comparisons across all SLMs.

---

## 📁 Repository Structure

| Folder / File | Description |
|:--|:--|
| **`/CSV Files/`** | 20 CodeCarbon CSV logs generated for each model–prompt combination (APV₀–APV₃ × 5 models). Each records energy, emission, and runtime metrics. |
| **`/Code File/`** | Two reference notebooks (`APV₀_8bit.ipynb`, `APV₃_4bit.ipynb`). All other models follow the same structure — only model name and quantization settings change. |
| **`/HumanEval_Integrated_Dataset/`** | Merged dataset of 164 Python tasks combining docstring definitions, canonical solutions, and entry points into runnable functions. |
| **`/Prompts/`** | Four prompt PDFs (`APV₀` to `APV₃`) illustrating incremental prompt complexity and feature addition. |
| **`/Test_Scripts_Generated_by_SLMs/`** | Five subfolders (one per SLM) containing test scripts generated under all four prompt variants. |
| **`Entropic_Prompt_Structure_Image.png`** | Visualization of the Anthropic-style prompt engineering pattern followed throughout DeCEAT. |
| **`Master_Sheet_For_All_Metrics.xlsx`** | Complete metric calculation sheet with formulas and values for SCI, SEI, CER, GQI, SVI, GFβ. |
| **`LICENSE`** | MIT License. |
| **`README.md`** | Project documentation (this file). |

---

## 📊 Metric Computation

Metric computations are derived from the processed CodeCarbon logs.  
Two constants are maintained throughout:
- **I** → Grid carbon intensity (gCO₂ / kWh)  
- **R = 5** → Number of code files per batch  

### Primary Metrics
- **SCI** – Sustainable Carbon Intensity (Emission per run)  
- **SEI** – Sustainable Energy Index (Inverse of SCI)  
- **CER** – Carbon Efficiency Ratio (Coverage per Emission)

### Derived Metrics
- **SI** – Stability Index  
- **SCV** – Sustainability Coverage Variance  
- **SVI** – Sustainable Velocity Index  
- **GFβ** – Green F-Beta Score for eco-efficiency and quality trade-off (β ∈ {0.3, 0.6, 0.9, 1.2, 1.5, 1.8})

All formulae, normalization steps, and complete calculation workflows are available in the Excel master sheet for reproducibility.

---

## 🧪 Reproducibility

Each model–prompt variant produces one CSV log per run, yielding a total of 20 logs (5 models × 4 prompts).  
Each log captures 33 executions per prompt variant, providing granularity for averaging and metric computation.  
The merged dataset, along with the Excel metric sheet, ensures **full transparency and replicability** of the sustainability analysis.

---



