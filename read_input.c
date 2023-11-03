#include <stdio.h>
#include <stdlib.h>

void read_input_with_limit(char *destination, const char *filename, size_t limit)
{
	size_t left_to_read = limit;

	FILE *file = fopen(filename, "rb");
	if (file == NULL)
	{
		perror("Error opening input file");
		exit(1);
	}

	while (!feof(file) && left_to_read > 0)
	{
		const size_t elements_to_read = left_to_read > 0x400 ? 0x400 : left_to_read;

		const size_t elements_read = fread(destination, sizeof(char), elements_to_read, file);
		if (ferror(file))
		{
			perror("Error reading input file");
			exit(1);
		}

		left_to_read -= elements_read;
		destination += elements_read;
	}

	fclose(file);
}

void read_input(char *destination, const char *filename)
{
	read_input_with_limit(destination, filename, 0xffffffffffffffff);
}
