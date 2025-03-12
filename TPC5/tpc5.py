import sys
from Maquina_Vending import Maquina_Vending
import json
from datetime import datetime

def start(stock_file):
        
    stock = {}
    with open(stock_file, 'r') as f:
        data = json.load(f)

    stock = data["stock"]
        
    maquina = Maquina_Vending()
    maquina.set_stock(stock)
    #maquina.ver_stock()
    if maquina.stock:
        data = datetime.today().strftime("%Y-%m-%d")
        print("maq: " + data + ", Stock carregado, Estado atualizado.")
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")
        while True:
            comando = input(">> ").strip()
            comando_lista = comando.split()

            match comando_lista[0]:
                case "LISTAR":
                    maquina.listar()
                
                case "MOEDA":
                    moedas = comando[6:].replace(".", "").split(",")  # Remove o ponto final e separa moedas
                    moedas = [m.strip() for m in moedas]  # Remove espaços extras
                    maquina.inserir_moedas(moedas)
                    saldo = maquina.verificar_saldo()
                    print(f"maq: Saldo = {int(saldo)}e{int((saldo * 100) % 100)}c")
                
                case "SAIR":
                    troco = maquina.devolver_troco()
                    if troco:
                        print("maq: Pode retirar o troco:", troco)
                    print("maq: Até à próxima!")
                    break
                
                case _:
                    print("maq: Comando inválido. Tente novamente.")

    



def main(argc, argv):
    if(argc < 2):
        print("USAGE: tpc5.py <stock_file>")
    elif argc == 2:
        start(argv[1])

    
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)