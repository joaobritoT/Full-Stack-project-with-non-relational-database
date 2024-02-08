from classe import Pessoa
import customtkinter
import json
from time import sleep
import subprocess
import os
import webbrowser

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")




#tela de cadastro
def cadastro():
    cadastro = customtkinter.CTk()
    cadastro.geometry("400x280")
    cadastro.iconbitmap("icone_agenda.ico")
    cadastro.title("Banco de contatos João Victor")
    lblcadastro = customtkinter.CTkLabel(cadastro,text="Digite os dados do contato",font=("Arial",20))
    lblcadastro.pack(padx=10,pady=10)
    entradanome = customtkinter.CTkEntry(cadastro,placeholder_text="Nome:",width=250,font=("Arial",15),placeholder_text_color="white")
    entradanome.pack(padx=10,pady=10)
    entradaemail = customtkinter.CTkEntry(cadastro,placeholder_text="E-mail:",width=250,font=("Arial",15),placeholder_text_color="white")
    entradaemail.pack(padx=10,pady=10)
    entradatelefone = customtkinter.CTkEntry(cadastro,placeholder_text="Telefone:",width=250,font=("Arial",15),placeholder_text_color="white")
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
                lbljacadastrado.configure(text_color="red")

            else:
                adicionar_contato(p1.Nome,p1.Email,p1.Telefone)
                cadastro.withdraw()
                confirmacao = customtkinter.CTk()
                confirmacao.geometry("300x50")
                confirmacao.title("Banco de contatos João Victor")
                confirmacao.iconbitmap("icone_agenda.ico")
                lbl_confirmacao = customtkinter.CTkLabel(confirmacao,text="Usuario cadastrado com sucesso",font=("Arial",15,"bold"),text_color="green")
                lbl_confirmacao.pack(padx=10,pady=10)
                confirmacao.mainloop()
                
                
                

    
            
    btncadastro = customtkinter.CTkButton(cadastro,text="Cadastar",command=cadastar,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=230,corner_radius=20)
    btncadastro.pack(padx=10,pady=10)
    lbljacadastrado = customtkinter.CTkLabel(cadastro,text='',font=("Arial",15,"bold"),text_color="red")
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
    exibicao.geometry("400x400")
    exibicao.title("Banco de contatos João Victor")
    exibicao.iconbitmap("icone_agenda.ico")
    texto = customtkinter.CTkLabel(exibicao,text="Lista dos contatos cadastrados no banco de dados: ",font=("Arial",20,"bold"),text_color="white",wraplength=350)
    texto.pack(padx=10,pady=10)
    frame = customtkinter.CTkScrollableFrame(exibicao,width=350,height=300,fg_color="white")
    frame.pack()
    for elementos in contatos_atualizados:
        label = customtkinter.CTkLabel(frame,text="Nome: {}\nEmail: {}\nTelefone: {}".format(elementos['nome'],elementos['email'],elementos['telefone']),wraplength=500,font=("Arial",15,"bold"),text_color="black",justify="left")
        label_divisao = customtkinter.CTkLabel(frame,text="================================================",text_color="black",font=("Arial",15,"bold"))
        label_divisao.pack(padx=10,pady=10)
        label.pack(padx=10,pady=10)
    
    exibicao.mainloop()

#buscar contato
def buscar():
    tela_buscar = customtkinter.CTk()
    tela_buscar.geometry("400x400")
    tela_buscar.iconbitmap("icone_agenda.ico")
    tela_buscar.title("Banco de contatos João Victor")
    lbl_buscar = customtkinter.CTkLabel(tela_buscar,text="Digite o nome do usuario que deseja buscar",font=("Arial",22),wraplength=300)
    lbl_buscar.pack(padx=10,pady=10)
    entradanome = customtkinter.CTkEntry(tela_buscar,placeholder_text="Nome:",width=250,font=("Arial",15),placeholder_text_color="white")
    entradanome.pack(padx=10,pady=10)
    entradaemail = customtkinter.CTkEntry(tela_buscar,placeholder_text="E-mail:",width=250,font=("Arial",15),placeholder_text_color="white")
    entradaemail.pack(padx=10,pady=10)
    entradatelefone = customtkinter.CTkEntry(tela_buscar,placeholder_text="Telefone:",width=250,font=("Arial",15),placeholder_text_color="white")
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
                stringvar = "CONTATO ENCONTRADO: \n ================ \n Nome: {} \n Email: {} \n Telefone: {}\n ================".format(retorno['nome'],retorno['email'],retorno['telefone'])
                lbl_retorno.configure(text=stringvar)
                lbl_retorno.configure(text_color="white")
                lbl_retorno.configure(font=("Arial",15,"bold"))
                break  
            else:
                retorno = "Nenhum contato encontrado"
                lbl_retorno.configure(text=retorno)
                lbl_retorno.configure(text_color="red")
                lbl_retorno.configure(font=("Arial",20))
                
                
        
    btn = customtkinter.CTkButton(tela_buscar,text="Buscar",command=lambda:[buscar_especifico(),entradanome.delete(0,'end'),entradaemail.delete(0,'end'),entradatelefone.delete(0,'end')],font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=230,corner_radius=20)
    btn.pack(padx=10,pady=10)
    lbl_retorno = customtkinter.CTkLabel(tela_buscar,text='',font=("Arial",15,"bold"))
    lbl_retorno.pack(padx=10,pady=10)
    
    
    tela_buscar.mainloop()

