x=float(input("Digite a nota do aluno: "))

match x:
      case 7|8|9|10:
        print("aluno aprovado")
      case 5|6:
        print("aluno em recuperação")
      case 0|1|2|3|4:
        print("aluno reprovado")
      case _:
        if 7<=x<=10:
          print("aluno aprovado")
        elif 5<=x<=6:
          print("aluno em recuperação")
        elif 0<=x<=4:
          print("aluno reprovado")
        else:
          print("nota inválida ")
