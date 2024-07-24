def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(count(file_contents))
    print(char_count(file_contents))

def count(string):
    words = string.split()
    return len(words)

def char_count(string):
    char_dict = {}
    lower_string = string.lower()
    for char in lower_string:
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] +=1
    return char_dict


main()