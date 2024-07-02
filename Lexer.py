import ply.lex as lex

# Definición de los tokens
tokens = ['integer', 'float', 'bool', 'date', 'CARGO_EMPLEADO', 'comma', 
          'pa', 'dp', 'pc', 'lla', 'llc', 'patron_url', 'ESTADO_PROYECTO', 'null',
          'fundacion', 'ingresos_anuales', 'pyme', 'link', 'calle', 'ciudad',
          'pais', 'nombre', 'jefe', 'edad', 'cargo', 'salario', 'activo', 'fecha_contratacion',
          'estado', 'fecha_inicio', 'fecha_fin', 'version', 'firma_digital', 'nombre_empresa', 'string', 'empresas', 
          'direccion', 'departamentos', 'subdepartamentos', 'empleados', 'proyectos'] 
 
# Expresiones regulares para los tokens

def t_proyectos(t):
    r'\"proyectos\"'
    return t

def t_empleados(t):
    r'\"empleados\"'
    return t

def t_subdepartamentos(t):
    r'\"subdepartamentos\"'
    return t

def t_departamentos(t):
    r'\"departamentos\"'
    return t

def t_fundacion(t):
    r'\"fundacion\"'
    return t

def t_direccion(t):
    r'\"direccion\"'
    return t

def t_ingresos_anuales(t):
    r'\"ingresos_anuales\"'
    return t

def t_pyme(t):
    r'\"pyme\"'
    return t

def t_link(t):
    r'\"link\"'
    return t

def t_calle(t):
    r'\"calle\"'
    return t

def t_ciudad(t):
    r'\"ciudad\"'
    return t

def t_pais(t):
    r'\"pais\"'
    return t

def t_nombre(t):
    r'\"nombre\"'
    return t

def t_jefe(t):
    r'\"jefe\"'
    return t

def t_edad(t):
    r'\"edad\"'
    return t

def t_cargo(t):
    r'\"cargo\"'
    return t

def t_salario(t):
    r'\"salario\"'
    return t

def t_activo(t):
    r'\"activo\"'
    return t

def t_fecha_contratacion(t):
    r'\"fecha_contratacion\"'
    return t

def t_estado(t):
    r'\"estado\"'
    return t

def t_fecha_inicio(t):
    r'\"fecha_inicio\"'
    return t

def t_fecha_fin(t):
    r'\"fecha_fin\"'
    return t

def t_nombre_empresa(t):
    r'\"nombre_empresa\"'
    return t

def t_firma_digital(t):
    r'\"firma_digital\"'
    return t

def t_version(t):
    r'\"version\"'
    return t

def t_empresas(t):
    r'\"empresas\"'
    return t

t_pa = r'\['
t_dp = r':' 
t_pc = r'\]'
t_lla = r'\{'
t_llc = r'\}'
t_comma = r','

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'



# Funciones para tokens más complejos, como URLs y valores específicos de cadenas, que usan expresiones regulares para coincidir con patrones específicos.
def t_patron_url(t):
    r'\"https?://[a-zA-Z0-9.-]+(?:\:\d+)?(?:/[a-zA-Z0-9._/#-]*)?\"'
    t.value = f"patron_url: {t.value}"
    return t

def t_CARGO_EMPLEADO(t):
    r'\"(?:Product\sAnalyst|Project\sManager|UX\sdesigner|Marketing|Developer|Devops|DB\sadmin)\"'
    t.value = f"CARGO_EMPLEADO: {t.value[1:-1]}"  # Excluimos las comillas dobles
    return t

def t_ESTADO_PROYECTO(t):
    r'\"(?:To\sdo|In\sprogress|Canceled|Done|On\shold)\"'
    t.value = f"ESTADO_PROYECTO: {t.value[1:-1]}"  # Excluimos las comillas dobles
    return t

# Funciones para reconocer diferentes tipos de datos
def t_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_bool(t):
    r'true|false'
    return t

def t_null(t):
    r'null'
    t.value = None
    return t

def t_date(t):
    r'\"(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\"'
    return t

def t_string(t):
    r'\"(?:[^\"\\]|\\.)*\"'
    return t

# Ajusta el contador de líneas cuando se encuentra una nueva línea.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Maneja caracteres no reconocidos, imprimiendo un mensaje de error y avanzando al siguiente carácter.
def t_error(t):
    print(f"Caracter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

print("Ingrese los tokens (ingrese 'finalizar' para terminar):")

while True:
    entrada = input("> ")
    if entrada == 'finalizar':
        break
    lexer.input(entrada)
    for token in lexer:
        print(f"Token: {token.type}, Valor: {token.value}")
