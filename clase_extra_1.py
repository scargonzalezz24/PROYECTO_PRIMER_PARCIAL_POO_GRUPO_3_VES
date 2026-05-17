"""
========================================================
PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3
--------------------------------------------------------
Archivo: ClienteEvento.py

Descripción:
Clase encargada de representar a los clientes
registrados dentro del sistema de eventos.

Esta clase aplica:
- Encapsulamiento
- Validaciones mediante propiedades
- Representación textual de objetos
- Uso de setters y getters

Autor: Grupo 3
Materia: Programación Orientada a Objetos
========================================================
"""


class ClienteEvento:

    """
    Clase que representa a un cliente del sistema.
    """

    def __init__(self, cedula, nombre, correo, telefono):

        """
        Constructor de la clase.

        Parámetros:
        cedula   -> Número de cédula del cliente.
        nombre   -> Nombre completo del cliente.
        correo   -> Correo electrónico del cliente.
        telefono -> Número telefónico del cliente.
        """

        self._cedula = None
        self._nombre = None
        self._correo = None
        self._telefono = None

        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # ====================================================
    # PROPIEDAD CEDULA
    # ====================================================

    @property
    def cedula(self):

        """
        Obtiene la cédula del cliente.
        """

        return self._cedula

    @cedula.setter
    def cedula(self, valor):

        """
        Valida y asigna la cédula.
        Si está vacía, asigna un valor por defecto.
        """

        if valor == "":
            self._cedula = "0000000000"
        else:
            self._cedula = valor

    # ====================================================
    # PROPIEDAD NOMBRE
    # ====================================================

    @property
    def nombre(self):

        """
        Obtiene el nombre del cliente.
        """

        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        """
        Valida y asigna el nombre.
        """

        if valor == "":
            self._nombre = "Cliente sin nombre"
        else:
            self._nombre = valor

    # ====================================================
    # PROPIEDAD CORREO
    # ====================================================

    @property
    def correo(self):

        """
        Obtiene el correo electrónico del cliente.
        """

        return self._correo

    @correo.setter
    def correo(self, valor):

        """
        Valida y asigna el correo electrónico.
        Si el correo no contiene '@' o está vacío,
        se asigna un correo por defecto.
        """

        if "@" not in valor or valor == "":
            self._correo = "sin-correo@dominio.com"
        else:
            self._correo = valor

    # ====================================================
    # PROPIEDAD TELEFONO
    # ====================================================

    @property
    def telefono(self):

        """
        Obtiene el número telefónico del cliente.
        """

        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        """
        Valida y asigna el número telefónico.
        """

        if valor == "":
            self._telefono = "0000000000"
        else:
            self._telefono = valor

    # ====================================================
    # REPRESENTACION TEXTUAL
    # ====================================================

    def __str__(self):

        """
        Retorna una representación textual del objeto.
        """

        return (
            f"Cliente: {self._nombre} | Cedula: {self._cedula} | "
            f"Correo: {self._correo} | Telefono: {self._telefono}"
        )


# =========================
# PRUEBAS
# =========================

if __name__ == "__main__":

    """
    Bloque de pruebas de ejecución directa.
    """

    print("=== PRUEBA 1 ===")

    cliente1 = ClienteEvento(
        "0912345678",
        "Raul Rabascall",
        "raul@gmail.com",
        "0999999999"
    )

    print(cliente1)

    print("\n=== PRUEBA 2 ===")

    cliente2 = ClienteEvento(
        "",
        "",
        "",
        ""
    )

    print(cliente2)
