# TPC4

Data: 03/03/2025 <br>
Nome: José Pedro Torres Vasconcelos <br>
Número Mecanográfico: A100763 <br> <br> <br>

![José Vasconcelos, A100763](/images/me.png)


<br>

## **Resumo**
Analisador léxico escrito em python, para uma liguagem de query com a qual se podem escrever frases do
género:

```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000

```



## **Resultados**

**Ficheiro de teste:** [query.txt](./query.txt)
<br>

**Utilização**
```
USAGE: python3 tpc4.py <query_file>
```
<br>

**Exemplo de utilização**
```
$ python3 tpc4.py query.txt

QUERY:
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000

('SELECT', 'select', 1, (0, 6))
('VARIABLE', '?nome', 1, (7, 12))
('VARIABLE', '?desc', 1, (13, 18))
('WHERE', 'where', 1, (19, 24))
('SYMBOL', '{', 1, (25, 26))
('VARIABLE', '?s', 2, (28, 30))
('IDENTIFIER', 'a', 2, (31, 32))
('IDENTIFIER', 'dbo:MusicalArtist', 2, (33, 50))
('SYMBOL', '.', 2, (50, 51))
('VARIABLE', '?s', 3, (53, 55))
('IDENTIFIER', 'foaf:name', 3, (56, 65))
('STRING', '"Chuck Berry"', 3, (66, 79))
('LANG_TAG', '@en', 3, (79, 82))
('SYMBOL', '.', 3, (83, 84))
('VARIABLE', '?w', 4, (86, 88))
('IDENTIFIER', 'dbo:artist', 4, (89, 99))
('VARIABLE', '?s', 4, (100, 102))
('SYMBOL', '.', 4, (102, 103))
('VARIABLE', '?w', 5, (105, 107))
('IDENTIFIER', 'foaf:name', 5, (108, 117))
('VARIABLE', '?nome', 5, (118, 123))
('SYMBOL', '.', 5, (123, 124))
('VARIABLE', '?w', 6, (126, 128))
('IDENTIFIER', 'dbo:abstract', 6, (129, 141))
('VARIABLE', '?desc', 6, (142, 147))
('SYMBOL', '}', 7, (148, 149))
('LIMIT', 'LIMIT', 7, (150, 155))
('NUMBER', 1000, 7, (156, 160))
```

