def dias_semana(n):
    return {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }.get(n, 'Dia inválido!')


# def dias_semana(n):
#     if n > 7 or n < 1:
#         return 'Dia inválido!'
#     return ['Domingo', 'Segunda', 'Terça', 'Quarta',
#             'Quinta', 'Sexta', 'Sábado'][n-1]

print(dias_semana(3))
print(dias_semana(0))
print(dias_semana(7))
