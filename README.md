# 🚌 UADEBUS - Sistema de Gestión de Pasajes Interprovinciales

## 📋 Descripción del Proyecto

UADEBUS es un sistema robusto de gestión y venta de pasajes de micro interprovincial desarrollado completamente en Python. El proyecto implementa estructuras de datos avanzadas, algoritmos recursivos, y manejo integral de archivos para ofrecer una solución completa de reservas de viajes.

## ✨ Características Principales

### 🎯 Funcionalidades Core
- **Sistema de Reservas Completo**: Gestión de compra, consulta, modificación y cancelación de pasajes
- **Gestión Multi-destino**: Soporte para 5 provincias argentinas (Buenos Aires, Misiones, Salta, Mendoza, Santa Fe)
- **Viajes de Ida y Vuelta**: Posibilidad de reservar viajes redondos con validación de fechas
- **Selección de Asientos**: Interfaz visual ASCII para elegir asientos disponibles en tiempo real
- **Sistema de Precios Dinámicos**: Horarios múltiples con precios diferenciados

### 💻 Características Técnicas Avanzadas

#### Estructuras de Datos
- **Matrices**: Gestión de asientos (11 filas × 4 columnas)
- **Listas anidadas**: Almacenamiento de datos de múltiples pasajeros
- **Diccionarios**: Configuración de horarios y precios por ruta
- **Archivos JSON**: Persistencia de configuración de horarios y precios
- **Archivos de texto**: Base de datos plana para reservas

#### Algoritmos y Técnicas
- **Recursividad**: Implementación de búsqueda recursiva de asientos (`buscar_asiento`)
- **Algoritmo de Zeller**: Cálculo del día de la semana para cualquier fecha (`diadelasemana`)
- **Validaciones robustas**: Verificación de emails, DNI, fechas, y datos de pago
- **Manejo de excepciones**: Try-except comprehensivo en todas las operaciones de I/O

#### Gestión de Archivos
- Lectura/escritura de archivos de texto
- Parsing de JSON para configuración
- Sistema de archivos temporales para operaciones CRUD
- Persistencia de datos sin uso de bases de datos

### 🎨 Experiencia de Usuario
- **Interfaz colorizada**: Uso de `colorama` para feedback visual
- **Calendario visual**: Visualización mensual de fechas disponibles con códigos de color
- **Mensajes contextuales**: Feedback claro en español con emojis
- **Simulación de pagos**: Validación de múltiples métodos de pago (tarjeta, transferencia, efectivo)

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Bibliotecas estándar**: `time`, `random`, `json`
- **Colorama**: Para output colorizado en consola
- **Manejo de archivos**: I/O de texto plano y JSON

## 📁 Estructura de Archivos

```
UADEBUS/
│
├── main.py                      # Programa principal
├── dias_disponibles.txt         # Calendario de fechas disponibles
├── horarios_precios.json        # Configuración de rutas, horarios y precios
├── reservas.txt                 # Base de datos de reservas
├── reservas_temp.txt            # Archivo temporal para operaciones
└── README.md
```

## 🚀 Instalación y Uso

### Requisitos
```bash
pip install colorama
```

### Ejecución
```bash
python main.py
```

### Menú Principal
1. **CONSULTAR PASAJE**: Ver, modificar o cancelar reservas existentes
2. **INICIAR COMPRA**: Nueva reserva de pasajes
3. **FINALIZAR PROGRAMA**: Salir del sistema

## 📊 Funcionalidades Detalladas

### Sistema de Reservas
- Selección de origen y destino
- Calendario interactivo con disponibilidad
- Múltiples horarios por ruta
- Precios diferenciados por horario
- Soporte para múltiples pasajeros
- Código de reserva único de 6 dígitos

### Gestión de Modificaciones
1. Ajuste de fecha
2. Reprogramación de hora
3. Modificación de origen/destino
4. Cambio de asiento
5. Corrección de datos personales

### Validaciones Implementadas
- ✅ Formato de email (usuario@dominio.com/.com.ar)
- ✅ DNI argentino (7-8 dígitos)
- ✅ Fechas válidas (hasta mayo 2025)
- ✅ Edad razonable (1-119 años)
- ✅ Asientos únicos por viaje/horario
- ✅ Fechas de vuelta posteriores a ida
- ✅ Datos de pago según método seleccionado

## 🎓 Conceptos de Programación Aplicados

### Estructuras de Datos
- Matrices bidimensionales
- Listas de listas (matrices irregulares)
- Diccionarios anidados
- Tuplas para datos inmutables

### Paradigmas
- Programación procedural
- Recursividad
- Manejo de excepciones
- Validación de datos

### Algoritmos
- Búsqueda recursiva
- Algoritmo de Zeller para fechas
- Parseo de cadenas
- CRUD sobre archivos

## 📝 Formato de Datos

### Estructura de Reserva (reservas.txt)
```
codigo;apellido;nombre;dni;edad;email;fecha;horario;precio;origen;destino;asiento
```

### Estructura de Horarios (horarios_precios.json)
```json
{
    "Origen": {
        "Destino": {
            "HH:MM AM/PM": precio
        }
    }
}
```

## 🔒 Seguridad y Robustez

- Manejo comprehensivo de excepciones (FileNotFoundError, OSError, ValueError)
- Validación de todos los inputs del usuario
- Cierre seguro de archivos con bloques `finally`
- Prevención de duplicados en asientos
- Validación de fechas lógicas (vuelta > ida)

## 🎯 Casos de Uso

1. **Usuario nuevo**: Compra de pasaje simple
2. **Viaje familiar**: Múltiples pasajeros en una reserva
3. **Viaje redondo**: Ida y vuelta en fechas diferentes
4. **Cambio de planes**: Modificación de reserva existente
5. **Cancelación**: Eliminación de reserva del sistema

## 📈 Estadísticas del Código

- **Funciones**: 20+ funciones modulares
- **Líneas de código**: ~750 líneas
- **Validaciones**: 15+ tipos de validación
- **Manejo de archivos**: 3 tipos (txt, json, temporal)
- **Estructuras de datos**: Matrices, listas, diccionarios, tuplas

## 🤝 Contribuciones

Este proyecto fue desarrollado como parte del curriculum de programación, enfocándose en:
- Manejo avanzado de estructuras de datos en Python
- Algoritmos recursivos
- Persistencia de datos sin SQL
- Experiencia de usuario en consola
- Control de versiones con Git

## 📄 Licencia

Proyecto educativo - Universidad Argentina de la Empresa (UADE)

## 👥 Autor

**Valentín Mendez**
- GitHub: @valenmendez01
- LinkedIn: https://www.linkedin.com/in/valentin-mendez/

## 🙏 Agradecimientos

Proyecto desarrollado como trabajo práctico del curso de Programación Orientada a Objetos.

---

⭐ Si te gustó este proyecto, no olvides darle una estrella en GitHub!
