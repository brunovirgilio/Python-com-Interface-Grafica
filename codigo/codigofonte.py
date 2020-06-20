from tkinter import *

c = 0

janela = Tk()
janela.title('QUIZ MENTE VERDE')

def result():
    global c
    q10 = int(en14.get())
    if q10 == 1:
        c += 1
        if 7 <= c <= 10:
            lb69['text'] = "VOCÊ ACERTOU {} QUESTÕES. PARABÉNS VOCÊ ENTENDE TUDO DE SUSTENTABILIDADE.".format(c)
        elif 4 >= c <= 6:
            lb69['text'] = 'VOCÊ ACERTOU {} QUESTÕES. VOCÊ TEM UM BOM CONHECIMENTO, MAS PODE MELHORAR.'.format(c)
        else:
            lb69['text'] = 'VOCÊ ACERTOU {} QUESTÕES. PRECISA ADIQUIRIR MAIS CONHECIMENTOS, TREINE MAIS.'.format(c)
    lb63.destroy()
    lb64.destroy()
    lb65.destroy()
    lb66.destroy()
    lb67.destroy()
    lb68.destroy()
    en14.destroy()
    bt11.destroy()



def quiz10():
    global c
    q9 = int(en13.get())
    if q9 == 3:
        c += 1
    lb57.destroy()
    lb58.destroy()
    lb59.destroy()
    lb60.destroy()
    lb61.destroy()
    lb62.destroy()
    en13.destroy()
    bt10.destroy()
    lb63['text'] = "10ª Pergunta: Qual alternativa apresenta uma vantagem da energia solar?"
    lb64['text'] = "1:Não polui."
    lb65['text'] = "2:Não é renovável."
    lb66['text'] = "3:É eficaz em qualquer clima."
    lb67['text'] = "4:É disponível a todo momento."
    lb68['text'] = "Digite a resposta."

def quiz9():
    global c
    q8 = int(en12.get())
    if q8 == 2:
        c += 1
    lb51.destroy()
    lb52.destroy()
    lb53.destroy()
    lb54.destroy()
    lb55.destroy()
    lb56.destroy()
    en12.destroy()
    bt9.destroy()
    lb57['text'] = "9ª Pergunta: Qual dos elementos abaixo não é utilizado como fonte de energia?"
    lb58['text'] = "1:Água corrente."
    lb59['text'] = "2:Petróleo."
    lb60['text'] = "3:Barra de ferro."
    lb61['text'] = "4:Sol."
    lb62['text'] = "Digite a resposta."

def quiz8():
    global c
    q7 = int(en11.get())
    if q7 == 2:
        c += 1
    lb45.destroy()
    lb46.destroy()
    lb47.destroy()
    lb48.destroy()
    lb49.destroy()
    lb50.destroy()
    en11.destroy()
    bt8.destroy()
    lb51['text'] = "8ª Pergunta: Qual dos gases abaixo não é conhecido como um dos gases do efeito estufa (GEE)?"
    lb52['text'] = "1:N2O – óxido nitroso."
    lb53['text'] = "2:O2 – oxigênio."
    lb54['text'] = "3:CO2 – dióxido de carbono ou gás carbônico."
    lb55['text'] = "4:CH4 – metano."
    lb56['text'] = "Digite a resposta."

def quiz7():
    global c
    q6 = int(en10.get())
    if q6 == 3:
        c += 1
    en10.destroy()
    bt7.destroy()
    lb39.destroy()
    lb40.destroy()
    lb41.destroy()
    lb42.destroy()
    lb43.destroy()
    lb44.destroy()
    lb45['text'] = "7º Pergunta: Como preservar árvores e florestas?"
    lb46['text'] = "1:Construindo uma casa na árvore."
    lb47['text'] = "2:Reciclando papéis, jornais e revistas."
    lb48['text'] = "3:Reutilizando metais e vidros."
    lb49['text'] = "4:Indo em parques"
    lb50['text'] = "Digite a resposta."

