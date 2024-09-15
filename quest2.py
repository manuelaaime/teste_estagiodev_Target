strings = ["Manuela", "Musica", "Batata", "Bebida", "Gato"]

count_a = 0

for string in strings:
    count_a += string.count('a') + string.count('A')

exists_a = any('a' in string or 'A' in string for string in strings)

print(f"A letra 'a/A' aparece {count_a} vezes nas strings.")
