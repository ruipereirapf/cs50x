#include <cs50.h>
#include <stdio.h>

// int main(void)
// {
//     int score1 = 72;
//     int score2 = 73;
//     int score3 = 33;

//     printf("Average: %i\n", (score1 + score2 + score3) / 3);

//     printf("Average: %f\n", (score1 + score2 + score3) / 3.0);

//     printf("Average: %f\n", (score1 + score2 + score3) / (float)3);
// }

// int main(void)
// {
//     int scores[3];
//     scores[0] = get_int("Score: ");
//     scores[1] = get_int("Score: ");
//     scores[2] = get_int("Score: ");

//     printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / (float)3);
// }

// int main(void)
// {
//     int scores[3];
//     for (int i = 0; i < 3; i++)
//     {
//         scores[i] = get_int("Score: ");
//     }

//     printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / (float)3);
// }


// const int n = 3;

// float average(int array[]);

// int main(void)
// {
//     int scores[n];
//     for (int i = 0; i < n; i++)
//     {
//         scores[i] = get_int("Score: ");
//     }

//     printf("Average: %f\n", average(scores));
// }

// float average(int array[])
// {
//     int sum = 0;
//     for (int i = 0; i < n; i++)
//     {
//         sum += array[i];
//     }
//     return sum / (float) n;
// }

const int n = 3;

float average(int length, int array[]);

int main(void)
{
    int scores[n];
    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score: ");
    }

    printf("Average: %f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