def quiz6():
    global c
    q5 = int(en9.get())
    if q5 == 4:
        c += 1
    en9.destroy()
    bt6.destroy()
    lb33.destroy()
    lb34.destroy()
    lb35.destroy()
    lb36.destroy()
    lb37.destroy()
    lb38.destroy()
    lb39['text'] = "6ª Pergunta: Como consumir de forma consciente?"
    lb40['text'] = "1:Trocando todos os nossos objetos sempre que um novo do mesmo tipo for lançado."
    lb41['text'] = "2:Usar a mangueira para lavar o quintal e o carro."
    lb42['text'] = "3: Utilizando os recursos naturais para satisfazer nossas necessidades e das gerações futuras."
    lb43['text'] = "4:Adquirindo qualquer tipo de produto se for barato."
    lb44['text'] = "Digite a resposta."


def quiz5():
    global c
    q4 = int(en8.get())
    if q4 == 4:
        c += 1
    en8.destroy()
    bt5.destroy()
    lb27.destroy()
    lb28.destroy()
    lb29.destroy()
    lb30.destroy()
    lb31.destroy()
    lb32.destroy()
    lb33['text'] = "5ª Pergunta: Uma das formas de colaborar com a preservação do meio ambiente é reduzir a produção de resíduos. Mas como?."
    lb34['text'] = "1:Optando pela compra de produtos com embalagens recicláveis."
    lb35['text'] = "2: Reutilizando os materiais e objetos sempre que possível."
    lb36['text'] = "3:Apoiando iniciativas de reciclagem."
    lb37['text'] = "4:Todas as anteriores."
    lb38['text'] = "Digite a resposta."


def quiz4():
    global c
    q3 = int(en7.get())
    if q3 == 1:
        c += 1
    en7.destroy()
    bt4.destroy()
    lb21.destroy()
    lb22.destroy()
    lb23.destroy()
    lb24.destroy()
    lb25.destroy()
    lb26.destroy()
    lb27['text'] = "4ª Pergunta:O que fazer com o lixo eletrônico - pilhas, baterias e equipamentos quebrados."
    lb28['text'] = "1:Recolher, organizar e armazenar em casa ou no máximo o tempo que der."
    lb29['text'] = "2:Juntar com plásticos e metais."
    lb30['text'] = "3:Jogar no lixo comum."
    lb31['text'] = "4:Procure locais específicos para seu descarte."
    lb32['text'] = "Digite a resposta."

def quiz3():
    global c
    q2 = int(en6.get())
    if q2 == 2:
        c += 1
    en6.destroy()
    bt3.destroy()
    lb15.destroy()
    lb16.destroy()
    lb17.destroy()
    lb18.destroy()
    lb19.destroy()
    lb20.destroy()
    lb21['text'] = "3ª Pergunta: O que é coleta seletiva?"
    lb22['text'] = "1: Processo de coleta e coleta de resíduos para reaproveitamento por meio de reciclagem"
    lb23['text'] = "2: Destinação de resíduos para lixões e aterros"
    lb24['text'] = "3: Processo de envio de todo o lixo produzido para cooperativas ou entrega para catadores de rua."
    lb25['text'] = "4:A escolha aleatória do melhor lixo produzido."
    lb26['text'] = "Digite a resposta."

def quiz2():
    global c
    q1 = int(en5.get())
    if q1 == 4:
        c += 1
    lb70.destroy()
    en5.destroy()
    bt2.destroy()
    lb9.destroy()
    lb10.destroy()
    lb11.destroy()
    lb12.destroy()
    lb13.destroy()
    lb14.destroy()
    lb15['text'] = "2ª Pergunta: Como separar corretamente o lixo?"
    lb16['text'] = "1:Juntar tudo na lixeira, pois os materiais já fazem o trabalho de separação."
    lb17['text'] = "2:Separar o lixo orgânico(restos de alimentos, papel sujo e lixo sanitário)dos resíduos."
    lb18['text'] = "3:Deixar plásticos sujos juntos com lixo orgânico."
    lb19['text'] = "4:Juntar todo tipo de lixo e descartar no ponto de coleta."
    lb20['text'] = "Digite a resposta."

