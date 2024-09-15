n = 10

t1, t2 = 0, 1

print("Sequência de Fibonacci com", n, "termos:")
print(t1, t2, end=", ")

for _ in range(3, n + 1):
    nextTerm = t1 + t2
    print(nextTerm, end=", ")
    t1, t2 = t2, nextTerm

