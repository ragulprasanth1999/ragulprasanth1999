coke_price = 50
total_amount_received = 0
Amount_Due = 0
Change_Owed = 0

while coke_price > total_amount_received:
    coin = int(input("Insert a coin: "))

    # Check if the coin is a valid denomination
    if coin in [25, 10, 5]:
        total_amount_received += coin
        Amount_Due = coke_price - total_amount_received
        print("Amount Due: ", max(Amount_Due, 0))  # Ensure Amount_Due is non-negative

       # Exit the loop after providing change
    else:
        print("Amount Due: 50")

# If the user input more than the price of a coke, show the balance amount in Change Owed
if total_amount_received >= coke_price:
    Change_Owed = total_amount_received - coke_price
    print("Change Owed: ", Change_Owed)
