from time import sleep
print("-"*100)
print("-"*40,"SEJA BEM-VINDO AO","-"*41)
print("-"*40,"QUIZ MENTE VERDE","-"*41)
print("-"*100)

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
escola = str(input('Digite o nome da sua escola: '))
serie = int(input('Digite sua série: '))
print()
print(f'Olá, {nome}!\nVamos Começar!')
print()

perguntas = {
   '\033[33m1ªPergunta\033[m': {
       'pergunta': 'O que é reciclagem? ',
       'respostas': {'1': 'Jogar fora o lixo produzido.', '2': 'Coletar todo o tipo de material existente em lixos '
                     'recicláveis.', '3': 'Nome dado para todo o processo após descarte.', '4': 'Processo de '
                     'transformação de materiais usados em novos produtos para consumo.'},
       'correta': '4',

   },


   '\033[33m2ª Pergunta\033[m': {
       'pergunta': 'Como separar corretamente o lixo? ',
       'respostas': {'1': 'Juntar tudo na lixeira, pois os materiais já fazem o trabalho de separação.', '2':
                     'Separar o lixo orgânico(restos de alimentos, papel sujo e lixo sanitário)dos resíduos.',
                     '3': 'Deixar plásticos sujos juntos com lixo orgânico.', '4':'Juntar todo tipo de lixo e '
                     'descartar no ponto de coleta.'},
       'correta': '2',

   },

   '\033[33m3ª Pergunta\033[m': {
       'pergunta': 'O que é coleta seletiva? ',
       'respostas': {'1': 'Processo de coleta e coleta de resíduos para reaproveitamento por meio de reciclagem.', '2':
                     'Destinação de resíduos para lixões e aterros.', '3': 'Processo de envio de todo o lixo '
                     'produzido para cooperativas ou entrega para catadores de rua.', '4': 'A escolha aleatória do '
                     'melhor lixo produzido.'},
       'correta': '1',

   },

   '\033[33m4ª Pergunta\033[m': {
       'pergunta': 'O que fazer com o lixo eletrônico - pilhas, baterias e equipamentos quebrados? ',
       'respostas': {'1': 'Recolher, organizar e armazenar em casa ou no máximo o tempo que der.', '2':
                          'Juntar com plásticos e metais.', '3': 'Jogar no lixo comum.', '4': 'Procure locais '
                          'específicos para seu descarte.'},
                          'correta': '4',
   },

   '\033[33m5ª Pergunta\033[m': {
       'pergunta': 'Uma das formas de colaborar com a preservação do meio ambiente é reduzir a produção de resíduos.'
                   ' Mas como? ',
       'respostas': {'1': 'Optando pela compra de produtos com embalagens recicláveis.', '2': 'Reutilizando os'
                     ' materiais e objetos sempre que possível.', '3': 'Apoiando iniciativas de reciclagem.', '4':
                     'Todas as anteriores. '},
       'correta': '4',
   },

   '\033[33m6ª Pergunta\033[m': {
       'pergunta': 'Como consumir de forma consciente? ',
       'respostas': {'1': 'Trocando todos os nossos objetos sempre que um novo do mesmo tipo for lançado.', '2':
                     'Usar a mangueira para lavar o quintal e o carro.', '3': 'Utilizando os recursos naturais para'
                     ' satisfazer nossas necessidades e das gerações futuras.', '4': 'Adquirindo qualquer tipo de '
                     'produto se for barato.'},
       'correta': '3',

   },

   '\033[33m7ª Pergunta\033[m': {
       'pergunta': 'Como preservar árvores e florestas? ',
       'respostas': {'1': 'Construindo uma casa na árvore.', '2': 'Reciclando papéis, jornais e revistas.', '3':
                     'Reutilizando metais e vidros.', '4': 'Indo em parques.'},
       'correta': '2',

   },

   '\033[33m8ª Pergunta\033[m': {
       'pergunta': 'Qual dos gases abaixo não é conhecido como um dos gases do efeito estufa (GEE)?',
       'respostas': {'1': 'N2O – óxido nitroso.', '2': 'O2 – oxigênio.', '3': 'CO2 – dióxido de carbono ou gás '
                     'carbônico.', '4': 'CH4 – metano.'},
       'correta': '2',

   },

   '\033[33m9ª Pergunta\033[m': {
       'pergunta': 'Qual dos elementos abaixo não é utilizado como fonte de energia?',
       'respostas': {'1': 'Água corrente.', '2': 'Petróleo.', '3': 'Barra de ferro.', '4': 'Sol.'},
       'correta': '3',

   },

  '\033[33m10ª Pergunta\033[m': {
       'pergunta': 'Qual alternativa apresenta uma vantagem da energia solar?',
       'respostas': {'1': 'Não polui.', '2': 'Não é renovável.', '3': 'É eficaz em qualquer clima.', '4': 'É '
       'disponível a todo momento.'},
       'correta': '1',

   },
}

