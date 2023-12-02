from tkinter import *
import pyodbc

# Função para inserir dados no banco de dados
def inserirDados(nome, peso, altura, endereco, imc):
    conexao_str = "DRIVER={SQL Server};SERVER=IMC\\SQLEXPRESS;DATABASE=IMC;Trusted_Connection=yes;"
    conexao = pyodbc.connect(conexao_str)
    cursor = conexao.cursor()

    #insere dados na tabela
    cursor.execute("INSERT INTO Pessoa (Nome, Peso, Altura, Endereco, IMC) VALUES (?, ?, ?, ?, ?)",
                   nome, peso, altura, endereco, imc)

    #confirma a inserção
    conexao.commit()

    #fecha a conexão
    cursor.close()
    conexao.close()


def calcularIMC():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    peso = float(entry_peso.get())
    altura = int(entry_altura.get())

    #converte cm para m
    alturaMetros = altura/100
    
    #calculo IMC
    imc = peso/(alturaMetros*alturaMetros)

    #define o status
    if(imc < 17):
        status = "Muito abaixo do peso"
    elif(imc < 18.5):
        status = "Abaixo do peso"
    elif(imc < 25):
        status = "Peso normal"
    elif(imc < 30):
        status = "Acima do peso"
    elif(imc < 35):
        status = "Obesidade I"
    elif(imc < 40):
        status = "Obesidade III (severa)"
    else:
        status = "Obesidade III (mórbida)"
    
    #exibe resultado
    resultado.config(text=f"O paciente {nome}\n residente no endereço {endereco}\n possui um IMC de {imc:.2f} ({status}).") 

def reiniciar():
    entry_nome.delete(0,END)
    entry_endereco.delete(0,END)
    entry_altura.delete(0,END)
    entry_peso.delete(0,END)
    resultado.config(text="Resultado: ")

#cria janela da aplicação
janela = Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")
#janela.geometry("400x200+550+300")

#cria os labels
label_nome = Label(janela, text="Nome do Paciente: ")
label_endereco = Label(janela, text="Endereço Completo: ")
label_altura = Label(janela, text="Altura (cm): ")
label_peso = Label(janela, text="Peso (Kg): ")
separador = Label(janela, text ="---------------------------------------------------")
resultado = Label(janela, text="Resultado: ")

#cria as entradas
entry_nome = Entry(janela)
entry_endereco = Entry(janela)
entry_altura = Entry(janela)
entry_peso = Entry(janela)

#cria os buttons
button_calcular = Button(janela, text="Calcular", command=calcularIMC)
button_reiniciar = Button(janela, text="Reiniciar", command=reiniciar)
button_sair = Button(janela, text="Sair", command=exit)

#organiza os componentes na janela
label_nome.grid(row=0, column=0)
entry_nome.grid(row=0, column=1)

label_endereco.grid(row=1, column=0)
entry_endereco.grid(row=1, column=1)

label_altura.grid(row=2, column=0)
entry_altura.grid(row=2, column=1)

label_peso.grid(row=3, column=0)
entry_peso.grid(row=3, column=1)

separador.grid(row=4, columnspan=5)

resultado.grid(row=5, column=1)

button_calcular.grid(row=6, column=0)
button_reiniciar.grid(row=6, column=1)
button_sair.grid(row=6, column=2)

janela.mainloop()
