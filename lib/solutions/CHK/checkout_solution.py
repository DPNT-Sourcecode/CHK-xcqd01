

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
    
    if not is_valid_sku_input(skus, valid_skus):
        return -1

    item_counts = initialize_item_counts(valid_skus)
    total_price = calculate_initial_price(skus, item_counts, prices)

    total_price += apply_special_offer(item_counts, prices)
    total_price -= apply_free_item_offers(item_counts, prices)
    total_price -= apply_discounted_items(item_counts, prices)

    return total_price

def is_valid_sku_input(skus, valid_skus):
    return isinstance(skus, str) and all(char in valid_skus for char in skus)

def initialize_item_counts(valid_skus):
    return {sku: 0 for sku in valid_skus}

def calculate_initial_price(skus, item_counts, prices):
    total_price = 0
    for sku in skus:
        item_counts[sku] += 1
        total_price += prices[sku]
    return total_price

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

def apply_free_item_offers(item_counts, prices):
    total_discount = 0
    
    free_Bs = item_counts['E'] // 2
    if free_Bs > 0:
        discount = min(free_Bs, item_counts['B']) * prices['B']
        total_discount -= discount
        item_counts['B'] -= min(free_Bs, item_counts['B'])

    free_Qs = item_counts['R'] // 3
    if free_Qs > 0:
        discount = min(free_Qs, item_counts['Q']) * prices['Q']
        total_discount -= discount
        item_counts['Q'] -= min(free_Qs, item_counts['Q'])

    return total_discount

def apply_discounted_items(item_counts, prices):
    total_discount = 0

    total_discount -= item_counts['F'] * prices['F']
    total_discount += calculate_F_price(item_counts, prices)

    total_discount -= (item_counts['A'] // 5) * 50
    total_discount -= (item_counts['A'] % 5 // 3) * 20
    total_discount -= (item_counts['B'] // 2) * 15
    total_discount -= (item_counts['K'] // 2) * 20
    total_discount -= (item_counts['P'] // 5) * 50
    total_discount -= (item_counts['Q'] // 3) * 10

    h_count = item_counts['H']
    total_discount -= (h_count // 10) * 20
    h_count %= 10
    total_discount -= (h_count // 5) * 5

    free_Ms = item_counts['N'] // 3
    if free_Ms > 0:
        discount = min(free_Ms, item_counts['M']) * prices['M']
        total_discount -= discount
        item_counts['M'] -= min(free_Ms, item_counts['M'])

    total_discount -= (item_counts['U'] // 4) * prices['U']

    v_count = item_counts['V']
    total_discount -= (v_count // 3) * 20
    v_count %= 3
    total_discount -= (v_count // 2) * 10

    return total_discount

def calculate_F_price(item_counts, prices):
    f_count = item_counts['F']
    group_of_3 = f_count // 3
    remainder = f_count % 3
    
    offer_price = group_of_3 * 20
    remainder_price = remainder * prices['F']
    
    return offer_price + remainder_price