def quiz():
    n1 = str(en1.get()).upper()
    lb5.destroy()
    lb6.destroy()
    lb7.destroy()
    lb8.destroy()
    en1.destroy()
    en2.destroy()
    en3.destroy()
    en4.destroy()
    bt1.destroy()
    lb70['text'] = 'OLÁ {}. VAMOS COMEÇAR!'.format(n1)
    lb9['text'] = "1ªPergunta: O que é reciclagem?"
    lb10['text'] = "1: Jogar fora o lixo produzido."
    lb11['text'] = "2: Coletar todo o tipo de material existente em lixos recicláveis."
    lb12['text'] = "3: Nome dado para todo o processo após descarte."
    lb13['text'] = "4: Processo de transformação de materiais usados em novos produtos para consumo."
    lb14['text'] = "Digite a resposta"


lb1 = Label(janela, text='-' * 130, fg='green')
lb1.pack()
lb2 = Label(janela, text='SEJA BEM-VINDO AO', fg='green', font='Arial 12')
lb2.pack()
lb3 = Label(janela, text='QUIZ MENTE VERDE', fg='green', font='Arial 12')
lb3.pack()
lb4 = Label(janela, text='-' * 130, fg='green')
lb4.pack()

lb5 = Label(janela, text='Digite seu nome')
lb5.pack()
en1 = Entry(janela, fg='green')
en1.pack()

lb6 = Label(janela, text='Digite sua idade')
lb6.pack()
en2 = Entry(janela, fg='green')
en2.pack()

lb7 = Label(janela, text='Digite o nome de sua escola')
lb7.pack()
en3 = Entry(janela,fg='green', width=50)
en3.pack()

lb8 = Label(janela, text='Digite a sua serie')
lb8.pack()
en4 = Entry(janela, fg='green')
en4.pack()

bt1 = Button(janela, text='Iniciar Quiz',fg='green', command=quiz)
bt1.pack()



#1
lb70 = Label(janela, text=' ')
lb70.pack()
lb9 = Label(janela, text=' ')
lb9.pack()
lb10 = Label(janela, text=' ')
lb10.pack(anchor=W)
lb11 = Label(janela, text=' ')
lb11.pack(anchor=W)
lb12 = Label(janela, text=' ')
lb12.pack(anchor=W)
lb13 = Label(janela, text=' ')
lb13.pack(anchor=W)
lb14 = Label(janela, text=' ')
lb14.pack()
en5 = Entry(janela)
en5.pack()
bt2 = Button(janela, text='Proxima', fg='green', command=quiz2,)
bt2.pack()

