# ERP Legacy FoxPro → Python (Migración Progresiva)

Este repositorio contiene un **ejemplo real de migración de un sistema ERP desarrollado en FoxPro 2.5 para DOS** hacia Python con la ayuda de la Inteligencia Artificial.

El sistema original está compuesto por:

* **281 programas (.PRG)**
* **52 archivos adicionales de soporte**
* Arquitectura orientada a procesos administrativos y contables de un ERP clásico.

El objetivo de este repositorio es:

1. Preservar parte del código histórico.
2. Mostrar cómo funciona el sistema original.
3. Demostrar la viabilidad de migración a tecnologías modernas.
4. Documentar el proceso de transformación a Python.
5. Servir como base para una futura migración completa del ERP.

---

## Estructura del repositorio

```
erp-foxpro-python-migration/
│
├── foxpro_original/
│   ├── FER000.PRG
│   └── FER110.PRG
│
├── python_version/
│   ├── fer000.py
│   └── fer110.py
│
├── docs/
│   └── analisis_migracion.md
│
└── README.md
```

---

## Sistema original

El ERP fue desarrollado en **FoxPro 2.5 para DOS**, una tecnología ampliamente utilizada en sistemas administrativos en los años 90.

Características del sistema original:

* Aplicación monolítica
* Lógica de negocio distribuida en múltiples programas
* Uso intensivo de DBF
* Menús y navegación en modo texto
* Procesos administrativos y contables

Ejemplo de programas incluidos en este repositorio:

* `FER000.PRG`
* `FER110.PRG`

Estos programas fueron seleccionados como **caso de estudio para migración**.

---

## Objetivo de la migración

La migración busca transformar el sistema hacia una arquitectura moderna basada en:

* Python
* Código mantenible
* Mejor estructura modular
* Posible integración futura con:

  * API REST
  * Base de datos moderna (PostgreSQL / SQLite)
  * Interfaz web o de escritorio

---

## Estrategia de migración

La migración se realizará de manera progresiva:

### Fase 1 — Análisis

* Comprensión del código FoxPro
* Identificación de reglas de negocio
* Documentación de procesos

### Fase 2 — Migración de programas clave

Conversión inicial de algunos módulos representativos:

* Menú principal
* Procesos administrativos
* Módulos de gestión

### Fase 3 — Refactorización en Python

Mejora del diseño:

* Separación por capas
* Funciones reutilizables
* Manejo moderno de datos

### Fase 4 — Migración completa (objetivo futuro)

Si el proyecto continúa:

* Migrar los **281 programas**
* Modernizar base de datos
* Crear nueva interfaz

---

## Ejemplo de migración

En este repositorio se incluye:

### Código original (FoxPro)

```
foxpro_original/
FER000.PRG
FER110.PRG
```

### Versión migrada a Python

```
python_version/
fer000.py
fer110.py
```

El objetivo no es solo traducir el código, sino:

* Mejorar la estructura
* Mantener la lógica del negocio
* Modernizar el sistema

---

## Motivación del proyecto

Este proyecto demuestra:

* Experiencia en sistemas legacy
* Comprensión de arquitecturas antiguas
* Capacidad de modernización tecnológica
* Análisis y migración de software empresarial

Muchos sistemas ERP históricos aún funcionan en FoxPro, por lo que este tipo de migración sigue siendo relevante.

---

## Tecnologías

Sistema original:

* FoxPro 2.5 para DOS

Migración:

* Python 3

Posibles tecnologías futuras:

* FastAPI
* PostgreSQL
* Pandas (para análisis de datos)
* Docker

---

## Estado del proyecto

Proyecto en etapa inicial.

* [x] Selección de programas de ejemplo
* [x] Publicación del código FoxPro
* [ ] Migración a Python
* [ ] Documentación de arquitectura
* [ ] Migración progresiva del ERP

---

## Autor

**José Luis Planes**

Analista en Computación Administrativa
Interés en:

* Migración de sistemas legacy
* Data Science
* Seguridad informática

---

## Nota sobre el sistema

Este repositorio representa solo una **parte demostrativa** de un ERP completo desarrollado durante varios años.

El objetivo es evaluar la posibilidad de modernización y migración tecnológica a largo plazo.

## 📄 Licencia

Código propietario — uso interno y demostrativo.  
El código Python generado es de libre uso para fines de estudio de migración.
