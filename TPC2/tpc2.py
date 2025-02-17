def split_csv_line(line):
    
    fields = []
    field = ""
    inside_quotes = False
    i = 0

    while i < len(line):
        char = line[i]

        if char == '"' and (i + 1 < len(line) and line[i + 1] == '"'):  
            # Dupla aspas dentro de um campo: mantém uma aspas e avança
            field += '"'
            i += 1  
        elif char == '"':
            # Alterna entre dentro e fora de aspas
            inside_quotes = not inside_quotes
        elif char == ";" and not inside_quotes:
            # Encontramos `;` fora das aspas, finalizamos um campo
            fields.append(field.strip())
            field = ""
        else:
            # Adicionamos o caractere ao campo atual
            field += char
        
        i += 1

    # Adiciona o último campo
    fields.append(field.strip())

    return fields



def csv_parser(ficheiro):
    obras_dic = {}
    
    with open(ficheiro, "r", encoding="utf-8") as f:
        j = 0
        linha_atual = ""

        for line in f:
            if j == 0:
                j += 1
                continue
            linha_atual += line.strip()

            
            if linha_atual.count('"') % 2 == 0:
                information = split_csv_line(linha_atual)

                # Garantir que a lista tenha exatamente 7 elementos
                information += [""] * (7 - len(information))

                nome = information[0].strip()
                obra = {
                    "desc": information[1].strip(),
                    "anoCriacao": information[2].strip(),
                    "periodo": information[3].strip(),
                    "compositor": information[4].strip(),
                    "duracao": information[5].strip(),
                    "id": information[6].strip()
                }

                obras_dic[nome] = obra
                j += 1
                linha_atual = ""  # Reseta a linha acumulada

    return obras_dic



def lista_compositores(obras_dic):
    compositores = set()

    for obra in obras_dic.values():
        compositor = obra.get("compositor", "").strip()
        if compositor:
            
            if "," in compositor:
                partes = compositor.split(",", 1) 
                compositor = partes[1].strip() + " " + partes[0].strip()  

            compositores.add(compositor)

    return sorted(compositores)


def nr_obras_por_periodo(obras_dic):
    dic = {}
    for obra in obras_dic.values():
        periodo = obra.get("periodo", "").strip()
        if periodo:
            if periodo not in dic:
                dic[periodo] = 0
            dic[periodo] += 1
    return dic

def obras_por_periodo(obras_dic):
    dic = {}
    for nome, obra in obras_dic.items():
        periodo = obra.get("periodo", "").strip()
        if periodo:
            if periodo not in dic:
                dic[periodo] = []
            dic[periodo].append(nome)
    return dic



def main():
    obras_dic = csv_parser("./assets/obras.csv")
    #lista_compositores_ordenada = lista_compositores(obras_dic)
    #print(lista_compositores_ordenada)
    #n_obras_por_periodo = nr_obras_por_periodo(obras_dic)
    #print(n_obras_por_periodo)
    obras_por_periodo_dic = obras_por_periodo(obras_dic)
    print(obras_por_periodo_dic)

main()
