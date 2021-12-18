#Write a Python program that accepts a word from the user and reverse it.
input=str(input("Enter a word : "))
for char in range(len(input) -1,-1,-1):
    print(input[char], end="")
print("\n")
