// Compiled with:
// gcc -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -z execstack main.c read_input.c target1.c -o target1

#include <stdio.h>
#include <stdlib.h>

void print_bad_grade()
{
    puts("Your grade is E.");
    exit(0);
}

void print_good_grade()
{
    puts("Your grade is A+.");
    exit(1);
}

void vulnerable(char *filename)
{
    char buf[4];

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
    print_bad_grade();

    return 0;
}
