import dialogos.textos as txt
import time
import personagens.personagens as p
from personagens.personagens import zeladora
import dialogos.desenhos as D



estado = {
    "sdd_visitada" : False,
    "voltar_chefe_usado" : False,
    "sdp_visitada" : False,
    "grito_usado" : False,
    "fep_visitada" : False,
    "armando_concluido" : False,
    "charadas_perguntadas" : False,
    "ssc_visitada" : False,
    "cachorro_concluido" : False,
    "gfe_visitada" : False,
    "bm_vencida" : False,
    "mata_leao_usado" : False,
    "grade_aberta" : False,
    "ssb_visitada" : False,
    "ti" : "nao_visitada",
    "mec_visitada" : False
}

def perguntar(validas) :
    while True :
        resposta = input("escolha entre " + ", ".join(str(v) for v in validas) + " : ")
        if resposta.isdigit() and int(resposta) in validas :
            return int(resposta)
        print("opcao invalida, tente de novo.")

def inicio() : 
    
    print(txt.bem_vindo)
    time.sleep(1)
    print("-" *30)
    print("CAPITULO 1")
    print("-" *30)
    print(D.bazinga)
    time.sleep(3)
    print(txt.intro)
    print(D.main)
    time.sleep(2)
    return "CAP1"
    
## capitulo 1

def CAP1(txt,p) :
    print(txt.escolha)
    print("1 -- Ir para a sala do seu chefe")
    print("2 -- Ir até a copa")
    escolha = perguntar([1,2])
    print(D.main_2)
    if escolha == 1 :
        return "SALA_CHEFE"
    return "COPA"

def sala_do_chefe(txt,p) : 
    print(txt.ir_sala_chefe)
    time.sleep(3)
    print("Seu chefe, Sr. Wag. A. Bündo Bichstenbäuer, pede para que você se sente.")
    print(D.chefe)
    print(txt.escolha)
    print("Pedir para sair mais cedo [1]")
    print("Pedir para sair mais cedo [2]")
    print("Nao tem outra opcão,voce precisa estar presente no aniversário de sua filha, custe o que custar! Pedir para sair mais cedo. [3]")
    perguntar([1,2,3])
    print(txt.resposta_do_chefe)
    time.sleep(6)
    print(D.caindo_alcapao)
    print("voce cai....")
    time.sleep(7)
    return "SDD"
    
def SDD(txt,p) :
    if estado["sdd_visitada"] == False :
        print("-" *30)
        print("CAPITULO 2")
        print("-" *30)
        time.sleep(5)
        print(txt.queda)
        time.sleep(3)
        print(txt.queda_2)
        print(D.corredor_iluminado)
        time.sleep(3)   
        estado["sdd_visitada"] = True
    else :
        print("Você está de volta à Sala de Descarte.")
        time.sleep(2)

    while True :
        print(txt.escolha)
        print("1 -- Seguir pelo corredor")
        print("2 -- Descer as escadas")
        if estado["voltar_chefe_usado"] == False :
            print("3 -- Voltar para a sala do chefe")
            escolha = perguntar([1,2,3])
        else :
            escolha = perguntar([1,2])

        if escolha == 1 :
            return "GFE"
        elif escolha == 2 :
            return "SDP"
        elif escolha == 3 :
            print("Você olha para o buraco de onde caiu e percebe que voltar para sala do chefe talvez seja um esforço estupidamente árduo, renderá uma quantidade estupidamente pequena de frutos e lhe fará parecer estupidamente estúpida.")
            time.sleep(3)
            estado["voltar_chefe_usado"] = True
            
            
    
    
    
def copa(txt,p) :
    print(D.copa)
    print("voce escolheu ir para a copa")
    print(txt.ir_copa)
    time.sleep(3)
    print(txt.ir_copa_2)
    time.sleep(3)
    print(txt.ir_copa_3)
    time.sleep(3)
    print(txt.ir_copa_4)
    time.sleep(3)

    if "TRELOSO" not in zeladora["inventario"] :
        zeladora["inventario"].append("TRELOSO")

    print(txt.escolha)
    print("1 -- Ir para a sala do seu chefe")
    print("2 -- Falar com os trabalhadores")
    escolha = perguntar([1,2])
    if escolha == 1 :
        return "SALA_CHEFE"
    return "TRABALHADORES"
    
def trabalhadores(txt,p) :
    print(txt.ir_trabalhadores)
    time.sleep(3)
    print("Eles perguntam se voê quer saber sobre o que eles estavam conversando.")
    print(txt.escolha)
    print("1 -- Ficar e saber mais")
    print("2 -- Recusar e ir falar com o seu chefe")
    escolha = perguntar([1,2])
    if escolha == 2 :
        return "SALA_CHEFE"

    print(txt.conversa_trabalhadores_1)
    time.sleep(3)
    print(txt.conversa_trabalhadores_2)
    time.sleep(3)
    print(txt.escolha)
    print("1 -- Trocar o pacote de TRELOSO pelo GATILHO")
    print("2 -- “Gatilho legal! Enfim, vou indo nessa…”")
    escolha = perguntar([1,2])
    if escolha == 1 :
        return "TROCA_GATILHO"
    return "SALA_CHEFE"
        
