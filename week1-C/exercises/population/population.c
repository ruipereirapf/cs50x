#include <cs50.h>
#include <stdio.h>

int get_start(void);
int get_end(int start);
int get_years(int start, int end);

int main(void)
{
    // TODO: Prompt for start size
    int start = get_start();

    // TODO: Prompt for end size
    int end = get_end(start);

    // TODO: Calculate number of years until we reach threshold
    int years = get_years(start, end);

    // TODO: Print number of years
    printf("Years: %d\n", years);
}

int get_start(void)
{
    int start;
    do
    {
        start = get_int("Start Size: ");
    }
    while (start < 9);
    return start;
}

int get_end(int start)
{
    int end;
    do
    {
        end = get_int("End Size: ");
    }
    while (end < start);
    return end;
}

int get_years(int start, int end)
{
    int years = 0;
    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        years++;
    }
    return years;
}
