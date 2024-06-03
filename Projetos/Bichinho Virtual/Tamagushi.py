class Tamagushi:
    __nome = ''
    __fome = 80  # 100 é 100% cheio/sem fome
    __saude = 80  # 100 é 100% saudável
    __humor = 0
    __tedio = 75  # 100 é 100% animado/sem tédio
    vivo = True

    def __init__(self, nome):
        self.__nome = nome

    def status(self):
        # Fome
        print('-' * 25)
        print(f'Status de {self.__nome}: \n')
        if self.__fome <= 0:
            print(f'{self.__nome} morreu de fome')
            self.vivo = False
        elif 1 < self.__fome < 26:
            print(f'{self.__nome} está morrendo de fome')
        elif self.__fome < 51:
            print(f'{self.__nome} está com muita fome')
        elif self.__fome < 76:
            print(f'{self.__nome} está com pouca fome')
        elif self.__fome >= 76:
            print(f'{self.__nome} está satisfeito')

        # Saúde
        if self.__saude <= 0:
            print(f'{self.__nome} ficou doente e morreu')
            self.vivo = False
        elif 1 < self.__saude < 26:
            print(f'{self.__nome} está doente')
        elif self.__saude < 51:
            print(f'{self.__nome} está febril')
        elif self.__saude < 76:
            print(f'{self.__nome} está com a saúde OK')
        elif self.__saude >= 76:
            print(f'{self.__nome} está muito saudável')

        # Humor
        if self.__humor < 26 and (self.__fome or self.__saude) <= 0:
            print(f'{self.__nome} está extremamente triste')
        elif self.__humor < 51:
            print(f'{self.__nome} está triste')
        elif self.__humor < 76:
            print(f'{self.__nome} está com o humor OK')
        elif self.__humor >= 76:
            print(f'{self.__nome} está muito feliz')

        # Tédio
        if self.__tedio <= 0:
            print(f'{self.__nome} literalmente morreu de tédio')
            self.vivo = False
        elif 1 < self.__tedio < 26:
            print(f'{self.__nome} está totalmente entediado')
        elif self.__tedio < 51:
            print(f'{self.__nome} está entediado')
        elif self.__tedio < 76:
            print(f'{self.__nome} quer brincar')
        elif self.__tedio >= 76:
            print(f'{self.__nome} não quer brincar')
        print('-' * 25)
        print('\n')

    @property
    def nome(self):
        return self.__nome

    def PortaSecreta(self):
        print('Status escondidos: \n')
        print(f'Nome: {self.__nome}')
        print(f'Fome: {self.__fome}')
        print(f'Saúde: {self.__saude}')
        print(f'Humor: {self.__humor}')
        print(f'Tédio: {self.__tedio}')

    # Ações
    def run_acoes(self, comando):
        if comando == 'a':
            self.alimentar(int(input(f'Digite o quanto você gostaria de alimentar {self.__nome} (1 a 100): ')))
            print(f'Você alimentou {self.__nome}!\n')
        elif comando == 'b':
            self.brincar(int(input(f'Digite por quantos minutos gostaria de brincar com {self.__nome} (1 a 100): ')))
            print(f'Você passou {comando} minutos brincando com {self.__nome}!\n')
        elif comando == 'd':
            self.descansar(int(input(f'Digite por quantos minutos gostaria {self.__nome} descanse (1 a 100): ')))
            print(f'Você passou {comando} minutos descansando com {self.__nome}!\n')
        elif comando == 'PortaSecreta':
            self.PortaSecreta()
            print('\n')
        else:
            print('Comando inválido!\n')

    def brincar(self, tempo):
        saude = self.__saude - (tempo // 2)
        fome = self.__fome - (tempo // 2)
        tedio = self.__tedio + tempo
        if tedio > 100:
            x = tedio - 100
            tedio -= x
        self.__tedio = tedio
        self.__fome = fome
        self.__saude = saude
        self.humor()
        self.checkar_vivo()

    def alimentar(self, quantidade):
        fome = self.__fome + quantidade
        tedio = self.__tedio - (quantidade // 2)
        if fome > 100:
            x = fome - 100
            fome -= x
        self.__fome = fome
        self.__tedio = tedio
        self.humor()
        self.checkar_vivo()

    def descansar(self, descanso):
        saude = self.__saude + descanso
        fome = self.__fome - descanso
        tedio = self.__tedio - descanso
        if saude > 100:
            x = saude - 100
            saude -= x
        self.__fome = fome
        self.__saude = saude
        self.__tedio = tedio
        if self.__fome <= 5:
            self.__fome = 5
        if self.__tedio <= 5:
            self.__tedio = 5
        self.humor()
        self.checkar_vivo()

    def humor(self):
        humor = (self.__saude + self.__fome) // 2
        self.__humor = humor

    def checkar_vivo(self):
        if self.__fome <= 0 or self.__saude <= 0 or self.__tedio <= 0:
            self.vivo = False

    def menu(self):
        txt = 'Com o tempo, ' + self.__nome + ' ficará com fome, saúde, humor e tédio baixos. \n'
        txt += 'Você poderá alimentar, brincar, ou botar seu pet para descansar. \n'
        txt += 'Isso fará ' + self.__nome + ' ficar feliz e saudável! \n'
        txt += 'Brincar por muito tempo, poderá forçar ' + self.__nome + ' demais\n'
        txt += 'Descansar por muito tempo fará mal a sua saúde \n'
        txt += 'A situação de ' + self.__nome + ' será informada a cada ação sua. \n\n'
        txt += '        COMANDOS: \n'
        txt += 'Alimentar: a \n'
        txt += 'Brincar: b \n'
        txt += 'Descansar: d \n\n'
        return txt

# Rodar jogo
bichinho = Tamagushi(input('Digite o nome do seu bichinho: '))
print(f'O nome do seu novo pet se chama {bichinho.nome}\n')
while bichinho.vivo:
    bichinho.status()
    print(bichinho.menu())
    bichinho.run_acoes(input('Digite o que você quer fazer com seu bichinho: '))
    if not bichinho.vivo:
        break

print('Fim de jogo')
