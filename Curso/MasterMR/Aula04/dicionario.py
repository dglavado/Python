dados = {
    'id123': #Chave única - Se inserir novamente, o dicionário substitui
    {
            'nome': 'Maricio Ribeiro',
            'empresa': 'Master MR',
            'tels':
            {
                'cel': 11999999999,
                'fixo': 1145612345
            }

    },
    'id124':
    {
        'nome': 'Mauricio',
        'empresa': 'Chesf',
        'tels':
        {
            'cel': 11999999998,
            'fixo': 1145612346
        }

    }
}

print(dados['id123'])
print(dados['id123']['empresa'])
print(dados['id123']['tels'])
print(dados['id123']['tels']['fixo'])

#Estrutura igual do JSON
#{'nome': 'Maricio Ribeiro', 'empresa': 'Master MR', 'tels': {'cel': 11999999999, 'fixo': 1145612345}}
#Master MR
#{'cel': 11999999999, 'fixo': 1145612345}
#1145612345

dados = dict()

pessoa = dict()
pessoa['nome'] = 'Marcio Ribeiro'
pessoa['empresa'] = 'Master MR'
pessoa['tels'] = {'cel': 11999999999, 'fixo': 1145612345 }

dados['id123'] = pessoa

pessoa = dict()
pessoa['nome'] = 'Mauricio'
pessoa['empresa'] = 'Chesf'
pessoa['tels'] = {'cel': 11999999998, 'fixo': 1145612346 }

dados['id124'] = pessoa

#dados['id125'] - erro

pessoa = dados.get('id123', 'id não encontrado')
pessoa = dados.get('id125', 'id não encontrado')

print(dados.get('id125', 'id não encontrado')) #get não dá erro e pode colocar mensagem caso não econtre

for pessoa in dados.values():
    print(pessoa)


for id in dados.keys():
    print(id)


for id, pessoa in dados.items():
    print(id)
    print(pessoa)


print('Fim')