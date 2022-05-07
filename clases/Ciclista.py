import re


class Ciclista:

    def __init__(self):
        self._nombre= None  
        self._edad=None
        self._pais=None 
        self._equipo=None   
        self._tiempo=None

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def pais(self):
        return self._pais
    
    @property
    def equipo(self):
        return self._equipo
    @property
    def tiempo (self):
        return self._tiempo

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @edad.setter
    def edad(self,edad):
        if (edad <0):
            print("ingrese una edad valida")
        else:
            self._edad=edad
    @pais.setter
    def pais(self,pais):
        self._pais=pais
    @equipo.setter
    def equipo(self,equipo):
        self._equipo=equipo
    @tiempo.setter
    def tiempo(self,tiempo):
        if(tiempo<0):
            print("ingrese una tiempo valido")
        else:
            self._tiempo=tiempo

    