#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>

int get_numb_letters(string text);
int get_numb_words(string text);
int get_numb_sentences(string text);
int get_grade(int letters, int words, int sentences);

int main(void)
{
    string text = get_string("Text: ");

    int letters = get_numb_letters(text);
    int words = get_numb_words(text);
    int sentences = get_numb_sentences(text);
    int grade = get_grade(letters, words, sentences);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int get_numb_letters(string text)
{
    int count = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            count += 1;
        }
    }
    return count;
}

int get_numb_words(string text)
{
    int count = 1;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == ' ')
        {
            count += 1;
        }
    }
    return count;
}

int get_numb_sentences(string text)
{
    int count = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            count += 1;
        }
    }
    return count;
}

int get_grade(int letters, int words, int sentences)
{
    int grade = 0;
    float S = (sentences / (float) words) * 100;
    float L = (letters / (float) words) * 100;

    grade = round(0.0588 * L - 0.296 * S - 15.8);

    return grade;
}
