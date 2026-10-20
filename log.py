feedback = input("Enter your feedback: ")

with open("log.txt", "a") as log:
    log.write(feedback + "\n")

print("Thank you for your feedback!")