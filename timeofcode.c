#include <stdio.h>

int main(){
    float temperatura, umidade;
    unsigned int estoque, estoqueMinimo = 1000;

    printf("Entre com a temperatura: \n");
    scanf("%f",&temperatura);
    printf("Entre com a umidade: \n");
    scanf("%f", &umidade);
    printf("Entre com o estoque: \n");
    scanf("%u", &estoque);

    if( temperatura > 30){
        printf("Temperatura ta alta bocó.\n");
    }  else {
        printf("Temperatura ta normal rlx.\n");
    }
    
    if(umidade > 50){
       printf("umidade elevada.\n");
    }  else {
       printf("Umidade ta normal rlx.\n");
    } 

    if(estoque < estoqueMinimo){
       printf("Estoque abaixo do minimo bocó!\n");
    }  else {
       printf("Estoque normal rlx!\n");
    }   
   
    
}