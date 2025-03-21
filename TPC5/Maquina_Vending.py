import re
import json

class Maquina_Vending:
    
    def __init__(self):
        self.stock_file = ""
        self.stock = {}
        self.saldo = 0.0
        
    def set_stock(self, stock):
        self.stock = stock
        
    def inserir_moedas(self, lista_de_moedas):
        
        valores_moedas = {
            "1e": 1.0,
            "2e": 2.0,
            "50c": 0.50,
            "20c": 0.20,
            "10c": 0.10,
            "5c": 0.05
        }
        
        for moeda in lista_de_moedas:
            
            if re.match(r'^(1e|2e|50c|20c|10c|5c)$', moeda):
                self.saldo += valores_moedas[moeda]
            else:
                print(f"Moeda inválida: {moeda}")
                
    def verificar_saldo(self):
        return self.saldo
    
    def ver_stock(self):
        print(self.stock)
    
    def listar(self):
        print("maq:")
        print("cod  | nome              | quantidade | preço")
        print("--------------------------------------------")
        for item in self.stock:
            print(f"{item['cod']:4} | {item['nome']:18}| {item['quant']:10} | {item['preco']:>5.2f}€")
            
    def devolver_troco(self):
        troco_disponivel = {
            200: "2e", 100: "1e",
            50: "50c", 20: "20c",
            10: "10c", 5: "5c",
            2: "2c", 1: "1c"
        }
        troco = int(self.saldo * 100)
        resultado_troco = {}

        for valor, moeda in troco_disponivel.items():
            if troco >= valor:
                quantidade = troco // valor
                troco -= quantidade * valor
                resultado_troco[moeda] = quantidade

        self.saldo = 0.0
        return ", ".join(f"{qtd}x {moeda}" for moeda, qtd in resultado_troco.items())
    
    def selecionar_produto(self, codigo_produto):
        produto = None
        for item in self.stock:
            if item['cod'] == codigo_produto:
                produto = item
        
        if produto is None:
            print("maq: Código inválido.")
            return
        
        if self.saldo < produto['preco']:
            print("maq: Saldo insuficiente para satisfazer o seu pedido")  
            print(f"maq: Saldo = {self.saldo}; Pedido = {produto['preco']}")
        elif produto['quant'] > 0:
            self.saldo -= produto['preco']
            print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
            print(f"maq: Saldo = {self.saldo}")
            produto['quant'] -= 1
            
    def ajuda(self):
        print("COMANDOS DISPONÍVEIS:")
        print("-> LISTAR")
        print("-> MOEDA <moedas>")
        print("-> SELECIONAR <codigo_produto>")
        print("-> SAIR")
            
    def guardar_estado(self):
            if self.stock_file:
                with open(self.stock_file, "w") as f:
                    json.dump({"stock": self.stock}, f, indent=4, ensure_ascii=False)
                print("maq: Estado guardado com sucesso!")
            else:
                print("maq: Erro ao guardar o estado. Nenhum ficheiro associado.")