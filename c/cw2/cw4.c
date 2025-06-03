#include<stdio.h>

int main(void) {
    int i, *p, *q;
    p = &i;
    i = 5;

    printf("%d \n", *p);

    *p = 6;
    printf("%d \n", i);
    q = p;
    printf("%d \n", *q);
    *q = 2;
    printf("%d \n", *p);

    return 0;
}
