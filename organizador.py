import unicodedata

def normalizar(texto):
    """Nomraliza o texto em minúsculo e sem acentos"""
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    resultado =  " "
    for letra in texto:
        if unicodedata.combining(letra) == 0:
            resultado += letra
    return resultado


print (normalizar("textos_exemplô1"))

regras = [
    {"pasta": "Curriculos", "palavras": ["curriculo", "cv"]},
    {"pasta": "Documentacoes", "palavras": ["python", "c++", "c#", "c", "java", "javascript"]},
    {"pasta": "FIAP/ProjetoX", "palavras": ["projetox"]},
    {"pasta": "FIAP", "palavras": ["fiap"]},
]