def apagar():
    tela_apagar = customtkinter.CTk()
    tela_apagar.geometry("300x230")
    tela_apagar.title("Banco de contatos João Victor")
    tela_apagar.iconbitmap("icone_agenda.ico")
    lbl_texto_apagar = customtkinter.CTkLabel(tela_apagar,text="Digite o nome do contato que deseja apagar",wraplength=250,font=("Arial",20))
    lbl_texto_apagar.pack(padx=10,pady=10)
    entradanome = customtkinter.CTkEntry(tela_apagar,placeholder_text="Nome:",width=200,font=("Arial",15),placeholder_text_color="white")
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
                lbl_apagado.configure(text="USUARIO DELETADO DO SISTEMA")
                lbl_apagado.configure(text_color="green")
                break
            else:
                print("erro")
                lbl_apagado.configure(text="USUARIO NÃO ENCONTRADO")
                lbl_apagado.configure(text_color="red")
    
    btn = customtkinter.CTkButton(tela_apagar,text="Apagar",command=lambda:[buscar_deletar(),entradanome.delete(0,'end')],font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=230,corner_radius=20)
    btn.pack(padx=10,pady=10)
    lbl_apagado = customtkinter.CTkLabel(tela_apagar,text='',font=("Arial",15,"bold"))
    lbl_apagado.pack(padx=10,pady=10)
    tela_apagar.mainloop()

def alterar():
    tela_alterar = customtkinter.CTk()
    tela_alterar.geometry("300x230")
    tela_alterar.title("Banco de contatos João Victor")
    tela_alterar.iconbitmap("icone_agenda.ico")
    lbl_texto_alterar = customtkinter.CTkLabel(tela_alterar,text="Digite o nome do usuario que deseja alterar",wraplength=250,font=("Arial",20))
    lbl_texto_alterar.pack(padx=10,pady=10)
    entradanome_alterar = customtkinter.CTkEntry(tela_alterar,placeholder_text="Nome",width=200,font=("Arial",15),placeholder_text_color="white")
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
                cadastro_alterar = customtkinter.CTk()
                cadastro_alterar.geometry("400x300")
                cadastro_alterar.title("Banco de contatos João Victor")
                cadastro_alterar.iconbitmap("icone_agenda.ico")
                lbl_alterar = customtkinter.CTkLabel(cadastro_alterar,text="Digite os dados atualizados do contato",font=("Arial",20),wraplength=280)
                lbl_alterar.pack(padx=10,pady=10)
                entradanome_aletrar_commit = customtkinter.CTkEntry(cadastro_alterar,placeholder_text="Nome",width=250,font=("Arial",15),placeholder_text_color="white")
                entradanome_aletrar_commit.pack(padx=10,pady=10)
                entradaemail_alterar_commit = customtkinter.CTkEntry(cadastro_alterar,placeholder_text="E-mail",width=250,font=("Arial",15),placeholder_text_color="white")
                entradaemail_alterar_commit.pack(padx=10,pady=10)
                entradatelefone_alterar_commit = customtkinter.CTkEntry(cadastro_alterar,placeholder_text="Telefone",width=250,font=("Arial",15),placeholder_text_color="white")
                entradatelefone_alterar_commit.pack(padx=10,pady=10) 
                tela_alterar.withdraw()

                def commit():
                    nome_alterar_commit = entradanome_aletrar_commit.get()
                    email_alterar_commit = entradaemail_alterar_commit.get()
                    telefone_alterar_commit = entradatelefone_alterar_commit.get()
                    if nome_alterar_commit.strip() == '' or email_alterar_commit.strip() == '' or telefone_alterar_commit.strip() == '':
                        nulo = True
                    else:
                        nulo = False
                    if nulo == True:
                        print("erro")
                        lblerro_nulo.configure(text='Digite um valor valido')
                        lblerro_nulo.configure(text_color='red')
                        
                    else:
                    

                        def ler_contatos():
                                try:
                                    with open("dados.json",'r') as file:
                                        contatos = json.load(file)
                                except:
                                    contatos = []
                                return contatos
                        contatos_atualizados = ler_contatos()

                        for elementos in contatos_atualizados:
                            if elementos['nome'] == nome_alterar_commit and elementos['email'] == email_alterar_commit and elementos['telefone'] == telefone_alterar_commit:
                                adcionado = True
                                break
                            else:
                                adcionado = False
                        if adcionado == False:

                            for pessoa in contatos_atualizados:
                                if pessoa.get("nome") == nome_alterar:
                                    pessoa["nome"] = nome_alterar_commit
                                    pessoa['email'] = email_alterar_commit
                                    pessoa['telefone'] = telefone_alterar_commit 
                            with open('dados.json', 'w') as arquivo:
                                json.dump(contatos_atualizados, arquivo, indent=2)
                            print("alterado")
                            print(nulo)
                            confirmacao_alterar = customtkinter.CTk()
                            confirmacao_alterar.geometry("300x50")
                            confirmacao_alterar.title("Banco de contatos João Victor")
                            confirmacao_alterar.iconbitmap("icone_agenda.ico")
                            lbl_confirmacao = customtkinter.CTkLabel(confirmacao_alterar,text="Usuario alterado com sucesso",font=("Arial",15,"bold"),text_color="green")
                            lbl_confirmacao.pack(padx=10,pady=10)
                            cadastro_alterar.withdraw()
                            confirmacao_alterar.mainloop()
                        else:
                            lblerro_nulo.configure(text='Usuario ja cadastrado')
                            lblerro_nulo.configure(text_color='red')


                    
                btncadastro = customtkinter.CTkButton(cadastro_alterar,text="alterar",command=commit,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=230,corner_radius=20)
                btncadastro.pack(padx=10,pady=10)
                lblerro_nulo = customtkinter.CTkLabel(cadastro_alterar,text="",font=("Arial",15,"bold"))
                lblerro_nulo.pack(padx=10,pady=10)
                cadastro_alterar.mainloop()
        else:
            print("erro")
            lblerro_nulo_busca.configure(text='Nenhum usuario encontrado')
            lblerro_nulo_busca.configure(text_color="red")
                
    btn = customtkinter.CTkButton(tela_alterar,text="buscar",command=lambda:[buscar_alterar(),entradanome_alterar.delete(0,'end')],font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=230,corner_radius=20)
    btn.pack(padx=10,pady=10)
    lblerro_nulo_busca = customtkinter.CTkLabel(tela_alterar,text="",font=("Arial",15,"bold"))
    lblerro_nulo_busca.pack(padx=10,pady=10)
    tela_alterar.mainloop()


