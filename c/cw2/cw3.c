#include<stdio.h>

int main(void) {
/*    int *pi;
    char *pc;
    float *pf, *pg;

    int *ptr = NULL;
    int *ptr2;

    printf("wskazniki: %p %p \n", ptr, ptr2);

    int a = 12, y;
    int *wa = &a;
    int *wa2 = wa;

    y = *wa;

    printf("%d %d \n", a, y);
*/
    int x = 10, y = 0;
    int *wsk_x = &x;

    printf("&x: %p \n", (void *)&x);
    printf("wsk_x: %p \n", (void *)wsk_x);

    printf("przed: x = %d, y = %d\n", x, y);

    (*wsk_x)++;
    y = *wsk_x;

    printf("po: x = %d, y = %d\n", x, y);

    return 0;
}
