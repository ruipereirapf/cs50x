#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // int x = get_int("x: ");
    // int y = get_int("y: ");

    // printf("%i\n", x + y);

    // long x = get_long("x: ");
    // long y = get_long("y: ");

    // printf("%li\n", x + y);

    // long x = get_long("x: ");
    // long y = get_long("y: ");

    // float z = (float)x / (float)y;

    // printf("%.20f\n", z);

    long x = get_long("x: ");
    long y = get_long("y: ");

    double z = (double)x / (double)y;

    printf("%.20f\n", z);
}
