

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = ['A', 'B', 'C']
    total_price = 0

    if not isinstance(skus, str) or not all(char in valid_skus for char in skus):
        return -1

    for sku in skus:
        total_price += get_price(sku)
    return total_price

def get_price(sku):
    if(sku == 'A'):
        return 50
    elif(sku == 'B'):
        return 30
    elif(sku == 'C'):
        return 20



