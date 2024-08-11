from load_data import items

# Example of populating unique_items
unique_items = set(item for sublist in items for item in sublist)

# Flatten the list of lists
flattened_list = [item for sublist in items for item in sublist]

# Get unique items by converting the list to a set
unique_items_set = set(flattened_list)

# Optional: Convert the set back to a list if you need it in list form
unique_items_list = list(unique_items_set)

# Define the categories and products mapping
product_to_category = {
    'salmon': {'category': 'seafood', 'image': 'resized_images/salmon.png'},
    'tea': {'category': 'beverages', 'image': 'resized_images/tea.png'},
    'cottage cheese': {'category': 'dairy', 'image': 'resized_images/cottage cheese.png'},
    'nuggets': {'category': 'meat', 'image': 'resized_images/nuggets.png'},
    'gums': {'category': 'snacks', 'image': 'resized_images/gums.png'},
    'shampoo': {'category': 'personal care', 'image': 'resized_images/shampoo.png'},
    'water spray': {'category': 'personal care', 'image': 'resized_images/water spray.png'},
    'ketchup': {'category': 'condiments', 'image': 'resized_images/ketchup.png'},
    'protein bar': {'category': 'snacks', 'image': 'resized_images/protein bar.png'},
    'butter': {'category': 'dairy', 'image': 'resized_images/butter.png'},
    'green grapes': {'category': 'fruits', 'image': 'resized_images/green grapes.png'},
    'pickles': {'category': 'condiments', 'image': 'resized_images/pickles.png'},
    'meatballs': {'category': 'meat', 'image': 'resized_images/meatballs.png'},
    'toothpaste': {'category': 'personal care', 'image': 'resized_images/toothpaste.png'},
    'body spray': {'category': 'personal care', 'image': 'resized_images/body spray.png'},
    'shrimp': {'category': 'seafood', 'image': 'resized_images/shrimp.png'},
    'oil': {'category': 'cooking essentials', 'image': 'resized_images/oil.png'},
    'flax seed': {'category': 'cooking essentials', 'image': 'resized_images/flax seed.png'},
    'chutney': {'category': 'condiments', 'image': 'resized_images/chutney.png'},
    'asparagus': {'category': 'vegetables', 'image': 'resized_images/asparagus.png'},
    'avocado': {'category': 'fruits', 'image': 'resized_images/avocado.png'},
    'light mayo': {'category': 'condiments', 'image': 'resized_images/light mayo.png'},
    'salad': {'category': 'vegetables', 'image': 'resized_images/salad.png'},
    'eggplant': {'category': 'vegetables', 'image': 'resized_images/eggplant.png'},
    'cooking oil': {'category': 'cooking essentials', 'image': 'resized_images/cooking oil.png'},
    'salt': {'category': 'cooking essentials', 'image': 'resized_images/salt.png'},
    'extra dark chocolate': {'category': 'snacks', 'image': 'resized_images/extra dark chocolate.png'},
    'magazines': {'category': 'miscellaneous', 'image': 'resized_images/magazines.png'},
    'antioxydant juice': {'category': 'beverages', 'image': 'resized_images/antioxydant juice.png'},
    'apple juice': {'category': 'beverages', 'image': 'resized_images/apple juice.png'},
    'honey': {'category': 'cooking essentials', 'image': 'resized_images/honey.png'},
    'chili': {'category': 'vegetables', 'image': 'resized_images/chili.png'},
    'babies food': {'category': 'baby care', 'image': 'resized_images/babies food.png'},
    'cider': {'category': 'beverages', 'image': 'resized_images/cider.png'},
    'vegetables mix': {'category': 'vegetables', 'image': 'resized_images/vegetables mix.png'},
    'redbull': {'category': 'beverages', 'image': 'resized_images/redbull.png'},
    'cheese cake': {'category': 'desserts', 'image': 'resized_images/cheese cake.png'},
    'herb & pepper': {'category': 'spices', 'image': 'resized_images/herb & pepper.png'},
    'cereals': {'category': 'breakfast', 'image': 'resized_images/cereals.png'},
    'corn': {'category': 'vegetables', 'image': 'resized_images/corn.png'},
    'mayonnaise': {'category': 'condiments', 'image': 'resized_images/mayonnaise.png'},
    'carrots': {'category': 'vegetables', 'image': 'resized_images/carrots.png'},
    'napkins': {'category': 'household', 'image': 'resized_images/napkins.png'},
    'chocolate': {'category': 'snacks', 'image': 'resized_images/chocolate.png'},
    'soup': {'category': 'canned goods', 'image': 'resized_images/soup.png'},
    'yams': {'category': 'vegetables', 'image': 'resized_images/yams.png'},
    'cake': {'category': 'desserts', 'image': 'resized_images/cake.png'},
    'mint': {'category': 'spices', 'image': 'resized_images/mint.png'},
    'spaghetti': {'category': 'pasta', 'image': 'resized_images/spaghetti.png'},
    'pasta': {'category': 'pasta', 'image': 'resized_images/pasta.png'},
    'fromage blanc': {'category': 'dairy', 'image': 'resized_images/fromage blanc.png'},
    'fresh bread': {'category': 'bakery', 'image': 'resized_images/fresh bread.png'},
    'cream': {'category': 'dairy', 'image': 'resized_images/cream.png'},
    'ground beef': {'category': 'meat', 'image': 'resized_images/ground beef.png'},
    'eggs': {'category': 'breakfast', 'image': 'resized_images/eggs.png'},
    'chicken': {'category': 'meat', 'image': 'resized_images/chicken.png'},
    'hand protein bar': {'category': 'snacks', 'image': 'resized_images/hand protein bar.png'},
    'energy drink': {'category': 'beverages', 'image': 'resized_images/energy drink.png'},
    'oatmeal': {'category': 'breakfast', 'image': 'resized_images/oatmeal.png'},
    'cookies': {'category': 'snacks', 'image': 'resized_images/cookies.png'},
    'muffins': {'category': 'bakery', 'image': 'resized_images/muffins.png'},
    'frozen vegetables': {'category': 'frozen foods', 'image': 'resized_images/frozen vegetables.png'},
    'almonds': {'category': 'nuts', 'image': 'resized_images/almonds.png'},
    'beef': {'category': 'meat', 'image': 'resized_images/beef.png'},
    'bug spray': {'category': 'household', 'image': 'resized_images/bug spray.png'},
    'tomato sauce': {'category': 'condiments', 'image': 'resized_images/tomato sauce.png'},
    'spinach': {'category': 'vegetables', 'image': 'resized_images/spinach.png'},
    'sparkling water': {'category': 'beverages', 'image': 'resized_images/sparkling water.png'},
    'cauliflower': {'category': 'vegetables', 'image': 'resized_images/cauliflower.png'},
    'whole wheat rice': {'category': 'grains', 'image': 'resized_images/whole wheat rice.png'},
    'chocolate bread': {'category': 'bakery', 'image': 'resized_images/chocolate bread.png'},
    'burger sauce': {'category': 'condiments', 'image': 'resized_images/burger sauce.png'},
    'shallot': {'category': 'vegetables', 'image': 'resized_images/shallot.png'},
    'whole weat flour': {'category': 'cooking essentials', 'image': 'resized_images/whole weat flour.png'},
    'white wine': {'category': 'beverages', 'image': 'resized_images/white wine.png'},
    'barbecue sauce': {'category': 'condiments', 'image': 'resized_images/barbecue sauce.png'},
    'fresh tuna': {'category': 'seafood', 'image': 'resized_images/fresh tuna.png'},
    'blueberries': {'category': 'fruits', 'image': 'resized_images/blueberries.png'},
    'energy bar': {'category': 'snacks', 'image': 'resized_images/energy bar.png'},
    'sandwich': {'category': 'snacks', 'image': 'resized_images/sandwich.png'},
    'light cream': {'category': 'dairy', 'image': 'resized_images/light cream.png'},
    'olive oil': {'category': 'cooking essentials', 'image': 'resized_images/olive oil.png'},
    'clothes accessories': {'category': 'miscellaneous', 'image': 'resized_images/clothes accessories.png'},
    'mushroom cream sauce': {'category': 'sauces', 'image': 'resized_images/mushroom cream sauce.png'},
    'escalope': {'category': 'meat', 'image': 'resized_images/escalope.png'},
    'pancakes': {'category': 'breakfast', 'image': 'resized_images/pancakes.png'},
    'black tea': {'category': 'beverages', 'image': 'resized_images/black tea.png'},
    'grated cheese': {'category': 'dairy', 'image': 'resized_images/grated cheese.png'},
    'whole wheat pasta': {'category': 'pasta', 'image': 'resized_images/whole wheat pasta.png'},
    'mineral water': {'category': 'beverages', 'image': 'resized_images/mineral water.png'},
    'tomato juice': {'category': 'beverages', 'image': 'resized_images/tomato juice.png'},
    'candy bars': {'category': 'snacks', 'image': 'resized_images/candy bars.png'},
    'pepper': {'category': 'spices', 'image': 'resized_images/pepper.png'},
    'pet food': {'category': 'pet care', 'image': 'resized_images/pet food.png'},
    'french fries': {'category': 'snacks', 'image': 'resized_images/french fries.png'},
    'green beans': {'category': 'vegetables', 'image': 'resized_images/green beans.png'},
    'strawberries': {'category': 'fruits', 'image': 'resized_images/strawberries.png'},
    'melons': {'category': 'fruits', 'image': 'resized_images/melons.png'},
    'zucchini': {'category': 'vegetables', 'image': 'resized_images/zucchini.png'},
    'brownies': {'category': 'desserts', 'image': 'resized_images/brownies.png'},
    'milk': {'category': 'dairy', 'image': 'resized_images/milk.png'},
    'bramble': {'category': 'fruits', 'image': 'resized_images/bramble.png'},
    'low fat yogurt': {'category': 'dairy', 'image': 'resized_images/low fat yogurt.png'},
    'yogurt cake': {'category': 'desserts', 'image': 'resized_images/yogurt cake.png'},
    'frozen smoothie': {'category': 'frozen foods', 'image': 'resized_images/frozen smoothie.png'},
    'mint green tea': {'category': 'beverages', 'image': 'resized_images/mint green tea.png'},
    'tomatoes': {'category': 'vegetables', 'image': 'resized_images/tomatoes.png'},
    'strong cheese': {'category': 'dairy', 'image': 'resized_images/strong cheese.png'},
    'nonfat milk': {'category': 'dairy', 'image': 'resized_images/nonfat milk.png'},
    'green tea': {'category': 'beverages', 'image': 'resized_images/green tea.png'},
    'rice': {'category': 'grains', 'image': 'resized_images/rice.png'},
    'hot dogs': {'category': 'meat', 'image': 'resized_images/hot dogs.png'},
    'soda': {'category': 'beverages', 'image': 'resized_images/soda.png'},
    'mashed potato': {'category': 'vegetables', 'image': 'resized_images/mashed potato.png'},
    'turkey': {'category': 'meat', 'image': 'resized_images/turkey.png'},
    'french wine': {'category': 'beverages', 'image': 'resized_images/french wine.png'},
    'parmesan cheese': {'category': 'dairy', 'image': 'resized_images/parmesan cheese.png'},
    'gluten free bar': {'category': 'snacks', 'image': 'resized_images/gluten free bar.png'},
    'burgers': {'category': 'meat', 'image': 'resized_images/burgers.png'}
}




# Initialize the goal format dictionary
goal_format = {
    "beverages": [],
    "dairy": [],
    "snacks": [],
    "seafood": [],
    "personal care": [],
    "vegetables": [],
    "fruits": [],
    "condiments": [],
    "cooking essentials": [],
    "meat": [],
    "baby care": [],
    "frozen foods": [],
    "nuts": [],
    "household": [],
    "breakfast": [],
    "bakery": [],
    "spices": [],
    "canned goods": [],
    "desserts": [],
    "pasta": [],
    "grains": [],
    "pet care": [],
    "sauces": [],
    "miscellaneous": [],
}

# Populate the goal_format dictionary with products from the unique_items_list
for product in unique_items_list:
    category_dict = product_to_category.get(product)  # Get the category dictionary
    if category_dict:
        category_name = category_dict['category']  # Extract the category name (string)
        goal_format[category_name].append(product)  # Use category name as key

# Optional: Remove duplicates (if any) in the product lists
for category in goal_format:
    goal_format[category] = list(set(goal_format[category]))