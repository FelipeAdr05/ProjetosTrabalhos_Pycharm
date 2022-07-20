# Função Filter joga fora tudo aquilo que é considerado Falso para uma certa análise

x = [1, 2, 5, 8, 9, 4, 7, 11, 45, 6]

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

f = list(filter(par, x))

print(f)


