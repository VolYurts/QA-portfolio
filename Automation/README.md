# 🤖 Automated Tests

This section of my QA portfolio showcases my skills in **automated testing**, including both **UI** and **API** testing. All tests are written in **Python** using the **Pytest** framework.

---

## 🧪 UI Testing

- Developed with **Selenium** and **Pytest**
- Tested on: [https://magento.softwaretestingboard.com](https://magento.softwaretestingboard.com)
- Key scenarios covered:
  - Product search functionality
  - Adding products to the cart
  - Navigating to the "Training" category

✅ Tests are run both **locally** and via **GitHub Actions CI/CD**  
📸 Screenshots of Allure reports are available in the `allure_screenshots` folder

---

## 🔌 API Testing

- Written using the `requests` library and `Pytest`
- Tests verify key API endpoints and response behavior
- Reusable fixtures and setup logic via `conftest.py`

---

## ⚙️ GitHub Actions Integration

UI tests are integrated into **GitHub Actions** workflows:
- Automatically triggered on `push`
- Manually triggered via `workflow_dispatch` with dropdown test selection

Each test run installs dependencies, sets up Chrome, and executes UI test cases on a Linux runner.

---

## 📷 Allure Reporting

- Local test runs generate Allure reports with:
  - Test status (passed/failed)
  - Timing and others
- Instead of publishing full reports, screenshots of Allure results are included for review

---

## 🧪 How to Run Tests Locally

### Run UI tests:
```bash
cd automation/ui_tests
pytest
cd automation/api_tests
pytest

---


## 🛠️ Tools & Technologies Used

- **Python**
- **Pytest**
- **Selenium**
- **Allure** (local reports)
- **requests**
- **GitHub Actions**

