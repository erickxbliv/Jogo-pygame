class dados:
    def __init__(self):
        #sempre seguir a mesma ordem: elevador, quarto...


        #quantidade
        self.qtd_EQCAEDRT = [1,6,0,0,0,0,0,0] #eu pensei em isso alterar com a dificuldade mas melhor n
        #salas com nivel maior nao podem aumentar a quantidade se nao o preco pra construir novas se elevaria demais
        #preco
        self.cnsm_EQCAEDRT = [0,0,0,0,0,0,0,0]
        #pagina1 = ["elevador","quarto","comida","agua"]
        #pagina2 = ["eletricidade","dinheiro","radio","treinamento"]
    
        self.pagina0 = [100//4,200//4,200//4,200//4]
        self.pagina1 = [200//4,100//4,300//4,500//4]

        self.preco = [[100,200,200,200],[200,100,300,500]]
        self.precoatual = None


        self.testeduplas = []
        self.testetrios = []

    def aumentar_qtd(self, id_sala):
        self.qtd_EQCAEDRT[id_sala] += 1
        if (id_sala // 3) < 1:
            self.preco[0][id_sala] = (self.pagina0[id_sala] * (self.qtd_EQCAEDRT[id_sala]-1)) + (self.pagina0[id_sala] * 4)
        else:
            self.preco[1][id_sala-4] += (self.pagina1[id_sala-4] * self.qtd_EQCAEDRT[id_sala]) + (self.pagina0[id_sala] * 4)
