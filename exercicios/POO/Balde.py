class Balde:
    '''
        A classe Balde modela um recipiente com capacidade cap. e
        volume atual vol.Ela armazena tambem o volume derramado e
        indica se esta cheio.
    '''

    def __init__(self, c):
        self.cap = c
        self.vol = 0
        self.der = 0
        self.cheio = False

    def deposita(self, v):
        '''
            Deposita um volume de água v e atualiza o estado do balde
        '''
        self.vol += v
        if self.vol >= self.cap:
            self.cheio = True
            self.der = self.vol - self.cap
            self.vol = self.cap
        return self.vol

    def __repr__(self):
        if self.vol == self.cap:
            return "*%2d*" % self.vol
        else:
            return "[%2d]" % self.vol


if __name__ == "__main__":
    # programa de teste da classe balde
    balde = Balde(10)
    d1 = balde.deposita(3)
    d2 = balde.deposita(4)
    print(balde)
    d3 = balde.deposita(5)
    print(balde)
    print(d1, d2, d3)
