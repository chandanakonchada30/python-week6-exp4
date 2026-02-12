#24331A05E2
#usage of in operator and to count the no.of lowercase characters in a string
fruits = "apple banana watermelon"
print("apple" in fruits) 
string = input("Enter a string: ")
low_count = 0
for char in string:
    if char.islower():
        low_count += 1
print("Number of lowercase characters:", low_count)