# FASTAPI-MONGODB & DJANGO-AUTH 


### Empezamos clonando https://github.com/luiisdelar/fast-api-mongo y ejecutando el Dockerfile

```
docker build -t fastapi --no-cache .
```

### Luego levantamos el contenedor

```
docker-compose up
```

### Ahora clonamos el servicio de autenticación https://github.com/luiisdelar/auth-django y ejecutamos el Dockerfile

```
docker build -t auth-django --no-cache .
```

### Por defecto los servicios estaran en las siguientes direcciones 

```
Django-Auth: 127.0.0.1:7000
FasApi-REST: 127.0.0.1:8008
```

### Django-Auth: Nos podemos registrar asi
![imagen](https://user-images.githubusercontent.com/25792969/232974957-f4cbf5a0-01aa-4a30-b205-78ad80299585.png)

### Django-Auth: Y asi podemos ver la lista de usuarios registrados
![imagen](https://user-images.githubusercontent.com/25792969/232975233-6ba0bfb9-cbea-448c-adb4-5aae984dc1fe.png)

### Django-Auth: Asi nos logeamos
![imagen](https://user-images.githubusercontent.com/25792969/232975826-370a5fbf-398e-423e-a8c4-1234ce2dee2b.png)

### Django-Auth: Y asi obtenemos el Access Token el cual utilizaremos para identificarnos en el servicio API REST pasandolo a cada solicitud como Bearer Token: ....
![imagen](https://user-images.githubusercontent.com/25792969/232976103-d2fd6e35-36ec-4d70-9342-ab912e01c2fb.png)

### FasApi-REST: Mediante este endpoint añadimos los datos de assets.csv a la base de datos en mongo, el cual ejecuta este script: https://github.com/luiisdelar/fast-api-mongo/blob/master/data/load_data.py  
![imagen](https://user-images.githubusercontent.com/25792969/232977173-7da22573-2ffb-45df-b1e9-5d9434d53058.png)

### FasApi-REST: Si nos dirigimos a 127.0.0.1:8008/docs/ podemos probar los diferentes endpoints de la API para consultar y modificar las distintas viviendas
![imagen](https://user-images.githubusercontent.com/25792969/232978215-1cf849e7-0ebb-475f-b658-5ace2e2a5f36.png)

### Ejemplo: para obtener una vivienda la consultamos con su id de base de datos y nos devolveria (http://127.0.0.1:8008/builds/643c6d3732e1a93093eb09f6):
![imagen](https://user-images.githubusercontent.com/25792969/232979920-1de4e7d3-41cf-4bf3-8339-eeaea30248d0.png)

### De igual forma lo podemos hacer para actualizar (PUT: http://127.0.0.1:8008/builds/643c6d3732e1a93093eb09f6)
![imagen](https://user-images.githubusercontent.com/25792969/232980551-7fdf43c5-8846-41a5-8c72-282c4a025354.png)
