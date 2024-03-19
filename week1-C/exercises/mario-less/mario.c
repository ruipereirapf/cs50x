#include <cs50.h>
#include <stdio.h>

int get_height(void);

int main(void)
{
    int n = get_height();

    for (int i = 0; i < n; i++)
    {
        for (int k = n - 1; k > i; k--)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

int get_height(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}
