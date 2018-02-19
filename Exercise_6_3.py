def count (word, letter1):
    count = 0
    for letter in word:
        if letter == letter1:
            count = count + 1
    return count
    
word = input("Enter the word: ")
letter = input("Enter the letter: ")
result = count(word,letter)
print(result)     
