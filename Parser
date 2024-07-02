import ply.yacc as yacc
import json
from Lexer import tokens

# Lista para almacenar errores
errores_gramatica = []

# Definición de las reglas gramaticales

def p_Sigma(p):
    '''Sigma : lla EmpresasI comma Version comma Firma_digital llc
             | lla EmpresasI comma Firma_digital comma Version llc
             | lla Version comma EmpresasI comma Firma_digital llc
             | lla Version comma Firma_digital comma EmpresasI llc
             | lla Firma_digital comma Version comma EmpresasI llc
             | lla Firma_digital comma EmpresasI comma Version llc
             | lla EmpresasI comma Version llc
             | lla EmpresasI comma Firma_digital llc
             | lla EmpresasI llc '''

def p_EmpresasI(p):
    '''EmpresasI : empresas dp pa Empresas pc'''

def p_Empresas(p):
    '''Empresas : Empresa_list'''

def p_Empresa_list(p):
    '''Empresa_list : Empresa_list comma Empresa
                    | Empresa'''

def p_Empresa(p):
    '''Empresa : lla Nombre_empresa comma Fundacion comma Direccion comma Ingresos_anuales comma Pyme comma Link comma Departamentos llc
               | lla Nombre_empresa comma Fundacion comma Direccion comma Ingresos_anuales comma Pyme comma Departamentos llc
               | lla Nombre_empresa comma Fundacion comma Ingresos_anuales comma Pyme comma Departamentos llc
               | lla Nombre_empresa comma Fundacion comma Ingresos_anuales comma Pyme comma Link comma Departamentos llc'''

def p_Nombre_empresa(p):
    '''Nombre_empresa : nombre_empresa dp string'''

def p_Direccion(p):
    '''Direccion : direccion dp lla Calle comma Ciudad comma Pais llc
                 | direccion dp lla Calle comma Pais comma Ciudad llc
                 | direccion dp lla Ciudad comma Calle comma Pais llc
                 | direccion dp lla Ciudad comma Pais comma Calle llc
                 | direccion dp lla Pais comma Calle comma Ciudad llc
                 | direccion dp lla Pais comma Ciudad comma Calle llc
                 | direccion dp lla llc'''

def p_Departamentos(p):
    '''Departamentos : departamentos dp pa Departamento_list pc'''

def p_Departamento_list(p):
    '''Departamento_list : Departamento_list comma Departamento
                         | Departamento'''

def p_Departamento(p):
    '''Departamento : lla Nombre comma Jefe comma Subdepartamentos llc
                    | lla Nombre comma Subdepartamentos llc
                    | lla Subdepartamentos comma Nombre comma Jefe llc
                    | lla Subdepartamentos comma Nombre llc
                    | lla Subdepartamentos comma Jefe comma Nombre llc
                    | lla Jefe comma Nombre comma Subdepartamentos llc
                    | lla Jefe comma Subdepartamentos comma Nombre llc'''

def p_Subdepartamentos(p):
    '''Subdepartamentos : subdepartamentos dp pa Subdepartamento_list pc'''

def p_Subdepartamento_list(p):
    '''Subdepartamento_list : Subdepartamento_list comma Subdepartamento
                            | Subdepartamento'''

def p_Subdepartamento(p):
    '''Subdepartamento : lla Nombre comma Jefe comma Empleados llc
                       | lla Nombre llc
                       | lla Nombre comma Jefe llc
                       | lla Nombre comma Empleados llc
                       | lla Jefe comma Nombre llc'''

def p_Empleados(p):
    '''Empleados : empleados dp pa Empleado_list pc
                 | empleados dp pa pc'''

def p_Empleado_list(p):
    '''Empleado_list : Empleado_list comma Empleado
                     | Empleado'''

def p_Empleado(p):
    '''Empleado : lla Nombre comma Edad comma Cargo comma Salario comma Activo comma Fecha_contratacion comma Proyectos llc
                | lla Nombre comma Cargo comma Salario comma Activo comma Fecha_contratacion llc
                | lla Nombre comma Cargo comma Salario comma Activo comma Fecha_contratacion comma Proyectos llc'''

