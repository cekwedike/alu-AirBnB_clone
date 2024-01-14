def calculate_total_cost(price_per_night, number_of_nights, discount=0):
    """
    Calculate the total cost of an AirBnB stay.

    Args:
        price_per_night (float): The price per night for the AirBnB.
        number_of_nights (int): The number of nights the guest is staying.
        discount (float): An optional discount percentage. Default is 0.

    Returns:
        float: The total cost of the AirBnB stay, including the discount.
    """
    total_cost = price_per_night * number_of_nights
    total_cost -= total_cost * (discount / 100)
    return total_cost
