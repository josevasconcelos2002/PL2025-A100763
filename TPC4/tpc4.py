import sys
import re

def tokenize(code):
    token_specification = [
        ('SELECT',   r'\bselect\b'),
        ('WHERE',    r'\bwhere\b'),
        ('LIMIT',    r'\bLIMIT\b'),
        ('VARIABLE', r'\?[a-zA-Z_][a-zA-Z0-9_]*'),
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_:]*'),
        ('NUMBER',   r'\d+'),
        ('STRING',   r'"[^"]*"'),
        ('LANG_TAG', r'@[a-zA-Z]+'),
        ('SYMBOL',   r'[{}().]'),
        ('COMPARATOR', r'[<>]'),
        ('DOT',      r'\.'),
        ('NEWLINE',  r'\n'),
        ('SKIP',     r'[ \t]+'),
        ('ERRO',     r'.'),
    ]
    
    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    
    for m in mo:
        dic = m.groupdict()
        
        if dic['SELECT'] is not None:
            t = ('SELECT', 'select', linha, m.span())
            
        elif dic['WHERE'] is not None:
            t = ('WHERE', 'where', linha, m.span())
            
        elif dic['LIMIT'] is not None:
            t = ('LIMIT', 'LIMIT', linha, m.span())
            
        elif dic['VARIABLE'] is not None:
            t = ('VARIABLE', dic['VARIABLE'], linha, m.span())
            
        elif dic['IDENTIFIER'] is not None:
            t = ('IDENTIFIER', dic['IDENTIFIER'], linha, m.span())
            
        elif dic['NUMBER'] is not None:
            t = ('NUMBER', int(dic['NUMBER']), linha, m.span())
            
        elif dic['STRING'] is not None:
            t = ('STRING', dic['STRING'], linha, m.span())
            
        elif dic['LANG_TAG'] is not None:
            t = ('LANG_TAG', dic['LANG_TAG'], linha, m.span())
            
        elif dic['SYMBOL'] is not None:
            t = ('SYMBOL', dic['SYMBOL'], linha, m.span())
            
        elif dic['COMPARATOR'] is not None:
            t = ('COMPARATOR', dic['COMPARATOR'], linha, m.span())
            
        elif dic['DOT'] is not None:
            t = ('DOT', dic['DOT'], linha, m.span())
            
        elif dic['NEWLINE'] is not None:
            linha += 1
            continue
        
        elif dic['SKIP'] is not None:
            continue
        
        else:
            t = ('ERRO', m.group(), linha, m.span())
        
        reconhecidos.append(t)
    
    return reconhecidos



def main(argc, argv):
    if(argc < 2):
        print("USAGE: tpc4.py <query_file>")
    
    elif(argc == 2):
        file_path = argv[1]
        try:
            with open(file_path, "r") as file:
                query = file.read()
                print("\nQUERY: \n" + query + "\n")
                tokens = tokenize(query)
                for token in tokens:
                    print(token)
                    
        except FileNotFoundError:
            print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    
    
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)