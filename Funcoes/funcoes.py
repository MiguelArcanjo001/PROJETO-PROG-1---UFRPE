import dialogos.textos as txt
import time
import personagens.personagens as p

def inicio() : 
    print(txt.bem_vindo)
    time.sleep(1)
    print(txt.intro)
    time.sleep(2)
    
## capitulo 1

def sala_do_chefe(txt) : 
    print(txt.ir_sala_chefe)
    time.sleep(3)
    print("Seu chefe, Sr. Wag. A. Bündo Bichstenbäuer, pede para que você se sente.")
    print("oque voce vai fazer agora?")
    
    print("- " * 30)
    print("Se escorar dentro da Fenda Estranha Pedrosa [FEP]")
    print("> Gritar que o chefe está vai chamar alguém para um sermão*")
    print("> Voltar para a Sala de Descarte [SDD]")
    print("- " * 30)
    
def copa(txt) :
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
    
def trabalhadores(txt,ir_sala_chefe) :
    print(txt.ir_trabalhadores)
    
    time.sleep(3)
    
    print("Eles perguntam se você quer saber sobre o que eles estavam conversando.")
    
    print("ficar e saber mais [3]")
    print("recusar e ir falar com o seu chefe[0]")
    resposta = int(input("escolha entre 3 e 0 : "))
    
    if resposta == 0  :
        ir_sala_chefe(txt)
    if resposta == 3 : 
        print(txt.conversa_trabalhadores_1)
        time.sleep(3)
        print(txt.conversa_trabalhadores_2)
        time.sleep(3)
        print("Trocar o pacote de TRELOSO pelo GATILHO [4]")
        print("“Gatilho legal! Enfim, vou indo nessa…” [0]")
        
def troca_gatilho(txt,ir_sala_chefe) :
    resposta = int(input("escolha entre 4 e 0 : "))
    if resposta == 0  :
        ir_sala_chefe(txt)
    if resposta == 4 :
        print(txt.conversa_trabalhadores_3)
