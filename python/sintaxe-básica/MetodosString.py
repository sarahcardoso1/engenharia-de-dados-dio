nome = "sArAH"

print(nome.upper())
print(nome.lower())
print(nome.title())

# ----------------eliminando espaços em branco 


texto = " Ola mundo      "

print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())


# ---------------- junçao e centralização

curso = "python"

print((curso.center(10, "*")).title())

print(".".join(curso))
