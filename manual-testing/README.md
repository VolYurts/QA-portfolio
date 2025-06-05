# Manual QA Portfolio

This repository contains the manual testing documentation for testing the Magento demo web application:  
🔗 [https://magento.softwaretestingboard.com/](https://magento.softwaretestingboard.com/)

## 📁 Contents

- `Test_Cases/` – Structured test cases in table format (Google Sheets or CSV)
- `Checklists/` – Functional checklists to verify UI and key features
- `Bug_Reports/` – Documented bug reports with reproducible steps and screenshots
- `Test-Plan` – High-level plan outlining scope, objectives, and testing approach
- `Test-Summary` – Summary of test execution results, passed/failed status, and findings
- `Test-Design-Techniques` – List of applied test design techniques (EP, BVA, Decision Table, etc.)
- `Test-Scenarios` – High-level testing scenarios describing typical user actions and expected flows

---

## 📌 Test Scope

- User Registration  
- Login Functionality  
- Shopping Cart  
- Checkout Process  
- Product Search & Filters  

---

## ✅ Test Design Techniques

Applied the following test design techniques:

- **Equivalence Partitioning (EP)**
- **Boundary Value Analysis (BVA)**
- **Decision Table Testing**
- **Error Guessing**

---

## 🐞 Bugs Found

| Bug ID  | Title                                      | Severity | Status   |
|--------|--------------------------------------------|----------|----------|
| BUG-001 | Registering with valid email shows error  | Major    | Open     |
| BUG-002 | Valid login fails with account error      | Critical | Open     |
| BUG-003 | Checkout fails due to login error         | Major    | Open     |
| BUG-004 | Empty login fields show no validation msg | Minor    | Open     |

---

## 🔧 Tools Used

- Testomat.io
- Google Sheets – for test case management  
- Visual Studio Code – for writing documentation  
- Screenshots – manually added to bug reports

---

## 📸 How to View Bug Reports with Images

Screenshots are stored in `/bug_reports/bug_reports_test_cases`.

---

## 📄 Author

**Volodymyr**  
  


---

> _This manual QA portfolio is part of my learning path and showcases real testing practice using a demo e-commerce website._
