import time
import dialogos.textos as txt
import personagens.personagens as p

print(txt.bem_vindo)
time.sleep(1)
print(txt.intro)
time.sleep(2)

print(txt.intro_2)
time.sleep(2)

def Historia(p) : 
 resposta = None

 print(txt.escolha)


 print("Ir pra sala do chefe [0]")
 print("Ir até a copa [1]")
 resposta = int(input("escolha entre 0 e 1 : "))
 if resposta == 0  :
    print(txt.ir_sala_chefe)
 if resposta == 1 : 

    print("voce escolheu ir para a copa")

    print(txt.ir_copa)
    time.sleep(3)

    print(txt.ir_copa_2)
    time.sleep(3)

    print(txt.ir_copa_3)

    time.sleep(3)
    print(txt.ir_copa_4)

    time.sleep(3)
    print(txt.escolha)

    print("Ir para a sala do chefe [0]")

    print("Falar com os trabalhadres [2]")
    resposta = int(input("escolha entre 0 e 2 : "))

    if resposta == 0  :
        print(txt.ir_sala_chefe)
    if resposta == 2 : 
      print(txt.ir_trabalhadores)

      time.sleep(3)

      print("Eles perguntam se você quer saber sobre o que eles estavam conversando.")

      print("ficar e saber mais [3]")
      print("recusar e ir falar com o seu chefe[0]")
      resposta = int(input("escolha entre 3 e 0 : "))

      if resposta == 0  :
          print(txt.ir_sala_chefe)
      if resposta == 3 : 
        print(txt.conversa_trabalhadores_1)
        time.sleep(3)
        print(txt.conversa_trabalhadores_2)
        time.sleep(3)
        print("Trocar o pacote de TRELOSO pelo GATILHO [4]")
        print("“Gatilho legal! Enfim, vou indo nessa…” [0]")
        if resposta == 0  :
            print(txt.ir_sala_chefe)
        resposta = int(input("escolha entre 4 e 0 : "))
        if resposta == 0  :
         print(txt.ir_sala_chefe)
        if resposta == 4 :
            print(txt.conversa_trabalhadores_3)

            time.sleep(3)
            print("Olhando mais de perto, o GATILHO tem um “A” encravado em outro ponto… estranho…")
            time.sleep(2)
            
            print(txt.ir_sala_chefe) 

Historia()
      
    

      



