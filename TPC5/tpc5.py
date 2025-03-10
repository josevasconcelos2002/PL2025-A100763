import sys
from Maquina_Vending import Maquina_Vending
import json

def start(stock_file):
        
    stock = {}
    with open(stock_file, 'r') as f:
        data = json.load(f)

    stock = data["stock"]
        
    maquina = Maquina_Vending()
    maquina.set_stock(stock)
    maquina.ver_stock()
    



def main(argc, argv):
    if(argc < 2):
        print("USAGE: tpc5.py <stock_file>")
    elif argc == 2:
        start(argv[1])

    
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)