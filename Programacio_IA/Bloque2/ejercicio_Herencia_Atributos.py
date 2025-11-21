# -------------------- CLASE BASE --------------------
class Empleado:
    def __init__(self, nombre, sueldo_base, id_interno):
        self.nombre = nombre            # Público
        self._sueldo_base = sueldo_base # Protegido
        self.__id_interno = id_interno  # Privado

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Sueldo base: {self._sueldo_base}")

    def _calcular_bonus(self):
        return self._sueldo_base * 0.05  # 5% por defecto


# -------------------- CLASE DERIVADA GERENTE --------------------
class Gerente(Empleado):
    def _calcular_bonus(self):
        return self._sueldo_base * 0.25  # 25% para gerentes

    def mostrar_detalle(self):
        print(f"[Gerente] {self.nombre} | Bonus: {self._calcular_bonus()}")


# -------------------- CLASE DERIVADA DESARROLLADOR --------------------
class Desarrollador(Empleado):
    def __init__(self, nombre, sueldo_base, id_interno, lenguaje):
        super().__init__(nombre, sueldo_base, id_interno)
        self._lenguaje = lenguaje  # Protegido

    def _calcular_bonus(self):
        return self._sueldo_base * 0.10  # 10% para desarrolladores

    def mostrar_detalle(self):
        print(f"[Dev] {self.nombre} | Lenguaje: {self._lenguaje} | Bonus: {self._calcular_bonus()}")


# -------------------- FUNCIÓN DE AUDITORÍA --------------------
def auditoria_interna(empleados):
    print("\n=== Auditoría Interna ===")
    for emp in empleados:
        # Acceso directo al atributo privado mediante name mangling
        id_privado = emp._Empleado__id_interno
        print(f"{emp.__class__.__name__} → {emp.nombre} | ID Interno: {id_privado}")


# -------------------- CÓDIGO PRINCIPAL --------------------
if __name__ == "__main__":
    # Crear instancias
    g = Gerente("Laura", 6000, 101)
    d = Desarrollador("Carlos", 4000, 102, "Python")

    # Mostrar información y detalles
    g.mostrar_info()
    g.mostrar_detalle()
    d.mostrar_info()
    d.mostrar_detalle()

    # Ejecutar auditoría interna (acceso a __id_interno)
    auditoria_interna([g, d])
