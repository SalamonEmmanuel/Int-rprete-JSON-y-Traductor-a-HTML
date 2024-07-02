import json 

archivo_json = input("Por favor, ingresa el nombre del archivo JSON (incluyendo la extensión): ")


try:

    with open(archivo_json, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"El archivo '{archivo_json}' no se encuentra.")
    exit()
except json.JSONDecodeError:
    print(f"Error al decodificar el archivo JSON '{archivo_json}'.")
    exit()


html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Empresas</title>
    <style>
        .empresa {
            border: 1px solid #ccc;
            padding: 20px;
            margin-bottom: 20px;
        }
        .departamento {
            margin-left: 20px;
        }
        .subdepartamento {
            margin-left: 40px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
"""

# Generar contenido HTML para cada empresa
for empresa in data['empresas']:
    html_content += f"""
    <div class="empresa">
        <h1>{empresa['nombre_empresa']}</h1>
    """
    if 'link' in empresa:
        html_content += f"""
        <p><a href="{empresa['link']}" type="button">Sitio web</a></p>
        """

    for depto in empresa['departamentos']:
        html_content += f"""
        <div class="departamento">
            <h2>Departamento: {depto['nombre']}</h2>
        """

        for subdepto in depto['subdepartamentos']:
            html_content += f"""
            <div class="subdepartamento">
                <h3>Subdepartamento: {subdepto['nombre']}</h3>
                <ul>
            """
            if 'empleados' in subdepto and subdepto['empleados']:
                for empleado in subdepto['empleados']:
                    html_content += f"""
                    <li>
                        {empleado['nombre']}
                    """
                    if 'proyectos' in empleado and empleado['proyectos']:
                        html_content += """
                        <table>
                            <tr>
                                <th>Nombre del Proyecto</th>
                                <th>Estado</th>
                                <th>Fecha de Inicio</th>
                                <th>Fecha de Fin</th>
                            </tr>
                        """
                        for proyecto in empleado['proyectos']:
                            html_content += f"""
                            <tr>
                                <td>{proyecto['nombre']}</td>
                                <td>{proyecto.get('estado', 'N/A')}</td>
                                <td>{proyecto.get('fecha_inicio', 'N/A')}</td>
                                <td>{proyecto.get('fecha_fin', 'N/A')}</td>
                            </tr>
                            """
                        html_content += """
                        </table>
                        """
                    html_content += """
                    </li>
                    """
            html_content += """
                </ul>
            </div>
            """

        html_content += """
        </div>
        """

    html_content += """
    </div>
    """

# Cerrar el contenido HTML
html_content += """
</body>
</html>
"""

# Escribir el contenido en un archivo HTML
with open('empresas.html', 'w') as file:
    file.write(html_content)

print("Archivo HTML generado exitosamente.")
