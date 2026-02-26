"""
fer110.py - Módulo de I.V.A. Ventas / Compras
==============================================
Migración de FER110.PRG (FoxPro 2.5 para DOS) a Python.

Módulo original: Presenta menú de opciones para trabajar con el libro
de IVA (ventas o compras), acumulados por período y gráfico de progresión.
Incluye procedimiento PIDE para solicitar mes y año de proceso.

Notas de migración:
  - Las sentencias @ row,col GET / SAY / BOX se reemplazan por input() de consola.
  - El MENU TO / PROMPT de FoxPro se reemplaza por selección numérica.
  - La validación RANGE 1,12 y BETWEEN() se implementa con bucles Python.
  - Los subprogramas fer111, fer112, fer113 son stubs hasta su migración.

Estado de migración: PROTOTIPO / DEMOSTRATIVO
"""

import sys
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

MESES = [
    "", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
    "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
]


# ---------------------------------------------------------------------------
# Stubs de subprogramas aún no migrados
# ---------------------------------------------------------------------------

def fer111(origen: str):
    """Genera libro contable de IVA. Origen: 'V'=Ventas, 'C'=Compras."""
    tipo = "VENTAS" if origen == "V" else "COMPRAS"
    print(f"\n  [PENDIENTE] fer111 → Emitir libro IVA {tipo}")
    input("  Presione Enter para continuar...")


def fer112(origen: str):
    """Acumulados por período de IVA."""
    tipo = "VENTAS" if origen == "V" else "COMPRAS"
    print(f"\n  [PENDIENTE] fer112 → Acumulados IVA {tipo}")
    input("  Presione Enter para continuar...")


def fer113(origen: str):
    """Gráfico de progresión de IVA."""
    tipo = "VENTAS" if origen == "V" else "COMPRAS"
    print(f"\n  [PENDIENTE] fer113 → Gráfico progresión IVA {tipo}")
    input("  Presione Enter para continuar...")


# ---------------------------------------------------------------------------
# Procedimiento PIDE  (equivale al PROCEDURE pide de FoxPro)
# ---------------------------------------------------------------------------

def pide(titulo: str) -> Optional[Tuple[int, int]]:
    """
    Solicita mes (1-12) y año (0-9999) al usuario.
    Retorna (mes, año) o None si el usuario cancela (ESC → Enter vacío).

    Equivale al PROCEDURE pide / PARAMETERS fil, col, tit de FER110.PRG.
    La posición en pantalla (fil, col) no aplica en modo consola.
    """
    print("\n  ┌─────────────────────────────────────────┐")
    print(f"  │  {titulo:<39}│")
    print("  ├─────────────────────────────────────────┤")

    # Pide mes
    while True:
        entrada = input("  │  Indique mes  (1-12, Enter=cancelar): ").strip()
        if not entrada:
            print("  └─────────────────────────────────────────┘")
            return None
        try:
            x_mes = int(entrada)
            if 1 <= x_mes <= 12:
                print(f"  │  Mes seleccionado: {MESES[x_mes]:<21}│")
                break
            else:
                print("  │  ⚠  Mes inválido. Ingrese un valor entre 1 y 12.  │")
        except ValueError:
            print("  │  ⚠  Ingrese un número.                          │")

    # Pide año
    while True:
        entrada = input("  │  Indique año  (0-9999, Enter=cancelar): ").strip()
        if not entrada:
            print("  └─────────────────────────────────────────┘")
            return None
        try:
            x_ano = int(entrada)
            if 0 <= x_ano <= 9999:
                print(f"  │  Año seleccionado : {x_ano:04d}                   │")
                break
            else:
                print("  │  ⚠  Año inválido. Ingrese un valor entre 0 y 9999. │")
        except ValueError:
            print("  │  ⚠  Ingrese un número.                          │")

    print("  └─────────────────────────────────────────┘")
    return (x_mes, x_ano)


# ---------------------------------------------------------------------------
# Menú principal del módulo  (equivale al DO WHILE .T. de FER110.PRG)
# ---------------------------------------------------------------------------

def menu_tipo_iva() -> Optional[str]:
    """
    Primer nivel: selecciona Ventas o Compras.
    Retorna 'V', 'C' o None para salir.
    """
    print("\n  ╔══════════════════════════╗")
    print("  ║       MÓDULO IVA         ║")
    print("  ╠══════════════════════════╣")
    print("  ║  [1]  Ventas             ║")
    print("  ║  [2]  Compras            ║")
    print("  ║  [0]  Volver             ║")
    print("  ╚══════════════════════════╝")
    try:
        opc = int(input("  Seleccione: "))
    except (ValueError, EOFError):
        return None
    if opc == 1:
        return "V"
    if opc == 2:
        return "C"
    return None


def menu_opciones_iva(origen: str) -> Optional[int]:
    """
    Segundo nivel: selecciona la operación a realizar.
    Retorna 1, 2, 3 o None para volver.
    """
    tipo = "VENTAS" if origen == "V" else "COMPRAS"
    print(f"\n  ┌─────────────────────────────┐")
    print(f"  │  Opciones — IVA {tipo:<12}│")
    print(f"  ├─────────────────────────────┤")
    print(f"  │  [1]  Genera libro contable  │")
    print(f"  │  [2]  Acumulados en período  │")
    print(f"  │  [3]  Gráfico de progresión  │")
    print(f"  │  [0]  Volver                 │")
    print(f"  └─────────────────────────────┘")
    try:
        opc = int(input("  Seleccione: "))
    except (ValueError, EOFError):
        return None
    return opc if opc in (1, 2, 3) else None


def main():
    """
    Punto de entrada del módulo IVA.
    Llamado desde fer000.py al elegir opción 14 (Liquidación de I.V.A.).
    Equivale al bloque principal de FER110.PRG.
    """
    while True:
        origen = menu_tipo_iva()
        if origen is None:
            break  # Salir del módulo IVA → retorna al menú principal

        opc = menu_opciones_iva(origen)
        if opc is None:
            continue  # Volver a elegir Ventas/Compras

        tipo_str = "ventas" if origen == "V" else "compras"

        if opc == 1:
            titulo = f"Emisión de libro iva/{tipo_str}"
            resultado = pide(titulo)
            if resultado:
                mes, ano = resultado
                print(f"\n  → Generando libro IVA {tipo_str.upper()} — {MESES[mes]} {ano:04d}")
                fer111(origen)

        elif opc == 2:
            titulo = f"Acumulados sobre {tipo_str}"
            resultado = pide(titulo)
            if resultado:
                mes, ano = resultado
                print(f"\n  → Acumulados IVA {tipo_str.upper()} — {MESES[mes]} {ano:04d}")
                fer112(origen)

        elif opc == 3:
            titulo = f"Progresión de iva/{tipo_str}"
            # Opción 3 no llama a pide() en el original
            fer113(origen)


if __name__ == "__main__":
    main()
