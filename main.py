def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(count(file_contents))

def count(string):
    words = string.split()
    return len(words)

main()