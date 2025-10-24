[![Playwright Tests](https://github.com/rzaqa/playwright-python-demo/actions/workflows/main.yml/badge.svg)](https://github.com/rzaqa/playwright-python-demo/actions/workflows/main.yml)

# 🧪 Playwright + Python System Tests for Saleor Dashboard

📊 **Allure Report:** [View Latest Report →](https://rzaqa.github.io/playwright-python-demo/)  
⚙️ **Main Pipeline:** [View or Run Workflow →](https://github.com/rzaqa/playwright-python-demo/actions/workflows/main.yml)

---

## 🧩 Testing Strategy and Scope

This repository focuses on **system-level test automation** for the **Saleor Dashboard**  
using **Playwright + Python (Pytest)**.

It covers multiple testing layers:
- 🖥️ **UI**
- 🔗 **API**
- 🧩 **Integration**
- 🚀 **E2E (End-to-End)**  
  *(with optional environment pre-checks before execution)*

> 🧠 **Note:**  
> Frontend **unit tests** (React components, validation logic, etc.) are **not** part of this repo.  
> They should be implemented in the **frontend project** using tools like **Jest** or **Vitest**.

---

## 🔹 Test Levels and Responsibilities

| **Level** | **Purpose** | **Location** | **Tools / Frameworks** |
|------------|-------------|---------------|--------------------------|
| 🧠 **Unit tests** | Verify isolated frontend or backend logic (pure functions, components, validation) | Inside the frontend / backend repositories | Jest / Vitest / Pytest |
| 🔗 **Integration tests** | Validate how backend modules and APIs interact | `tests/integration/` | Pytest + Requests |
| 🧩 **UI component (smoke) tests** | Verify that pages render correctly — all expected UI elements are visible and accessible | `tests/ui/...` | Playwright |
| 🚀 **Functional UI (E2E) tests** | Validate real user flows through the browser (login, product management, etc.) | `tests/ui/...` or `tests/e2e/...` | Playwright |
| ⚙️ **System / Contract tests** | Validate consistency between UI ↔ API contracts and external integrations | `tests/contract/` | Pytest + Schemathesis / OpenAPI |
| 📈 **Performance (optional)** | Basic API or UI performance checks | Optional | Locust / Playwright Trace Viewer |

---

## 🔹 Philosophy

This project follows a clear testing ownership model:

- 🧩 **Frontend repo** — handles **unit testing** (business logic, React components).  
- ⚙️ **This repo** — focuses on **system-level automation**:
  - UI + API + Integration + E2E verification  
  - Traceability from **requirements → tests → reports**  

🧪 **Playwright** — validates real browser behavior (not unit-level logic).  
📊 **Pytest + Allure** — provide rich reporting, tagging, and coverage tracking.
