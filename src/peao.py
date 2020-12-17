from db import base
from src.excecoes import InputError
from db.dominioTabelas import Session, atualizarBD, Peao


def criarPeoes():
    try:
        excecao = InputError()
        cores = base.peoesCoresDisponiveis
        posicao = 0
        for cor in cores:
            for i in range(4):
                codigo = excecao.gerarCodigoPeao()
                print(armazenaPeao(codigo, cor, posicao))
        return 0

    except:
        return 1


def armazenaPeao(codigo, corPeao, posicao, nojogo=True):
    try:
        session = Session()
        peao = Peao(codigo=codigo, cor=corPeao, posicao=posicao, nojogo=nojogo)
        session.add(peao)
        atualizarBD()
        return 0
    except:
        return 1

def coresDisponiveis():
    cores = base.peoesCoresDisponiveis
    return cores


def removeCor(cor):
    cores = base.peoesCoresDisponiveis
    cores.remove(cor)
    base.peoesCoresDisponiveis = cores
