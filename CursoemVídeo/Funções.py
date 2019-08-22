'''A diferença entre Funções X Métodos, é que em função, nós definimos uma instrução,
onde toda vez que eu precisar ultilizar ela eu a chamo e ela executa o meu comando,
como se fosse um procedimento invocado. Sempre meus parâmetros serão invocados no
começo da função, sendo obrigatório estabelecer o objeto de cada parametro da função.
Ja os métodos, nós definimos os parâmetros e ele após executar o bloco de comando,
 ele da continuidade ao programa.
'''
def minha_func():
    print('Só funciona se eu chamar a função, senão ele retorna 0.')
minha_func()
'''Quando utilizamos uma função quer dizer que definimos uma lista de parâmetros que deve ser passado.
Já quando invocamos essa função nós iremos dizer os argumentos que iremos passar para a função.
Ou seja, Cabeçalho da Função = Parâmetros... Rodapé da Função = Argumentos.'''
print()
def soma(x, y):
    total = x + y
    print('O total da soma é:{}'.format(total))

soma(10, 50)
'''Existe a maneira de fazer a atribuição dos parâmetros da função no início da função,
quando eu faço isso no argumento, não necessito colocar meus parâmetros, pois eles já estão 
préestabelecidos, e vão ser impressos no meu bloco de comando. 
Lembrando que eles não podem ser alterados de maneira que atrapalhe na sua ordem de impressão,
pois todo parâmetro declarado, na hora de chamar a função ela imprimirá na ordem pré estabelecida.'''
def login(sistema = input('Qual o sistema usado: '), usuario = 'Rui', senha = 'Maria210806'):
    print('O sistema usado é:{}'.format(sistema))
    print('Usuário:{}'.format(usuario))
    print('Senha:{}'.format(senha))
login()
'''Argumentos Posicionais = Quando denominamos os parâmetros dentro de uma tupla, 
eles ficam com posições fixas e imutáveis.
Argumentos Nomeados = Já é como nos dicionários,
enviamos os parâmetros com o valor pré estabelecidos.'''
def dados_pessoais(nome, sobrenome, idade, sexo):
    print('Nome:{}\nSobrenome:{}\nIdade:{}\nSexo:{}'.format(nome, sobrenome, idade, sexo))
#Passando a função como Argumento Posicional.
dados_pessoais('Rui', 'Rodrigues', '30', 'Masculino')
#Se eu inverter os dados dentro da invocação da função ficará embaralhado,
#Por isso tenho que deixar meus parâmetros alinhados com as posições digitadas.
dados_pessoais('30', 'masculino', 'Rui', 'Rodrigues')
print()
#Já na função nomeada, não interessa minha ordem pois eu estou associando o nome ao parâmetro.
dados_pessoais(nome='Rui', sobrenome='Rodrigues', idade='30', sexo='Masculino')
print()
#Passando a função como Argumento Nomeado.
dados_pessoais(sobrenome='Rodrigues', nome='Rui', sexo='Masculino', idade='30')
'''Se quiser eu posso nomear parâmetros posicionais e nomeados na mesma função,
poré à partir do momento que eu nomear o primeiro nomeado, 
todos os demais terão que ser nomeados também.'''

#RETORNANDO VALORES
def soma(x, y):
    num = x * y
    return num
print(soma(10, 20))
'''QUANDO MINHA FUNÇÃO RECEBE O RETURN, SIGNIFICA QUE ELA FOI FINALIZADA
E NÃO IRÁ MAIS EXIBIR O BLOCO DE COMANDOS, VAI RETORNAR AO VALOR SOLICITADO E TERMINARÁ.'''

#RETORNANDO VALORES MULTIPLOS

def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado, cubo
q, c = potencia(2)
print(q)
print(c)

'''QUANDO FAZEMOS MULTIPLOS RETORNOS ASSOCIAMOS AS VARIAVEIS DENTRO DO BLOCO DE COMANDOS
DA FUNÇÃO E DEPOIS ASSOCIAMOS ELAS A OUTRAS VARIAVEIS TORNANDO ELAS ATRIBUIDAS A MINHA FUNÇÃO'''

#FUNÇÃO VARIADICA
'''É TODA A FUNÇÃO CAPAZ DE RECEBER VÁRIOS VALORES COMO PARÂMETROS,
OU SEJA quando não sbemos a quantidade que vamos usar,
usamos (*args) e (**kwargs) PODEndo RECEBER DE 0 ATÉ N PARÂMETROS.'''

def lista_de_argumentos(*args):
    print(args)
def lista_de_argumentos_assossiativos(**kwargs):
    print(kwargs)
def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos('um','dois','três','quatro')
'''Tipo Tupla'''
lista_de_argumentos_assossiativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_assossiativos(um=1, dois=2, tres=3, quatro=4)
'''Tipo Dicionário'''
argumentos(1,2,3,4,5,6,um=1,dois=2,tres=3,quatro=4)
'''Tupla e Dicionário juntas, com posicional e nomeado sendo representado por parâmetros
descriminados no cabeçalho da minha função.'''