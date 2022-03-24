'''Programa criado em Python, utilazando tkinter e API
para encurtar link's inseridos nele'''
import tkinter as tk
import requests

#função
def encurtar():
    '''Função de encurtar url's utilizando API cutt'''
    saida.delete(0, tk.END)
    url = entrada.get()
    print(url)
    entrada.delete(0, tk.END)
    key = '810a9a8b098d37a69d33abe26ebe27d1fe6b8'
    url_api = f"https://cutt.ly/api/api.php?key={key}&short={url}"
    retorno_api =  requests.get(url_api).json()["url"]
    url_curto = retorno_api['shortLink']
    if retorno_api['status'] == 7:
        msg = url_curto
        print(msg)
        saida.insert(0, msg)
    else:
        msg = 'ERRO, não foi possível encurtar o link'
        print(msg)
        saida.insert(0, msg)


janela = tk.Tk()
janela.title('Encurtador de link')
janela.iconbitmap(default='icon.ico')
janela.geometry('600x300+400+200') #largura x comprimento + dist esquerda +dist topo

label_0 = tk.Label(janela, text="Link original",width=20,font=("bold", 10))
label_0.place(relwidth=0.3, relheight=0.3) #, relx= 0.1, rely=0.1)

entrada = tk.Entry(janela)
entrada.place(relwidth=0.7, relx= 0.3, rely=0.12, height=20)

botao = tk.Button(janela, text='Encurtar', width=20, command=encurtar)
botao.place(relwidth=0.8, relheight=0.1, rely=0.4, relx=0.1, height=10)

label_1 = tk.Label(janela, text="Link curto",width=20,font=("bold", 10))
label_1.place(relwidth=0.3, relheight=0.3, rely=0.6)

saida = tk.Entry(janela)
saida.place(relwidth=0.7, relx= 0.3, rely=0.72, height=20)

janela.mainloop()
