from time import sleep

laluno = []
lmatricula = []
ln1 = []
ln2 = []
lmedia = []
lcadastro = [laluno, lmatricula, ln1, ln2, lmedia]

aluno = 0
matricula = 0
n1 = 0
n2 = 0
media = 0
alterarAluno = 0
alterarN1 = 0
alterarN2 = 0
alterarMedia = 0
salvarCasdastro = 0

def menu():
    print('==========MENU===========')
    print('1 - Matricular Aluno')
    print('2 - Excluir')
    print('3 - Alterar')
    print('4 - Situação do aluno')
    print('5 - Pesquisar')
    print('6 - Listar Alunos matriculados')
    print('7 - Ver Cadastro')
    print('8 - Sair')
    print('========================\n')
    op = input('Digite a opção que deseja realizar: \n')
    return op

def adiocionarMatricula():
    aluno = str(input('Digite  o nome do aluno: ')).strip()
    aluno = aluno.upper()
    if aluno in laluno:
        print('Aluno já está matriculado')
    else:
        laluno.append(aluno)
        matricula = int(input('Digite a matricula do aluno: '))
        lmatricula.append(matricula)
        print('Aguarde...')
        sleep(3)
        print('Aluno Matriculado com sucesso!')
    pass

def excluir():
    aluno = str(input('Digite o nome do aluno: ')).strip()
    aluno = aluno.upper()
    if aluno in laluno:
        laluno.remove(aluno)
        lmatricula.clear()
        ln1.clear()
        ln2.clear()
        lmedia.clear()
        print('Removendo aluno....')
        sleep(1)
        print('Aluno removido com sucesso!')
    else:
        print('Esse aluno não está matriculado, ou já foi removido')
    pass

def removeAll():
    laluno.clear()
    ln1.clear()
    ln2.clear()
    lmedia.clear()
    pass

def alterar():
    alterarAluno = str(input('Digite o nome do aluno: ')).strip()
    alterarAluno = alterarAluno.upper()
    alterarN1 = float(input('Digite a primeira nota do aluno: '))
    alterarN2 = float(input('Digite a seunda nota do aluno: '))
    alterarMedia = ((alterarN1 + alterarN2) / 2)
    if aluno == alterarAluno:
        print('Aluno não existe, por tanto, não é possível alterar!')
    else:
        removeAll()

        laluno.append(alterarAluno)
        ln1.append(alterarN1)
        ln2.append(alterarN2)
        lmedia.append(alterarMedia)

        print('Alterando...')
        sleep(3)
        print('Cadastro alterado com sucesso')
    pass

def situacaoAluno():
    aluno = str(input('Digite o nome do aluno: ')).strip()
    aluno = aluno.upper()
    if aluno in laluno:
        n1 = float(input('Digite a primeira nota do aluno: '))
        n2 = float(input('Digite a segunda nota do aluno: '))
        media = ((n1 + n2) / 2)
        ln1.append(n1)
        ln2.append(n2)
        lmedia.append(media)
        print(media)
        if media >= 7:
            print('Aprovado')
        elif 4 <= media < 7:
            print('Exame')
            print('Aguarde...')
            sleep(3)
            print('Prova Final')
            media = float(input('Digite a nota da prova final do aluno: '))
            if media >= 5:
                print('Aprovado na prova final')
            else:
                print('Reprovado na prova final')
        elif media < 4:
            print('Reprovado')
    pass

def pesquisar():
    aluno = str(input('Digite o nome ou matricula que deseja pesquisa pelo aluno: ')).strip()
    aluno = aluno.upper()
    if aluno in laluno:
        print('Pesquisando por aluno...')
        sleep(2)
        print('Aluno: {}, matricula: {}, primeira nota: {}, segunda nota: {}, media: {}'.format(laluno, lmatricula, ln1, ln2, lmedia))
    else:
        print('Aluno não existe!')
    pass

def listarAlunos():
    print('Listando alunos matriculados...')
    sleep(2)
    print('Alunos matriculados ', laluno)
    pass

def leCadastro():
    print(lcadastro)
    pass

def maniArq():
    arq = open('dados.txt', 'a')
    arq.write('\nDados dos Alunos Cadastrados: \n')
    arq.writelines('Aluno: {}, matricula: {}, primeira nota: {}, segunda nota: {}, média: {}'.format(laluno, lmatricula, ln1, ln2, lmedia))
    arq.close()
    pass

def salvarCadastro():
    salvar = str(input('Deseja salvar o cadastro?'))
    print('Aguarde...')
    sleep(3)
    if salvar == 'sim':
        maniArq()
        print('Cadastro Salvo com sucesso')
    elif salvar == 'nao':
        print('Cadastro cancelado')
    pass

opcao = menu()
while opcao != '8':
    if opcao == '1':
        adiocionarMatricula()
    elif opcao == '2':
        excluir()
    elif opcao == '3':
        alterar()
    elif opcao == '4':
        situacaoAluno()
    elif opcao == '5':
        pesquisar()
    elif opcao == '6':
        listarAlunos()
    elif opcao == '7':
        leCadastro()
    opcao = menu()
salvarCadastro()
