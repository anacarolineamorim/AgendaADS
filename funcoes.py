#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = raw_input("Nome do Contato:")
	telefone = raw_input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	
def listar():
	
print("Lista de Contatos")
agenda = open("agendatelefonica.csv")
numero = 0
lista = []
while numero < 25:
        lista.append(agenda.readline())
        print (agenda.readline())
        numero = numero + 1
print("Listado correctamente")	
agenda.close()
print(lista)


def falha():
	print("Opcao Incorreta")
