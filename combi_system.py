from cooccurance import get_recommendations, co_occurrence_df
from jaccard_similarity import collaborative_recommendations, product_item_matrix


def combi_system(product):
    # Test Cosine Similarity Based Recommendations with Confidence
    cosine_recommendations = get_recommendations(product, co_occurrence_df, product_item_matrix)

    # Test Item-Based Collaborative Filtering with Jacquard Similarity
    jacquard_recommendations = collaborative_recommendations(product)

    # Combine recommendations
    common_recommendations = set(cosine_recommendations) | set(jacquard_recommendations)

    return list(common_recommendations)  # Return the combined recommendations