def Abrir_api():
    try:
        subprocess.Popen(['python','api.py'])
    except Exception as e:
        print("erro {}".format(e))
    new =2
    url = 'http://localhost:5000/dados'
    sleep(1)
    webbrowser.open(url,new=new)

#tela principal
principal = customtkinter.CTk()
principal.geometry("400x450")
principal.iconbitmap("icone_agenda.ico")
principal.title("Banco de contatos João Victor")
lblmain = customtkinter.CTkLabel(principal,text="MEU BANCO DE CONTATOS",font=('Arial',26))
lblmain.pack(padx=10,pady=10)
lbl1 = customtkinter.CTkLabel(principal,text="Selecione uma opcao: ",font=("Arial",20))
lbl1.pack(padx=10,pady=10)
btn1 = customtkinter.CTkButton(principal,text="Cadastrar contato",command=cadastro,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=300,corner_radius=20)
btn1.pack(padx=10,pady=10)
btn2 = customtkinter.CTkButton(principal,text="Ver lista de contatos",command=mostrar_contatos,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=300,corner_radius=20)
btn2.pack(padx = 10,pady = 10)
btn3 = customtkinter.CTkButton(principal,text="Buscar contato especifico",command=buscar,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=300,corner_radius=20)
btn3.pack(padx=10,pady=10)
btn4 = customtkinter.CTkButton(principal,text="Apagar contato",command=apagar,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=300,corner_radius=20)
btn4.pack(padx=10,pady=10)
btn5 = customtkinter.CTkButton(principal,text="Alterar contato",command=alterar,font=("Arial",15,"bold"),fg_color="#514FFA",hover_color="#1714FA",width=300,corner_radius=20)
btn5.pack(padx=10,pady=10)
btn7 = customtkinter.CTkButton(principal,text="Abrir API",command=Abrir_api,font=("Arial",15,"bold"),fg_color="#0BDB19",hover_color="#16752F",width=300,corner_radius=20)
btn7.pack(padx=10,pady=10)
btn6 = customtkinter.CTkButton(principal,text="Sair",command=principal.destroy,font=("Arial",15,"bold"),fg_color="#FA5C4F",hover_color="#FA0201",width=300,corner_radius=20)
btn6.pack(padx=10,pady=10)



principal.mainloop()



