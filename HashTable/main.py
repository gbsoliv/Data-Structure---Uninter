class NodoListaSimples:
    def __init__(self, sigla=None, nomeEstado=None):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir(self, sigla, nomeEstado):
        nodo = NodoListaSimples(sigla, nomeEstado)
        if self.head == None:
            self.head = nodo
            return 0
        else:
            nodo.proximo = self.head
            self.head = nodo 
            return 0
        
    def imprimir(self):
        nodo = self.head
        while nodo != None:
            print(f'Sigla: {nodo.sigla}, Nome: {nodo.nomeEstado}')
            nodo = nodo.proximo


class TabelaHash:
        def __init__(self):
          self.tam = 10
          self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]

        def hashFunction(self, k):
            if k == "DF":
                return 7
            k = list(k)
            return (ord(k[0]) + ord(k[1])) % self.tam

        def inserir(self, sigla, nomeEstado):
            pos = self.hashFunction(sigla)
            add = self.h[pos].inserir(sigla, nomeEstado)


        def imprimir(self):
            for i in range(0, self.tam):
                print(f'{i}: ', end='')
                nodo = self.h[i].head
                while nodo != None:
                    print(f'{nodo.sigla} -> ', end='')
                    nodo = nodo.proximo
                print('None')




tabela = TabelaHash() 

tabela.inserir("SC", "Santa Catarina")
tabela.inserir("RN", "Rio Grande do Norte")
tabela.inserir("MS", "Mato Grosso do Sul")
tabela.inserir("GO", "Goias") 
tabela.inserir("RO", "Rondonia") 
tabela.inserir("MT", "Mato Grosso") 
tabela.inserir("BA", "Bahia") 
tabela.inserir("AL", "Alagoas") 
tabela.inserir("SE", "Sergipe") 
tabela.inserir("PR", "Parana") 
tabela.inserir("MA", "Maranhao") 
tabela.inserir("ES", "Espirito Santo") 
tabela.inserir("AM", "Amazonas") 
tabela.inserir("AC", "Acre") 
tabela.inserir("TO", "Tocantins") 
tabela.inserir("SP", "Sao Paulo") 
tabela.inserir("PI", "Piaui") 
tabela.inserir("RR", "Roraima") 
tabela.inserir("RS", "Rio Grande do Sul") 
tabela.inserir("PA", "Para") 
tabela.inserir("AP", "Amapa") 
tabela.inserir("RJ", "Rio de Janeiro") 
tabela.inserir("PB", "Paraiba") 
tabela.inserir("CE", "Ceara") 
tabela.inserir("DF", "Distrito Federal") 
tabela.inserir("MG", "Minas Gerais") 
tabela.inserir("PE", "Pernambuco") 

tabela.inserir("GO", "Gabriela Aparecida Menezes de Oliveira") 

tabela.imprimir()
