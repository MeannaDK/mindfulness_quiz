from flask import Flask

app = Flask(__name__)

# Define your routes
@app.route("/")
def home():
    return "Welcome to Your Mindfulness Snapshot Quiz!"

# Replace this with your quiz logic
questions = [
    "How often do you feel overwhelmed or stuck?",
    "How consistent are you with practicing mindfulness or self-care?"
]
answers = ["A", "B", "C", "D"]

score = 0

for i, question in enumerate(questions):
    print("\n" + question)
    answer = answers[i]  # Predefined answers
    print(f"Your answer: {answer}")
    if answer == "A":
        score += 1

print("\nYour Results Are In...")
if score <= 1:
    print("You are at the STARTING LINE. Small steps will make a big difference.")
else:
    print("You are EXPLORING NEW POSSIBILITIES. Keep going!")

# Port binding for Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
