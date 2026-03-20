#include <stdio.h>

int main() {
    int idade;

    printf("Digite a sua idade: \n");
    scanf("%d", &idade);

    // começando do maior como o prof pediu :P 
    if (idade >= 60) {
        printf("Você é um velhote!\n");
    } 
    // Se não é velhote é adulto (18 até 59)
    else if (idade >= 18) {
        printf("Você é um adulto!\n");
    } 
    // Se não é adulto é aborrecente (12 até 17)
    else if (idade >= 12) {
        printf("Você é um aborrecente!\n");
    } 
    
    else {
        printf("Você é uma criancinha!\n");
    }

    return 0;
}