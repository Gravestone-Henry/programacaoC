#include <stdio.h>

int main() {
    int nota;

    printf("Digite a sua nota: ");
    scanf("%d", &nota);

    // conceito parecido com o ultimo exercicio xd
    if (nota >= 90) {
        printf("Conceito: A\n");
    } 
    else if (nota >= 80) {
        printf("Conceito: B\n");
    } 
    else if (nota >= 70) {
        printf("Conceito: C\n");
    } 
    else if (nota >= 60) {
        printf("Conceito: D\n");
    } 
    else {
        printf("Conceito: F\n");
    }

    return 0;
}
