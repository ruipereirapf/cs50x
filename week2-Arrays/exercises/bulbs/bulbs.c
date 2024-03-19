// char *data = "01100001";
// //data2 = data >> 2
// char *data2 = "00000011";
// char c = strtol(data2, 0, 2);
// printf("%s = %c = %d = 0x%.2X\n", data2, c, c, c);


// 01100001 = "a"


// text[i] >> j -> 01100001 >> 7 -> 00000000 & 00000001 -> 00000000 = 0

// text[i] >> j -> 01100001 >> 6 -> 00000001 & 00000001 -> 00000001 = 1

// text[i] >> j -> 01100001 >> 5 -> 00000011 & 00000001 -> 00000001 = 1

// text[i] >> j -> 01100001 >> 4 -> 00000110 & 00000001 -> 00000000 = 0

// text[i] >> j -> 01100001 >> 3 -> 00001100 & 00000001 -> 00000000 = 0

// text[i] >> j -> 01100001 >> 2 -> 00011000 & 00000001 -> 00000000 = 0

// text[i] >> j -> 01100001 >> 1 -> 00110000 & 00000001 -> 00000000 = 0

// text[i] >> j -> 01100001 >> 0 -> 01100001 & 00000001 -> 00000001 = 1



#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string text = get_string("Text: ");

    for (int i = 0; text[i] != '\0'; i++)
    {
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            int bit = (text[i] >> j) & 1;
            print_bulb(bit);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
