# 📄 Test Summary Report – Magento Demo Store

## 🔎 Project Name:
Magento Demo Store QA Testing

## 🧪 Test Type:
Manual Functional Testing (Web UI)

## 📅 Test Period:
June 5–7, 2025

## 👨‍💻 Tester:
Volodymyr

---

## ✅ Test Execution Summary

| Test Scenario                     | Status   | Comments                                                                                     |
|----------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS01: Register with valid data   | **Failed**  | Confusing success message; no clear next steps (e.g., no login or reset password links).      |
| TS02: Invalid email              | Passed   | Proper validation message displayed.                                                        |
| TS03: Existing email             | Passed   | Duplicate email prevented correctly.                                                        |
| TS04: Valid login                | Passed   | User logged in successfully.                                                                |
| TS05: Incorrect password         | **Failed**  | User cannot log in even with correct credentials — possible authentication bug or user status issue. |
| TS06: Logout                     | **Failed**  | Error message on logout/login is too generic and misleading, may confuse users about account status. |
| TS07: Add to cart as guest       | Passed   | Item added successfully to cart.                                                            |
| TS08: Update item quantity       | Passed   | Quantity updated and total price correct.                                                   |
| TS09: Cart persists on refresh   | Passed   | Cart contents retained after page refresh.                                                  |
| TS10: Complete checkout          | **Failed**  | User unexpectedly logged out or rejected during checkout despite valid session; core functionality blocked. |
| TS11: Missing shipping info      | Passed   | Proper warning message displayed when shipping info is missing.                             |
| TS12: Product search             | Passed   | Search results correctly matched input query.                                               |

---

## 📊 Overall Result:
**8 Passed, 4 Failed** – Key issues in registration messaging, login/logout flows, and checkout process block some critical user actions.

---

## 📝 Issues & Recommendations:

### TS01 (Registration Success Message)
- Add clear instructions or links after registration (e.g., "Proceed to Login", "Reset Password").

### TS05 (Login with Correct Credentials Fails)
- Investigate authentication backend or user account status.
- Check if account is locked, disabled, or if backend service errors occur.

### TS06 (Logout Error Message)
- Improve error message clarity; avoid generic texts that confuse users.
- Ensure consistent user feedback on logout and login errors.

### TS10 (Checkout Failure)
- Investigate session handling and authorization during checkout.
- Ensure user remains logged in throughout checkout process.
- Fix any bugs causing unexpected logout or rejection.

---

## 📋 Checklist Review Summary:

All checklists were completed during the testing process.  
✅ **All checklist items were verified and passed without issues.**  
They helped ensure comprehensive coverage of UI elements, validation, and expected behavior across features.

---

## 📎 Attachments:
- Screenshots of failed scenarios  
- Logs from authentication and checkout modules  
- Bug reports filed with priority to TS05 and TS10

---
