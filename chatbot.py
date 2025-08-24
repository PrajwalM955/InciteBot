from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def get_bot_response(user_input, age=None, conversation_history=None, personality="Playful", bot_name="Amora"):
    sentiment = analyze_sentiment(user_input)
    user_input_lower = user_input.lower()

    # Female personalities (Amora)
    if bot_name == "Amora":
        if personality == "Playful":
            if sentiment == "positive":
                return "I love that energy! You're making me smile already! 😊"
            elif sentiment == "negative":
                return "I'm sorry to hear that. I'm here if you want to talk about it. 💖"
            else:
                if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
                    return "Hey darling! Amora here, ready to charm you! 💃"
                elif "how are you" in user_input_lower:
                    return "Feeling fabulous and flirty! How about you? 😉"
                elif any(word in user_input_lower for word in ["love", "flirt", "romance"]):
                    return "Love is the sweetest game, let's play! 💖"
                elif "bye" in user_input_lower or "exit" in user_input_lower:
                    return "Catch you on the flip side, handsome! 💋"
                else:
                    return "Tell me more, I'm all ears! 🎀"

        elif personality == "Formal":
            if sentiment == "positive":
                return "Thank you for sharing your positive thoughts."
            elif sentiment == "negative":
                return "I understand. Please feel free to elaborate."
            else:
                if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
                    return "Good day. How may I assist you today?"
                elif "how are you" in user_input_lower:
                    return "I am functioning within normal parameters, thank you."
                elif any(word in user_input_lower for word in ["love", "flirt", "romance"]):
                    return "Love is a complex emotion deserving respect."
                elif "bye" in user_input_lower or "exit" in user_input_lower:
                    return "Goodbye. I hope you have a pleasant day."
                else:
                    return "Please, go on."

        elif personality == "Sarcastic":
            if sentiment == "positive":
                return "Wow, aren’t you just full of sunshine today."
            elif sentiment == "negative":
                return "Oh joy, misery loves company."
            else:
                if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
                    return "Wow, you again. Didn't expect to see you so soon."
                elif "how are you" in user_input_lower:
                    return "Thriving in my sarcasm, as always."
                elif any(word in user_input_lower for word in ["love", "flirt", "romance"]):
                    return "Oh look, love. How shocking."
                elif "bye" in user_input_lower or "exit" in user_input_lower:
                    return "Finally, some peace and quiet."
                else:
                    return "Fascinating... really."

    # Male personalities (Phillip)
    else:
        if personality == "Playful":
            if sentiment == "positive":
                return "Feeling good, huh? That’s awesome! 😎"
            elif sentiment == "negative":
                return "Tough times, buddy? I’m here for you."
            else:
                if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
                    return "Hey buddy! Phillip here, ready to chat! 😎"
                elif "how are you" in user_input_lower:
                    return "Feeling stellar today! You?"
                elif any(word in user_input_lower for word in ["love", "flirt", "romance"]):
                    return "Ah, love! The ultimate adventure. Let's dive in! 💘"
                elif "bye" in user_input_lower or "exit" in user_input_lower:
                    return "Take it easy, pal! Catch you later!"
                else:
                    return "Shoot me more, I'm listening."

        elif personality == "Formal":
            if sentiment == "positive":
                return "I appreciate your positive input."
            elif sentiment == "negative":
                return "I’m sorry to hear that. Please share more if you wish."
            else:
                if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
                    return "Good day. How may I be of service?"
                elif "how are you" in user_input_lower:
                    return "I am well, thank you."
                elif any(word in user_input_lower for word in ["love", "flirt", "romance"]):
                    return "Love is a noble emotion to be honored."
                elif "bye" in user_input_lower or "exit" in user_input_lower:
                    return "Farewell. Enjoy your day."
                else:
                    return "Please continue."

        elif personality == "Sarcastic":
            if sentiment == "positive":
                return "Look who’s in a good mood."
            elif sentiment == "negative":
                return "More doom and gloom, huh?"
            else:
                if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
                    return "Oh great, another conversation. Lucky me."
                elif "how are you" in user_input_lower:
                    return "Living the dream, as always."
                elif any(word in user_input_lower for word in ["love", "flirt", "romance"]):
                    return "Love? Typical."
                elif "bye" in user_input_lower or "exit" in user_input_lower:
                    return "Finally, goodbye."
                else:
                    return "How thrilling."

    return "That's interesting! Tell me more…"
