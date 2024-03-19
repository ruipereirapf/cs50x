from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = get_numb_letters(text)
    words = get_numb_words(text)
    sentences = get_numb_sentences(text)
    grade = get_grade(letters, words, sentences)

    if grade < 1:
        print(f"Before Grade 1")
    elif grade >= 16:
        print(f"Grade 16+")
    else:
        print(f"Grade {grade}")


def get_numb_letters(text):
    count = 0

    for char in text:
        if char.isalpha():
            count += 1
    return count


def get_numb_words(text):
    count = 1

    for char in text:
        if char == " ":
            count += 1
    return count


def get_numb_sentences(text):
    count = 0
    punctuation = [".", "?", "!"]
    for char in text:
        if char in punctuation:
            count += 1
    return count


def get_grade(letters, words, sentences):
    grade = 0

    S = (sentences / float(words)) * 100
    L = (letters / float(words)) * 100

    grade = round(0.0588 * L - 0.296 * S - 15.8)

    return grade


if __name__ == "__main__":
    main()
