#include <stdio.h>

int main() {
    // nome dos produto
    char produtoY[30] = "Produto Y";
    char produtoX[30] = "Produto X";

    // estoque
    unsigned int estoqueY = 666;
    unsigned int estoqueX = 999;

    // valor unitario
    float valorY = 10.50;
    float valorX = 20.50;

    // minimo pra ter controle
    unsigned int estoqueMinimoY = 333;
    unsigned int estoqueMinimoX = 499;

    // caulculos de estoque henry
    double valorTotalY = (double)estoqueY * valorY;
    double valorTotalX = (double)estoqueX * valorX;

    // Exibir info dos produtos
    printf("--- RELATÓRIO DE ESTOQUE ---\n");
    
    printf("Produto: %s\n", produtoY);
    printf("Estoque: %u | Valor Unitário: R$ %.2f\n", estoqueY, valorY);
    printf("Valor Total em Estoque: R$ %.2f\n", valorTotalY);
    
    printf("----------------------------\n");

    printf("Produto: %s\n", produtoX);
    printf("Estoque: %u | Valor Unitário: R$ %.2f\n", estoqueX, valorX);
    printf("Valor Total em Estoque: R$ %.2f\n", valorTotalX);

    // Comparando os estoques mínimos
    printf("\n--- comparar estoque minimo :P ---\n");

    if (estoqueMinimoY > estoqueMinimoX) {
        printf("O %s tem o maior estoque mínimo (%u).\n", produtoY, estoqueMinimoY);
    } else if (estoqueMinimoX > estoqueMinimoY) {
        printf("O %s tem o maior estoque mínimo (%u).\n", produtoX, estoqueMinimoX);
    } else {
        printf("Ambos os produtos têm o mesmo estoque mínimo (%u).\n", estoqueMinimoY);
    }

    return 0;
}