corretas = 0
for pk, pv in perguntas.items():
   print(f'{pk}: {pv["pergunta"]}')
   print('Respostas: ')
   for rk, rv in pv['respostas'].items():
       print(f'{rk}: {rv}')

   ru = input('Digite sua resposta: ')
   while ru >= '5':
       print('Opção Invalida, responda de 1 a 4')
       ru = input("Qual a opção correta? ")
   if ru == pv['correta']:
    print('\033[34mParabéns você acertou!\033[m')
    corretas += 1
   else:
       print(f'\033[31mVocê errou! A resposta correta é: {pv["correta"]}\033[m')
conf = str(input("Aperte qualquer tecla para ver sua pontuação!"))

print()
print('\033[7;37;40mSua pontuação...\033[m')
print()
sleep(1)
print('-' * 67)
if corretas >= 7 and corretas <= 10:
    print(f'\033[34mPARABÉNS {nome}, Acertou {corretas}. Você entende tudo de SUSTENTABILIDADE.\033[m ')
elif corretas >= 4 and corretas <= 6:
   print(f'\033[32mVOCÊ TEM UM BOM CONHECIMENTO, {nome}, ACERTOU {corretas}, MAS PODE MELHORAR.\033[m')
elif corretas <= 3:
   print(f'\033[33mPRECISA ADIQUIRIR MAIS CONHECIMENTO. TREINE MAIS. Foram {corretas} acertos.\033[m')
   print('-' * 67)

