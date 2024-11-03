

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = ['A', 'B', 'C', 'D', 'E']
    total_price = 0
    item_counts = {sku: 0 for sku in valid_skus}

    if not isinstance(skus, str) or not all(char in valid_skus for char in skus):
        return -1

    for sku in skus:
        item_counts[sku] += 1

    total_price -= (item_counts['A'] // 3) * 20
    total_price -= (item_counts['B'] // 2) * 15
    free_Bs = item_counts['E'] // 2
    total_price -= min(free_Bs, item_counts['B']) * prices['B']
    
    return total_price

def get_price(sku):
    if(sku == 'A'):
        return 50
    elif(sku == 'B'):
        return 30
    elif(sku == 'C'):
        return 20
    elif(sku == 'D'):
        return 15
    elif(sku == 'E'):
        return 40

