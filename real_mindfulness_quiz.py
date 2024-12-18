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
    <p><a href="{{ pdf_link }}" download>Click here to download your tracker</a></p>
    <p><strong>Want to take your mindfulness further? Check out our 'Mindfulness in 5' program and discover how just 5 minutes can help you achieve calm and balance.</strong></p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        score = sum(int(request.form.get(f"q{i}", 0)) for i in range(1, 8))

        # Log score for debugging
        print(f"Score calculated: {score}")

        if score <= 6:
            result = "You are at the STARTING LINE. Small steps will make a big difference."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_0cdeb9323eca4413a4068ba95ca53031.pdf"  # Little Wins Tracker
        elif 7 <= score <= 8:
            result = "You are EXPLORING NEW POSSIBILITIES. You're curious and ready to grow."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_35f937935c4047bf8c3ae16e9f0307b7.pdf"  # Mindful Habits Tracker
        elif 9 <= score <= 11:
            result = "You are BUILDING THE FOUNDATION. Consistency is key to lasting change."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_0b5509e208034a57be546d14bdc43e93.pdf"  # Mindful Reflection Tracker
        else:
            result = "You are THRIVING IN BALANCE. Keep nurturing your journey to deeper peace."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_656b6736b6474552ac3e2b079cae732a.pdf"  # 7-Day Habit Tracker

        # Log the result and link for debugging
        print(f"Result: {result}")
        print(f"PDF Link: {pdf_link}")

        return render_template_string(quiz_template, result=result, pdf_link=pdf_link)

    return render_template_string(quiz_template, result=None)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
