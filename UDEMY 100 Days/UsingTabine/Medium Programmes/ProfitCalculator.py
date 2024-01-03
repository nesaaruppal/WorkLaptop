def calculate_profit(cost_price_per_unit, sell_price_per_unit, starting_inventory):
    """
    Calculates the total profit made from selling a product given the cost price per unit, sell price per unit, and starting inventory.

    Args:
        cost_price_per_unit (float): The cost price per unit of the product.
        sell_price_per_unit (float): The sell price per unit of the product.
        starting_inventory (int): The starting inventory of the product.

    Returns:
        float: The total profit made from selling the product, rounded to the nearest dollar.

    """
    profit = sell_price_per_unit * starting_inventory - cost_price_per_unit * starting_inventory
    return round(profit, 2)

input_dict = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}

profit = calculate_profit(input_dict['cost_price'], input_dict['sell_price'], input_dict['inventory'])
print(f"Your total profit is: £{profit}!!")