from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template for the quiz
quiz_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Mindfulness Snapshot Quiz</title>
</head>
<body>
    <h1>Welcome to Your Mindfulness Snapshot Quiz!</h1>
<form method="POST">
  <p>1. How often do you feel overwhelmed or stuck?</p>
  <label><input type="radio" name="q1" value="1"> A) Almost always</label><br>
  <label><input type="radio" name="q1" value="2"> B) Often</label><br>
  <label><input type="radio" name="q1" value="3"> C) Sometimes</label><br>
  <label><input type="radio" name="q1" value="4"> D) Rarely</label><br><br>

  <p>2. How consistent are you with practicing mindfulness or self-care?</p>
  <label><input type="radio" name="q2" value="1"> A) Not consistent at all</label><br>
  <label><input type="radio" name="q2" value="2"> B) Rarely</label><br>
  <label><input type="radio" name="q2" value="3"> C) Occasionally</label><br>
  <label><input type="radio" name="q2" value="4"> D) Very consistent</label><br><br>

  <p>3. How important is it to you to make a lifestyle change?</p>
  <label><input type="radio" name="q3" value="1"> A) Not important</label><br>
  <label><input type="radio" name="q3" value="2"> B) Somewhat important</label><br>
  <label><input type="radio" name="q3" value="3"> C) Very important</label><br>
  <label><input type="radio" name="q3" value="4"> D) Extremely important</label><br><br>

  <p>4. How prepared do you feel to take actionable steps toward your goals?</p>
  <label><input type="radio" name="q4" value="1"> A) Never</label><br>
  <label><input type="radio" name="q4" value="2"> B) Slightly prepared</label><br>
  <label><input type="radio" name="q4" value="3"> C) Moderately prepared</label><br>
  <label><input type="radio" name="q4" value="4"> D) Fully prepared</label><br><br>

  <p>5. How often do you celebrate your wins, big or small?</p>
  <label><input type="radio" name="q5" value="1"> A) Never</label><br>
  <label><input type="radio" name="q5" value="2"> B) Rarely</label><br>
  <label><input type="radio" name="q5" value="3"> C) Occasionally</label><br>
  <label><input type="radio" name="q5" value="4"> D) Regularly</label><br><br>

  <p>6. How connected do you feel to your core values?</p>
  <label><input type="radio" name="q6" value="1"> A) Not connected</label><br>
  <label><input type="radio" name="q6" value="2"> B) Slightly connected</label><br>
  <label><input type="radio" name="q6" value="3"> C) Moderately connected</label><br>
  <label><input type="radio" name="q6" value="4"> D) Deeply connected</label><br><br>

  <p>7. How often do you take time to pause and reflect on your progress?</p>
  <label><input type="radio" name="q7" value="1"> A) Never</label><br>
  <label><input type="radio" name="q7" value="2"> B) Rarely</label><br>
  <label><input type="radio" name="q7" value="3"> C) Occasionally</label><br>
  <label><input type="radio" name="q7" value="4"> D) Regularly</label><br><br>

  <input type="submit" value="Submit">
</form>

    {% if result %}
    <h2>Your Results Are In...</h2>
    <p>{{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Calculate the score
        score = sum(int(request.form.get(f"q{i}", 0)) for i in range(1, 8))

        # Display results based on score
        if score <= 6:
            result = "You are at the STARTING LINE. Small steps will make a big difference."
        elif score <= 9:
            result = "You are EXPLORING NEW POSSIBILITIES. You're curious and ready to grow."
        elif score <= 12:
            result = "You are BUILDING THE FOUNDATION. Consistency is key to lasting change."
        else:
            result = "You are THRIVING IN BALANCE. Keep nurturing your journey to deeper peace."

        return render_template_string(quiz_template, result=result)
    
    return render_template_string(quiz_template, result=None)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned PORT
    app.run(host="0.0.0.0", port=port, debug=False)
