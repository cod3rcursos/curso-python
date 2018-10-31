# %%
esta_chuvendo = False

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chuvendo])
print('Hoje estou com as roupas ' + 
      ('molhadas.' if esta_chuvendo else 'secas.'))
