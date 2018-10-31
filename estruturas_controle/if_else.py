# Conceitos   Notas
# A           De 10,0 à 9,1
# A-          De 9,0 à 8,1
# B           De 8,0 à 7,1
# B-          De 7,0 à 6,1
# C           De 6,0 à 5,1
# C-          De 5,0 à 4,1
# D           De 4,0 à 3,1
# D-          De 3,0 à 2,1
# E           De 2,0 à 1,1
# E-          De 1,0 à 0,0

# *Para notas maiores que 10 e menores que 0 será impresso "Nota inválida"
valor_informado = input('Nota do aluno: ')
nota = float(valor_informado)

if nota > 10:
    print('Nota inválida')
elif nota >= 9.1:
    print('A')
elif nota >= 8.1:
    print('A-')
elif nota >= 7.1:
    print('B')
elif nota >= 6.1:
    print('B-')
elif nota >= 5.1:
    print('C')
elif nota >= 4.1:
    print('C-')
elif nota >= 3.1:
    print('D')
elif nota >= 2.1:
    print('D-')
elif nota >= 1.1:
    print('E')
elif nota >= 0:
    print('E-')
else:
    print('Nota inválida')
