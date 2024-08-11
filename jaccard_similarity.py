import pandas as pd
from sklearn.metrics import jaccard_score
import numpy as np
from load_data import items

# Example of populating unique_items
unique_items = set(item for sublist in items for item in sublist)

# Create a product-item matrix
unique_items_list = list(unique_items)
product_item_matrix = pd.DataFrame(0, index=range(len(items)), columns=unique_items_list)

# Populate the product-item matrix
for i, transaction in enumerate(items):
    for item in transaction:
        product_item_matrix.loc[i, item] += 1

# Convert the DataFrame to a binary matrix
product_item_matrix_binary = product_item_matrix.map(lambda x: 1 if x > 0 else 0)

# Calculate Jacquard similarity
similarity_matrix_jaccard = pd.DataFrame(np.nan, index=product_item_matrix.columns, columns=product_item_matrix.columns)

for i in range(len(similarity_matrix_jaccard.columns)):
    for j in range(len(similarity_matrix_jaccard.columns)):
        similarity_matrix_jaccard.iloc[i, j] = jaccard_score(
            product_item_matrix_binary.iloc[:, i],
            product_item_matrix_binary.iloc[:, j]
        )


# Function to get collaborative recommendations based on a product
def collaborative_recommendations(product_name, similarity_matrix=similarity_matrix_jaccard, threshold=0.01):
    if product_name not in unique_items_list:
        return f"Product '{product_name}' not found in the database."

    similar_products = similarity_matrix[product_name][similarity_matrix[product_name] > threshold].sort_values(ascending=False).index.tolist()
    return similar_products[:5]  # top 5 most similar products
