import random
import time

sentences = [
    "Python is a powerful programming language",
    "Practice makes a man perfect",
    "Artificial intelligence is the future",
    "Never give up on your dreams",
    "Typing speed improves with practice"
]

# Pick random sentence
ran = random.choice(sentences)
print("⚡ Typing Speed Test ⚡")
print("Type fast as you can!")
print("\n👉", ran)   # show only the random sentence

s = input("Press Enter to start the timer...")

# Start timer
start_time = time.time()
typed = input("\nStart typing here:\n")
stop_time = time.time()

# Calculate time
time_taken = stop_time - start_time

# Split words
words = ran.split()
typed_words = typed.split()

# Check correct words
correct_words = 0
for i in range(min(len(words), len(typed_words))):
    if words[i] == typed_words[i]:
        correct_words += 1

# Accuracy
accuracy = (correct_words / len(words)) * 100

# Words per minute
wpm = (len(typed_words) / time_taken) * 60

# Results
print(f"\n⌛ Time taken: {round(time_taken, 2)} seconds")
print(f"📖 Words typed: {len(typed_words)}")
print(f"✅ Correct words: {correct_words}")
print(f"🎯 Accuracy: {round(accuracy, 2)}%")
print(f"⚡ Speed: {round(wpm, 2)} WPM")