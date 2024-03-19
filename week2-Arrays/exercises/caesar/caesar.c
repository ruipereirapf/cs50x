#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

char *cipher_text(string text, string cipher, int n);

int main(int argc, string argv[])
{
    int n = 0;
    if (argc == 2)
    {
        for (int i = 0; argv[1][i]; i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caeser key\n");
                return 1;
            }
        }
        n = atoi(argv[1]);
    }
    else
    {
        printf("Usage: ./caeser key\n");
        return 1;
    }

    string text = get_string("plaintext:  ");
    string cipher = text;

    cipher = cipher_text(text, cipher, n);
    printf("ciphertext: %s\n", cipher);
}

char *cipher_text(string text, string cipher, int n)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            if (islower(text[i]))
            {
                cipher[i] = ((text[i] - 'a' + n) % 26) + 'a';
            }
            else
            {
                cipher[i] = ((text[i] - 'A' + n) % 26) + 'A';
            }
        }
    }
    return cipher;
}
