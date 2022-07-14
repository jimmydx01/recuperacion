class Empleado:
    def __init__(self,n="universidad",t="economista",d="contabilidad",e="casado",a="25/04/2018"):
        self.Nivel_estudio=n
        self.titulo=t
        self.departamento=d
        self.estado=e
        self.año_ingreso=a


class cajero(Empleado):
    def __init__(self,c="1"):
        self.nume_cajero =c
class servico_client(Empleado):
    def __init__(self,t=True,m=True):
        self.modaliva=m
        self.tipo_servicio=t 
    def valida_servicio(self):
        if self.tipo_servicio==True:
            return "presatamos"
        else:
            return "quejas "
    def  modal(self):

        if  self.modaliva ==True:
            return "presencial"
        else:
            return "online"    
    

          
