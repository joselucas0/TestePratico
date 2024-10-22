Aqui está o arquivo `README.md` em Markdown:

```markdown
# Desafio Técnico - Sequência de Fibonacci e Verificação de Letras

Este repositório contém a solução para dois problemas de lógica utilizando a linguagem Python.

## 1. Verificação de número na sequência de Fibonacci

### Descrição do problema

A sequência de Fibonacci é uma série de números onde o próximo número é sempre a soma dos dois anteriores, começando com 0 e 1. O desafio é verificar se um número informado pertence ou não à sequência de Fibonacci.

### Exemplo de sequência de Fibonacci

```plaintext
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
```

### Como funciona o código

O código percorre a sequência de Fibonacci, calculando cada novo valor até que o número informado seja encontrado ou ultrapassado. Se o número estiver na sequência, o programa retorna uma mensagem informando que o número pertence à sequência; caso contrário, ele retorna que o número não pertence.

### Código de exemplo

```python
def is_fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    if n in fib:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = 34
print(is_fibonacci(numero))
```

### Como executar

1. Clone o repositório.
2. Execute o script em Python com o número que deseja verificar.
3. A resposta será exibida no console, indicando se o número pertence ou não à sequência de Fibonacci.

---

## 2. Verificação da letra 'a' em uma string

### Descrição do problema

O segundo desafio é verificar se a letra 'a' (seja maiúscula ou minúscula) aparece em uma string e contar quantas vezes ela ocorre.

### Como funciona o código

O código converte a string para minúsculas e, em seguida, conta quantas vezes a letra 'a' aparece. Ele então retorna a quantidade encontrada.

### Código de exemplo

```python
def contar_a(string):
    count = string.lower().count('a')
    return f"A letra 'a' ocorre {count} vezes na string."

# Exemplo de uso:
string = "Amazônia"
print(contar_a(string))
```

### Como executar

1. Clone o repositório.
2. Execute o script em Python passando a string que deseja verificar.
3. A resposta será exibida no console, indicando quantas vezes a letra 'a' aparece na string.

---

## Requisitos

- Python 3.x
- Editor de texto ou IDE (ex: VSCode, PyCharm)

## Como rodar o projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/desafio-tecnico
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd desafio-tecnico
    ```

3. Execute os scripts Python:
    ```bash
    python fibonacci.py
    python verificar_a.py
    ```
