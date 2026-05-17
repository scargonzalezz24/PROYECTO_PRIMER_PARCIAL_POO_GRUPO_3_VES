# Sistema de Gestión de Servicios de Cine / Eventos
**Programación Orientada a Objetos — Proyecto Primer Parcial**  
**Grupo 3**

---
## Descripción

Sistema desarrollado en Python que permite gestionar entradas de cine y reservas de eventos. Aplica los tres pilares de la POO: encapsulamiento, herencia y polimorfismo. El sistema registra clientes, calcula costos automáticamente según el tipo de servicio y genera reportes organizados por categoría.

---
## Estructura del proyecto
ProyectoPOO_Parcial1/
├── clase_base.py       → ServicioEvento (superclase)
├── clase_hija_1.py     → EntradaCine
├── clase_hija_2.py     → ReservaEvento
├── clase_extra_1.py    → ClienteEvento
├── clase_extra_2.py    → GestorEventos
├── main.py             → Programa principal
└── README.md

---
## Diagrama de clases
ServicioEvento          ← clase_base.py (superclase)
                _codigo
                _nombre
                _descripcion
                calcular_total()        ← polimórfico
                mostrar_info()          ← polimórfico
                __str__()
                     |
       +─────────────+─────────────+
       |                           |
 EntradaCine                 ReservaEvento
 clase_hija_1.py             clase_hija_2.py
 _tipo_sala                  _num_personas
 _horario                    _ubicacion
 _categoria                  _servicio_incluido
 _cantidad
 calcular_total()            calcular_total()
 mostrar_info()              mostrar_info()
 __str__()                   __str__()

 ClienteEvento                 GestorEventos
clase_extra_1.py              clase_extra_2.py
_cedula                       _nombre_empresa
_nombre                       _servicios []
_correo                       agregar_servicio()
_telefono                     calcular_total()   ← polimórfico
str()                     mostrar_info()     ← polimórfico
str()

---
## Detalle de cada clase

### ServicioEvento — `clase_base.py`
Superclase que representa un servicio general de cine o evento.

| Atributo | Tipo | Validación setter |
|---|---|---|
| `_codigo` | str | Vacío → `"SIN-CODIGO"` |
| `_nombre` | str | Vacío → `"Sin nombre"` |
| `_descripcion` | str | Vacío → `"Sin descripcion"` |

Métodos: `calcular_total()` · `mostrar_info()` · `__str__()`

---
### EntradaCine — `clase_hija_1.py`
Hereda de `ServicioEvento`. El costo varía según tipo de sala, horario y categoría.

| Atributo | Valores válidos | Valor por defecto |
|---|---|---|
| `_tipo_sala` | `2D` · `3D` · `IMAX` · `4DX` | `2D` |
| `_horario` | `matinal` · `normal` · `noche` | `normal` |
| `_categoria` | `general` · `estudiante` · `tercera_edad` · `nino` | `general` |
| `_cantidad` | Mayor a 0 | `1` |

**Fórmula:**
precio_sala × multiplicador_horario × (1 - descuento_categoria) × cantidad
| Sala | Precio | Horario | Multiplicador | Categoría | Descuento |
|---|---|---|---|---|---|
| 2D | $5.00 | Matinal | 0.80 | General | 0% |
| 3D | $7.50 | Normal | 1.00 | Estudiante | 15% |
| IMAX | $10.00 | Noche | 1.20 | Tercera edad | 20% |
| 4DX | $12.00 | | | Niño | 25% |

---

### ReservaEvento — `clase_hija_2.py`
Hereda de `ServicioEvento`. El costo se calcula por número de personas, ubicación y servicio incluido.

| Atributo | Valores válidos | Valor por defecto |
|---|---|---|
| `_num_personas` | Mayor a 0 | `1` |
| `_ubicacion` | `general` · `preferencial` · `vip` · `palco` | `general` |
| `_servicio_incluido` | `ninguno` · `buffet` · `cena` · `bebidas` | `ninguno` |

**Fórmula:**
(precio_ubicacion + costo_servicio) × num_personas
| Ubicación | Precio | Servicio | Costo extra |
|---|---|---|---|
| General | $15.00 | Ninguno | $0.00 |
| Preferencial | $25.00 | Buffet | $12.00 |
| VIP | $50.00 | Cena | $20.00 |
| Palco | $80.00 | Bebidas | $8.00 |

---

### ClienteEvento — `clase_extra_1.py`
Representa a un cliente del cine o evento.

| Atributo | Validación setter |
|---|---|
| `_cedula` | Vacío → `"0000000000"` |
| `_nombre` | Vacío → `"Cliente sin nombre"` |
| `_correo` | Sin `@` o vacío → `"sin-correo@dominio.com"` |
| `_telefono` | Vacío → `"0000000000"` |

---

### GestorEventos — `clase_extra_2.py`
Administra la lista de servicios y ejecuta los métodos polimórficos.

| Atributo / Método | Descripción |
|---|---|
| `_nombre_empresa` | Nombre de la empresa, vacío → `"Empresa sin nombre"` |
| `_servicios []` | Lista que almacena objetos de `ServicioEvento` o sus hijos |
| `agregar_servicio()` | Agrega un servicio a la lista |
| `calcular_total()` | Suma `calcular_total()` de cada objeto sin preguntar su clase |
| `mostrar_info()` | Llama `mostrar_info()` de cada objeto sin preguntar su clase |

---

## Encapsulamiento aplicado

Todos los atributos son privados (`_atributo`). El acceso y modificación se realiza únicamente mediante `@property` y `@setter`.

Cada setter valida el dato y asigna un valor por defecto si es inválido, **sin usar `raise`**. El `__init__` siempre llama al setter en lugar de asignar directo, para que la validación se ejecute desde el primer momento:

```python
# Correcto: llama al setter, activa la validación
self.tipo_sala = tipo_sala

# Incorrecto: asigna directo, salta la validación
self._tipo_sala = tipo_sala
```

---

## Polimorfismo aplicado

`GestorEventos` recorre la lista sin preguntar a qué clase pertenece cada objeto:

```python
def calcular_total(self):
    total = 0.0
    for servicio in self._servicios:
        total += servicio.calcular_total()  # cada objeto responde diferente
    return round(total, 2)
```

---

## Requisitos

- Python 3.8 o superior
- PyCharm (recomendado) o cualquier IDE compatible
- Git instalado en el sistema

---
## Instalación y uso

```bash
git clone [https://github.com/raul-rabascall/ProyectoPOO_Parcial1.gi](https://github.com/scargonzalezz24/PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3_VES.git)t
```
Abrir la carpeta en PyCharm y ejecutar:

```bash
python main.py
```

---
## Evidencias
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/09e49a95-48ae-4f74-b98a-97417e7cd0d1" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/34cfe274-0f41-44d9-8eca-1453d31316fb" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/a407fb66-badd-45ae-9ab3-f3279fdb626e" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/3d9352ca-67fe-4526-b68f-4753e1c049b7" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/ebaaf093-cbf5-4500-8c78-0bad532dc9b1" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/336988d0-2d48-42cd-93a0-b8cc3d3323da" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/134a3be4-2a19-4d9c-a6d2-0cf339f720ef" />

---
## Video explicativo
<!-- Agregar enlace al video de máximo 2 minutos con permisos de visualización -->

---
## Integrantes — Grupo 3
- Bajaña Ordeñana Lervith Alexander
- González Rodriguez Scarlet Anabella
- Guzman 
- Robins Barros Emeli Carina
- Rabascall 
