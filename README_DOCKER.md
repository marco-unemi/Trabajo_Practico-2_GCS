# Pasos 5 a 8 - Docker y persistencia

## Paso 5: Infraestructura como codigo

Se agregaron:

- `Dockerfile`: empaqueta la aplicacion Flask con sus dependencias.
- `docker-compose.yml`: orquesta la app Flask y una base de datos MySQL 8.0 con volumen persistente.
- `requirements.txt`: define las dependencias Python necesarias para la imagen.

## Paso 6: Construccion y despliegue

Desde esta carpeta ejecutar:

```powershell
docker compose up --build -d
```

Verificar contenedores:

```powershell
docker compose ps
```

## Paso 7: Migracion e inyeccion de datos iniciales

Con los contenedores en ejecucion, cargar el SQL:

```powershell
Get-Content .\my-app\BD\crud_python.sql | docker compose exec -T db mysql -uroot -pNuevaPassword123!
```

Validar registros:

```powershell
docker compose exec db mysql -uroot -pNuevaPassword123! -D crud_python -e "SELECT COUNT(*) AS empleados FROM tbl_empleados; SELECT COUNT(*) AS usuarios FROM users;"
```

## Paso 8: Verificacion y pruebas de persistencia

Abrir la app:

```text
http://localhost:5600
```

Probar persistencia:

```powershell
docker compose down
docker compose up -d
docker compose exec db mysql -uroot -pNuevaPassword123! -D crud_python -e "SELECT COUNT(*) AS empleados FROM tbl_empleados; SELECT COUNT(*) AS usuarios FROM users;"
```

Los datos deben mantenerse porque MySQL usa el volumen `mysql_data`.
