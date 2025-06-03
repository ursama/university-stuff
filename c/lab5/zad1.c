#include<stdio.h>

int main() {
    int i = 0;
    char s[] = "Mata";
    char t[5];

    while(s[i] != '\0') {
        t[i] = s[i];
        i++;
    }
    t[i] = '\0';

    printf("Napis: %s", &t);

    return 0;
}
