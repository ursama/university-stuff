#include<stdio.h>
#include<math.h>

double delta(double a, double b, double c);

int main(void) {
    double a, b, c, d;

    printf("Podaj a, b, c: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    d = delta(a, b, c);
    printf("\nDelta: %.2lf\n", d);

    if (d >= 0) {
        printf("p1 = %.2lf \n", ((-b + sqrt(d)) / 2 * a));
        printf("p2 = %.2lf \n", ((-b - sqrt(d)) / 2 * a));
    } else {
        printf("p1 = %.2lf - %.2lfi \n", (-b / 2 * a), (sqrt(-d) / 2 * a));
        printf("p2 = %.2lf + %.2lfi \n", (-b / 2 * a), (sqrt(-d) / 2 * a));
    }

    return 0;
}

double delta(double a, double b, double c) {
    return b * b - 4 * a * c;
}
