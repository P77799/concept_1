
print("Welcome to what kind of programmer are u ? Quiz")
print("Answer the following question honestly!!! ")

score_creative=0
score_logical=0
score_lazy=0

print("Q2. How do you start a new project? ")

print("a) Jump straight into coding — I’ll figure it out later ")
print("b) Plan everything first — structure matters ")
print("c) Search online for inspiration )")

answer1=input("Your answr: ").lower()
if answer1=="a":
    score_creative+=2
elif answer1=="b":
    score_logical+=2
elif answer1=="c":
    score_lazy+=2

print(" \n Q2 What’s your biggest struggle while coding?")

print("a) Losing focus and opening YouTube ")
print("b) Debugging for hours ")
print("c) Naming variables creatively )")

answer2=input("Your answr: ").lower()
if answer2=="a":
    score_creative+=2
elif answer2=="b":
    score_logical+=2
elif answer2=="c":
    score_lazy+=2



print("\n Q3 If your code doesn’t work, you…?")

print("a) Take a break and blame Python ")
print("b) Debug systematically until I find the issue ")
print("c) Rewrite the entire thing from scratch)")

answer3=input("Your answr: ").lower()
if answer3=="a":
    score_creative+=2
elif answer3=="b":
    score_logical+=2
elif answer3=="c":
    score_lazy+=2

print("\n Q3What’s your favorite way to learn programming?")

print("a)Building cool things and experimenting 🧩")
print("b) Studying logic and theory deeply")
print("c) Watching tutorials and copying code)")
answer4=input("your anser: ").lower()

if answer4=="a":
    score_creative+=2
elif answer4=="b":
    score_logical+=2
elif answer4=="c":
    score_lazy+=2

print("\n🔍 Calculating your results...\n")

if score_creative>score_logical and score_creative>score_lazy:
    print("you are creative coder!!!")

elif score_logical>score_creative and score_logical>score_lazy:
    print("You are logical programmer !!")
elif score_lazy>score_creative and score_lazy>score_logical:
    print("YOu are lazy Geneus!!")
else:
    print("Yor are a balanced programmer!!")