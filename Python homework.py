def cm_to_inches():
    try:
        cm = float(input("Enter size in cm: "))
        if cm <= 0:
            print("Size must be a positive number.")
        else:
            inches = cm / 2.54
            print(f"{cm} cm = {inches:.2f} inches")
    except ValueError:
        print("Invalid input! Please enter a number.")



brands = {
    "Teodor": ["formal", "business"],
    "Sinsay": ["casual", "sport"],
    "LC Waikiki": ["casual"],
    "Reserved": ["business", "casual"]
}

def recommend_brand(style):
    for brand, styles in brands.items():
        if style in styles:
            return brand
    return None



def generate_store_link(description):
    description = description.lower().replace(" ", "-")
    return f"https://store.example.com/{description}"
