class fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes 
        self.año = año 
    
    def celular_dif_fechas(self):
        return 


    def __str__(self):
        return f" {self.dia:02d}/{self.mes:02d}/{self.año:04d}"

    def mostrar_fecha(self):
        return self.__str__()

    def __add__(self, otro):


     def __eq__(self.otro):
        primerfecha = self.num . 
        srgundafecha = otra.fecha


         



#EJERCICIO 2 


class alumno:
    def __init__(self, nombre, Dni, fechaingreso, carrera):
        self.datos = {
            "nombre" : nombre, 
            "Dni" : Dni,
            "fechaingreso" : fechaingreso,
            "carrera" : carrera 
        }
    
    def mostrar_informacion(self):
        print("nombre:", self.nombre)
        print("Dni:" , self.nombre)
        print("fechaingreso", self.fechaingreso)
        print("carrera:", carrera)

    def actualizar_informacion(self,clave,valor):
        if clave in self.informacion:
            self.informacion[clave] = valor
            return True 
        else:
            return False 
    def mostrar_datos(self):
        for clave , valor in self.datos.items():
            print(f"{clave}:{valor}")

    def __str__(self):
        datos_str = "," . join(f"{clave}:{valor}" for clave , valor in self.datos.items())
        return f"alumno({datos_str})" 

    def __eq__(self,otro):
        if isinstance(otro,alumno):
            return self.datos == otro.datos
        return False 
        
                           


 #EJERCICIO 3 

 class NODO:
    def __init__(self):
        self.valor = valor 
        self.siguiente = None 
        self.anterior = None 


 class ListadoblementeEnlazada:
    def __init__(self):
        self.primero = None 
        self.ultimo = None 
        self.len = 0 

def intertar(self, dato):
    nodo = NODO(dato)    

    if self.primero is None :
        self.primero = nodo 
        self.ultimo = self.primero 

    else :
        nodo.anterior = self.ultimo
        self.ultimo.siguiente = nodo
        self.ultimo = nodo 

    self.len + = 1 

def iter (self):
    actual = self.primero

    while actual : 
        dato = actual.dato 
        actual = actual.siguiente
        return dato 

datoAlumno = ListadoblementeEnlazada()
print ("datosAlumno", datos.alumno) 
datos.intertar("maximiiano")
print("datosAlumno",datos.alumno)



