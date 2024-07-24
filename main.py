def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_count = count(file_contents)
    char_dict = char_count(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()