# TPC5

Data: 10/03/2025 <br>
Nome: José Pedro Torres Vasconcelos <br>
Número Mecanográfico: A100763 <br> <br> <br>

![José Vasconcelos, A100763](/images/me.png)


<br>

## **Resumo**
Programa escrito em python, que simula uma máquina de vending.

Inicialmente, é carregado um ficheiro JSON que listas de triplos,
compostas pelo nome do produto, quantidade e preço. (ficheiro de exemplo [stock.json](stock.json))


## **Comandos**

#### AJUDA
```
>> AJUDA
COMANDOS DISPONÍVEIS:
-> LISTAR
-> MOEDA <moedas>
-> SELECIONAR <codigo_produto>
-> SAIR
```

#### LISTAR
Exemplo:
```
>> LISTAR
maq:
cod  | nome              | quantidade | preço
--------------------------------------------
A23  | água 0.5L         |          8 |  0.70€
B14  | Coca-Cola 0.5L    |          5 |  1.20€
C56  | Pepsi 0.5L        |         10 |  1.10€
D89  | Fanta 0.5L        |          6 |  1.00€
E22  | Limonada 0.5L     |          4 |  1.30€
```


#### SELECIONAR
Exemplo:
```
>> SELECIONAR A23

```


#### MOEDA
Exemplo:
```
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c

```

#### SAIR
Exemplo:
```
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c
maq: Até à próxima
```