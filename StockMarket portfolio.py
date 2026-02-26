# Stock Portfolio Tracker
stock_prices = {
    "NIFTY 50": 180,
    "SENSEX": 250,
    "BANK NIFTY": 140,
    "BSE 100": 320
}

total_investment = 0
portfolio = {}

print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            portfolio[stock_name] = quantity
            total_investment += stock_prices[stock_name] * quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not available in price list.")

print("\n----- Portfolio Summary -----")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    print(f"{stock} - {qty} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save_option == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-----------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock} - {qty} shares x ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    
    print("Portfolio saved to 'portfolio_summary.txt'")

print("Program Ended.")
