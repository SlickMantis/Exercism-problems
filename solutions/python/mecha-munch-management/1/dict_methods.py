"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    temp = dict.fromkeys(items_to_add, 0)

    # Step 2: count how many times each item appears
    for item in items_to_add:
        temp[item] += 1

    # Step 3: update the current cart with those counts
    for item, count in temp.items():
        current_cart[item] = current_cart.get(item, 0) + count

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for recipe, new_ingredients in recipe_updates:
        # Replace the old recipe with the new one
        ideas[recipe] = new_ingredients
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}

    # combine cart quantities with aisle info + refrigeration
    for item, quantity in cart.items():
        aisle, refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]

    # sort keys in reverse alphabetical order and build new dict
    sorted_fulfillment_cart = {
        item: fulfillment_cart[item] for item in sorted(fulfillment_cart.keys(), reverse=True)
    }

    return sorted_fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, details in fulfillment_cart.items():
        ordered_qty = details[0]  # how many the customer ordered
        stock_qty, aisle, refrigeration = store_inventory[item]

        # Subtract ordered from stock
        new_qty = stock_qty - ordered_qty

        # If stock hits 0 → replace with "Out of Stock"
        if new_qty <= 0:
            store_inventory[item][0] = "Out of Stock"
        else:
            store_inventory[item][0] = new_qty

    return store_inventory