def troca_gatilho(txt,p) :
    print(txt.conversa_trabalhadores_3)
    print(D.gatilho)
    time.sleep(3)
    if "TRELOSO" in zeladora["inventario"] :
        zeladora["inventario"].remove("TRELOSO")
    if "GATILHO" not in zeladora["inventario"] :
        zeladora["inventario"].append("GATILHO")
    return "SALA_CHEFE"
        
## capitulo 2

def SDP(txt,p) :
    if estado["sdp_visitada"] == False :
        print(txt.SDP_1)
        print(D.fenda_na_parede)
        time.sleep(5)
        estado["sdp_visitada"] = True
    else :
        print("Você está de volta à Sala de Punição.")
        time.sleep(2)

    while True :
        print(txt.escolha)
        print("1 -- Se escorar dentro da Fenda Estranha Pedrosa")
        if estado["grito_usado"] == False :
            print("2 -- Gritar que o chefe vai chamar alguém para um sermão")
            print("3 -- Voltar para a Sala de Descarte")
            escolha = perguntar([1,2,3])
        else :
            print("2 -- Voltar para a Sala de Descarte")
            escolha = perguntar([1,2])
            if escolha == 2 :
                escolha = 3

        if escolha == 1 :
            return "FEP"
        elif escolha == 2 :
            print(txt.grito_SDP)
            time.sleep(5)
            estado["grito_usado"] = True
        elif escolha == 3 :
            return "SDD"


def FEP(txt,p) :
    if estado["fep_visitada"] == False :
        print(txt.chegada_FEP)
        print(D.homem_cachorro)
        time.sleep(5)
        estado["fep_visitada"] = True
    else :
        print("Você está de volta à Fenda Estranha Pedrosa.")
        time.sleep(2)

    print(txt.escolha)
    print("1 -- Falar com o homem")
    print("2 -- Inspecionar o cachorro")
    print("3 -- Voltar para a Sala de Punição")
    escolha = perguntar([1,2,3])
    if escolha == 1 :
        return "ARMANDO"
    elif escolha == 2 :
        return "SSC"
    return "SDP"


def ARMANDO(txt,p) :
    if estado["armando_concluido"] == True :
        print(txt.dH1)
        time.sleep(3)
        return "FEP"

    print(txt.dialogo_1_H1)
    time.sleep(5)
    print(txt.dialogo_2_H1)
    time.sleep(5)

    while True :
        print(txt.escolha)
        print("1 -- Responder as perguntas")
        print("2 -- “Nam, valeu… :/”")
        if estado["charadas_perguntadas"] == False :
            print("3 -- Qual é a das charadas?")
            escolha = perguntar([1,2,3])
        else :
            escolha = perguntar([1,2])

        if escolha == 1 :
            charadas = [txt.armando1, txt.armando2, txt.resposta1, txt.armando3, txt.armando4, txt.resposta2, txt.armando5, txt.resposta3, txt.armando6, txt.resposta4, txt.armando7, txt.armando8, txt.resposta5, txt.armando9, txt.resposta6, txt.armando10]
            for fala in charadas :
                print(fala)
                time.sleep(3)
            print(txt.agradecimento)
            time.sleep(3)
            print(txt.fimdH1)
            print(D.chave_engracada)
            time.sleep(3)
            if "CHAVE ENGRACADA" not in zeladora["inventario"] :
                zeladora["inventario"].append("CHAVE ENGRACADA")
            estado["armando_concluido"] = True
            return "FEP"
        elif escolha == 2 :
            return "FEP"
        elif escolha == 3 :
            print("Armando fala que na cela especial de punição dele a única coisa que ele tinha era esse livro com mais de 200 super piadas e charadas que ele leu e releu centenas de vezes. Fazer algo para pôr elas em uso seria legal, ao mesmo tempo ele se livra desse peso de papel que é essa CHAVE ENGRAÇADA.")
            time.sleep(5)
            estado["charadas_perguntadas"] = True


def SSC(txt,p) :
    if estado["ssc_visitada"] == False :
        print(txt.SSC1)
        time.sleep(3)
        print(txt.SSC2)
        time.sleep(3)
        estado["ssc_visitada"] = True
    else :
        print("Você está de volta à Sala Secreta Canina.")
        time.sleep(2)

    print(txt.escolha)
    print("1 -- Voltar de onde veio")
    print("2 -- Conversar com o cachorro")
    escolha = perguntar([1,2])
    if escolha == 1 :
        return "FEP"
    return "CACHORRO"


