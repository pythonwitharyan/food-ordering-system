# 🍔 Food Ordering System

### ### 🐍 PYTHON 3.X | 🟢 BEGINNER | 🚀 MINI PROJECT | 💻 CONSOLE

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Level](https://img.shields.io/badge/Level-Beginner-green) ![Project](https://img.shields.io/badge/Project-Mini%20Project-orange) ![Platform](https://img.shields.io/badge/Platform-Console-lightgrey)
### 🐙 VIEW ON GITHUB

[⭐ Visit Repository](https://github.com/pythonwitharyan/food-ordering-system)

---

## 📌 Introduction

The **Food Ordering System** is a basic Python project that allows users to log in, enter customer details, view a food menu, select food items, enter quantities, calculate the total bill, and apply a coupon.

This project is created using basic Python concepts up to **functions**, making it suitable for beginners.

---

## 🎯 Objectives

The main objectives of this project are:

- Provide a simple login system.
- Take customer name and phone number.
- Display a food menu with prices.
- Allow the user to select food items.
- Take the quantity of each item.
- Calculate the price of ordered food.
- Allow the user to order multiple items.
- Calculate the total amount.
- Apply a coupon discount.
- Display the final bill.
- Confirm the order.

---

## 🛠️ Technologies Used

- **Python**
- **Markdown**

### Python Concepts Used

- Variables
- Input and Output
- Data Types
- Operators
- `if-elif-else`
- `while` loop
- `for` loop
- Lists
- Functions
- String methods
- Basic calculations

---

## 🔐 Login System

The project contains a simple login system.

The user must enter a valid email and password before placing an order.

### Login Details

- **Email:** `aryan@gmail.com`
- **Password:** `aryan123`

If the user enters an incorrect email or password, the program asks the user to enter the correct information again.

---

## 👤 Customer Details

After successful login, the program takes the following customer information:

- Customer Name
- Phone Number

The customer name is used in the welcome message and final bill.

---

## 🍽️ Food Menu

The project contains the following food items:

| No. | Food Item | Price |
|---:|---|---:|
| 1 | 🍗 Chicken Biryani | ₹180 |
| 2 | 🍔 Cheese Burger | ₹130 |
| 3 | 🍕 Margherita Pizza | ₹200 |
| 4 | 🌯 Veg Roll | ₹90 |
| 5 | 🥤 Cold Coffee | ₹70 |

---

## ⚙️ Working of the Project

The project works in the following steps:

1. The program starts with the login system.
2. The user enters their email.
3. The email is checked for validity.
4. The user enters their password.
5. The password is checked.
6. After successful login, the customer enters their name and phone number.
7. A welcome message is displayed.
8. The food menu is displayed.
9. The user selects a food item.
10. The user enters the required quantity.
11. The program calculates the price of the selected item.
12. The amount is added to the current total.
13. The user can order another food item.
14. The process continues until the user chooses not to order more.
15. The program asks for a coupon code.
16. A valid coupon discount is applied.
17. The final bill is displayed.
18. The order is confirmed.

---

## 🧩 Functions Used

### 1. `show_menu()`

Displays all available food items and their prices.

### 2. `select_food()`

Takes the food number from the user and checks whether the selected food item is valid.

### 3. `enter_quantity()`

Takes the quantity from the user and checks that the quantity is greater than zero.

### 4. `calculate_price()`

Calculates the price of the selected food according to its quantity.

### 5. `food_order()`

Controls the complete food ordering process.

It allows the user to:

- View the menu
- Select food
- Enter quantity
- Calculate the subtotal
- Add items to the total
- Order multiple food items

### 6. `apply_coupon()`

Allows the user to enter a coupon code and applies the available discount.

---

## 🎟️ Coupon System

The project includes a simple coupon system.

### Available Coupons

| Coupon Code | Discount |
|---|---:|
| `food50` | ₹50 |
| `food100` | ₹100 |
| `no` | No Discount |

The user can enter a coupon after completing the food order.

If an invalid coupon is entered, the program asks the user to enter a valid coupon code.

---

## 🧮 Price Calculation

The price of an item is calculated using:

**Item Price × Quantity = Subtotal**

For example:

- Chicken Biryani = ₹180
- Quantity = 2

**Subtotal = ₹180 × 2 = ₹360**

The subtotal is then added to the total order amount.

---

## 🔄 Project Workflow

```text
START
  ↓
Login
  ↓
Enter Email
  ↓
Check Email
  ↓
Enter Password
  ↓
Check Password
  ↓
Enter Customer Details
  ↓
Display Food Menu
  ↓
Select Food
  ↓
Enter Quantity
  ↓
Calculate Price
  ↓
Add Amount to Total
  ↓
Order More?
  ├── Yes → Display Menu Again
  │
  └── No
       ↓
  Apply Coupon
       ↓
Calculate Final Amount
       ↓
Display Final Bill
       ↓
Order Confirmed
       ↓
      END
````

---

## 📥 Input

The program takes the following inputs:

* Email
* Password
* Customer name
* Phone number
* Food item number
* Food quantity
* Choice to order more food
* Coupon code

### Example Input

```text
Email: aryan@gmail.com
Password: aryan123

Customer Name: Aryan
Phone Number: 9876543210

Food Number: 1
Quantity: 2

Order More: no
Coupon: food50
```

---

## 📤 Output

The program displays:

* Login status
* Welcome message
* Food menu
* Selected food item
* Food price
* Quantity
* Subtotal
* Current total
* Coupon discount
* Final amount
* Order confirmation

### Example Final Bill

```text
========== FINAL BILL ==========

Customer Name: Aryan
Phone Number: 9876543210

Food Total: ₹360
Final Amount: ₹310

Order Confirmed!

Thank you for ordering!

Have a great day!
```

---

## 📂 Project Structure

```text
Food-Ordering-System/
│
├── food_ordering.py
│
└── README.md
```

---

## ✅ Advantages

* Easy to understand.
* Beginner-friendly.
* Uses basic Python concepts.
* Includes a simple login system.
* Provides a simple food menu.
* Allows multiple food items.
* Calculates the total automatically.
* Includes a coupon system.
* Uses functions to divide the program into different tasks.
* Useful for practicing basic Python programming.

---

## 🔮 Future Improvements

The project can be improved in the future by adding:

* More food items
* Food categories
* GST calculation
* Payment options
* Order receipt
* Order history
* File handling
* Database
* GUI interface
* Online payment
* Delivery tracking

---

## 👨‍💻 Author

**Aryan Gill**

### ⭐ Project Level

**Beginner Python Project**

This project is created for learning and practicing basic Python programming concepts up to **functions**.

---

## 📌 Conclusion

The **Food Ordering System** is a simple beginner-level Python project that demonstrates how basic programming concepts can be used to create a practical application.

The project includes **login validation, customer details, food selection, quantity calculation, multiple food orders, coupon discounts, functions, and final bill generation**.

It is useful for beginners who want to understand how Python functions and basic programming concepts work together in a real-world project.

---

### 💖 MADE WITH

**💖 & 🐍 PYTHON**

**🟢 BEGINNER-FRIENDLY**

---

### ⭐ VISIT REPOSITORY

[🐙 ⭐ VISIT REPOSITORY](https://github.com/pythonwitharyan/food-ordering-system)

```

You can copy **everything inside the code box** and paste it directly into your GitHub `README.md`.
```
