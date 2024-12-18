print("\nWelcome to Your Mindfulness Snapshot Quiz!")
print("Take a moment to answer these 7 quick questions to see where you are on your journey.")
print("Let's get started!\n")

score = 0
questions = [
    "1. How often do you feel overwhelmed or stuck?\nA) Almost always  B) Often  C) Sometimes  D) Rarely or never",
    "2. How consistent are you with practicing mindfulness or self-care?\nA) Not consistent at all  B) Rarely consistent  C) Somewhat consistent  D) Very consistent",
    "3. How important is it to you to make a lifestyle change?\nA) Not important  B) Somewhat important  C) Very important  D) Extremely important",
    "4. How prepared do you feel to take actionable steps toward your goals?\nA) Never  B) Slightly prepared  C) Moderately prepared  D) Fully prepared",
    "5. How often do you celebrate your wins, big or small?\nA) Never  B) Rarely  C) Occasionally  D) Often",
    "6. How connected do you feel to your core values?\nA) Not connected  B) Slightly connected  C) Moderately connected  D) Deeply connected",
    "7. How often do you take time to pause and reflect on your progress?\nA) Never  B) Rarely  C) Occasionally  D) Regularly"
]

# Ask the questions and calculate the score
for question in questions:
    print("\n" + question)
    answers = ["A", "B", "C", "D", "A", "B", "C"]  # Example fixed answers
score = 0

# Replace this loop
for i, question in enumerate(questions):
    print("\n", question)
    answer = answers[i]  # Use pre-determined answers instead of input
    print(f"Your answer: {answer}")
    if answer == "A":
        score += 1
    elif answer == "B":
        score += 2
    elif answer == "C":
        score += 3
    elif answer == "D":
        score += 4
# Display results based on score
print("\nYour Results Are In...\n")

if score <= 12:
    print("🛠 You are at the STARTING LINE. Small steps will make a big difference.")
    print("➡ Download your 'Mindful Habits Tracker' to kickstart your routine here:")
    print("https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_fd0d302e952e487d8e7eddeaca9163c6.pdf")

elif 13 <= score <= 17:
    print("✨ You are EXPLORING NEW POSSIBILITIES. You're curious and ready to grow.")
    print("➡ Download your 'Celebrate Your Little Wins Tracker' to stay encouraged here:")
    print("https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_8d97081e4f6f4a14bfdb1a30758a8e70.pdf")

elif 18 <= score <= 23:
    print("🧱 You are BUILDING THE FOUNDATION. Consistency is key to lasting change.")
    print("➡ Download your 'Mindful Reflection Checklist' to deepen your focus here:")
    print("https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_11968017ea9d4981b5d55c7d73a298ac.pdf")

else:
    print("🌱 You are THRIVING IN BALANCE. Keep nurturing your journey to deeper peace.")
    print("➡ Download your '7-Day Mindfulness Challenge' for ongoing inspiration here:")
    print("https://9c428778-7ec4-4d4f-b578-316e46ca64cb.usrfiles.com/ugd/9c4287_79031ba3912c47ffa27570704eac8166.pdf")

print("\nThank you for taking the quiz! Visit https://meannadk.com to access more tools and resources for your journey.")
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
