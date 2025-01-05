def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = word_count(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"The document has {num_words} words!")
        print("")
        characters = char_count(file_contents)
        for i in characters:
            print(f"The '{i}' character appears {characters[i]} times")
        print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    for word in text.lower():
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    char_dict = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    char_dict = dict(char_dict)
    return char_dict

main()