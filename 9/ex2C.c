#include <stdio.h>

void func(){
    char password[16] = "supersecret";
    char answer[16];

    printf("What is your name?\n");
    gets(answer);

    printf("Your name is: %s \n", answer);
    printf("Your password is: %s \n", password);
}

void main(int argc, char **argv){
    func();
}
