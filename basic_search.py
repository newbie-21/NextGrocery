from load_data import items


# Simple search function
def search_products(query, items):
    results = []
    for transaction in items:
        for item in transaction:
            if query.lower() in item.lower():
                results.append(item)
    return list(set(results))
