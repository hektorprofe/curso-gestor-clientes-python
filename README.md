# curso-gestor-clientes-python

La idea es hacer un pequeño gestor de clientes paso a paso añadiendo mejoras progresivamente en futuras versiones, pero dependerá del éxito del curso en la academia:

1. ~~[Desarrollo del prototipo funcional](https://github.com/hcosta/curso-gestor-clientes-python/tree/1.0)~~
2. ~~[Revisión utilizando clases estáticas](https://github.com/hcosta/curso-gestor-clientes-python/tree/2.0)~~
3. Revisión añadiendo pruebas unitarias
4. Revisión guardando datos en ficheros
5. Revisión guardando datos con SQLite
6. Revisión añadiendo una interfaz gráfica

## Instalar las dependencias

_Nota: Sólo incluye pytest para realizar pruebas unitarias._

```bash
pip install -r requirements.txt
```

## Para probar el programa

```bash
python ./gestor/core.py
```

## Para ejecutar los tests

```bash
pytest tests -v
```