dec = input('Se quiser repetir? Digite 1[SIM] / 2[NÃO]')
while dec == '1':
    print("-"*100)
    print("-"*40,"SEJA BEM-VINDO AO","-"*41)
    print("-"*40,"QUIZ MENTE VERDE","-"*41)
    print("-"*100)

    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    escola = str(input('Digite o nome da sua escola: '))
    serie = int(input('Digite sua série: '))
    print()
    print(f'Olá, {nome}!\nVamos Começar!')
    print()

    perguntas = {
       '\033[33m1ªPergunta\033[m': {
           'pergunta': 'O que é reciclagem? ',
           'respostas': {'1': 'Jogar fora o lixo produzido.', '2': 'Coletar todo o tipo de material existente em lixos '
                         'recicláveis.', '3': 'Nome dado para todo o processo após descarte.', '4': 'Processo de '
                         'transformação de materiais usados em novos produtos para consumo.'},
           'correta': '4',

       },


       '\033[33m2ª Pergunta\033[m': {
           'pergunta': 'Como separar corretamente o lixo? ',
           'respostas': {'1': 'Juntar tudo na lixeira, pois os materiais já fazem o trabalho de separação.', '2':
                         'Separar o lixo orgânico(restos de alimentos, papel sujo e lixo sanitário)dos resíduos.',
                         '3': 'Deixar plásticos sujos juntos com lixo orgânico.', '4':'Juntar todo tipo de lixo e '
                         'descartar no ponto de coleta.'},
           'correta': '2',

       },

       '\033[33m3ª Pergunta\033[m': {
           'pergunta': 'O que é coleta seletiva? ',
           'respostas': {'1': 'Processo de coleta e coleta de resíduos para reaproveitamento por meio de reciclagem.', '2':
                         'Destinação de resíduos para lixões e aterros.', '3': 'Processo de envio de todo o lixo '
                         'produzido para cooperativas ou entrega para catadores de rua.', '4': 'A escolha aleatória do '
                         'melhor lixo produzido.'},
           'correta': '1',

       },

       '\033[33m4ª Pergunta\033[m': {
           'pergunta': 'O que fazer com o lixo eletrônico - pilhas, baterias e equipamentos quebrados? ',
           'respostas': {'1': 'Recolher, organizar e armazenar em casa ou no máximo o tempo que der.', '2':
                              'Juntar com plásticos e metais.', '3': 'Jogar no lixo comum.', '4': 'Procure locais '
                              'específicos para seu descarte.'},
                              'correta': '4',
       },

       '\033[33m5ª Pergunta\033[m': {
           'pergunta': 'Uma das formas de colaborar com a preservação do meio ambiente é reduzir a produção de resíduos.'
                       ' Mas como? ',
           'respostas': {'1': 'Optando pela compra de produtos com embalagens recicláveis.', '2': 'Reutilizando os'
                         ' materiais e objetos sempre que possível.', '3': 'Apoiando iniciativas de reciclagem.', '4':
                         'Todas as anteriores. '},
           'correta': '4',
       },

       '\033[33m6ª Pergunta\033[m': {
           'pergunta': 'Como consumir de forma consciente? ',
           'respostas': {'1': 'Trocando todos os nossos objetos sempre que um novo do mesmo tipo for lançado.', '2':
                         'Usar a mangueira para lavar o quintal e o carro.', '3': 'Utilizando os recursos naturais para'
                         ' satisfazer nossas necessidades e das gerações futuras.', '4': 'Adquirindo qualquer tipo de '
                         'produto se for barato.'},
           'correta': '3',

       },

       '\033[33m7ª Pergunta\033[m': {
           'pergunta': 'Como preservar árvores e florestas? ',
           'respostas': {'1': 'Construindo uma casa na árvore.', '2': 'Reciclando papéis, jornais e revistas.', '3':
                         'Reutilizando metais e vidros.', '4': 'Indo em parques.'},
           'correta': '2',

       },

       '\033[33m8ª Pergunta\033[m': {
           'pergunta': 'Qual dos gases abaixo não é conhecido como um dos gases do efeito estufa (GEE)?',
           'respostas': {'1': 'N2O – óxido nitroso.', '2': 'O2 – oxigênio.', '3': 'CO2 – dióxido de carbono ou gás '
                         'carbônico.', '4': 'CH4 – metano.'},
           'correta': '2',

       },

       '\033[33m9ª Pergunta\033[m': {
           'pergunta': 'Qual dos elementos abaixo não é utilizado como fonte de energia?',
           'respostas': {'1': 'Água corrente.', '2': 'Petróleo.', '3': 'Barra de ferro.', '4': 'Sol.'},
           'correta': '3',

       },

      '\033[33m10ª Pergunta\033[m': {
           'pergunta': 'Qual alternativa apresenta uma vantagem da energia solar?',
           'respostas': {'1': 'Não polui.', '2': 'Não é renovável.', '3': 'É eficaz em qualquer clima.', '4': 'É '
           'disponível a todo momento.'},
           'correta': '1',

       },
    }

    corretas = 0
    for pk, pv in perguntas.items():
       print(f'{pk}: {pv["pergunta"]}')
       print('Respostas: ')
       for rk, rv in pv['respostas'].items():
           print(f'{rk}: {rv}')

       ru = input('Digite sua resposta: ')
       while ru >= '5':
           print('Opção Invalida, responda de 1 a 4')
           ru = input("Qual a opção correta? ")
       if ru == pv['correta']:
        print('\033[34mParabéns você acertou!\033[m')
        corretas += 1
       else:
           print(f'\033[31mVocê errou! A resposta correta é: {pv["correta"]}\033[m')
    conf = str(input("Aperte qualquer tecla para ver sua pontuação!"))

    print()
    print('\033[7;37;40mSua pontuação...\033[m')
    print()
    sleep(3)

    print('-' * 67)
    if corretas >= 7 and corretas <= 10:
       print(f'\033[34mPARABÉNS {nome}, Acertou {corretas}. Você entende tudo de SUSTENTABILIDADE.\033[m ')
    elif corretas >= 4 and corretas <= 6:
       print(f'\033[32mVOCÊ TEM UM BOM CONHECIMENTO, {nome}, ACERTOU {corretas}, MAS PODE MELHORAR.\033[m')
    elif corretas <= 3:
       print(f'\033[33mPRECISA ADIQUIRIR MAIS CONHECIMENTO. TREINE MAIS. Foram {corretas} acertos.\033[m')
    print('-' * 67)
print('Obrigado')