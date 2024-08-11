# main.py

from basic_search import search_products
from combi_system import combi_system
from category_based import cat_recc
from unique_product_mapping import product_to_category, goal_format
from load_data import items


def main():
    # Prompt user for input
    selected_item = input("Enter the name of the product: ").strip().lower()

    # Check if the product exists in the database
    if selected_item not in product_to_category:
        print(f"Product '{selected_item}' not found in the database.")
        return

    # Basic Search Results
    print("\nBasic Search Results:")
    search_results = search_products(selected_item, items)
    if search_results:
        print("Found the following matching items:")
        for result in search_results:
            print(f"- {result}")
    else:
        print("No matching items found.")

    print("\n" + "-"*50 + "\n")

    # Combined Recommendations
    print("Items Bought With It:")
    combi_system(selected_item)

    print("\n" + "-"*50 + "\n")

    # Category-Based Recommendations
    print("Category-Based Recommendations:")
    cat_recc(selected_item)


if __name__ == "__main__":
    main()
