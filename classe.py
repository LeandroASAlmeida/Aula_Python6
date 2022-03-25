# Dependendo da empresa é bom usar CamelCase para Classes('MinhaCasa')

# pass # Permite passar um objeto vazio

# Criando os atributos da Classe atributos ja criados
class Veiculo:
    #    ano=2022
    #     cor='branco'
    #     protas= 4
    #     velMaxima= 260
    #     print(Veiculo.cor)

    # Construtor - Atributos de instância(Criação)
    # Metodo de classes
    def __init__(self, ano, cor, portas, velMaxima):  # __init__ = metodo magico
        self.ano = ano
        self.cor = cor
        self.portas = portas
        self.VelMaxima = velMaxima
        self.ligado = False
        self.totalMarchas = 5
        self.marcha = 0
        self.velocidade = 0
        self.MudarMarcha = 0

    def ligar(self, ligar=True):
        # O carro somente podera ser ligado se estiver no pornto neutro (marcha 0)
        if self.marcha == 0:
            if not (self.ligado):
                self.ligado = True
                self.MudarMarcha = True
                return 'Carro Ligado'
            return 'Carro ja esta Ligado'
        return 'O Carro precisa estar no ponto morto para ligar'

    def desligar(self):
        # O carro somente podera ser desligado se estiver no pornto neutro (marcha 0)
        if self.marcha == 0:
            if self.ligado:
                self.ligado = False
                self.MudarMarcha = False
                return 'Carro Desligado'
            return 'O Carro ja esta Desligado'
        return 'O Carro precisa estar no ponto morto para desligar'

        # O veiculo somente podera subir marcha até atingir a marcha maxima
        # A cada invocação de metodo deve mostrar em qual marcha esta
        # Somente podera subir marcha com o carro ligado

    def subirMarcha(self):
        if self.ligado:
            if self.marcha < self.totalMarchas:
                self.marcha += 1
                return 'Esta na marcha' + str(self.marcha)
            return 'Ja esta na marcha ' + str(self.marcha)
        return 'O carro precisa estar ligado para subir marcha'

    # O veiculo somente podera descer marcha até a marcha ré (-1)
    # A cada inovação do metodo deve mostrar em qual marcha esta.
    # Somente podera subir marcha com o carro ligado

    def descerMarcha(self):
        if self.ligado:
            if self.marcha > -1:
                self.marcha -= 1
                if self.marcha == -1:
                    return 'O carro esta na marcha ré'
                return 'Esta na marcha' + str(self.marcha)
            return 'O carro ja esta na marcha ré'
        return 'O carro precisa estar ligado para descer de marcha'

#########################################################################################################################
    
        #A cada acelarada sobe a velocidade em 20
        #-Velocidade-|- Marcha-
        #-20         | Ré
        #0           | Neutro
        #20          | 1
        #40          | 2
        #60          | 2
        #80          | 3
        #100         | 4
        #120         | 4
        #140         | 5
        #Até a veloidade maxima 5
        #Somente podera acelerar/desacelerar com o veiculo ligado
        #não pode impactar no que ja esta funcionando [ex: ligar o carro na 3º marcha]
        

    def acelerar(self):
        if self.MudarMarcha:
            self.velocidade += 20
            if self.velocidade >= 20:
              print(self.subirMarcha())
            elif self.velocidade <= 60:
                print(self.subirMarcha())
            elif self.velocidade <= 80:
                print(self.MudarMarcha())
            elif self.velocidade < self.VelMaxima:
                print(self.subirMarcha())
            return 'A velocidade esta em ' + str(self.velocidade)
        return ' O carro  precisa estar ligado para acelerar'


    def desacelerar(self):
        pass






# instanciar ( criar ) o objeto c1

#c1 = Veiculo(2000,'Preto',2,250)
#c2 = Veiculo(2010,'Vermelho',4,150)
# c1.ligar(False)
# print(c1.ligado)
# print(c2.ligado)
#print ('Ano Classe - '+ str(Veiculo.ano))
#print ('Ano Objeto - '+ str(c1.ano) )
