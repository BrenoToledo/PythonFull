from DAO import *
from Models import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler

        for i in x:
            if i.categoria == novaCategoria :
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso!")
        else:

            print("A Categoria que deseja cadastrar já existe!")

    def removerCategoria(self,categoriaRemover):
        listaCategoria =  DaoCategoria.ler()
        categoriasEncontradas = list(filter(lambda x: x.categoria == categoriaRemover, x ))

        if  len(categoriasEncontradas) >0:
            print("A categoria que deseja remover não existe !")

        else:
            
            for i in range(len(listaCategoria)):
                if listaCategoria[i].categoria == categoriasEncontradas:
                    del listaCategoria[i]
                    break
                print('Categoria Removida com sucesso')

                with open('categoria.txt', 'w') as arq:
                    for i in listaCategoria :
                         arq.writelines(i.categoria)
                         arq.writelines('\n')