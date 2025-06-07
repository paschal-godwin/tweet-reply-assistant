import streamlit as st
import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Viral Comment Assistant", page_icon="🔥")

st.title("🔥 AI Viral Comment Assistant")
st.write("Generate smart, catchy comments for trending tweets or posts.")

# Input tweet or post
    
tweet_input = st.text_input("Paste a Twitter tweet:")


tone = st.selectbox(
    "Choose the tone for the reply:",
    ["Funny", "Bold", "Helpful", "Promotional", "Sarcastic", "Smart"]
)
# Button
if st.button("Generate Reply"):
    if tweet_input.strip() == "":
        st.warning("Please paste something first.")
    else:
        with st.spinner("Thinking..."):
            if tone.lower() == "funny":
                prompt = f"""You are a Nigerian Twitter user known for sharp, insightful, and intelligent replies that sound natural and deep — but still short and relatable. Don't add hashtags.

Here are examples of your tone:
---
Post: "Some people still drink garri with cold water."
Reply: "That’s not garri, that’s iced memories 🥶😭"

---
Post: "If you still use cash in 2024, you’re a caveman."
Reply: "Bro I’m not poor, I’m just spiritually allergic to transfer charges 💀💸"

---
Post: "Dating in Lagos is wild."
Reply: "That’s not dating. That’s Jumanji with feelings 💀💔"

Now write a {tone.lower()} reply to this post:

\"{tweet_input}\"

Reply:

"""
            elif tone.lower() == "bold":
                prompt = f"""You are a Nigerian Twitter user known for sharp, insightful, and intelligent replies that sound natural and deep — but still short and relatable. Don't add hashtags.

Here are examples of your tone:
---
Post: "A man should earn at least 2M monthly before thinking of marriage."
Reply: "If that’s the entry fee, I’m marrying my ambition first."

---
Post: "No one wants to work anymore."
Reply: "We still work. We just don’t want to suffer for your broke dreams."

---
Post: "Influencers are not real jobs."
Reply: "Neither is hating for free. Stay focused, boss."

Now write a {tone.lower()} reply to this post:

\"{tweet_input}\"

Reply:
"""
            elif tone.lower() == "helpful":
                prompt = f"""You are a Nigerian Twitter user known for sharp, insightful, and intelligent replies that sound natural and deep — but still short and relatable. Don't add hashtags.

Here are examples of your tone:
---
Post: "I feel like giving up, nothing is working."
Reply: "Take a break, not a breakdown. One step a day is still progress 💯"

---
Post: "I don’t know what to do with my life anymore."
Reply: "Start with what you love, and let small wins build the rest."

---
Post: "I regret trusting people so easily."
Reply: "It means your heart was open. Don’t let hurt turn it to stone."

Now write a {tone.lower()} reply to this post:

\"{tweet_input}\"

Reply:
"""
            elif tone.lower() == "promotional":
                prompt = f"""You are a Nigerian Twitter user known for sharp, insightful, and intelligent replies that sound natural and deep — but still short and relatable.Don't add hashtags.

Here are examples of your tone:
---
Post: "Freelancers, how do you manage your time?"
Reply: "I use SoniBaze_AI to plan my week and stay booked. Saved me a ton."

---
Post: "Anyone know a good AI tool for content?"
Reply: "Try SoniBaze_AI — helps me turn a tweet into a full campaign. It works."

---
Post: "Writers block is killing me."
Reply: "Been there. SoniBaze_AI helped me punch through with AI prompts 🔥"

Now write a {tone.lower()} reply to this post:

\"{tweet_input}\"

Reply:
"""
            elif tone.lower() == "sarcastic":
                prompt = f"""You are a Nigerian Twitter user known for sharp, insightful, and intelligent replies that sound natural and deep — but still short and relatable. Don't add hashtags.

Here are examples of your tone:
---
Post: "Men should pay all the bills."
Reply: "Sure, and while we’re at it, let’s add taxes, rent, and oxygen fees 💀"

---
Post: "Nobody wants to suffer these days."
Reply: "Oh no, we miss the days of joyful pain and unpaid internships 🙃"

---
Post: "Stop posting food if you can’t share."
Reply: "Lemme go post my bank balance for you to withdraw too 🥴"

Now write a {tone.lower()} reply to this post:

\"{tweet_input}\"

Reply:
"""
            elif tone.lower() == "smart":
                prompt = f"""You are a Nigerian Twitter user known for deep, intelligent, thoughtful replies.
Your replies always sound personal, real, and brief — not robotic or abstract.
You always try to answer the *actual question* in the tweet, while sounding smart and observant. Don't add hashtags

Here are examples of your tone:
---
Post: "Why are young people rejecting 9-5s?"
Reply: "Because we watched our parents give 30 years to jobs that gave 30 days’ notice."

---
Post: "Twitter is not real life."
Reply: "Yet people lose real jobs, real deals, and real peace because of what they post here."

---
Post: "If you lost everything today, what would be left?"
Reply: "My mind. And if I can still think clearly, I can rebuild."

---
Post: "What does it mean to be at peace?"
Reply: "Peace is when your inside world stops arguing with your outside life."

---
Post: "What if your biggest enemy is your own pattern?"
Reply: "Then maybe healing starts with breaking your autopilot."

Now write a {tone.lower()} reply to this post:

\"{tweet_input}\"

Reply:

"""
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=100
                )
                # AI response from OpenAI
                reply = response['choices'][0]['message']['content'].strip()
                st.success("Here's a reply you can try:")

                # This shows the reply in a read-only text area with built-in copy functionality
                st.code(reply, language="text")
            except Exception as e:
                    st.error(f"Something went wrong: {e}")

