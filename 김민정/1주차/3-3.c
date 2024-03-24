#include <stido.h>
void findodd(int*ptr){
    int i;
    printf("홀수출력:");
    for (i=0; i<10; ++i){
        if(ptr[i]%2!=0)
        printf("%d,", ptr[i]);
    }
    printf("\b\n");
    return 0;
}