# Exercicio 1

def soma_digitos(nome_ficheiro):
    soma = 0
    on = False
    ficheiro = open(nome_ficheiro)

    for linha in ficheiro:
        linha = linha.strip()  # Remove espaços e '\n'
        palavras = linha.split(" ")
        palavra_aux = ""

        for palavra in palavras:
            if has_off(palavra):
                on = False
                print("OFF")
            elif has_on(palavra):
                on = True
                print("ON")
            
            # Verifica se há "=" na palavra e imprime a soma parcial
            for _ in range(nr_equals(palavra)):
                print("Soma:", soma)

            for caracter in palavra:
                if on and caracter.isdigit():
                    palavra_aux += caracter
                else:
                    if on and palavra_aux:
                        soma += int(palavra_aux)
                        palavra_aux = ""

            if on and palavra_aux:
                soma += int(palavra_aux)
                palavra_aux = ""

    ficheiro.close()

# Exercicio 2

def has_off(word):
    return "off" in word.lower()

# Exercicio 3

def has_on(word):
    return "on" in word.lower()


# Exercicio 4

def nr_equals(word):
    nr = 0
    for char in word:
        if char == "=":
            nr += 1
    return nr




def main():
    soma_digitos("./testes/teste1.txt")

main()
