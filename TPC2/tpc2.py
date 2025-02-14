
def csv_parser(ficheiro):
    obras_dic = {}
    f = open(ficheiro, "r", encoding="utf-8")
    j = 0
    
    for line in f:
        
        if j == 0:
            j += 1
            continue
        
        linha = line.strip()
        information = linha.split(";")
        for i in range(len(information)):
            information[i] = information[i].strip()
        print(len(information))
        
        obra = {}
        nome = information[0]
        obra["desc"] = information[1]
        obra["anoCriacao"] = information[2]
        obra["periodo"] = information[3]
        
        name = information[4].replace(",", "")
        obra["compositor"] = name
        obra["duracao"] = information[5]
        
        obras_dic[nome] = obra
        j += 1
        
    f.close()
    
    return obras_dic


def main():
    obras_dic = csv_parser("./assets/obras.csv")
    print(obras_dic)
    
main()