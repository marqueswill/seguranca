# %% [markdown]
# 1. Elaborar  os  códigos  para  realizar  a  cifra  por  deslocamento  e  a  respectiva
# decifração (dica: validar para cifra de César onde k=3);
#
# 2. Elaborar  os  códigos  que  quebram  a  cifra  por  deslocamento,  através  de  duas
# estratégias de ataques à cifra (CipherText-only):
#     - por ataque de força bruta;
#     - por distribuição de frequência;
#
# 3. Descrever a viabilidade das estratégias, comparar a complexidade dos algoritmos e
# tempo de execução, onde cada técnica seria melhor aplicada etc.

# %% [markdown]
# Utilização da lógica modular
#
# Considera a diferença de código ASCII dos caracteres maiúsculos e minúsculos
#
# Mantém a pontuação, mas não considera caracteres especiais (é,ã,Ç, etc.)


# %%
def shift_cipher(plain_text: str, k=3):
    letters = []
    for c in plain_text:
        letter_ascii = ord(c)
        if letter_ascii in range(65, 91):
            offset = 65

        if letter_ascii in range(95, 123):
            offset = 97

        letter_code = letter_ascii - offset
        if letter_code in range(26):
            shifted_letter = chr((letter_code + k) % 26 + offset)
            letters.append(shifted_letter)

        else:
            letters.append(c)

    cipher_text = "".join(letters)
    return cipher_text


plain_text_example = "Duas coisas são infinitas: o universo e a estupidez humana. Mas, em relação ao universo, ainda não tenho certeza absoluta."
shift_cipher(plain_text_example, 3)

# %% [markdown]
# Reutiliza o algoritmo de cifra, mas com o negativo da chave
# Desloca de volta


# %%
def shift_decipher(cipher_text: str, k=3):
    plain_text = shift_cipher(cipher_text, -k)
    return plain_text


cipher_text_exemple = "Gxdv frlvdv vãr lqilqlwdv: r xqlyhuvr h d hvwxslghc kxpdqd. Pdv, hp uhodçãr dr xqlyhuvr, dlqgd qãr whqkr fhuwhcd devroxwd."
shift_decipher(cipher_text_exemple, 3)

# %%
import nltk
from nltk.corpus import words
from langdetect import detect

nltk.download("words")

palavras_portugues = set(words.words())


def not_gibberish(text):
    palavras_no_texto = text.split()
    palavras_reais = [
        palavra
        for palavra in palavras_no_texto
        if palavra.lower() in palavras_portugues
    ]
    return len(palavras_reais) / max(len(palavras_no_texto), 1) > 0.5


# def not_gibberish(text):
#     try:
#         return detect(text) == "pt"
#     except:
#         return False


# break_shift_cipher_1(cipher_text_exemple)


# %%
def break_shift_cipher_1(cipher_text: str):
    for k in range(1, 26):
        plain_text = shift_decipher(cipher_text, k)
        if not_gibberish(plain_text):
            return k


break_shift_cipher_1(cipher_text_exemple)