#2
lb15 = Label(janela, text=' ')
lb15.pack()
lb16 = Label(janela, text=' ')
lb16.pack(anchor=W)
lb17 = Label(janela, text=' ')
lb17.pack(anchor=W)
lb18 = Label(janela, text=' ')
lb18.pack(anchor=W)
lb19 = Label(janela, text=' ')
lb19.pack(anchor=W)
lb20 = Label(janela, text=' ')
lb20.pack()
en6 = Entry(janela)
en6.pack()
bt3 = Button(janela, text='Proxima', fg='green', command=quiz3)
bt3.pack()
#3
lb21 = Label(janela, text=' ')
lb21.pack()
lb22 = Label(janela, text=' ')
lb22.pack(anchor=W)
lb23 = Label(janela, text=' ')
lb23.pack(anchor=W)
lb24 = Label(janela, text=' ')
lb24.pack(anchor=W)
lb25 = Label(janela, text=' ')
lb25.pack(anchor=W)
lb26 = Label(janela, text=' ')
lb26.pack()
en7 = Entry(janela)
en7.pack()
bt4 = Button(janela, text='Proxima', fg='green', command=quiz4)
bt4.pack()
#4
lb27 = Label(janela, text=' ')
lb27.pack()
lb28 = Label(janela, text=' ')
lb28.pack(anchor=W)
lb29 = Label(janela, text=' ')
lb29.pack(anchor=W)
lb30 = Label(janela, text=' ')
lb30.pack(anchor=W)
lb31 = Label(janela, text=' ')
lb31.pack(anchor=W)
lb32 = Label(janela, text=' ')
lb32.pack()
en8 = Entry(janela)
en8.pack()
bt5 = Button(janela, text='Proxima', fg='green', command=quiz5)
bt5.pack()
#5
lb33 = Label(janela, text=' ')
lb33.pack()
lb34 = Label(janela, text=' ')
lb34.pack(anchor=W)
lb35 = Label(janela, text=' ')
lb35.pack(anchor=W)
lb36 = Label(janela, text=' ')
lb36.pack(anchor=W)
lb37 = Label(janela, text=' ')
lb37.pack(anchor=W)
lb38 = Label(janela, text=' ')
lb38.pack()
en9 = Entry(janela)
en9.pack()
bt6 = Button(janela, text='Proxima', fg='green', command=quiz6)
bt6.pack()
#6
lb39 = Label(janela, text=' ')
lb39.pack()
lb40 = Label(janela, text=' ')
lb40.pack(anchor=W)
lb41 = Label(janela, text=' ')
lb41.pack(anchor=W)
lb42 = Label(janela, text=' ')
lb42.pack(anchor=W)
lb43 = Label(janela, text=' ')
lb43.pack(anchor=W)
lb44 = Label(janela, text=' ')
lb44.pack()
en10 = Entry(janela)
en10.pack()
bt7 = Button(janela, text='Proxima', fg='green', command=quiz7)
bt7.pack()
#7
lb45 = Label(janela, text=' ')
lb45.pack()
lb46 = Label(janela, text=' ')
lb46.pack(anchor=W)
lb47 = Label(janela, text=' ')
lb47.pack(anchor=W)
lb48 = Label(janela, text=' ')
lb48.pack(anchor=W)
lb49 = Label(janela, text=' ')
lb49.pack(anchor=W)
lb50 = Label(janela, text=' ')
lb50.pack()

en11 = Entry(janela)
en11.pack()
bt8 = Button(janela, text='Proxima', fg='green', command=quiz8)
bt8.pack()
#8
lb51 = Label(janela, text='')
lb51.pack()
lb52 = Label(janela, text='')
lb52.pack(anchor=W)
lb53 = Label(janela, text='')
lb53.pack(anchor=W)
lb54 = Label(janela, text='')
lb54.pack(anchor=W)
lb55 = Label(janela, text='')
lb55.pack(anchor=W)
lb56 = Label(janela, text='')
lb56.pack()
en12 = Entry(janela)
en12.pack()
bt9 = Button(janela, text='Proxima', fg='green', command=quiz9)
bt9.pack()
#9
lb57 = Label(janela, text='')
lb57.pack()
lb58 = Label(janela, text='')
lb58.pack(anchor=W)
lb59 = Label(janela, text='')
lb59.pack(anchor=W)
lb60 = Label(janela, text='')
lb60.pack(anchor=W)
lb61 = Label(janela, text='')
lb61.pack(anchor=W)
lb62 = Label(janela, text='')
lb62.pack()
en13 = Entry(janela)
en13.pack()
bt10 = Button(janela, text='Proxima', fg='green', command=quiz10)
bt10.pack()

#10
lb63 = Label(janela, text='')
lb63.pack()
lb64 = Label(janela, text='')
lb64.pack(anchor=W)
lb65 = Label(janela, text='')
lb65.pack(anchor=W)
lb66 = Label(janela, text='')
lb66.pack(anchor=W)
lb67 = Label(janela, text='')
lb67.pack(anchor=W)
lb68 = Label(janela, text='')
lb68.pack()
en14 = Entry(janela)
en14.pack()
bt11 = Button(janela, text='Veja o resultado Final', fg='green', command=result)
bt11.pack()
#resul
lb69=Label(janela, text='')
lb69.pack()

largura = 700
altura = 300

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

janela.resizable(False, False)

janela.mainloop()