def p_Proyectos(p):
    '''Proyectos : proyectos dp pa Proyecto_list pc
                 | proyectos dp pa pc
                 | proyectos dp null'''

def p_Proyecto_list(p):
    '''Proyecto_list : Proyecto_list comma Proyecto
                     | Proyecto'''

def p_Proyecto(p):
    '''Proyecto : lla Nombre comma Estado comma Fecha_inicio comma Fecha_fin llc
                | lla Nombre comma Fecha_inicio llc
                | lla Nombre comma Estado comma Fecha_inicio llc'''

def p_Version(p):
    '''Version : version dp null
               | version dp string'''

def p_Firma_digital(p):
    '''Firma_digital : firma_digital dp string
                     | firma_digital dp null'''

def p_Estado(p):
    '''Estado : estado dp ESTADO_PROYECTO
              | estado dp null'''

def p_Jefe(p):
    '''Jefe : jefe dp null
            | jefe dp string'''

def p_Link(p):
    '''Link : link dp patron_url
            | link dp null'''

def p_Fecha_inicio(p):
    '''Fecha_inicio : fecha_inicio dp date'''

def p_Fecha_fin(p):
    '''Fecha_fin : fecha_fin dp null
                 | fecha_fin dp date'''

def p_Fecha_contratacion(p):
    '''Fecha_contratacion : fecha_contratacion dp date'''

def p_Nombre(p):
    '''Nombre : nombre dp string'''

def p_Pais(p):
    '''Pais : pais dp string'''

def p_Calle(p):
    '''Calle : calle dp string'''

def p_Ciudad(p):
    '''Ciudad : ciudad dp string'''

def p_Fundacion(p):
    '''Fundacion : fundacion dp integer'''

def p_Activo(p):
    '''Activo : activo dp bool'''

def p_Pyme(p):
    '''Pyme : pyme dp bool'''

def p_Ingresos_anuales(p):
    '''Ingresos_anuales : ingresos_anuales dp float'''

def p_Cargo(p):
    '''Cargo : cargo dp CARGO_EMPLEADO'''

def p_Salario(p):
    '''Salario : salario dp float'''

def p_Edad(p):
    '''Edad : edad dp integer'''

def p_error(p):
    global errores_gramatica
    if p:
        error_message = f"Error en la línea {p.lineno}, cadena no reconocida: {p.value}"
    else:
        error_message = "Error de sintaxis al final del archivo"
    errores_gramatica.append(error_message)
    print(error_message)

# Construir el parser
parser = yacc.yacc()

# Función para analizar desde una cadena de entrada
def parse_input(input_string):
    global errores_gramatica
    errores_gramatica = []  # Limpiar errores anteriores
    parser.parse(input_string)

# Función para analizar desde un archivo JSON
def parse_json_file(filename):
    with open(filename, 'r') as file:
        parse_input(file.read())

# Ejemplo de uso:
if __name__ == "__main__":
    while True:
        opcion = input("Por favor, selecciona una opción:\n  1. Ingresar cadena para análisis sintáctico.\n  2. Ingresar nombre de archivo JSON para análisis sintáctico.\n  3. Salir\nOpción: ")
        
        if opcion == '1':
            prueba = input("Ingresa la cadena para análisis sintáctico: ")
            parse_input(prueba)
            if not errores_gramatica:
                print("Análisis sintáctico exitoso")
            else:
                print("Errores encontrados:")
                for error in errores_gramatica:
                    print(error)
        
        elif opcion == '2':
            archivo_json = input("Ingresa el nombre del archivo JSON (incluyendo la extensión): ")
            try:
                parse_json_file(archivo_json)
                if not errores_gramatica:
                    print("Análisis sintáctico exitoso")
                else:
                    print("Errores encontrados:")
                    for error in errores_gramatica:
                        print(error)
            except FileNotFoundError:
                print(f"El archivo {archivo_json} no fue encontrado.")
        
        elif opcion == '3':
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1, 2 o 3).")
            
 # type: ignore
