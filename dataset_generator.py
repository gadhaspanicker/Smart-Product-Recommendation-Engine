import pandas as pd
import random

# -----------------------------
# Product Dictionary (Category + Brand)
# -----------------------------
products_dict = {

    # ---------------- Electronics ----------------
    "Electronics": {
        "Samsung": [
            "Samsung Galaxy S23",
            "Samsung Galaxy S24",
            "Samsung Galaxy A54",
            "Samsung Galaxy Z Fold",
            "Samsung Galaxy M14",
            "Samsung Galaxy Note 20"
        ],

        "Apple": [
            "iPhone 15",
            "iPhone 14",
            "MacBook Air",
            "iPad Pro",
            "Apple Watch Series 9",
            "AirPods Pro"
        ],

        "Google": [
            "Google Pixel 8",
            "Google Pixel 7",
            "Google Pixel 6a",
            "Google Nest Hub",
            "Google Chromecast",
            "Google Pixel Tablet"
        ],

        "OnePlus": [
            "OnePlus 11",
            "OnePlus Nord CE",
            "OnePlus 10 Pro",
            "OnePlus Nord 3",
            "OnePlus Buds",
            "OnePlus Watch"
        ]
    },

    # ---------------- Books ----------------
    "Books": {
        "Penguin": [
            "1984",
            "The Great Gatsby",
            "To Kill a Mockingbird",
            "Pride and Prejudice",
            "The Alchemist",
            "The Book Thief"
        ],

        "Bloomsbury": [
            "Harry Potter",
            "The Hobbit",
            "Fantastic Beasts",
            "The Lord of the Rings",
            "Percy Jackson",
            "The Chronicles of Narnia"
        ]
    },

    # ---------------- Games ----------------
    "Games": {
        "EA Sports": [
            "FIFA 24",
            "NBA 2K24",
            "UFC 5",
            "Madden NFL 24",
            "F1 23",
            "NHL 24"
        ],

        "Mojang": [
            "Minecraft",
            "Minecraft Dungeons",
            "Minecraft Legends",
            "Minecraft Story Mode",
            "Minecraft Education Edition",
            "Minecraft Pocket Edition"
        ],

        "Activision": [
            "Call of Duty",
            "Call of Duty Warzone",
            "Call of Duty Modern Warfare",
            "Call of Duty Black Ops",
            "Crash Bandicoot",
            "Tony Hawk Pro Skater"
        ]
    },

    # ---------------- Sports ----------------
    "Sports": {
        "Nike": [
            "Nike Air Max",
            "Nike Running Shoes",
            "Nike Revolution 6",
            "Nike Zoom Pegasus",
            "Nike Football Boots",
            "Nike Sports Jacket"
        ],

        "Adidas": [
            "Adidas Ultraboost",
            "Adidas Superstar",
            "Adidas Running Shoes",
            "Adidas Football Jersey",
            "Adidas Predator Boots",
            "Adidas Training Shorts"
        ],

        "Reebok": [
            "Reebok Classic",
            "Reebok Nano X3",
            "Reebok Running Shoes",
            "Reebok CrossFit Trainer",
            "Reebok Sports T-Shirt",
            "Reebok Gym Bag"
        ],

        "Wilson": [
            "Wilson Tennis Racket",
            "Wilson Basketball",
            "Wilson Football",
            "Wilson Badminton Racket",
            "Wilson Sports Gloves",
            "Wilson Tennis Balls Pack"
        ]
    },

    # ---------------- Beauty ----------------
    "Beauty": {
        "Nivea": [
            "Nivea Moisturizer",
            "Nivea Body Lotion",
            "Nivea Face Wash",
            "Nivea Sunscreen SPF50",
            "Nivea Lip Balm",
            "Nivea Men Shaving Gel"
        ],

        "Maybelline": [
            "Maybelline Mascara",
            "Maybelline Lipstick",
            "Maybelline Foundation",
            "Maybelline Eyeliner",
            "Maybelline Compact Powder",
            "Maybelline Blush"
        ],

        "Clinique": [
            "Clinique Serum",
            "Clinique Face Cream",
            "Clinique Moisture Surge",
            "Clinique Eye Cream",
            "Clinique Cleanser",
            "Clinique Toner"
        ],

        "Dove": [
            "Dove Shampoo",
            "Dove Conditioner",
            "Dove Body Wash",
            "Dove Beauty Bar Soap",
            "Dove Hair Mask",
            "Dove Deodorant Spray"
        ]
    },

    # ---------------- Movies ----------------
    "Movies": {
        "Marvel": [
            "Avengers BluRay",
            "Iron Man DVD",
            "Spider-Man No Way Home BluRay",
            "Captain America Civil War DVD",
            "Black Panther BluRay",
            "Doctor Strange DVD"
        ],

        "DC": [
            "Joker DVD",
            "Batman Begins BluRay",
            "The Dark Knight DVD",
            "Justice League BluRay",
            "Wonder Woman DVD",
            "Aquaman BluRay"
        ],

        "Disney": [
            "Frozen II DVD",
            "The Lion King BluRay",
            "Moana DVD",
            "Toy Story BluRay",
            "Aladdin DVD",
            "Coco BluRay"
        ]
    }
}

# -----------------------------
# Generate Dataset
# -----------------------------
data = []

for category, brands in products_dict.items():
    for brand, products in brands.items():
        for product in products:
            data.append({
                "Product_Name": product,
                "Category": category,
                "Brand": brand,
                "Price": round(random.uniform(100, 1500), 2),
                "Rating": round(random.uniform(3.5, 5.0), 1)
            })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save Dataset
df.to_csv("products_dataset.csv", index=False)

print("✅ Dataset created successfully: products_dataset.csv")
print(df.head())
