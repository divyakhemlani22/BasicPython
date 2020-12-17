# 2D and Nested Loops
# 4 rows and 3 columns
# Grid Like Structure

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]

]

print(number_grid[2][1])

for row in number_grid:
    for col in number_grid:
        print(col)

# Translator - Changing Vowels to G
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))


