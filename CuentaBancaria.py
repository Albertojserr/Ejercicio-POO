class CuentaBancaria():
    # id=""
    # titular=""
    # fecha=""
    # numerocuenta=0
    # saldo=0
    def __init__(self,id,titular,fecha,numerocuenta,saldo):
        self.id=id
        self.titular=titular
        self.fecha=fecha
        self.numerocuenta=numerocuenta
        self.saldo=saldo


    def setid(self,id):
        self.id=id

    def settitular(self,titular):
        self.titular=titular

    def setFecha(self,fecha):
        self.fecha=fecha

    def setnumerocuenta(self,numerocuenta):
        self.numerocuenta=numerocuenta

    def setsaldo(self,saldo):
        self.saldo=saldo

    def getid(self):
        return self.id

    def gettitular(self):
        return self.titular

    def getFecha(self):
        return self.fecha

    def getnumerocuenta(self):
        return self.numerocuenta

    def getsaldo(self):
        return self.saldo

    def retirardinero(self,dinero):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
        else:
            print("Error, quiere retirar más dinero del que tienes")

    def ingresardinero(self, dinero):
        self.saldo=self.saldo+dinero

    def transferirdinero(self,dinero,cuenta):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
            cuenta.saldo=cuenta.saldo+dinero
        else:
            print("Error, quiere transferir más dinero del que tienes")
