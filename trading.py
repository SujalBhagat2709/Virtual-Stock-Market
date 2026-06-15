from market import StockMarket


market = StockMarket()

if not market.get_market():

    market.create_company(
        "TechX",
        100
    )

    market.create_company(
        "GameCorp",
        50
    )

    market.create_company(
        "FoodHub",
        75
    )

print(
    "\n====================="
)

print(
    "VIRTUAL STOCK MARKET"
)

print(
    "====================="
)

while True:

    print(
        "\nAvailable Companies:"
    )

    for company, data in (
        market.get_market()
        .items()
    ):

        print(
            f"{company}"
            f" ₹{data['price']}"
        )

    command = input(
        "\nCommand:\n"
        "buy company qty\n"
        "sell company qty\n"
        "exit\n> "
    )

    if command.lower() == "exit":

        break

    parts = command.split()

    if len(parts) != 3:

        print(
            "Invalid Command"
        )

        continue

    action = parts[0]

    company = parts[1]

    qty = int(parts[2])

    stock = market.get_company(
        company
    )

    if not stock:

        print(
            "Company Not Found"
        )

        continue

    if action == "buy":

        stock["price"] += qty // 10

        stock["volume"] += qty

        print(
            f"\nBought {qty}"
            f" shares of {company}"
        )

    elif action == "sell":

        stock["price"] -= qty // 10

        stock["volume"] -= qty

        if stock["price"] < 1:

            stock["price"] = 1

        print(
            f"\nSold {qty}"
            f" shares of {company}"
        )

    market.save()

    print(
        f"\nNew Price:"
        f" ₹{stock['price']}"
    )