def CACHORRO(txt,p) :
    if estado["cachorro_concluido"] == True :
        print("“Boa sorte”")
        time.sleep(3)
        return "SSC"

    if "OVO COZIDO" in zeladora["inventario"] :
        print(txt.cachorro1_1)
        time.sleep(3)
        print(txt.cachorro1_2)
        time.sleep(3)
        print(txt.cachorro1_3)
        print(D.cano)
        time.sleep(3)
        zeladora["inventario"].remove("OVO COZIDO")
        zeladora["inventario"].append("CANO")
        estado["cachorro_concluido"] = True
        return "SSC"

    print(txt.cachorro1)
    time.sleep(5)
    print(txt.cachorro2)
    time.sleep(3)
    print('zeladoraa: " Ok ".')
    return "SSC"


def GFE(txt,p) :
    if estado["gfe_visitada"] == False :
        print(txt.chegada_GFE)
        time.sleep(5)
        estado["gfe_visitada"] = True
    else :
        print("Você está de volta à Grade Férrea Engraçada.")
        time.sleep(2)

    while True :
        print(txt.escolha)
        if estado["mata_leao_usado"] == False :
            print("1 -- Dar um mata-leão no Tadeo, pra ele ficar esperto")
        print("2 -- Inspecionar o cadeado engraçado")
        print("3 -- Voltar para a Sala de Descarte")

        if estado["mata_leao_usado"] == False :
            escolha = perguntar([1,2,3])
        else :
            escolha = perguntar([2,3])

        if escolha == 1 :
            print("A tentação é grande.")
            time.sleep(3)
            estado["mata_leao_usado"] = True
        elif escolha == 2 :
            if estado["grade_aberta"] == True :
                print("O cadeado já está aberto. Você segue pelo corredor.")
                time.sleep(2)
                return "SSB"
            elif "CHAVE ENGRACADA" in zeladora["inventario"] :
                print(txt.ce1)
                time.sleep(3)
                print(txt.tadeo_tambor)
                print(D.tambor)
                time.sleep(3)
                zeladora["inventario"].append("TAMBOR")
                estado["grade_aberta"] = True
                return "SSB"
            else :
                print(txt.ce0)
                time.sleep(3)
        elif escolha == 3 :
            return "SDD"


def SSB(txt,p) :
    if estado["ssb_visitada"] == False :
        print(txt.chegada_SSB)
        time.sleep(5)
        estado["ssb_visitada"] = True
    else :
        print("Você está de volta à Simples e Silenciosa Bifurcação.")
        time.sleep(2)

    print(txt.escolha)
    print("1 -- Seguir pelo corredor")
    print("2 -- Entrar na sala do TI")
    print("3 -- Voltar pelo corredor")
    escolha = perguntar([1,2,3])
    if escolha == 1 :
        return "MEC"
    elif escolha == 2 :
        return "STI"
    return "GFE"


def STI(txt,p) :
    if estado["ti"] == "recusou" :
        print(txt.sti_recusado)
        time.sleep(3)
        return "SSB"
    elif estado["ti"] == "aceitou" :
        print(txt.sti_depois)
        time.sleep(3)
        return "SSB"
    print(D.caras_do_ti)
    print(D.caras_do_ti_2)

    falas = [txt.sti1, txt.sti_r1, txt.sti2, txt.sti_r2, txt.sti3, txt.sti_r3, txt.sti4, txt.sti5]
    for fala in falas :
        print(fala)
        time.sleep(3)

    print(txt.escolha)
    print("1 -- Aceitar")
    print("2 -- Recusar")
    escolha = perguntar([1,2])
    if escolha == 2 :
        print(txt.sti_X)
        time.sleep(3)
        estado["ti"] = "recusou"
        return "SSB"

    print(txt.sti_V1)
    time.sleep(5)
    print(txt.sti_V2)
    time.sleep(5)
    print(txt.sti_V3)
    print(D.cabo)
    time.sleep(3)
    zeladora["inventario"].append("CABO")
    zeladora["inventario"].append("CAO")
    estado["ti"] = "aceitou"
    return "SSB"


def MEC(txt,p) :
    if estado["mec_visitada"] == False :
        print(txt.chegada_MEC)
        print(D.menina_com_espada)
        time.sleep(5)
        estado["mec_visitada"] = True
    else :
        print("Você está de volta ao Magnífico Elevador Cromado.")
        time.sleep(2)

    print(txt.escolha)
    print("1 -- Voltar para a Simples Silenciosa Bifurcação")
    if estado["bm_vencida"] == False :
        print("2 -- ( ! ) Entrar no elevador")
    else :
        print("2 -- Entrar no elevador")
    escolha = perguntar([1,2])
    if escolha == 1 :
        return "SSB"
    if estado["bm_vencida"] == True :
        print(txt.bm_fim2)
        time.sleep(3)
        return "CAP3"
    return "BM"


