
from flask import Flask, request, jsonify
import pandas as pd

df_books = pd.read_excel('Books_With_Mood.xlsx')

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend_books():
    data = request.get_json()
    mood = data.get('mood', None)

    if mood:
        recommendations = df_books[df_books['Mood'].str.contains(mood, case=False, na=False)]

        if not recommendations.empty:
            books = recommendations[['Book-Title', 'Book-Author']].head(3).to_dict(orient='records')
            return jsonify(books)

    return jsonify({"message": "No recommendations found."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
