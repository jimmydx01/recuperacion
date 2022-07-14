from usuario import Usuario


class Prestamo:
    def __init__(self,n,f,ci,v,i,nu,vc):
      self.Id_prestamo =n
      self.fecha=f
      self.cedula=ci
      self.valor_prestamo=v
      self.numer_meses=nu
      self.interestes=i
      self.valor_cuotas=vc


class pago(Prestamo):
    def __init__(self,fp,ip):     
        super().__init__(self,vc="30",v="15.000")
        self.Id_pago =ip
        self.fecha_pago=fp