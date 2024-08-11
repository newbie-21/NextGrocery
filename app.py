import streamlit as st
from PIL import Image
from io import BytesIO
from unique_product_mapping import product_to_category, goal_format, unique_items_list
from cooccurance import get_recommendations, co_occurrence_df
from jaccard_similarity import collaborative_recommendations, product_item_matrix

# Helper function to load images
def load_image(image_path):
    try:
        with open(image_path, "rb") as f:
            img = Image.open(BytesIO(f.read()))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# Function to get items bought together
def get_items_bought_together(product_name):
    cosine_recommendations = get_recommendations(product_name, co_occurrence_df, product_item_matrix)
    jacquard_recommendations = collaborative_recommendations(product_name)
    common_recommendations = set(cosine_recommendations) | set(jacquard_recommendations)
    return list(common_recommendations)

# Streamlit UI
def main():
    st.title("Groceries Recommender")

    # Product list for selection
    product_list = unique_items_list

    # Select a product
    selected_product = st.selectbox("Type or select a product", options=product_list)
    search_button = st.button("Commence Search")

    if search_button:
        if selected_product:
            # Display the basic search results
            st.write("Basic Search Results:")
            st.image(load_image(product_to_category[selected_product]['image']), caption=selected_product.capitalize())

            product_info = product_to_category[selected_product]

            # Display items bought together
            st.write("Items Bought Together:")
            items_bought_together = get_items_bought_together(selected_product)
            if items_bought_together:
                for i in range(0, len(items_bought_together), 4):
                    cols = st.columns(min(4, len(items_bought_together) - i))
                    for j, item in enumerate(items_bought_together[i:i + 4]):
                        cols[j].image(load_image(product_to_category[item]['image']), caption=item.capitalize())
            else:
                st.write("No items bought together recommendations found.")

            # Display category-based recommendations
            st.write(f"Products From {product_info['category'].capitalize()} Category:")
            category_items = goal_format.get(product_info['category'], [])
            if category_items:
                for i in range(0, len(category_items), 4):
                    cols = st.columns(min(4, len(category_items) - i))
                    for j, item in enumerate(category_items[i:i + 4]):
                        cols[j].image(load_image(product_to_category[item]['image']), caption=item.capitalize())
            else:
                st.write(f"No other products found in {product_info['category']} category.")
        else:
            st.write("No product selected.")

if __name__ == "__main__":
    main()
