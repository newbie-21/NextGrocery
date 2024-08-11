import pandas as pd
from itertools import combinations
from collections import defaultdict
from load_data import items

# Flatten the items into a single list for vectorization
flat_items = [item for sublist in items for item in sublist]

# Create a co-occurrence matrix
product_co_occurrence = defaultdict(int)
for sublist in items:
    for combination in combinations(sublist, 2):
        product_co_occurrence[tuple(sorted(combination))] += 1

# Convert to DataFrame
co_occurrence_df = pd.DataFrame(list(product_co_occurrence.items()), columns=["Pair", "Frequency"])

# Sort to find the most common co-occurring products
co_occurrence_df = co_occurrence_df.sort_values(by="Frequency", ascending=False)


# Function to calculate confidence
def calculate_confidence(item1, item2, df):
    item1_transactions = df[df[item1] > 0].shape[0]
    both_transactions = df[(df[item1] > 0) & (df[item2] > 0)].shape[0]
    return both_transactions / item1_transactions


# Function to get recommendations based on a product
def get_recommendations(product_name, co_occurrence_df, df, confidence_threshold=0.1):
    # Find pairs that include the product name
    relevant_pairs = co_occurrence_df[co_occurrence_df["Pair"].apply(lambda x: product_name in x)]

    # Extract the other product in the pair and calculate confidence
    recommended_products = []
    for pair in relevant_pairs["Pair"]:
        other_product = pair[0] if pair[1] == product_name else pair[1]
        confidence = calculate_confidence(product_name, other_product, df)
        if confidence > confidence_threshold:
            recommended_products.append(other_product)

    # Return the top recommendations
    return recommended_products[:3]
