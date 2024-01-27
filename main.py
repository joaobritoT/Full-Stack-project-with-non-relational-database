from classe import Pessoa
import customtkinter
import json
from time import sleep

#tela de cadastro
def cadastro():
    cadastro = customtkinter.CTk()
    cadastro.geometry("400x400")
    entradanome = customtkinter.CTkEntry(cadastro,placeholder_text="Nome")
    entradanome.pack(padx=10,pady=10)
    entradaemail = customtkinter.CTkEntry(cadastro,placeholder_text="E-mail")
    entradaemail.pack(padx=10,pady=10)
    entradatelefone = customtkinter.CTkEntry(cadastro,placeholder_text="Telefone")
    entradatelefone.pack(padx=10,pady=10)
    def cadastar():
        p1 = Pessoa(entradanome.get(),entradaemail.get(),entradatelefone.get())
        if p1.Nome.strip() == '' or p1.Email.strip() == '' or p1.Telefone == '':
            print("nulo")
            lbljacadastrado.configure(text='Digite valores validos')
        else:

            def ler_contatos():
                try:
                    with open("dados.json",'r') as file:
                        contatos = json.load(file)
                except:
                    contatos = []
                return contatos
            def adicionar_contato(nome,email,telefone):
                novo_contato = {"nome":nome,"email":email,"telefone":telefone}
                contatos = ler_contatos()
                contatos.append(novo_contato)

                with open('dados.json','w') as file:
                    json.dump(contatos,file,indent=2)
            contatos_atualizados = ler_contatos()
            adicionado = False
            for elementos in contatos_atualizados:
                if elementos['nome'] == p1.Nome and elementos['email'] == p1.Email and elementos['telefone'] == p1.Telefone:
                    adicionado = True
                else:
                    adicionado = False
            if adicionado == True:
                lbljacadastrado.configure(text='Usuario ja cadastrado')

            else:
                adicionar_contato(p1.Nome,p1.Email,p1.Telefone)
                lbljacadastrado.configure(text='Usuario cadastrado com sucesso')
    
            
    btncadastro = customtkinter.CTkButton(cadastro,text="Cadastar",command=cadastar)
    btncadastro.pack(padx=10,pady=10)
    lbljacadastrado = customtkinter.CTkLabel(cadastro,text='')
    lbljacadastrado.pack(padx=10,pady=10)
    cadastro.mainloop()
#lista dos contatos cadastrados
def mostrar_contatos():
    def ler_contatos():
            try:
                with open("dados.json",'r') as file:
                    contatos = json.load(file)
            except:
                contatos = []
            return contatos
    
    contatos_atualizados = ler_contatos()
    exibicao = customtkinter.CTk()
    texto = customtkinter.CTkLabel(exibicao,text="Lista dos contatos cadastrados no banco de dados: ")
    texto.pack(padx=10,pady=10)
    for elementos in contatos_atualizados:
        label = customtkinter.CTkLabel(exibicao,text="Nome: {}\n Email: {}\n Telefone: {}".format(elementos['nome'],elementos['email'],elementos['telefone']),wraplength=500)
        label_divisao = customtkinter.CTkLabel(exibicao,text="=================")
        label_divisao.pack()
        label.pack(padx=10,pady=10)
    
    exibicao.geometry("500x500")
    exibicao.mainloop()

#buscar contato
def buscar():
    tela_buscar = customtkinter.CTk()
    tela_buscar.geometry("500x500")
    entradanome = customtkinter.CTkEntry(tela_buscar,placeholder_text="Nome")
    entradanome.pack(padx=10,pady=10)
    entradaemail = customtkinter.CTkEntry(tela_buscar,placeholder_text="E-mail")
    entradaemail.pack(padx=10,pady=10)
    entradatelefone = customtkinter.CTkEntry(tela_buscar,placeholder_text="Telefone")
    entradatelefone.pack(padx=10,pady=10)
    def buscar_especifico():
        nome = entradanome.get()
        email = entradaemail.get()
        telefone = entradatelefone.get()
        def ler_contatos():
                try:
                    with open("dados.json",'r') as file:
                        contatos = json.load(file)
                except:
                    contatos = []
                return contatos
        contatos_atualizados = ler_contatos()
       
        for elementos in contatos_atualizados:
            if nome == elementos['nome'] or email == elementos['email'] or telefone == elementos['telefone']:
                retorno = elementos
                stringvar = "contato encontrado: \n Nome: {} \n Email:{} \n Telefone: {}".format(retorno['nome'],retorno['email'],retorno['telefone'])
                lbl_retorno.configure(text=stringvar)    
            else:
                retorno = "nenhum contato encontrado"
                lbl_retorno.configure(text=retorno)
                
                
        
    btn = customtkinter.CTkButton(tela_buscar,text="Buscar",command=buscar_especifico)
    btn.pack(padx=10,pady=10)
    lbl_retorno = customtkinter.CTkLabel(tela_buscar,text='')
    lbl_retorno.pack(padx=10,pady=10)
    
    
    tela_buscar.mainloop()

