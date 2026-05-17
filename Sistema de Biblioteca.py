def biblioteca():
    while True:
        
        escolha = int(input("1-Cadastrar livro \n2-Consultar livro \n3-Emprestar livro \n4-Devolver livro \n5-Listar livros \n0-Sair \nEscreva aqui:"))


        if escolha == 1:
            codigo = input("Escreva o código do livro:")
            titulo = input("Escreva o título do livro:")
            autor = input("Escreva o autor do livro:")

            with open("livros.txt","a") as file:
                file.write(codigo+";"+titulo+";"+autor+";"+"disponível"+"\n")
                file.close()

        elif escolha == 2:
            consulta = input("Escreva o código do livro que deseja consultar:")
            with open("livros.txt","r") as file:
                for linha in file:
                    if consulta in linha:
                        print(f"código encontrado: {linha.strip()}")
                        break
                else:
                    print("Código não encontrado!")


        
        elif escolha == 3:
            emprestar = input("Escreva o código do livro que deseja emprestar:")
            with open("livros.txt","r") as file:
                banco = file.readlines()

            with open("livros.txt","w") as file:
                encontrado = False
                for linha in banco:
                    livros = linha.strip().split(";")
                    if livros[0] == emprestar:
                        encontrado = True
                        if livros[3] == "disponível":
                            linha = linha.replace("disponível","emprestado")
                            print("O livro foi emprestado!")
    
                    file.write(linha)

            if not encontrado:
                print("Código não encontrado!")



        elif escolha == 4:
            devolver = input("Escreva o código do livro que deseja devolver:")
            with open("livros.txt","r") as file:
                banco = file.readlines()

            with open("livros.txt","w") as file:
                encontrado = False
                for linha in banco:
                    livros = linha.strip().split(";")
                    if livros[0] == devolver:
                        encontrado = True
                        if livros[3] == "emprestado":
                            linha = linha.replace("emprestado","disponível")
                            print("O livro foi devolvido!")
    
                    file.write(linha)

            if not encontrado:
                print("Código não encontrado!")



        elif escolha == 5:
            with open("livros.txt","r") as file:
                print(file.read())
  
        elif escolha == 0:
            print("Sistema fechado")
            break

        else:
            print("Escolha uma das escolhas!")
biblioteca()