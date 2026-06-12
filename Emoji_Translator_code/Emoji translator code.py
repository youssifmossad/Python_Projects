# Usage:
# Enter a sentence containing :) or :(
# Example: Hello :) I am sad :(
# Output:  Hello 😀 I am sad 😞
emojis = {
    ":)": "😀",
    ":(": "😞"
}

words = input(">").split()

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)