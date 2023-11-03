// Compiled with:
// gcc -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -Wno-nonnull main.c read_input.c target5.c -o target5

#include <stdio.h>
#include <unistd.h>

void run_ls()
{
    execve("/bin/ls", NULL, NULL);
}

void do_nothing(char *a, char *b, char *d) {}

void vulnerable(char *filename)
{
    char *a, *b, *c;
    char buf[10];

    read_input(buf, filename);
    do_nothing(a, b, c);
}

int _main(int argc, char *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Error: Need a command-line argument\n");
        return 1;
    }

    setuid(0);
    vulnerable(argv[1]);
    run_ls();

    return 0;
}
