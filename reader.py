import argparse

# python reader.py --file file_to_read.txt


def longest_words(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    max_length = max(len(word) for word in words)
    long_words_list = [word for word in words if len(word) == max_length]

    return long_words_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Пошук найдовших слів у тексті")
    parser.add_argument("--file", help="Шлях до файлу")
    args = parser.parse_args()

    if args.file:
        longest_words_list = longest_words(args.file)
        print("Найдовші слова:", ", ".join(longest_words_list))
    else:
        print("Будь ласка, вкажіть шлях до файлу")
