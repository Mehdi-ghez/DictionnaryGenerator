from itertools import product

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
length = 5

def generate_words():
    for word in product(alphabet, repeat=length):
        yield ''.join(word)

# Exemple d'utilisation :
with open("generated_words.txt", "w") as file:
    for word in generate_words():
        file.write(word + "\n")

print("Génération terminée. Les mots sont enregistrés dans 'generated_words.txt'.")
