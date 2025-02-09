#File handeling and metaprogramming
#Reads the number of words in the text file and
def count_words(filename="task6_readme.txt"):
    with open(filename, "r") as file:
        content = file.read()
    words = content.split()
    return len(words)


#Runs the function``
if __name__ == "__main__":
    count = count_words()
    print(f"Number of words: {count}")