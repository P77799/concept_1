#show user random word
import random
import time

sentences=[    "Python is a powerful programming language",
    "Practice makes a man perfect",
    "Artificial intelligence is the future",
    "Never give up on your dreams",
    "Typing speed improves with practice"
]

ran=random.choice(sentences)
print("Typing speed test")
print("type fast as u can")
print("\n",ran)

s=input("Enter start to start the timer: ")

#start timer
start_time=time.time()
typed=input("enter here : ")
stop_time=time.time()

#calculate time
time_taken=stop_time-start_time

#count word 
words = ran.split()
typed_word=typed.split()

#check how many words are correct
correct_word=0
for i in range(min(len(words),len(typed_word))):
    if words[i]==typed_word[i]:
        correct_word+=1
    

#accuracy
accuracy=correct_word/len(words) *100

#word per minute
wpm=len(typed_word)/time_taken*60


print(f"Time taken:{time_taken}")
print(f"word type:{len(typed_word)}")
print(f"correct word: {correct_word}")
print(f"accuracy: {accuracy}")
print(f"word per minute{wpm}")


   