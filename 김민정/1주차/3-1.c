#include <stdio.h>
int main(void)
{
    int x;
    int y;
    int sum, diff, mul, div, rest;

    x=7;
    y=3;

    sum = x+y;
    diff = x-y;
    mul = x*y;
    div = x/y;
    rest = x%y;

    printf("두수의 합: %d\n", sum);
    printf("두수의 차: %d\n", diff);
    printf("두수의 곱: %d\n", mul);
    printf("두수의 몫: %d\n", div);
    printf("나머지: %d\n", rest);
    return 0;
}