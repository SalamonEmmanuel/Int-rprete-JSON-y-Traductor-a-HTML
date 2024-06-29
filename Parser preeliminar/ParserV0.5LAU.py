# BIBLIA DEL PARSER -----------------
# Los NO TERMINALES en la gramática serán FUNCIONES en el Parser
# Los TERMINALES son los tokens del analizador léxico
# Algunos videos dicen que por cada or en una regla gramatical tiene que haber una función, pero chatgpt no lo hace así
#--------------------------------------------
# PENDIENTE -------------------------
# Expresiones regulares para los tokens
#------------------------------------
import ply.yacc as yacc
from main import tokens 

# Definicion de las reglas gramaticasles

def p_empresas(p):
    #Empresas -> [ Empresa ]
    #p[0] = empresa(p[1], "empresa")
    pass 

def p_empresa(p):
    #Empresa -> { NombreEmpresa Fundacion Direccion IngresosAnuales Pyme Link [ Departamentos ] }
    p[0] = { 'NombreEmpresa': p[1], 'Fundacion': p[2], 'Direccion': p[3], 'IngresosAnuales': p[4], 'Pyme': p[5], 
            'Link': p[6] }

def p_departamentos(p):
    #Departamentos -> { departamento }
    pass

def p_departamento(p):
    #Departamento -> { nombre jefe [ Subdepartamentos ] } | { Nombre [ Subdepartamentos ] } | { [ Subdepartamentos ] Nombre Jefe} | 
    #{ Subdepartamentos, Nombre } | { Jefe, Nombre, Subdepartamentos } | { Jefe, Subdepartamentos, Nombre }
    pass

def p_subDepartamentos(p):
    #subDepartamentos -> { subDepartamento }
    pass

def p_subDepartamento(p):
    #subDepartamento -> { Nombre , Jefe , Empleados } | { Nombre } | {Nombre , Jefe} | { Nombre , Empleados }
    pass

def p_empleados(p):
    #Empleados -> { [ Empleado ] | [] } <- cuestionable esos corchetes vacios
    pass

def p_empleado(p):
    #Empleado ->  { Nombre , Edad , Cargo , Salario , Activo , Fecha_contratacion , Proyectos } |
    #{ Nombre , Cargo , Salario , Activo , Fecha_contratacion } | 
    #{ Nombre, Edad , Cargo , Salario , Activo , Fecha_contratacion} | 
    #{ Nombre , Cargo , Salario, Activo , Fecha_contratacion , Proyectos } 
    pass 

def p_proyectos(p):
    #Proyectos -> [ Proyectos ] | [ ]
    pass

def p_proyecto(p):
    #proyecto -> { Nombre , Estado , Fecha_inicio , Fecha_fin } | { Nombre , Fecha_inicio } | 
    # { Nombre , Fecha_inicio , Fecha_fin } | { Nombre , Estado , Fecha_inicio }
    pass 

#Error
def p_error(p):
    print("ERROR DE SINTAXIS")
    print("Error en la linea")+str(p.lineno)

parser = yacc.yacc()
result = parser.parse(" ")#Tendría que poder leer el código fuente

print(result) 