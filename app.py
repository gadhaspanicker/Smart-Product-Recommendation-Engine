from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("products_dataset.csv")


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_products(product_name, top_n=5):

    # If product exists
    if product_name in df["Product_Name"].values:

        # Get Brand of entered product
        brand = df[df["Product_Name"] == product_name]["Brand"].values[0]

        message = ""  # No message if found

        # Recommend ONLY SAME BRAND products
        recommendations = (
            df[(df["Brand"] == brand) & (df["Product_Name"] != product_name)]
            .sort_values(by="Rating", ascending=False)
            .head(top_n)["Product_Name"]
            .tolist()
        )

        # If brand has less than top_n products
        if len(recommendations) == 0:
            recommendations = ["No other products available in this brand"]

    # If product not found (Cold Start)
    else:
        message = "Product not found. Showing popular products instead."

        recommendations = (
            df.sort_values(by="Rating", ascending=False)
            .head(top_n)["Product_Name"]
            .tolist()
        )

    return recommendations, message


# -----------------------------
# Flask Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    product_name = request.form["product_name"]

    recommendations, message = recommend_products(product_name)

    return render_template(
        "result.html",
        product_name=product_name,
        recommendations=recommendations,
        message=message
    )


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
