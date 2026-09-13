# 🍔 Food Ordering System

## 📌 Introduction

The **Food Ordering System** is a basic Python project that allows users to view a food menu, select food items, enter quantities, and calculate the total bill.

This project is created using basic Python concepts up to **functions**, making it suitable for beginners.

---

## 🎯 Objectives

The main objectives of this project are:

* Display a food menu.
* Allow the user to select food items.
* Take the quantity of each item.
* Calculate the total price.
* Display the final bill.
* Provide a simple and easy-to-use menu.

---

## 🛠️ Technologies Used

* **Python**
* **Markdown**

### Python Concepts Used

* Variables
* Input and Output
* Data Types
* Operators
* `if-elif-else`
* `while` loop
* Lists
* Dictionaries
* Functions

---

## 🍕 Food Menu

| No. | Food Item    | Price |
| --- | ------------ | ----: |
| 1   | Pizza        |  ₹200 |
| 2   | Burger       |  ₹100 |
| 3   | Sandwich     |   ₹80 |
| 4   | Pasta        |  ₹150 |
| 5   | French Fries |   ₹70 |
| 6   | Exit         |     - |

---

## ⚙️ Working of the Project

The project works in the following steps:

1. The program displays the food menu.
2. The user selects a food item.
3. The program asks for the quantity.
4. The price is multiplied by the quantity.
5. The amount is added to the total bill.
6. The menu is displayed again.
7. The user can order another item.
8. When the user selects **Exit**, the final bill is displayed.

---

## 🧩 Functions Used

### 1. `show_menu()`

This function displays all available food items and their prices.

### 2. `order_food()`

This function takes the user's food choice and quantity and calculates the price.

### 3. `calculate_bill()`

This function calculates and displays the final total amount.

### 4. `main()`

This is the main function that controls the complete program.

---

## 💻 Sample Code

```python
menu = {
    1: ["Pizza", 200],
    2: ["Burger", 100],
    3: ["Sandwich", 80],
    4: ["Pasta", 150],
    5: ["French Fries", 70]
}

total = 0


def show_menu():
    print("\n----- FOOD MENU -----")

    for number, item in menu.items():
        print(number, item[0], "- ₹", item[1])

    print("6. Exit")


def order_food():
    global total

    choice = int(input("Enter your choice: "))

    if choice >= 1 and choice <= 5:
        quantity = int(input("Enter quantity: "))

        price = menu[choice][1]
        amount = price * quantity

        total = total + amount

        print(menu[choice][0], "added to your order.")
        print("Amount: ₹", amount)

    elif choice == 6:
        print("\nThank you for ordering!")

    else:
        print("Invalid choice.")


def calculate_bill():
    print("\n======================")
    print("      FINAL BILL")
    print("======================")
    print("Total Amount: ₹", total)
    print("======================")


def main():
    while True:
        show_menu()

        choice = int(input("Enter your choice: "))

        if choice == 6:
            break

        elif choice >= 1 and choice <= 5:
            quantity = int(input("Enter quantity: "))

            price = menu[choice][1]
            amount = price * quantity

            global total
            total = total + amount

            print(menu[choice][0], "added successfully!")
            print("Amount: ₹", amount)

        else:
            print("Invalid choice. Please try again.")

    calculate_bill()


main()
```

---

## 📥 Input

The program takes the following inputs from the user:

* Food item number
* Quantity of food
* User's choice to continue or exit

### Example

```text
Enter your choice: 1
Enter quantity: 2
```

---

## 📤 Output

Example output:

```text
----- FOOD MENU -----
1 Pizza - ₹ 200
2 Burger - ₹ 100
3 Sandwich - ₹ 80
4 Pasta - ₹ 150
5 French Fries - ₹ 70
6. Exit

Enter your choice: 1
Enter quantity: 2

Pizza added successfully!
Amount: ₹ 400
```

After selecting Exit:

```text
======================
      FINAL BILL
======================
Total Amount: ₹ 400
======================
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
* Simple menu-based system.
* Calculates the bill automatically.
* Good project for practicing functions.

---

## 🔮 Future Improvements

The project can be improved in the future by adding:

* Customer name
* Food order receipt
* Discount system
* GST calculation
* More food items
* Order history
* File handling
* Database
* GUI interface

---

## 👨‍💻 Author

**Aryan Gill**

### ⭐ Project Level

**Beginner Python Project**

This project is created for learning and practicing basic Python programming concepts.
