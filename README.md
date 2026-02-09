# Smart Product Recommendation Engine

This project is a **Smart Product Recommendation System** that suggests relevant products based on user input using a **Hybrid Recommendation Approach**.

It combines multiple techniques to improve recommendation accuracy and diversity.

---

## 🚀 Features
- Recommends top-N similar products instantly
- Hybrid model for better accuracy
- Flask-based web interface for real-time search
- Evaluation using Precision@K and Recall@K

---

## 🛠️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- TruncatedSVD  
- Cosine Similarity  
- Flask  
- HTML/CSS  

---

## 📊 Recommendation Techniques

This system uses a **Hybrid Recommendation Engine** combining:

### 1. Collaborative Filtering (SVD)
- Matrix factorization using **TruncatedSVD**
- Learns hidden relationships between products

### 2. Similarity-Based Filtering
- Uses **cosine similarity** for item-to-item recommendations

### 3. Association / Co-occurrence Analysis
- Recommends products frequently viewed or purchased together

---

## ⭐ Hybrid Model Advantage
By combining SVD, similarity scores, and co-occurrence patterns, the system provides:

- More accurate recommendations  
- Better product diversity  
- Improved relevance compared to single-method models  

---

## 📈 Model Evaluation
The recommendation performance is measured using:

- **Precision@K**
- **Recall@K**

## ❄️ Cold Start Handling

To address the cold-start problem (new products with limited interaction data), the system applies:

- Category-based fallback recommendations  
- Popular product suggestions when similarity scores are unavailable  

This ensures meaningful recommendations even for unseen items.

## 🔍 Recommendation Explainability

The system provides explainable recommendations by showing:

- Similarity score between products  
- Co-occurrence relationships (frequently bought/viewed together)  
- Reason for recommendation (same category/brand patterns)

This improves transparency and user trust.

---

## ▶️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Smart-Product-Recommendation-Engine.git
