

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = ['A', 'B', 'C', 'D', 'E']
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    item_counts = {sku: 0 for sku in valid_skus}
    total_price = 0

    if not isinstance(skus, str) or not all(char in valid_skus for char in skus):
        return -1

    for sku in skus:
        item_counts[sku] += 1
        total_price += prices[sku]

    total_price -= (item_counts['A'] // 3) * 20
    total_price -= (item_counts['B'] // 2) * 15
    free_Bs = item_counts['E'] // 2
    total_price -= min(free_Bs, item_counts['B']) * prices['B']

    return total_price

def get_price(sku):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    return prices.get(sku, 0)

