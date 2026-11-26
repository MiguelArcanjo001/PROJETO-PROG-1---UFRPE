import dialogos.textos as txt
import json
import os
import dialogos.textos as txt
import personagens.personagens as p
from personagens.personagens import zeladora
import Funcoes.funcoes as f
from Funcoes.funcoes import inicio,CAP1, sala_do_chefe, copa, trabalhadores, SDD,troca_gatilho,CACHORRO,ARMANDO, SDP, FEP,SSC, GFE, SSB, STI, MEC, BM, CAP3, CAP4A, CAP4B





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

def salvar(cena) :
    dados = {
        "cena" : cena,
        "estado" : f.estado,
        "inventario" : zeladora["inventario"]
    }
    arquivo = open("save.json", "w", encoding="utf-8")
    json.dump(dados, arquivo)
    arquivo.close()


def carregar() :
    arquivo = open("save.json", "r", encoding="utf-8")
    dados = json.load(arquivo)
    arquivo.close()
    f.estado.update(dados["estado"])
    zeladora["inventario"] = dados["inventario"]
    return dados["cena"]


if os.path.exists("save.json") :
    print("1 -- Continuar")
    print("2 -- Novo jogo")
    escolha = f.perguntar([1,2])
    if escolha == 1 :
        cena = carregar()
    else :
        cena = f.inicio()
else :
    cena = f.inicio()

while cena != "FIM" :
    salvar(cena)
    cena = cenas[cena](txt,p)

os.remove("save.json")

