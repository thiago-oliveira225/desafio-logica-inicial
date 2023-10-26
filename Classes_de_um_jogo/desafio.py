class Heroi:
    
    ## CRIANDO UM MÉTODO CONSTRUTOR, OU SEJA, A FORMA DO OBJETO FUTURO
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


    ## CRIANDO UM MÉTODO, OU SEJA, ALGUMA COISA PARA FAZER COM OS ATRIBUTOS DEFINIDOS ACIMA
    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        print(f"O {self.tipo} atacou usando {ataque}")
            

    ## CRIANDO UM OUTRO MÉTODO, OU SEJA, ALGUMA OUTRA COISA PARA FAZER COM OS ATRIBUTOS DEFINIDOS ACIMA    

heroi = Heroi("Thiago", 28, "guerreiro")

heroi.atacar()
        