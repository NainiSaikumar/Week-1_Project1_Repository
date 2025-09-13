# Emoji Mood Responder

def mood_responder():
    print("Welcome to Emoji Mood Responder! (type 'exit' to quit)\n")

    while True:
        mood = input("How are you feeling today? ").lower().strip()

        if mood == "exit":
            print("Goodbye! 👋")
            break

        if "happy" in mood:
            print("🙂 That's great to hear! 😊")
        elif "sad" in mood:
            print("😔 Cheer up! Here's a hug 🤗")
        elif "angry" in mood:
            print("😡 Take a deep breath 😤")
        elif "tired" in mood:
            print("😴 Rest well! 😴")
        elif "excited" in mood:
            print("🥳 Let’s celebrate! 🥳")
        else:
            print("🤔 I’m not sure how to respond, but I’m here for you!")

# Call the function
mood_responder()

