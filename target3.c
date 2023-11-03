// Compiled with:
// gcc -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -z execstack main.c read_input.c target3.c -o target3

#include <stdio.h>

void vulnerable(char *filename)
{
    long *p;
    long a;
    char buf[2048];

    read_input_with_limit(buf, filename, sizeof(buf) + 16);
    *p = a;
}

int _main(int argc, char *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Error: Need a command-line argument\n");
        return 1;
    }

    vulnerable(argv[1]);

    return 0;
}
