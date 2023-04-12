# Write a program that uses a tuple to represent a person's
# name, age, and gender, and then prints out a message 
# that says "Hello, my name is [name], I am [age] 
# years old, and I am [gender]."

a = "Alice"
b =20
c ="Female"
print(f"Hello my name is {a}, I am a {c} and I am {b} years old")

# Write a program that creates a dictionary of English words
# and their corresponding definitions, and 
# then prompts the user to enter a word and 
# prints out its definition (if it exists in the dictionary).

dictionary = {
    "apple": "a round fruit with shiny red or green skin and a hard white core",
    "book": "a written or printed work consisting of pages glued or sewn together along one side and bound in covers",
    "computer": "an electronic device that can perform calculations and manipulate data",
    "dog": "a domesticated mammal that is related to the wolves and is commonly kept as a pet",
}
word = input("Enter a word to look up in the dictionary: ")
if word in dictionary: print("{}: {}".format(word, dictionary[word]))
   
else:
    print("Sorry, the word '{}' is not in the dictionary.".format(word))
    
# Write a program that creates a set of all the vowels
# in the English alphabet, and then prompts the user
# to enter a word and prints out all the vowels that appear in the word.
# Define the set of vowels
  
vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Enter a word: ")
word_vowels = set()
for char in word:
    if char.lower() in vowels:
        word_vowels.add(char.lower())
if len(word_vowels) > 0:
    print("The vowels in the word are:", ', '.join(word_vowels))
else:
    print("The word has no vowels.") 
   