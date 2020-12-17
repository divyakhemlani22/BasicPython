# Loops

# While Loops
# Define variable
i = 1
# while condition
# As long as condition is true - it will loop
while i <= 10:
    print(i)
    i += 1

print("Done with Loop")

# Building a Guessing Game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while (guess != secret_word) and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

# For Loops

# Printing each letter
for letter in "Giraffe Academy":
    print(letter)

# Printing each element in an array
friends = ["Jim", "Karen", "Kevin"]
print(len(friends))

for friend in friends:
    print(friend)

# Printing from range 3 to 10 (not including 10)
for index in range(3, 10):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")

