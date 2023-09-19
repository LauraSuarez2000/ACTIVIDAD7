from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def _eq_(self, other):
        return self.nombre == other.nombre

class Conjunto:
    contador = 0

    def _init_(self, nombre):
        self.elementos = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def _add_(self, otro_conjunto):
        resultado = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        resultado.elementos = self.elementos.copy()
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre_resultado)
        resultado.elementos = elementos_comunes
        return resultado

    def _str_(self):
        elementos_str = ', '.join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
