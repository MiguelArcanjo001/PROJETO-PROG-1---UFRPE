import dialogos.textos as txt
import personagens.personagens as p
from Funcoes.funcoes import inicio,CAP1, sala_do_chefe, copa, trabalhadores, SDD,troca_gatilho,CACHORRO,ARMANDO, SDP, FEP,SSC, GFE, SSB, STI, MEC, BM, CAP3, CAP4A, CAP4B


def escolha_inicial(txt) :
    print(txt.escolha)
    print("1 -- Ir para a sala do seu chefe [SALA_CHEFE]")
    print("2 -- Ir até a copa [COPA]")

    while True :
        escolha = int(input("escolha entre 1 e 2 : "))
        if escolha == 1 :
            return "SALA_CHEFE"
        elif escolha == 2 :
            return "COPA"


cenas = {
    "CAP1" : CAP1,
    "COPA" : copa,
    "TRABALHADORES" : trabalhadores,
    "TROCA_GATILHO" : troca_gatilho,
    "SALA_CHEFE" : sala_do_chefe,
    "SDD" : SDD,
    "SDP" : SDP,
    "FEP" : FEP,
    "ARMANDO" : ARMANDO,
    "SSC" : SSC,
    "CACHORRO" : CACHORRO,
    "GFE" : GFE,
    "SSB" : SSB,
    "STI" : STI,
    "MEC" : MEC,
    "BM" : BM,
    "CAP3" : CAP3,
    "CAP4A" : CAP4A,
    "CAP4B" : CAP4B
}

cena = inicio()
while cena != "FIM" :
    cena = cenas[cena](txt,p)

