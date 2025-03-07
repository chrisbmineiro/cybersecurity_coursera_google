import itertools
import string

def brute_force(target_password, max_length=8):
    chars = string.ascii_letters + string.digits + string.punctuation  # Caracteres possíveis
    attempts = 0

    for length in range(1, max_length + 1):  # Tenta senhas de 1 a max_length caracteres
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)  # Combina os caracteres para formar a senha
            if guess == target_password:
                return f"Senha encontrada: {guess} (em {attempts} tentativas)"
            print(f"Tentativa {attempts}: {guess}")  # Mostra as tentativas (opcional)

    return "Senha não encontrada."

# Exemplo de uso
if __name__ == "__main__":
    target_password = input("Digite a senha alvo: ")  # Permite ao usuário inserir a senha
    max_length = int(input("Digite o comprimento máximo: "))  # Permite ao usuário definir o comprimento máximo
    if max_length < 1:
        print("O comprimento máximo deve ser pelo menos 1.")
    else:
        result = brute_force(target_password, max_length=max_length)
        print(result)