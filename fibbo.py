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