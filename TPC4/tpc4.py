import re
from typing import List, Tuple

# Definição de tokens
TOKENS = [
    (r'\bselect\b', 'SELECT'),
    (r'\bwhere\b', 'WHERE'),
    (r'\bLIMIT\b', 'LIMIT'),
    (r'\?[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE'),  # Captura variáveis corretamente
    (r'[a-zA-Z_][a-zA-Z0-9_:]*', 'IDENTIFIER'),
    (r'[0-9]+', 'NUMBER'),
    (r'"[^"]*"', 'STRING'),
    (r'@[a-zA-Z]+', 'LANG_TAG'),
    (r'[{}().]', 'SYMBOL'),
    (r'[<>]', 'COMPARATOR'),
    (r'\.', 'DOT'),
    (r'\s+', 'WHITESPACE')
]

class Lexer:
    def __init__(self, query: str):
        self.query = query
        self.tokens = []

    def tokenize(self) -> List[Tuple[str, str]]:
        """Tokeniza a string de entrada."""
        pos = 0
        while pos < len(self.query):
            match = None
            for pattern, tag in TOKENS:
                regex = re.compile(pattern)
                match = regex.match(self.query, pos)
                if match:
                    token_value = match.group(0)
                    if tag != 'WHITESPACE':  # Ignora espaços em branco
                        self.tokens.append((token_value, tag))
                    pos = match.end()
                    break
            if not match:
                raise SyntaxError(f'Caractere inesperado: {self.query[pos]}')
        return self.tokens

# Exemplo de uso:
query = """
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
"""

lexer = Lexer(query)
tokens = lexer.tokenize()
for token in tokens:
    print(token)