def apagar():
    tela_apagar = customtkinter.CTk()
    tela_apagar.geometry("500x500")
    entradanome = customtkinter.CTkEntry(tela_apagar,placeholder_text="Nome")
    entradanome.pack(padx=10,pady=10)
    def buscar_deletar():
        nome = entradanome.get()
        def ler_contatos():
                try:
                    with open("dados.json",'r') as file:
                        contatos = json.load(file)
                except:
                    contatos = []
                return contatos
        contatos_atualizados = ler_contatos()
        for elementos in contatos_atualizados:
            if elementos['nome'] == nome:
                contatos_atualizados.remove(elementos)
                with open('dados.json','w') as file:
                    json.dump(contatos_atualizados,file,indent=2)
                print("apagado")
            else:
                print("erro")
    
    btn = customtkinter.CTkButton(tela_apagar,text="Apagar",command=buscar_deletar)
    btn.pack(padx=10,pady=10)
    tela_apagar.mainloop()

def alterar():
    tela_alterar = customtkinter.CTk()
    tela_alterar.geometry("500x500")
    lbl_alterar = customtkinter.CTkLabel(tela_alterar,text="Digite o nome do contato que deseja altrar:")
    lbl_alterar.pack(padx=10,pady=10)
    entradanome_alterar = customtkinter.CTkEntry(tela_alterar,placeholder_text="Nome")
    entradanome_alterar.pack(padx=10,pady=10)
    def buscar_alterar():
        nome_alterar = entradanome_alterar.get()
        def ler_contatos():
                try:
                    with open("dados.json",'r') as file:
                        contatos = json.load(file)
                except:
                    contatos = []
                return contatos
        contatos_atualizados = ler_contatos()
        for elementos in contatos_atualizados:
            if elementos['nome'] == nome_alterar:
                existe = True
                break
            else:
                existe = False
        if existe == True:
                cadastro = customtkinter.CTk()
                cadastro.geometry("400x400")
                entradanome_aletrar_commit = customtkinter.CTkEntry(cadastro,placeholder_text="Nome")
                entradanome_aletrar_commit.pack(padx=10,pady=10)
                entradaemail_alterar_commit = customtkinter.CTkEntry(cadastro,placeholder_text="E-mail")
                entradaemail_alterar_commit.pack(padx=10,pady=10)
                entradatelefone_alterar_commit = customtkinter.CTkEntry(cadastro,placeholder_text="Telefone")
                entradatelefone_alterar_commit.pack(padx=10,pady=10) 

                def commit():
                    nome_alterar_commit = entradanome_aletrar_commit.get()
                    email_alterar_commit = entradaemail_alterar_commit.get()
                    telefone_alterar_commit = entradatelefone_alterar_commit.get()

                    def ler_contatos():
                            try:
                                with open("dados.json",'r') as file:
                                    contatos = json.load(file)
                            except:
                                contatos = []
                            return contatos
                    contatos_atualizados = ler_contatos()


                    for pessoa in contatos_atualizados:
                        if pessoa.get("nome") == nome_alterar:
                            pessoa["nome"] = nome_alterar_commit
                            pessoa['email'] = email_alterar_commit
                            pessoa['telefone'] = telefone_alterar_commit 
                    with open('dados.json', 'w') as arquivo:
                        json.dump(contatos_atualizados, arquivo, indent=2)
                    print("alterado")


                    
                btncadastro = customtkinter.CTkButton(cadastro,text="alterar",command=commit)
                btncadastro.pack(padx=10,pady=10)
                lbljacadastrado = customtkinter.CTkLabel(cadastro,text='')
                lbljacadastrado.pack(padx=10,pady=10)
                cadastro.mainloop()
        else:
            print("erro")
            print(nome_alterar)
            print(existe)
                
    btn = customtkinter.CTkButton(tela_alterar,text="alterar",command=buscar_alterar)
    btn.pack(padx=10,pady=10)
    tela_alterar.mainloop()


#tela principal
principal = customtkinter.CTk()
principal.geometry("300x300")
lbl1 = customtkinter.CTkLabel(principal,text="Selecione uma opcao: ")
lbl1.pack(padx=10,pady=10)
btn1 = customtkinter.CTkButton(principal,text="Cadastrar contato",command=cadastro)
btn1.pack(padx=10,pady=10)
btn2 = customtkinter.CTkButton(principal,text="Lista dos contatos cadastrados",command=mostrar_contatos)
btn2.pack(padx = 10,pady = 10)
btn3 = customtkinter.CTkButton(principal,text="Buscar contato",command=buscar)
btn3.pack(padx=10,pady=10)
btn4 = customtkinter.CTkButton(principal,text="apagar contato",command=apagar)
btn4.pack(padx=10,pady=10)
btn5 = customtkinter.CTkButton(principal,text="Alterar contato",command=alterar)
btn5.pack(padx=10,pady=10)



principal.mainloop()


