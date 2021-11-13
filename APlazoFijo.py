from CuentaBancaria import CuentaBancaria


class APlazoFijo(CuentaBancaria):
    def __init__(self,id,titular,fecha,numerocuenta,saldo,vencimiento):
        CuentaBancaria.__init__(self,id,titular,fecha,numerocuenta,saldo)
        self.vencimiento=vencimiento

    def retirardinero(self,dinero,fechaactual):
        if(fechaactual<self.vencimiento):
            dinero=dinero*1.05
        CuentaBancaria.retirardinero(dinero)