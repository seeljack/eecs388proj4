// Compiled with:
// gcc -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -z execstack -DMINIASLR main.c read_input.c target6.c -o target6

#include <stdio.h>

void vulnerable(char *filename)
{
    char buf[1024];

    read_input(buf, filename);
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
