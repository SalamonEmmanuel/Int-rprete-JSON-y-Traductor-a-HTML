import multiprocessing
from Lexer import lexer
from Parser import parser
import GeneradorHTML

def validar_json(json_data):
    lexer = lexer()
    parser = parser()
    tokens = lexer.tokenize(json_data)
    parse_result = parser.parse(tokens)
    return parse_result

if __name__ == "__main":
    json_file = 'datos.json'

    # Leer el JSON
    with open(json_file, 'r') as file:
        json_data = file.read()

    # Proceso de validación en paralelo
    pool = multiprocessing.Pool(processes=2)  # Ejecutar hasta 2 procesos simultáneamente
    result = pool.apply_async(validar_json, (json_data,))
    parse_result = result.get()  # Obtener el resultado de la validación
