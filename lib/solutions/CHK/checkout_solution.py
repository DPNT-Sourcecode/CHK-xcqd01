

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = ['A', 'B', 'C', 'D', 'E', 'F']
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    item_counts = {sku: 0 for sku in valid_skus}
    total_price = 0

    if not isinstance(skus, str) or not all(char in valid_skus for char in skus):
        return -1

    for sku in skus:
        item_counts[sku] += 1
        total_price += prices[sku]

    free_Bs = item_counts['E'] // 2
    free_Fs = item_counts['F'] // 2

    ## FF -> 20, - value of 1F, return 10
    # FFF -> 30, - value of 1 F, return 20
        # works correctly ^ 
    # FFFF -> 40, - value of 1 F, return 30 
        # returns 20 instead of 30 ^ 
    # FFFFF -> 50, - value of 1 F, return 40
    # FFFFFFF -> 60, - value of 2 F, return 50

    if free_Bs > 0:
        total_price -= min(free_Bs, item_counts['B']) * prices['B']
        item_counts['B'] -= min(free_Bs, item_counts['B']) 

    if free_Fs > 0 and item_counts['F'] > 2:
        total_price -= free_Fs * prices['F']
        item_counts['F'] -= free_Fs  # Adjust the count of 'F's

    total_price -= (item_counts['A'] // 5) * 50 
    total_price -= (item_counts['A'] % 5 // 3) * 20  
    total_price -= (item_counts['B'] // 2) * 15


    return total_price

def get_price(sku):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    return prices.get(sku, 0)