def BM(txt,p) :
    falas = [txt.bm1, txt.bm2, txt.bm_r1, txt.bm3, txt.bm_r2, txt.bm4, txt.bm5]
    for fala in falas :
        print(fala)
        time.sleep(3)

    print("-" *30)
    print("LUTA! LUTA! LUTA!")
    print("Vs. Menina Porteira Espadachim!!!")
    print("-" *30)
    time.sleep(5)

    print(txt.escolha)
    print("1 -- Usar os sprays dentro das caixas para cegar ela.")
    print("2 -- Força bruta. Desferir outro soco direcionado.")
    print("3 -- Preparar um ácido forte com os produtos de limpeza.")
    perguntar([1,2,3])

    print(txt.bm_luta1)
    time.sleep(3)
    print(txt.bm_luta2)
    time.sleep(3)
    print("...")
    time.sleep(2)
    print("VITÓRIA!!!")
    time.sleep(3)
    print(txt.bm_drops)
    time.sleep(2)
    print("1 -- Continuar")
    perguntar([1])

    print(txt.bm_fim)
    time.sleep(3)
    zeladora["inventario"].append("OVO COZIDO")
    zeladora["inventario"].append("CHAVE DO ELEVADOR")
    estado["bm_vencida"] = True
    return "MEC"
    

## CAPITULO 3

def CAP3(txt,p) :
    print("-" *30)
    print("CAPITULO 3")
    print("-" *30)
    time.sleep(5)

    print(txt.cap3_1)
    print(D.marcelo)
    time.sleep(3)
    print(txt.cap3_r1)
    time.sleep(2)
    print(txt.cap3_m1)
    time.sleep(5)
    print(txt.cap3_r2)
    time.sleep(2)
    print(txt.cap3_m2)
    time.sleep(4)
    print(txt.cap3_m3)
    time.sleep(4)
    print(txt.cap3_m4)
    time.sleep(3)

    pecas = ["GATILHO","CANO","TAMBOR","CABO","CAO"]
    tem_todas = True

    for peca in pecas :
        if peca not in zeladora["inventario"] :
            tem_todas = False

    if tem_todas == True :
        print(txt.cap3_roxo_r)
        time.sleep(2)
        print(txt.cap3_roxo1)
        print(D.sonega)
        time.sleep(4)
        print(txt.cap3_roxo2)
        time.sleep(4)
        print(txt.cap3_roxo3)
        time.sleep(4)
        print(txt.cap3_roxo4)
        time.sleep(4)
        print(txt.cap3_salao)
        time.sleep(5)
        print(txt.escolha)
        print("1 -- Fazer que nem o Pistoleiro Papaco e se despedir desse paspalho “Até um outro dia”.")

        while True :
            escolha = int(input("digite 1 para continuar : "))
            if escolha == 1 :
                return "CAP4A"

    else :
        print(txt.cap3_laranja_r)
        time.sleep(2)
        print(txt.cap3_laranja1)
        time.sleep(3)
        print(txt.cap3_laranja2)
        time.sleep(6)
        print(txt.cap3_laranja3)
        time.sleep(4)
        print(txt.cap3_laranja4)
        time.sleep(3)
        print(txt.cap3_salao)
        time.sleep(5)
        print(txt.escolha)
        print("1 -- Fazer como em Maze Runner e… correr? Você nunca viu esses filmes, só via os cartazes deles no cinema e achava legais. Enfim, é agora ou nunca.")

        while True :
            escolha = int(input("digite 1 para continuar : "))
            if escolha == 1 :
                return "CAP4B"


def CAP4A(txt,p) :
    print("-" *30)
    print("CAPITULO 4")
    print("-" *30)
    time.sleep(5)

    print(txt.cap4a_1)
    time.sleep(5)
    print(txt.cap4a_2)
    print(D.bolo_aniversario)
    time.sleep(6)
    print(txt.cap4a_3)
    time.sleep(6)
    print(txt.cap4a_4)
    time.sleep(5)
    return "FIM"


def CAP4B(txt,p) :
    print("-" *30)
    print("CAPITULO 4")
    print("-" *30)
    print(txt.cap4b_1)
    time.sleep(6)
    print(txt.cap4b_2)
    time.sleep(6)
    print(txt.cap4b_3)
    time.sleep(5)
    print(txt.cap4b_4)
    time.sleep(5)
    print("…")
    time.sleep(4)
    print(txt.cap4b_5)
    time.sleep(6)
    return "FIM"
            
                
                
                        
                
                            
                        
        
    


            
        
        
        
