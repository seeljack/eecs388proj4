// Compiled with:
// gcc -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -z execstack main.c read_input.c target0.c -o target0

#include <stdio.h>
#include <string.h>

void vulnerable(char *filename)
{
    char grade[5];
    char name[10];

    strcpy(grade, "E");
    read_input(name, filename);
    printf("Hi %s! Your grade is %s.\n", name, grade);
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
