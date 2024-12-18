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

      <!-- Repeat for all questions -->

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

        # Assign results based on score
        if score <= 6:
            result = "You are at the STARTING LINE. Small steps will make a big difference."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_35f937935c4047bf8c3ae16e9f0307b7.pdf"
        elif 7 <= score <= 10:
            result = "You are BUILDING MOMENTUM. Consistency is key to lasting change."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_0b5509e208034a57be546d14bdc43e93.pdf"
        else:
            result = "You are THRIVING IN PLACE. Keep nurturing your journey to deeper peace."
            pdf_link = "https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_656b6736b6474552ac3e2b079cae732a.pdf"

        return render_template_string(quiz_template, result=result, pdf_link=pdf_link)

    return render_template_string(quiz_template, result=None)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
