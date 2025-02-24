# TPC3

Data: 24/02/2025 <br>
Nome: José Pedro Torres Vasconcelos <br>
Número Mecanográfico: A100763 <br> <br> <br>

![José Vasconcelos, A100763](/images/me.png)


<br>

## **Resumo**
Programa escrito em python, responsável por converter MarkDown para HTML, mais especificamente, os seguintes elementos:

* **Cabeçalhos**: linhas iniciadas por "# texto", ou "## texto" ou "### texto";

* **Bold**: pedaços de texto entre "**";

* **Itálico**: pedaços de texto entre "*";

* **Lista numerada**;

* **Link**: "[texto](endereço URL)";

* **Imagem**: "![texto alternativo](path para a imagem)".

## **Resultados**

### [Ficheiro de teste](./test.md)

```
# Título Principal
## Subtítulo
### Cabeçalho Menor

Texto normal com **negrito** e *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Veja [Google](https://www.google.com).

Imagem: <img src="#" alt="Exemplo"/>
```

### Resultado
```
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
<h3>Cabeçalho Menor</h3>

Texto normal com <b>negrito</b> e <i>itálico</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

Veja <a href="https://www.google.com">Google</a>.

Imagem: <img src="#" alt="Exemplo"/>
```
