# Métodos da Classe `str` em Python

Abaixo está uma lista de métodos disponíveis para objetos do tipo `str` (string) em Python, com uma breve descrição de cada um.

| Método         | Descrição |
|----------------|-----------|
| `capitalize()` | Converte o primeiro caractere para maiúsculo. |
| `casefold()`   | Converte a string para minúsculas de forma agressiva (útil para comparações). |
| `center()`     | Retorna a string centralizada em um campo de tamanho especificado. |
| `count()`      | Retorna o número de ocorrências de um valor específico na string. |
| `encode()`     | Retorna uma versão codificada da string (em bytes). |
| `endswith()`   | Retorna `True` se a string terminar com o valor especificado. |
| `expandtabs()` | Define o tamanho de tabulação da string. |
| `find()`       | Procura um valor na string e retorna a posição da primeira ocorrência. |
| `format()`     | Formata valores especificados dentro da string. |
| `format_map()` | Semelhante ao `format()`, mas utiliza um dicionário de mapeamento. |
| `index()`      | Igual ao `find()`, mas lança exceção se o valor não for encontrado. |
| `isalnum()`    | Retorna `True` se todos os caracteres forem alfanuméricos. |
| `isalpha()`    | Retorna `True` se todos os caracteres forem letras. |
| `isascii()`    | Retorna `True` se todos os caracteres forem ASCII. |
| `isdecimal()`  | Retorna `True` se todos os caracteres forem decimais. |
| `isdigit()`    | Retorna `True` se todos os caracteres forem dígitos. |
| `isidentifier()` | Retorna `True` se a string for um identificador válido. |
| `islower()`    | Retorna `True` se todos os caracteres forem minúsculos. |
| `isnumeric()`  | Retorna `True` se todos os caracteres forem numéricos. |
| `isprintable()`| Retorna `True` se todos os caracteres forem imprimíveis. |
| `isspace()`    | Retorna `True` se todos os caracteres forem espaços em branco. |
| `istitle()`    | Retorna `True` se a string estiver no formato de título. |
| `isupper()`    | Retorna `True` se todos os caracteres forem maiúsculos. |
| `join()`       | Junta elementos de um iterável, inserindo a string entre eles. |
| `ljust()`      | Retorna a string justificada à esquerda. |
| `lower()`      | Converte todos os caracteres para minúsculo. |
| `lstrip()`     | Remove espaços em branco à esquerda. |
| `maketrans()`  | Retorna uma tabela de tradução para ser usada com `translate()`. |
| `partition()`  | Divide a string em três partes com base em um separador. |
| `replace()`    | Substitui uma parte da string por outra. |
| `rfind()`      | Retorna a posição da última ocorrência de um valor. |
| `rindex()`     | Igual ao `rfind()`, mas lança exceção se o valor não for encontrado. |
| `rjust()`      | Retorna a string justificada à direita. |
| `rpartition()` | Divide a string em três partes com base na última ocorrência do separador. |
| `rsplit()`     | Divide a string da direita para a esquerda, com base em um separador. |
| `rstrip()`     | Remove espaços em branco à direita. |
| `split()`      | Divide a string com base em um separador. |
| `splitlines()` | Divide a string nas quebras de linha. |
| `startswith()` | Retorna `True` se a string começar com o valor especificado. |
| `strip()`      | Remove espaços em branco do início e do fim da string. |
| `swapcase()`   | Inverte as letras minúsculas e maiúsculas. |
| `title()`      | Coloca a primeira letra de cada palavra em maiúsculo. |
| `translate()`  | Retorna a string traduzida, conforme uma tabela de tradução. |
| `upper()`      | Converte todos os caracteres para maiúsculo. |
| `zfill()`      | Preenche a string com zeros à esquerda até atingir o tamanho especificado. |

---

📌 **Observação:** Todos esses métodos são **não destrutivos** — eles retornam uma nova string e não alteram a original, pois strings em Python são **imutáveis**.
