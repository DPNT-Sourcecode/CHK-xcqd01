# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 
        'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 
        'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17, 
        'Y': 20, 'Z': 21
    }
   
    item_counts = {sku: 0 for sku in valid_skus}
    total_price = 0

    if not is_valid_sku_input(skus, valid_skus):
        return -1

    for sku in skus:
        item_counts[sku] += 1
        total_price += prices[sku]

    total_price += apply_special_offer(item_counts, prices)
    total_price += calculate_F_price(item_counts, prices)
    total_price -= item_counts['F'] * prices['F']
    total_price -= apply_free_item_offer(item_counts, prices)
    total_price -= apply_basic_discounts(item_counts)

    return total_price

def is_valid_sku_input(skus, valid_skus):
    return isinstance(skus, str) and all(char in valid_skus for char in skus)

def calculate_F_price(item_counts, prices):
    f_count = item_counts['F']
    group_of_3 = f_count // 3
    remainder = f_count % 3

    return group_of_3 * 20 + remainder * prices['F']

def apply_special_offer(item_counts, prices):
    stxyz_count = sum(item_counts[item] for item in ['S', 'T', 'X', 'Y', 'Z'])
    sets_of_three = stxyz_count // 3
    total_price = sets_of_three * 45

    items_used_in_sets = sets_of_three * 3
    for item in ['S', 'T', 'X', 'Y', 'Z']:
        while items_used_in_sets > 0 and item_counts[item] > 0:
            total_price -= prices[item]
            item_counts[item] -= 1
            items_used_in_sets -= 1

    return total_price

def apply_free_item_offer(item_counts, prices):
    total_discount = 0
    free_items = {
        'B': item_counts['E'] // 2,
        'Q': item_counts['R'] // 3,
        'M': item_counts['N'] // 3
    }

    for item, free_count in free_items.items():
        if free_count > 0:
            total_discount += min(free_count, item_counts[item]) * prices[item]
            item_counts[item] -= min(free_count, item_counts[item])

    return total_discount

def apply_basic_discounts(item_counts):
    total_discount = 0
    discounts = {
        'A': (5, 50),
        'B': (2, 15),
        'H': (10, 20),
        'K': (2, 20),
        'P': (5, 50),
        'Q': (3, 10),
        'U': (4, 40),
        'V': (3, 20)
    }

    for item, (quantity, discount) in discounts.items():
        total_discount += (item_counts[item] // quantity) * discount

    total_discount += (item_counts['H'] % 10 // 5) * 5
    total_discount += (item_counts['A'] % 5 // 3) * 20
    total_discount += (item_counts['V'] % 3 // 2) * 10

    return total_discount
