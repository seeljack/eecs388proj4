// Compiled with:
// gcc -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -z execstack main.c read_input.c target4.c -o target4

#include <alloca.h>
#include <stddef.h>
#include <stdio.h>

void read_elements(FILE *f, unsigned int *buf, size_t count)
{
    for (size_t i = 0; i < count; i++)
    {
        if (fread(&buf[i], sizeof(unsigned int), 1, f) < 1)
        {
            break;
        }
    }
}

void read_file(char *name)
{
    FILE *f = fopen(name, "rb");
    if (f == NULL)
    {
        fprintf(stderr, "Error: Cannot open file\n");
        return;
    }

    size_t count;
    fread(&count, sizeof(size_t), 1, f);

    unsigned int *buf = alloca(count * sizeof(unsigned int));
    if (buf == NULL)
    {
        fprintf(stderr, "Error: Cannot allocate a buffer\n");
        return;
    }

    read_elements(f, buf, count);
}

int _main(int argc, char *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Error: Need a command-line argument\n");
        return 1;
    }

    read_file(argv[1]);

    return 0;
}
