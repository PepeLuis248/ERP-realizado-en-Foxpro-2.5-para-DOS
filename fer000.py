"""
fer000.py - Menú Principal del Sistema ERP
==========================================
Migración de FER000.PRG (FoxPro 2.5 para DOS) a Python.

Módulo original: Menú principal del sistema de gestión comercial.
Controla el acceso a todos los módulos del ERP según jerarquía del usuario.

Notas de migración:
  - La interfaz de texto (curses/DOS) se reemplaza por menú de consola interactivo.
  - El manejo de "work areas" (SELECT 1..10) de FoxPro se reemplaza por
    conexiones/sesiones de base de datos gestionadas por SQLAlchemy o similar.
  - Las variables PUBLIC de FoxPro se modelan como un objeto de sesión global.
  - El módulo de auditoría (tabla AUDITOR) se preserva con la misma lógica.

Estado de migración: PROTOTIPO / DEMOSTRATIVO
"""

import sys
import datetime
from typing import Optional

# ---------------------------------------------------------------------------
# Simulación de objetos de sesión (en producción: leer desde BD / config)
# ---------------------------------------------------------------------------

class Sesion:
    """Almacena el estado de la sesión activa (equivale a las PUBLIC vars de FoxPro)."""
    def __init__(self):
        self.usuario: str = ""
        self.jerarquia: int = 0       # 1=bajo, 2=medio, 3=supervisor, etc.
        self.comercio: str = ""
        self.spool: str = ""
        self.detalle: bool = False

sesion = Sesion()


# ---------------------------------------------------------------------------
# Stub de módulos aún no migrados (llamarán a los .PRG originales en DOS
# hasta que se complete la migración total)
# ---------------------------------------------------------------------------

def stub_modulo(nombre: str):
    print(f"\n  [PENDIENTE DE MIGRACIÓN] → {nombre}")
    input("  Presione Enter para continuar...")


def registrar_auditoria(detalle: str):
    """
    Registra en la tabla de auditoría un intento de acceso no autorizado.
    Equivale al bloque: USE auditor / APPEND BLANK / REPLACE ... / USE
    """
    print(f"  [AUDITORÍA] Usuario '{sesion.usuario}' — {detalle} — {datetime.datetime.now()}")
    # TODO: INSERT INTO auditor (ideusu, fecusu, horusu, detusu) VALUES (...)


def acceso_autorizado(jerarquia_minima: int, nombre_modulo: str) -> bool:
    """
    Verifica jerarquía del usuario, equivale al bloque IF jerarquia < 3 de FoxPro.
    Retorna True si tiene acceso, False y registra auditoría si no.
    """
    if sesion.jerarquia < jerarquia_minima:
        print("\n  ╔══════════════════════════╗")
        print("  ║  Usuario no autorizado   ║")
        print("  ╚══════════════════════════╝")
        registrar_auditoria(f"Intento utilizar módulo: {nombre_modulo}")
        input("  Presione Enter para continuar...")
        return False
    return True


# ---------------------------------------------------------------------------
# Definición del menú principal
# ---------------------------------------------------------------------------

MENU_OPCIONES = [
    (1,  "Gestión de Clientes",          lambda: stub_modulo("fer001 - Clientes")),
    (2,  "Gestión de Proveedores",        lambda: stub_modulo("fer002 - Proveedores")),
    (3,  "Gestión de Vendedores",         None),   # requiere jerarquía >= 3
    (4,  "Gestión de Depósitos",          lambda: stub_modulo("fer030 - Depósitos")),
    (5,  "Gestión de Tarjetas",           None),   # requiere jerarquía >= 3
    (6,  "Gestión de Artículos",          lambda: stub_modulo("fer004 - Artículos")),
    (7,  "Control de Existencias",        lambda: stub_modulo("fer005 - Existencias")),
    (8,  "Gestión de Compras",            lambda: stub_modulo("fer006 - Compras")),
    (9,  "Gestión de Ventas",             lambda: stub_modulo("fer007 - Ventas")),
    (10, "Precios",                       lambda: stub_modulo("fer008 - Precios")),
    (11, "Ofertas",                       lambda: stub_modulo("fer009 - Ofertas")),
    (12, "Control de Caja",              lambda: stub_modulo("fer100 - Caja")),
    (13, "Listado Mayor de Cuentas",      lambda: stub_modulo("may000 - Mayor")),
    (14, "Liquidación de I.V.A.",         None),   # requiere jerarquía >= 3
    (15, "Estadísticas",                  lambda: stub_modulo("fer120 - Estadísticas")),
    (16, "Auditorías de Operaciones",     None),   # requiere jerarquía >= 3
    (17, "Cuentas Corrientes",            lambda: stub_modulo("fer140 - Ctas.Ctes.")),
    (0,  "Salir",                         None),
]

MODULOS_RESTRINGIDOS = {
    3:  ("fer700 - Vendedores",           "módulo de vendedores"),
    5:  ("fer003 - Tarjetas/Crédito",     "módulo tarjetas/crédito"),
    14: ("fer110 - IVA",                  "liquidaciones/IVA"),
    16: ("fer130 - Auditorías",           "auditorías/operaciones"),
}


def mostrar_menu():
    print("\n" + "═" * 60)
    print(f"  SISTEMA ERP — {sesion.comercio or 'Demo'}")
    print("═" * 60)
    for num, desc, _ in MENU_OPCIONES:
        if num == 0:
            print("  ─" * 30)
        print(f"  [{num:2d}]  {desc}")
    print("═" * 60)


def ejecutar_opcion(opc: int):
    if opc == 0:
        return False  # salir

    # Buscar la opción en el menú
    entrada = next((e for e in MENU_OPCIONES if e[0] == opc), None)
    if not entrada:
        print("  Opción inválida.")
        return True

    # Módulos con restricción de jerarquía
    if opc in MODULOS_RESTRINGIDOS:
        nombre_modulo_prg, desc_auditoria = MODULOS_RESTRINGIDOS[opc]
        if not acceso_autorizado(3, desc_auditoria):
            return True
        # Si tiene acceso, ejecutar el stub o la función real
        stub_modulo(nombre_modulo_prg)
        return True

    # Módulos libres
    _, _, fn = entrada
    if fn:
        fn()

    return True


def main():
    """Punto de entrada equivalente al DO WHILE .T. de FER000.PRG"""
    # TODO: cargar sesion.usuario, sesion.jerarquia desde login / base de datos
    sesion.usuario = "DEMO"
    sesion.jerarquia = 3
    sesion.comercio = "Mi Comercio S.A."

    while True:
        mostrar_menu()
        try:
            opc = int(input("  Seleccione opción: "))
        except (ValueError, EOFError):
            continue

        if not ejecutar_opcion(opc):
            print("\n  Cerrando sistema...\n")
            break


if __name__ == "__main__":
    main()
