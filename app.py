import customtkinter as ctk

#configuracao da aparencia
ctk.set_appearance_mode('dark')

# criacao das funcoes de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # verificar se o usuario é giovanna e a senha é admin123

    if usuario == "giovanna" and senha == "admin123":
        resultado_login.configure(text="Login efetuado com sucesso!", text_color="green")
    else:
        resultado_login.configure(text="Login incorreto", text_color="red")

#criacao da janela princial
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#criacao dos campos

# label usuario
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=10)

# entry
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

# label
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

# entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha")
campo_senha.pack(pady=10)

# botao
botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=10)

# campo feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)


# iniciar a aplicacao
app.mainloop()