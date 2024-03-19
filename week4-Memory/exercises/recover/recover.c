#include <stdint.h> // Include this header for uint8_t type
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for correct usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <forensic_image>\n", argv[0]);
        return 1;
    }

    // Open the forensic image file for reading in binary mode
    FILE *input_file = fopen(argv[1], "rb");
    if (input_file == NULL)
    {
        printf("Error: Could not open forensic image file %s\n", argv[1]);
        return 2;
    }

    // Store array of 512 bytes
    unsigned char buffer[512];

    // Track the number of generated images
    int count_image = 0;

    // File pointer for output file
    FILE *output_file = NULL;

    // Filename buffer
    char filename[10]; // Changed the size to 10, considering the format %03i.jpg

    // Read the 512 bytes array
    while (fread(buffer, sizeof(char), 512, input_file) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous output file if it's open
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            // Write JPEG filename
            sprintf(filename, "%03i.jpg", count_image);

            // Open file for writing in binary mode
            output_file = fopen(filename, "wb");

            if (output_file == NULL)
            {
                fprintf(stderr, "Error: Could not create output file %s\n", filename);
                return 3;
            }

            count_image++;
        }

        // Check if output is valid
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }

    // Close the last output file
    if (output_file != NULL)
    {
        fclose(output_file);
    }

    fclose(input_file);

    return 0;
}
