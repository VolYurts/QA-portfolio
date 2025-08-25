# Playwright Tests 🚀

Automated UI tests using **Playwright (Python)** with **Page Object Model (POM)** structure.

## Folder Structure
- `pages/` – page classes (BasePage, SimplePage, LikeAButton)
- `tests/` – Pytest test scripts
- `conftest.py` – pytest fixtures

# Run all tests
pytest tests

# Run specific test
pytest tests/test_like_a_button.py::test_like_a_button_click
