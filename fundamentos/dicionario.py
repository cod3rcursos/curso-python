# %%
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38,
          'cursos': ['Inglês', 'Português']}
type(pessoa)
dir(dict)
len(pessoa)

pessoa
pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]
# pessoa['tags']
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')
pessoa.get('tags')
pessoa.get('tags', [])

# %%
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa
pessoa.pop('idade')
pessoa
pessoa.update({'idade': 40, 'Sexo': 'M'})
pessoa
del pessoa['cursos']
pessoa
pessoa.clear()
pessoa
