# Quiz Program (3 new questions)

name = input("What is your name? ")
print("Welcome,", name, "!\n")

score = 0

# Q1
print("Q1: What is 5 + 3?")
ans1 = input("Your answer: ")

if ans1 == "8":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is 8.\n")

# Q2
print("Q2: What color is the sky on a clear day?")
ans2 = input("Your answer: ").lower()

if ans2 == "blue":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is blue.\n")

# Q3
print("Q3: Which animal barks? (dog/cat)")
ans3 = input("Your answer: ").lower()

if ans3 == "dog":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is dog.\n")

# Final result
print(name, "you scored", score, "out of 3.")
