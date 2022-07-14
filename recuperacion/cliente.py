class Cliente:
    def __init__(self,n="universitario",t="doctor",s="1200",c="0980172512",a=False):

        self.neivel_educacion=n
        self.trabajo_actual=t
        self.sueldo_actual=s
        self.celular=c
        self.adeuda=a
    def valida_deuda(self):
       if  self.adeuda==True:
            return "debes pagar ya "
       else:
        return "sin deuda"    
            
            
class Cuenta(Cliente):
    def __init__(self,n="1202351536",t=True,f="20/12/2005",p="10.000",b=15.000):
        self.N_cuenta=n
        self.Tipo_cuenta=t
        self.fecha_creacion=f
        self.prestamo=p
        self.balance=b
    def vavalida_cuenta(self):
        if  self.Tipo_cuenta==True:
            return "cuenta de ahorros"
        else:
            return "cuenta corriente"        
