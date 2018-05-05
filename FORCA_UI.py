# coding=utf-8
# encoding=utf8
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import Common

class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        master.minsize (width=800, height=800)


        self.codigoErroTentativaLetra = {0: "Você já tentou essa letra", 1: "Palavra secreta não possui a letra",
                                         2: "Palavra secreta possui a letra"}

        self.pack()

        self.winfo_toplevel().title("Forca - by Ricardo Varjão")



        #variaveis
        self.palavraSecreta = ""  #palavra a ser adivinhada
        self.palpite = ""         #palavra como será apresentada na tela
        self.letrasJaTentadas = [ ] #letras que já foram tentadas
        self.mensagem = ""        #mensagens de erro, de game over, ou de já ganhou

        self.colors = {"mensagem" : "black"}

        self.vidas = 6

        #CRIA OBJETOS DA TELA INICIAL
        self.create_widgets()
        self.novoJogo()



    def create_widgets(self):
        #CRIA OBJETOS DA TELA INICIAL
        self.btnNewGame = tk.Button(self)
        self.btnNewGame["text"] = "Novo jogo"
        self.btnNewGame["command"] = self.novoJogo
        self.btnNewGame.pack()

        self.labelTitulo = tk.Label(self)
        self.labelTitulo.pack()
        self.labelTitulo["text"] = "Titulo"

        self.labelDica = tk.Label(self)
        self.labelDica["text"] = "Dica"
        self.labelDica.pack()

        self.labelMensagem = tk.Label(self)
        self.labelMensagem["text"] = "Mensagem"
        self.labelMensagem.pack()

        self.frameDoJogo = tk.Frame(self)
        self.frameDoJogo.pack (fill="both", expand="yes")

        img = ImageTk.PhotoImage (Image.open ("imagens_forca/forca6.jpg"))
        self.labelImage = tk.Label (self.frameDoJogo, image=img)
        self.labelImage.image = img
        self.labelImage.pack(side = "left")

        self.labelPalavra = tk.Label(self.frameDoJogo)
        self.labelPalavra["text"] = "PALAVRA SECRETA"
        self.labelPalavra.pack(side = "right")

        self.frameDaEntrada = tk.Frame(self)
        self.frameDaEntrada.pack()

        self.labelLetras = tk.Label(self.frameDaEntrada)
        self.labelLetras["text"] = "Letras tentadas"
        self.labelLetras.pack(side="top")

        self.labelNovaLetra = tk.Label (self.frameDaEntrada)
        self.labelNovaLetra[ "text" ] = "Nova letra: "
        self.labelNovaLetra.pack (side="left")

        self.btnOk = tk.Button(self.frameDaEntrada)
        self.btnOk["text"] = "Ok"
        self.btnOk.pack(side = "right")
        self.btnOk["command"] = self.buttonOk

        self.campoNovaLetra = tk.Entry(self.frameDaEntrada)
        self.campoNovaLetra.pack(side = "right")

        fontSize = 20
        self.labelPalavra.configure(font=("Helvetica", 40))
        self.labelLetras.configure(font=("Helvetica", fontSize))
        self.labelDica.configure(font=("Helvetica", fontSize))
        self.labelMensagem.configure(font=("Helvetica", int(fontSize * 1.5)))
        self.labelNovaLetra.configurefont=("Helvetica", fontSize)
        self.labelTitulo.configure(font=("Helvetica", fontSize))

        # w = Label (master, text="Helvetica", font=("Helvetica", 16))

    def novoJogo(self):

        self.campoNovaLetra.config(state = 'normal')

        self.palpite = ""
        self.mensagem = ""
        self.palavraSecreta = ""
        self.dica = ""
        self.letrasJaTentadas = []
        self.vidas = 6

        self.dicionarioPalavraSecreta = self.EscolhaUmaPalavra()

        self.palavraSecreta = Common.remover_acentos(self.dicionarioPalavraSecreta["palavra"].upper())
        self.categoria = self.dicionarioPalavraSecreta["categoria"]
        self.dica = self.dicionarioPalavraSecreta["dica"]

        self.titulo = "Categoria: {}".format (self.dicionarioPalavraSecreta[ "categoria" ])

        self.palpite = ""
        charOculto = "*"

        # tira os espacos em branco do palpite
        for (i, char) in enumerate (self.palavraSecreta):
            if char == " ":
                self.palpite += char
            else:
                self.palpite += charOculto


        self.updateLabels()

    def buttonOk(self):
        letra = self.campoNovaLetra.get()[0].upper()
        self.set_text(self.campoNovaLetra, "")
        self.tentaLetra(letra)


    def tentaLetra(self, letra):
        # verifica a letra e retorna um dicionario contendo uma mensagem e um codigo de erro ou acerto

        charOculto = "*"
        self.mensagem = ""

        if self.letrasJaTentadas.__contains__(letra):
            self.mensagem = "Você já tentou essa letra."
            self.colors[ "mensagem" ] = "yellow"

        else:
            self.letrasJaTentadas.append(letra)
            self.letrasJaTentadas.sort()
            if self.palavraSecreta.find(letra) == -1 :
                self.mensagem = "Palavra secreta não possui a letra: {}".format(letra)
                self.vidas -= 1
                self.colors[ "mensagem" ] = "red"
                if self.vidas == 0 :
                    self.mensagem = "Você perdeu. Palavra secreta é: {}".format(self.palavraSecreta)
                    self.fimDeJogo()

            else:
                temp = ""

                for (i, char) in enumerate(self.palavraSecreta):
                    if char == letra : temp += char
                    else: temp += self.palpite[i]

                self.palpite = temp
                self.colors[ "mensagem" ] = "black"

                if self.palpite.find(charOculto) == -1:
                    self.mensagem = "Você venceu"
                    self.colors[ "mensagem" ] = "green"
                    self.fimDeJogo()



        self.updateLabels()



    def updateLabels(self):

        #LABEL DAS LETRAS TENTADAS
        strLetras = "Letras já tentadas:["

        for (i, letra) in enumerate (self.letrasJaTentadas):
            strLetras += letra
            if i < len (self.letrasJaTentadas) - 1:
                strLetras += ","
        strLetras += "]"

        print("mensgem: {}".format(self.mensagem))
        print("   dica: {}".format(self.dica))
        print("palpite: {}".format(self.palpite))
        print(" titulo: {}".format(self.titulo))
        print("mensgem: {}".format(self.mensagem))


        self.labelMensagem.configure(fg=self.colors["mensagem"])
        self.labelMensagem["text"] = self.mensagem

        self.labelLetras["text"] = strLetras
        self.labelDica["text"] = self.dica
        self.labelPalavra["text"] = self.palpite
        self.labelTitulo["text"] = self.titulo

        fileName = "imagens_forca/forca{}.jpg".format(self.vidas)
        img = ImageTk.PhotoImage (Image.open (fileName))
        self.labelImage.configure(image = img)
        self.labelImage.image = img

    # img2 = ImageTk.PhotoImage(Image.open(path2))
    # panel.configure(image=img2)
    # panel.image = img2


    #             self.labelImage = tk.Label (self.frameDoJogo, image=img)


    def fimDeJogo(self):
        self.campoNovaLetra.config(state = 'disabled')
        self.updateLabels()
        print("fim de jogo")





    def set_text(self, field, text):
        field.delete (0, END)
        field.insert (0, text)
        return


    def EscolhaUmaPalavra(self):
        #SELECIONA UMA PALAVRA DENTRO DO BANCO DE DADOS
        import json
        import random

        file_obj = open ("LISTA_11_FORCA.txt", "r")
        # text = file_obj.read ( ).decode (encoding="utf-8")
        # database = json.loads (text, encoding="utf-8")
        text = file_obj.read ( )
        database = json.loads (text, encoding="utf-8")

        categorias = [ "filmes", "estados e capitais", "paises e capitais", "times", "nomes dos alunos" ]

        # escolhe uma categoria
        categoria = categorias[ random.randrange (0, len (categorias)) ]

        # pega todos os itens daquela categoria
        itens = database[ categoria ]

        # escolhe um item daquela categoria
        item = itens[ random.randrange (0, len (itens)) ]

        textoDica = ""
        chave = ""
        # como o banco de dados nao esta padronizado, dependendo da categoria escolhida tem que
        # ser feita a busca em chaves diferentes
        if categoria == "filmes":
            chave = "titulo"
            textoDica = "Ganhador da {}a edicao do Oscar".format (item[ "edicao" ])
        elif categoria == "times":
            chave = "nome"
            textoDica = "Time da 1a divisão do Campeonato Brasileiro de 2018"
        elif categoria == "estados e capitais":
            chave = "capital"
            estado = item[ "estado" ]
            textoDica = "Capital de {}".format (estado)
        elif categoria == "paises e capitais":
            chave = "pais"
            continente = item[ "continente" ]
            textoDica = "Continente: {}".format (continente)
        elif categoria == "nomes dos alunos":
            chave = "nome"
            textoDica = "Nome de um aluno(a)"

        palavra = item[ chave ]
        retornar = {"categoria": categoria, "palavra": palavra, "dica": textoDica}

        return retornar




root = tk.Tk()
app = Application(master=root)
root.resizable (width=False, height=False)
root.size()
app.mainloop()

