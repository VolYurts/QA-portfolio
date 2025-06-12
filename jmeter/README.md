# JMeter Performance Tests for Magento Demo Store

This repository contains basic performance tests created with Apache JMeter for the demo Magento store [magento.softwaretestingboard.com](https://magento.softwaretestingboard.com).

## Test Scenarios

1. **Home Page Load Test**  
   - **Request Type:** GET  
   - **URL:** `/`  
   - **Purpose:** Measure the load time of the home page.  
   - **Expected Result:** HTTP 200 OK with page content loaded within acceptable time.

2. **Product Page Load Test**  
   - **Request Type:** GET  
   - **URL:** `/fusion-backpack.html`  
   - **Purpose:** Check performance of the "Fusion Backpack" product page.  
   - **Expected Result:** HTTP 200 OK, page contains product details and "Add to Cart" button.

3. **Add to Cart Test**  
   - **Request Type:** POST  
   - **URL:** `/checkout/cart/add/uenc/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9icmVhdGhlLWVhc3ktdGFuay5odG1s/product/1812`  
   - **Purpose:** Verify that the "Breathe-Easy Tank" product can be successfully added to the shopping cart.  
   - **Expected Result:** HTTP 302 Found (redirect), product is added to the cart.

4. **Load Test with 250 Users**  
   - **Purpose:** Simulate 250 concurrent users performing actions on the site.  
   - **Outcome:** One failed request detected during the test.  
   - **Evidence:** Screenshots of this test run, including the failure, are saved in the `jmeter/screenshots` folder.

## Folder Structure

- `jmeter/` — contains JMeter test plans (`.jmx` files) and related test artifacts  
- `jmeter/screenshots/` — contains screenshots from test runs for documentation and debugging, including the 250 users load test and failure evidence  

## Tools Used

- Apache JMeter 5.x for test execution    
- Chrome browser for manual verification  

---
