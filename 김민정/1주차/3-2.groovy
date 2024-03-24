#include <stdio.h>
int main(){
    int score = 0;

    print("점수를 입력하세요:");
    scanf("%d",&score);

    if(score>+ 90 && score <=100){
    printf("%d점은 A입니다.\n",score);
} else if (score >= 80){
    printf("%d점은 B입니다.\n",score);
}else if(score>=70){
    printf("%d점은 C입니다.\n", score);
} else if(score>=60){
    printf("%d점은 D입니다.\n", score);
} else {
    printf("$d점은 F입니다.\n", score);
}
return 0;
}
