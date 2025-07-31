# PassKit CLI en Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://badge.fury.io/py/passkit-python-grpc-sdk.svg)](https://pypi.org/project/passkit-python-grpc-sdk/)

## Descripción

Este proyecto proporciona un cliente de línea de comandos (CLI) que simplifica el uso del SDK gRPC de PassKit desde Python. Con él es posible crear programas de membresía, inscribir miembros y generar cupones directamente desde la terminal.

La aplicación está implementada con la biblioteca [Click](https://click.palletsprojects.com/) y utiliza el paquete [`passkit-python-grpc-sdk`](https://pypi.org/project/passkit-python-grpc-sdk/) para comunicarse de forma segura con los servicios de PassKit.

## Requisitos

- Cuenta en [PassKit](https://app.passkit.com) y credenciales para el SDK (archivos `certificate.pem`, `ca-chain.pem` y `key.pem`).
- Python 3.7 o superior.
- Acceso a internet para instalar las dependencias desde PyPI.

Coloca los archivos de certificado en un directorio `certs` dentro del proyecto o define las variables de entorno `PASSKIT_CA_CHAIN`, `PASSKIT_CERT` y `PASSKIT_KEY` apuntando a sus rutas.

## Instalación y compilación

1. Clona este repositorio y sitúate en la carpeta raíz.
2. Ejecuta:
   ```bash
   pip install -e .
   ```
   Esto instalará las dependencias y compilará el paquete en modo editable, dejando disponible el comando `passkit` en tu entorno.

## Uso del CLI

Configura las variables de entorno con las rutas de tus certificados (si no usas la carpeta `certs` por defecto) e invoca los comandos. Algunos ejemplos:

```bash
export PASSKIT_CA_CHAIN=/ruta/ca-chain.pem
export PASSKIT_CERT=/ruta/certificate.pem
export PASSKIT_KEY=/ruta/key.pem

# Crear un programa de membresía
passkit membership create-program --name "Mi Programa"

# Inscribir un miembro
passkit membership enrol-member --program-id PRG_ID --tier-id TIER_ID \
    --forename Juan --surname Perez --email juan@example.com

# Crear un cupón
passkit coupons create --campaign-id CAMP_ID --offer-id OFFER_ID \
    --forename Ana --surname Lopez --email ana@example.com
```

Ejecuta `passkit --help` para obtener la lista completa de comandos y opciones disponibles.

### Comandos principales

- **membership create-program**: crea un nuevo programa de membresía.
- **membership enrol-member**: inscribe un miembro en un programa y devuelve su identificador.
- **coupons create**: genera un cupón asociado a una campaña y oferta.

Dentro de las carpetas `passkit_cli/membership` y `passkit_cli/coupons` encontrarás otros scripts de ejemplo para operaciones adicionales (crear campañas, crear ofertas, actualizar cupones, etc.).

## Documentación

- [Documentación oficial de Membership](https://docs.passkit.io/protocols/member)
- [Documentación oficial de Coupons](https://docs.passkit.io/protocols/coupon)
- [Documentación oficial de Event Tickets](https://docs.passkit.io/protocols/event-tickets/)
