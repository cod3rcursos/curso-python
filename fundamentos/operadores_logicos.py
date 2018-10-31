# %%
True or False
7 != 3 and 2 > 3

# Tabela verdade do AND
True and True
True and False
False and True
False and False
True and True and False and True and True and True

# Tabela verdade do OR
True or True
True or False
False or True
False or False
False or False or True or False or False or False

# Tabela verdade do XOR
# True != True
# True != False
# False != True
# False != False

# Operador de Negação (unário)
not True
not False

not 0
not 1
not not -1
not not True

# Cuidado!
True & False
False | True
True ^ False

# AND Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 10
3 & 2

# OR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 11
3 | 2

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 01
3 ^ 2

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
meta

# %%
# Desafio Operadores Lógicos

# Os Trabalhos
trabalho_terca = False
trabalho_quinta = False

"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # xor
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))

# "{}, {} = {}".format(1, False, 'resultado')
