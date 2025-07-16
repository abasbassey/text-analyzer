textQuery = input("Enter word/words here: ").lower()
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
legnthChecker = len(textQuery)
vowelCount = 0
consCount = 0
spaceChecker = 0
for text in textQuery:
    if text in vowels:
        vowelCount += 1
    elif text in consonants:
        consCount += 1
    elif text == " ":
        spaceChecker += 1
print(f"There are {vowelCount} vowels in the word '{textQuery}'")
print(f"There are {consCount} consonants in the word '{textQuery}'")
print(f"There are {spaceChecker} spaces in the word '{textQuery}'")