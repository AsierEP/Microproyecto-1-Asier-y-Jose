

class MaquinaTuring:

    def __init__(self,MT,cinta,Pos):
        self.MT=MT
        self.cinta=list(cinta)
        self.Estado=1
        self.Pos=Pos


    def CargarLogica(self):
        List=self.MT.split("\n")
        Lista2=[]
        for i in List:
            Lista2.append(i.split(","))
        return Lista2
    
    def BuscarTransicion(self,entrada):
        Logica= self.CargarLogica()
        Transicion=[]
        for i in Logica:
            if int(i[0])==int(self.Estado) and int(i[1])==int(entrada):
                Transicion.append(i[2])
                Transicion.append(i[3])
                Transicion.append(i[4])
                return Transicion
        return False
    
    def SetEstado(self,NuevoEstado):
        self.Estado=NuevoEstado
    
    def SetPos(self,nuevaPos):
        self.Pos=nuevaPos

    def GetEstado(self):
        return self.Estado
    
    def GetPos(self):
        return self.Pos
    
    def operar(self):
        entrada=self.cinta[self.Pos]
        transicion=self.BuscarTransicion(entrada)
        self.Estado=transicion[0]
        self.cinta[self.Pos]=transicion[1]
        self.Pos=self.Pos+int(transicion[2])
        print(self.Estado)
        
    def obtenerCinta(self):
        string = ""
        for i in self.cinta:
            string+=i
        return string