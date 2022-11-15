class dados:
    def __init__(self):
        #sempre seguir a mesma ordem: elevador, quarto...
        #a maioria desses dados so se atualiza no erguer, atualizar ou demolir!!!

        #quantidade
        self.qtd_EQCAEDRT = [1,6,0,0,0,0,0,0] #eu pensei em isso alterar com a dificuldade mas melhor n
        #salas com nivel maior nao podem aumentar a quantidade se nao o preco pra construir novas se elevaria demais
        #preco
        self.cnsm_EQCAEDRT = [10,15,20,20,5,20,30,30] #isso ja ta certo
        self.cosumo = None
        #pagina1 = ["elevador","quarto","cozinha","tratamento"]
        #pagina2 = ["gerador","renda","laboratorio","treinamento"]      #cancelei radio
    
        self.producao = [0,0,0,0,10,0,0,0]
        self.pagina0 = [100//4,80//4,200//4,200//4]
        self.pagina1 = [200//4,100//4,200//4,500//4]

        self.preco = [[100,80,200,200],[200,100,200,500]]
        self.precoatual = None

        self.lucrodia = None
        #self.totaldwellers = None

        self.gastoagua = self.gastocomida = 20   #por pessoa
        self.minimo = 10 #quando cada pessoa tem menos do minimo a barra fica vermelha, que e metade dos gastos

        #self.testeduplas = []
        #self.testetrios = []

    def aumentar_qtd(self, id_sala):
        self.qtd_EQCAEDRT[id_sala] += 1
        if (id_sala // 3) < 1:
            self.preco[0][id_sala] = (self.pagina0[id_sala] * (self.qtd_EQCAEDRT[id_sala]-1)) + (self.pagina0[id_sala] * 4)
        else:
            self.preco[1][id_sala-4] = (self.pagina1[id_sala-4] * self.qtd_EQCAEDRT[id_sala-4]) + (self.pagina0[id_sala-4] * 4)
    
    def calcconsumo(self):
        self.consumo = 0
        qtd = 0
        while qtd < 8:
            self.consumo += (self.qtd_EQCAEDRT[qtd] * self.cnsm_EQCAEDRT[qtd])
            qtd += 1

