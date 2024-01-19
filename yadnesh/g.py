# Define a function to convert a number to its word representation
def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= num < 20:
        return units[num]
    elif 20 <= num <= 99:
        return tens[num // 10] + units[num % 10]
    else:
        return "onehundred"  # Handle the number 100 separately

# Calculate the sum of characters in the word representations from 1 to 600
total_characters = sum(len(number_to_words(num)) for num in range(1, 601))

print("Sum of characters:", total_characters)
