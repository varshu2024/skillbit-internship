# skillbit internship

# 🧠 Python Quiz Game

A simple command-line **Quiz Game** built using Python that tests users with multiple-choice questions and gives a final score at the end.

## 🚀 Features

- 📝 Multiple-choice questions
- ✅ Instant feedback on correct/wrong answers
- 📊 Final score display
- 🔁 Option to replay the quiz

## 🛠️ Tech Stack

- Python 3.x

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-quiz-game.git
   cd python-quiz-game
   
Example Screenshot
mathematica
Copy
Edit
Question 1: What is the capital of France?
A. Paris
B. London
C. Berlin
D. Madrid



# 🔢 Python Calculator

A simple and interactive **command-line calculator** built using Python. This calculator supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## 📌 Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- ❌ Error handling (e.g., division by zero)
- 🔁 Continuous operation loop until user quits

## 🛠️ Tech Stack

- Python 3.x

## 📂 Project Structure

calculator.py # Main calculator logic
README.md # Project overview and instructions

bash
Copy
Edit

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/python-calculator.git
   cd python-calculator
Run the script

bash
Copy
Edit
python calculator.py
Follow the prompts to perform calculations.

Example:

sql
Copy
Edit
🔢 Basic Calculator
Choose operation: +, -, *, /

Enter operation (+ - * / or 'q' to quit): +
Enter first number: 5
Enter second number: 3



# 🎬 Movie Recommendation System

A simple **command-line movie recommendation system** built using Python. This project uses content-based filtering to recommend movies based on genre similarity with the user's favorite movie.

## 📌 Features

- 🧠 Content-based filtering using genre overlap
- 🎯 Personalized movie suggestions
- 🗂️ Easy-to-edit movie database (Python dictionary)
- 💬 Interactive CLI input

## 🛠️ Tech Stack

- Python 3.x (no external libraries required)

## 🚀 Getting Started

### 📂 Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender-python.git
cd movie-recommender-python
▶️ Run the Program
bash
Copy
Edit
python movie_recommender.py
🧠 How It Works
User inputs a movie they like.

The program finds that movie in its built-in database.

It compares genres and recommends the top 5 similar movies.

🎥 Sample Output
sql
Copy
Edit
🎥 Welcome to the Movie Recommender!
Here are some movies you can choose from:
• Inception
• Titanic
• Avengers: Endgame
• The Matrix
...

Enter the name of a movie you like: Inception

🎯 Based on your interest in 'Inception', you might like:
• The Matrix
• Avengers: Endgame
• Interstellar
• The Dark Knight
...
📌 Customization
You can easily add more movies in the movies list inside the movie_recommender.py file:

python
Copy
Edit
movies = [
    {"title": "Inception", "genre": ["Action", "Sci-Fi", "Thriller"]},
    {"title": "Titanic", "genre": ["Romance", "Drama"]},
    # Add your own here...
]
💡 Possible Improvements
Integrate TMDB or IMDb API for real-time data

Use TF-IDF + cosine similarity for descriptions

Add collaborative filtering based on ratings

Web version using Flask or Django
✅ Result: 8.0
