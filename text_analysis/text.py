def count_words_in_file(file_path):
    word_counts = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?()[]{}\'"').lower()
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1

        for word, count in word_counts.items():
            print(f'{word}: {count}')

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "/Users/vedantrai/vsc/python/text_analysis/lorem_ipsum.txt"  
    count_words_in_file(file_path)
