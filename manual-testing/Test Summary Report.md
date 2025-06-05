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

## ✅ Test Execution Summary (Grouped by Module)

### 1. 👤 User Registration
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS01         | Register with valid user data        | ❌ Failed | Confusing success message; no clear next steps (e.g., no login or reset password links).     |
| TS02         | Register with invalid email          | ✅ Passed | Proper validation message displayed.                                                         |
| TS03         | Register with existing email         | ✅ Passed | Duplicate email prevented correctly.                                                         |

---

### 2. 🔐 Login Functionality
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS04         | Successful login with valid credential | ❌ Failed | User cannot log in even with correct credentials — possible authentication or user status issue. |
| TS05         | Login with incorrect password        | ❌ Failed | Incorrect password message too generic or not shown; validation unclear.                     |
| TS06         | Login with empty fields              | ✅ Passed | Validation works correctly; user prevented from submitting empty form.                       |

---

### 3. 🛒 Shopping Cart
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS07         | Add to cart as guest                 | ✅ Passed | Item added successfully to cart.                                                             |
| TS08         | Update item quantity                 | ✅ Passed | Quantity updated and total price correct.                                                    |
| TS09         | Cart persists on refresh             | ✅ Passed | Cart contents retained after page refresh.                                                   |

---

### 4. 💳 Checkout Process
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS10         | Complete checkout                    | ❌ Failed | User unexpectedly logged out or rejected during checkout despite valid session.              |
| TS11         | Missing shipping info                | ✅ Passed | Proper warning message displayed when shipping info is missing.                              |

---

### 5. 🔍 Product Search
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS12         | Product search                       | ✅ Passed | Search results correctly matched input query.                                                |

---

## 📊 Overall Result:
**8 Passed, 4 Failed** – Critical issues found in registration, login, and checkout flows. These must be fixed before release.

---

## 📝 Issues & Recommendations:

### TS01 – Register with valid data
- Add clear post-registration instructions or redirect (e.g., "Proceed to Login", "Reset Password").

### TS04 – Login with valid credentials
- Review authentication logic; verify account status, session handling, and error logs.

### TS05 – Login with incorrect password
- Improve error messaging. Ensure incorrect password shows clear validation.

### TS10 – Checkout process fails
- Investigate session expiration or authorization issues causing logout during checkout.

---

## 📋 Checklist Review Summary:

All functional checklists were filled and verified.  
✅ **All checklist items passed** – including validations, field visibility, and user interaction flows.

---

## 📎 Attachments:
- Screenshots of failed test scenarios  
- Authentication, registration, and checkout logs  
- Bug reports filed for TS01, TS04, TS05, and TS10

---
