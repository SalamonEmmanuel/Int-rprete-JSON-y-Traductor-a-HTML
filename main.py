import ply.lex as lex
import re

# Definición de los tokens
tokens = ['string', 'integer', 'float', 'bool', 'date', 't_version', 't_firma_digital',
        't_nombre_empresa', 't_fundacion', 't_calle', 't_ciudad', 't_pais',
        't_ingresos_anuales', 't_pyme', 't_link',
        't_nombre', 't_jefe', 't_edad', 't_cargo', 't_salario', 't_activo',
        't_fecha_contratacion', 't_estado', 't_fecha_inicio', 't_fecha_fin', 'CARGO_EMPLEADO', 'coma', 'pa', 'dp', 'pc', 'lla', 'llc', 'patron_url', 'ESTADO_PROYECTO']


reservadas = {
    '"version"': 't_version',
    '"firma_digital"': 't_firma_digital',
    '"nombre_empresa"' : 't_nombre_empresa',
    '"fundacion"': 't_fundacion',
    '"calle"': 't_calle',
    '"ciudad"': 't_ciudad',
    '"pais"': 't_pais',
    '"ingresos_anuales"': 't_ingresos_anuales',
    '"pyme"': 't_pyme',
    '"link"': 't_link', 
    '"nombre"': 't_nombre', #Nombre para Departamento, Empleado, SubDepartamento y proyecto
    '"jefe"': 't_jefe', 
    '"edad"': 't_edad', 
    '"cargo"': 't_cargo', 
    '"salario"': 't_salario',
    '"activo"': 't_activo',
    '"fecha_contratacion"': 't_fecha_contratacion',
    '"estado"': 't_estado', 
    '"fecha_inicio"': 't_fecha_inicio',
    '"fecha_fin"':'t_fecha_fin'
}

# Definición de las expresiones regulares para los tokens

#la primera barra invertida hace que los metacaracteres del paréntesis y las llaves se interpreten literalmente y no como su significado especial en expresiones regulares.
# necesitamos colocar una barra invertida adicional para indicar que la primera barra invertida debe interpretarse literalmente como '\', ya que también es un metacaracter
t_pa = '\\['
t_dp = ':'
t_pc = '\\]'
t_lla = '\\{'
t_llc = '\\}'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

def t_patron_url(t):
    r'(https?://[a-zA-Z0-9.-]+(?:\:\d+)?(?:/[a-zA-Z0-9._/#-]*)?)'
    t.value = f"patron_url: {t.value}"  
    return t


def t_CARGO_EMPLEADO(t):
    r'"(?:Product\sAnalyst|Project\sManager|UX\sdesigner|Marketing|Developer|Devops|DB\sadmin)"'
    t.value = f"CARGO_EMPLEADO: {t.value[1:-1]}"  # Excluimos las comillas dobles
    return t

def t_ESTADO_PROYECTO(t):
    r'"(?:To\sdo|In\sprogress|Canceled|Done|On\shold)"'
    t.value = f"ESTADO_PROYECTO: {t.value[1:-1]}"  # Excluimos las comillas dobles
    return t


#Al colocar la función t_date antes de la función t_string, el lexer primero intentará reconocer la entrada como una fecha antes de intentar reconocerla como una cadena de caracteres.
def t_date(t):
    r'^"(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"$'
    return t


def t_string(t):
    r'"(?:[^"\\]|\\.)*"'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    else:
        t.type = 'string'
    return t


def t_integer(t):
    r'^\d+$'
    t.value = int(t.value)
    return t


def t_float(t):
    r'^\d+\.\d{1,2}$'
    t.value = float(t.value)
    return t


def t_bool(t):
    r'^(true|false)$'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Caracter no reconocido: '%s'" % t.value[0])
    t.lexer.skip(1)




lexer = lex.lex()

print("Ingrese los tokens (ingrese 'finalizar' para terminar):")

while True:
    entrada = input("> ")
    lexer.input(entrada)
    if entrada == 'finalizar':
        break
   
    for token in lexer:
        print(f"Token: {token.type}, Valor: {token.value}")


