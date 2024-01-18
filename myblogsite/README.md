
# Blog CodeerHouse

El Blog CodeerHouse es una plataforma web desarrollada con Django, permitiendo a los usuarios leer, publicar y comentar entradas de blog. Cada entrada de blog puede incluir texto, imágenes y una categoría específica. Los usuarios pueden registrarse, iniciar sesión, crear, editar y borrar sus propias entradas de blog, así como añadir comentarios a las entradas de otros usuarios.

## Características Principales

- **Autenticación de Usuarios**: Regístrate, inicia sesión, edita tu perfil y sube tu foto de perfil.
- **Gestión de Blogs**: Crea, lee, actualiza y elimina entradas de blog.
- **Comentarios**: Añade y visualiza comentarios en las entradas de blog.
- **Interfaz de Administrador**: Gestiona usuarios y entradas de blog a través de una interfaz de administrador intuitiva.

## Cómo Empezar

Sigue estos pasos para instalar y ejecutar el Blog CodeerHouse en tu entorno local.

### Pre-requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

### Instalación

1. **Clonar el Repositorio**

    ```bash
    git clone https://github.com/BelialDaNoS/Python-CodeerHouse-Final.git
    cd Python-CodeerHouse-Final
    ```

2. **Configurar un Entorno Virtual (Opcional)**

    - Crear un entorno virtual:
    
        ```bash
        python -m venv venv
        ```

    - Activar el entorno virtual:

        - Windows:
        
            ```bash
            .\venv\Scripts\activate
            ```

        - Linux/Mac:
        
            ```bash
            source venv/bin/activate
            ```

3. **Instalar las Dependencias**

    ```bash
    pip install -r requirements.txt
    ```

### Configuración

4. **Configurar Variables de Entorno**

    - Copia `env.sample` a `.env` y ajusta las variables de entorno según sea necesario.

5. **Ejecutar Migraciones**

    ```bash
    python manage.py migrate
    ```

6. **Recoger Archivos Estáticos (En Producción)**

    - Si estás en un entorno de producción, ejecuta:

        ```bash
        python manage.py collectstatic
        ```

### Ejecución

7. **Iniciar el Servidor de Desarrollo**

    ```bash
    python manage.py runserver
    ```

    Ahora puedes acceder a la aplicación en `http://localhost:8000` en tu navegador.

### Administración

8. **Crear un Superusuario**

    - Para acceder a la interfaz de administración, primero debes crear un superusuario:

        ```bash
        python manage.py createsuperuser
        ```

    - Sigue las instrucciones y luego accede a `http://localhost:8000/admin`.

---

Este archivo `README.md` proporciona una descripción general de tu aplicación, instrucciones detalladas para la instalación y configuración, así como pasos para ejecutar y administrar la aplicación. Asegúrate de ajustar cualquier paso o comando según sea necesario para tu entorno específico o preferencias de configuración.
