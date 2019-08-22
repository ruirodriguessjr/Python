#TuplasComTimesDeFutebol

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
		'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
     	'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
     	'Vasco', 'Sport Recife', 'América-MG', 'Vitória', 'Paraná')
print(f'==============================\nLista de times do Brasileirão: {times}')
print('==============================')
print(f'Os 5 primeiro colocados são: {times[0:5]}')
print('==============================')
print(f'Os 4 últimos são: {times[-4:]}')
print('==============================')
print(f'Times em ordem alfabética: {sorted(times)}')
print('==============================')
for c in range(0, len(times)):
	if times[c] == 'Chapecoense':
		print(f'A Chapecoense está na {c} posição.')
