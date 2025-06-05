# 🛠 Test Design Techniques – Magento Demo Store (Shortened)

---

## 1. ✅ Equivalence Partitioning (EP)  
Used for:  
- Registration (valid/invalid email)  
- Login (correct/incorrect password)  
- Checkout (valid/invalid payment or shipping info)  

**Example:**  
- Valid email: user@example.com  
- Invalid email: user@com, @example.com  

---

## 2. 📏 Boundary Value Analysis (BVA)  
Used for:  
- Password length (min/max characters)  
- Quantity field in cart (0, 1, max allowed)  

**Example:**  
- Password length 8–20 characters → test with 7, 8, 20, 21 characters  

---

## 3. 🧩 Decision Table Testing  
Used for:  
- Login combinations of email and password  

| Email Valid | Password Valid | Result           |  
|-------------|----------------|------------------|  
| Yes         | Yes            | Login success    |  
| Yes         | No             | Error message    |  
| No          | Yes            | Error message    |  
| No          | No             | Error message    |  

---

## 4. 🔄 State Transition Testing  
Used for:  
- Cart states (Empty → Added item → Updated quantity → Removed item)  
- Login flow (Login → Account page → Logout → Guest view)  

---

## 5. ❌ Error Guessing  
Used for:  
- Missing required fields  
- Invalid characters in input fields  
- Invalid promo codes or payment details  
