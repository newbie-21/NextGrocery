from unique_product_mapping import product_to_category, goal_format


def get_recommendations(selected_item, goal_format):
    # Find the class/category of the selected item
    selected_class_dict = product_to_category.get(selected_item, None)

    if selected_class_dict is None:
        print("Product not found.")
        return None, []

    selected_class = selected_class_dict.get('category', None)
    if not selected_class:
        print("Category not found for the selected product.")
        return None, []

    print(f"Selected Category: {selected_class}")

    # Filter all products in the same class/category
    same_class_products = goal_format.get(selected_class, [])

    # Remove the selected item itself from the list of recommendations (optional)
    if selected_item in same_class_products:
        same_class_products.remove(selected_item)

    # Prepare a list of recommendations with their image paths
    recommendations_with_images = [
        {"product": product, "image": product_to_category.get(product, {}).get('image', 'No image available')}
        for product in same_class_products
    ]

    return selected_class, recommendations_with_images


def cat_recc(selected_item):
    category, recommendations = get_recommendations(selected_item, goal_format)
    print(f"Selected Item: {selected_item}")
    print("Recommended:")
    for recommendation in recommendations:
        print(f"Product: {recommendation['product']}, Image Path: {recommendation['image']}")
