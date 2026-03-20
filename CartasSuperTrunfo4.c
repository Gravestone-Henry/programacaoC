#include <stdio.h>

int main() {
    // --- Variáveis Carta 1 ---
    char estado1;
    char codigo1[4], nomeCidade1[50];
    unsigned long int populacao1;
    float area1, pib1, densidade1, pibPerCapita1, superPoder1;
    int pontosTuristicos1;

    // --- Variáveis Carta 2 ---
    char estado2;
    char codigo2[4], nomeCidade2[50];
    unsigned long int populacao2;
    float area2, pib2, densidade2, pibPerCapita2, superPoder2;
    int pontosTuristicos2;

    // --- Cadastro 1 ---
    printf("--- Cadastro da Carta 1 ---\n");
    printf("Estado (A-H): ");
    scanf(" %c", &estado1); 
    printf("Código da Carta (ex: A01): ");
    scanf("%3s", codigo1); 
    printf("Nome da Cidade: ");
    scanf(" %[^\n]", nomeCidade1); 
    printf("População: ");
    scanf("%lu", &populacao1);
    printf("Área (km²): ");
    scanf("%f", &area1);
    printf("PIB (em bilhões): ");
    scanf("%f", &pib1);
    printf("Pontos Turísticos: ");
    scanf("%d", &pontosTuristicos1);

    // Cálculo Carta 1
    densidade1 = (float)populacao1 / area1;
    pibPerCapita1 = (pib1 * 1000000000.0) / (float)populacao1;
    superPoder1 = (float)populacao1 + area1 + (pib1 * 1000000000.0) + (float)pontosTuristicos1 + pibPerCapita1 + (1.0f / densidade1);

    printf("\n");

    // --- Cadastro 2 ---
    printf("--- Cadastro da Carta 2 ---\n");
    printf("Estado (A-H): ");
    scanf(" %c", &estado2);
    printf("Código da Carta: ");
    scanf("%3s", codigo2);
    printf("Nome da Cidade: ");
    scanf(" %[^\n]", nomeCidade2);
    printf("População: ");
    scanf("%lu", &populacao2);
    printf("Área (km²): ");
    scanf("%f", &area2);
    printf("PIB (em bilhões): ");
    scanf("%f", &pib2);
    printf("Número de Pontos Turísticos: ");
    scanf("%d", &pontosTuristicos2);

    // Cálculos Carta 2
    densidade2 = (float)populacao2 / area2;
    pibPerCapita2 = (pib2 * 1000000000.0) / (float)populacao2;
    superPoder2 = (float)populacao2 + area2 + (pib2 * 1000000000.0) + (float)pontosTuristicos2 + pibPerCapita2 + (1.0f / densidade2);

    // --- COMPARAÇÃO COM IF/ELSE ---
    printf("\n=================================\n");
    printf("       RESULTADO DA BATALHA      \n");
    printf("=================================\n");

    // Comparação população
    printf("População: ");
    if (populacao1 > populacao2) printf("Carta 1 (%s) venceu!\n", nomeCidade1);
    else if (populacao2 > populacao1) printf("Carta 2 (%s) venceu!\n", nomeCidade2);
    else printf("Empate!\n");

    // Comparação Área
    printf("Área: ");
    if (area1 > area2) printf("Carta 1 venceu!\n");
    else if (area2 > area1) printf("Carta 2 venceu!\n");
    else printf("Empate!\n");

    // Comparação PIB
    printf("PIB: ");
    if (pib1 > pib2) printf("Carta 1 venceu!\n");
    else if (pib2 > pib1) printf("Carta 2 venceu!\n");
    else printf("Empate!\n");

    // Comparação de Densidade ( Menor vence)
    printf("Densidade Populacional: ");
    if (densidade1 < densidade2) printf("Carta 1 venceu (Menor densidade)!\n");
    else if (densidade2 < densidade1) printf("Carta 2 venceu (Menor densidade)!\n");
    else printf("Empate!\n");

    // Comparação final poder fodao
    printf("---------------------------------\n");
    printf("SUPER PODER (Geral): ");
    if (superPoder1 > superPoder2) {
        printf("VITORIA DA CARTA 1: %s!\n", nomeCidade1);
    } else if (superPoder2 > superPoder1) {
        printf("VITORIA DA CARTA 2: %s!\n", nomeCidade2);
    } else {
        printf("EMPATE BOCÓ!\n");
    }
    printf("=================================\n");

    return 0;
}