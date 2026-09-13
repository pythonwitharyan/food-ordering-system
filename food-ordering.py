
# Login Details
db = ["aryan@gmail.com", "aryan123"]

# Login
while True:
    email = input("📧 Enter your email: ")

    if email in db:
        break
    else:
        print("❌ Enter valid email!")


while True:
    password = input("🔐 Enter your password: ")

    if password == db[1]:
        print("✅ Login successful!")
        break
    else:
        print("❌ Enter valid password!")


# Customer Details
customer = input("\n👤 Enter your name: ")
phone = input("📞 Enter your phone number: ")


print(f"\n👋 Welcome, {customer}!")
print("🍽️ Please select items from the menu")


# Food Menu
food = [
    "🍗 Chicken Biryani",
    "🍔 Cheese Burger",
    "🍕 Margherita Pizza",
    "🌯 Veg Roll",
    "🥤 Cold Coffee"
]

prices = [180, 130, 200, 90, 70]


# Function to Display Menu
def show_menu():
    print("\n===== 🍽️ FOOD MENU =====")

    for i in range(len(food)):
        print(f"{i + 1}. {food[i]} - ₹{prices[i]}")


# Function to Select Food
def select_food():
    while True:
        choice = input("\n🍕 Enter food number: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(food):
                return choice - 1

        print("❌ Invalid food number! Please try again.")


# Function to Enter Quantity
def enter_quantity():
    while True:
        quantity = input("🔢 Enter quantity: ")

        if quantity.isdigit():
            quantity = int(quantity)

            if quantity > 0:
                return quantity

        print("❌ Quantity must be greater than 0!")


# Function to Calculate Price
def calculate_price(food_index, quantity):
    return prices[food_index] * quantity


# Function to Take Order
def food_order():
    total = 0

    while True:
        show_menu()

        food_index = select_food()

        quantity = enter_quantity()

        price = calculate_price(food_index, quantity)

        total = total + price

        print("\n===== 🛒 ORDER DETAILS =====")
        print(f"🍽️ Item: {food[food_index]}")
        print(f"💵 Price: ₹{prices[food_index]}")
        print(f"🔢 Quantity: {quantity}")
        print(f"🧾 Subtotal: ₹{price}")
        print(f"💰 Current Total: ₹{total}")

        more = input(
            "\n🔄 Do you want to order anything more? (yes/no): "
        ).lower()

        if more == "no":
            break

        elif more != "yes":
            print("❌ Please enter yes or no!")

    return total


# Function to Apply Coupon
def apply_coupon(total):
    while True:
        coupon = input(
            "\n🎟️ Enter coupon code (food50 / food100 / no): "
        ).lower()

        if coupon == "food50":
            print("🎉 ₹50 coupon applied!")
            total = total - 50
            return total

        elif coupon == "food100":
            print("🎉 ₹100 coupon applied!")
            total = total - 100
            return total

        elif coupon == "no":
            print("❌ No coupon applied.")
            return total

        else:
            print("❌ Invalid coupon code!")


# Start Food Ordering
total = food_order()

# Apply Coupon
final_amount = apply_coupon(total)


# Final Bill
print("\n========== 🧾 FINAL BILL ==========")
print(f"👤 Customer Name: {customer}")
print(f"📞 Phone Number: {phone}")
print(f"💰 Food Total: ₹{total}")
print(f"💵 Final Amount: ₹{final_amount}")

print("\n✅ Order Confirmed!")
print("🙏 Thank you for ordering!")
print("🎉 Have a great day! 😊")

