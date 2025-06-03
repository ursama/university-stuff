#include<stdio.h>

int main(void) {
    int n, a = 2;

    printf("Podaj n: ");
    scanf("%d", &n);

    return 0;
}

int a(int n, int a) {
    int sum = 0;
    for (int i=0; i<n; i++){
        sum += a;
    }

    return sum;
}

int b()
