# #task1
# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     result = ""
#     for char in string:
#         if char.lower() not in vowels:
#             result += char
#     return result

# input_string = input("Enter a string to remove vowels from it ")
# print("after removing vowels ", remove_vowels(input_string))

# def replace_vowels(strings_list):
#     result = []
#     for s in strings_list:
#         result.append(remove_vowels(s))
#     return result

# input_strings = input("Enter a list of strings separated by spaces ")
# print("after removing vowels ", replace_vowels(input_strings.split()))

# #task2
# def character_locator(string, character):
#     indices = []
#     for index in range(len(string)):
#         if string[index] == character:
#             indices.append(index)

#     if not indices:
#         return "cant find the character in the string"
#     return indices

# input_string = input("Enter a string to search for a character ")
# character = input("Enter a character to find its indices in the string  ")
# print(character_locator(input_string, character))


# #task3
# def multiplcation_table(number):
#     table = []
#     for i in range(1, number+1):
#         number_table = []
#         for j in range(1, i+1):
#             number_table.append(i * j)
#         table.append(number_table)
#     return table

# number = int(input("Enter a number "))
# print("Multiplication table for", number, "is: ")
# print(multiplcation_table(number))

# #task4
# def calculate_area( shape, *dimensions):
#     if shape == "c":
#         area = 22/7 * dimensions[0] ** 2
#     elif shape == "s":
#         area = dimensions[0] ** 2
#     elif shape == "r":
#         area = dimensions[0] * dimensions[1]
#     elif shape == "t":
#         area = 0.5 * dimensions[0] * dimensions[1]
#     else:
#         return "Invalid shape"
#     return area

# print("""
# Choose a shape to calculate its area:
# c - circle
# s - square
# r - rectangle
# t - triangle
# """)
# shape = input("Enter the shape [c|s|r|t] ")
# dimensions = input("Enter the dimensions separated by spaces: ").split()
# dimensions = list(map(float, dimensions))
# print(f"The area is:", calculate_area(shape, *dimensions))


#task5
def sort_words(words_list):
    words_list.sort()
    words_dict = {}
    for word in words_list:
        if word[0].lower() not in words_dict:
            words_dict[word[0].lower()] = []
        words_dict[word[0].lower()].append(word)
    return words_dict

input_words = input("Enter a list of words separated by spaces ")
print("Sorted words " , sort_words(input_words.split()))


#task6
def mario_pyramid(levels):
    for i in range(1, levels + 1):
        for j in range(levels):
            if j < levels - i:
                print(" ", end="")
            else:
                print("*", end="")
        print()  

input_levels = int(input("Enter the number of levels for triangl "))
mario_pyramid(input_levels)