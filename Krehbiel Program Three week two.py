#Programmer: Ben Krehbiel
#Date: 1/27/2025
#Title: Vending machine store

items = {
    1: 3.50, 2: 5.00, 3: 12.00, 4: 1.50,
    5: 7.50, 6: 0.75, 7: 13.00, 8: 4.75, 9: 19.00
}
total = 0.0

def calculate_total_purchase():
    global total
    print("                     Welcome to our Store! \n"
          "   please select the number relating to the item you would like\n"
          "   1 - 12 Eggs $3.50 | 2 - Bag of flour $5.00 | 3 - Beef $12.00\n"
          "4 - Twix bar $1.50 | 5 - Apple juice $7.50 | 6 - Corn $0.75 per head\n"
          " 7 - Lambchop - $13.00 | 8 - Bag of celery $4.75 | 9 - Sushi $19.00")
    for i in range(5):
        item_number = int(input("Enter a number, then repeat: "))
        if item_number in items:
            total += items[item_number]
        else:
            print("Invalid choice, try again.")


#mainline
calculate_total_purchase()
print(f"Your total is ${total:.2f}")