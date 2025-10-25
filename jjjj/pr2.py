import time
print("welcome to my mind reading game!!!")
print("you: i can guess what u think!!")
print("you: if u donot believe think a number from 1-10")
input("Press Enter when done...")

print("\nyou:Now multiply the number with 2")
input("Press Enter when done...")
print("\nyou: now add 8 to number u think")
input("Press Enter when done...")
print("\nyou:now divide them by 2")
input("Press Enter when done...")
print("\n you: Now subtract the numbers by your first number")
input("Press Enter when done...")

print("\nAnalyzing your mind",end="")
for i in range(3):
    time.sleep(0.10)
    print(".",end="")
time.sleep(2)
print("\nyou:the number in your mind is : 4")
print("\n may i guessed in right..")
