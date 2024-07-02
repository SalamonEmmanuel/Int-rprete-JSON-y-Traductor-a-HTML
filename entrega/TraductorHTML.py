import json
import multiprocessing
from Lexer import lexer
from Parser import parser
import generadorHTML

def validar_json(json_data):
    global errores
    errores = []
    lexer_instance = lexer()
    parser_instance = parser()
    tokens = lexer_instance.tokenize(json_data)
    parser_instance.parse(tokens)
    return errores

def generar_html(errores):
    if errores:
        html_content = "<html><body><h1>Errores de Compilación</h1><ul>"
        for error in errores:
            html_content += f"<li>{error}</li>"
        html_content += "</ul></body></html>"
    else:
        html_content = "<html><body><h1>Compilación Exitosa</h1></body></html>"
    
    with open('resultado.html', 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    while True:
        json_file = input("Por favor, ingresa el nombre del archivo JSON (incluyendo la extensión): ")
        if json_file.lower() == 'salir':
            break

        # Leer el JSON
        try:
            with open(json_file, 'r') as file:
                json_data = file.read()
            json.loads(json_data)  # Verificar si es un JSON válido
        except FileNotFoundError:
            print(f"El archivo {json_file} no fue encontrado.")
            continue
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON '{json_file}'.")
            continue

        # Proceso de validación en paralelo
        pool = multiprocessing.Pool(processes=2)  # Ejecutar hasta 2 procesos simultáneamente
        result = pool.apply_async(validar_json, (json_data,))
        errores = result.get()  # Obtener el resultado de la validación
        
        # Generar HTML con el resultado
        generar_html(errores)

