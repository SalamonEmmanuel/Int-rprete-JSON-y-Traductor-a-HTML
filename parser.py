import ply.yacc as yacc
from lexer import tokens

# Definición de la gramática

#regla1
def p_Sigma(p):
    '''Sigma : lla EmpresasI comma Version comma Firma_digital llc
             | lla EmpresasI comma Firma_digital comma Version llc
             | lla Version comma EmpresasI comma Firma_digital llc
             | lla Version comma Firma_digital comma pa EmpresasI pc llc
             | lla Firma_digital comma Version comma EmpresasI llc
             | lla Firma_digital comma EmpresasI comma Version llc
             | lla EmpresasI comma Version llc
             | lla EmpresasI comma Firma_digital llc
             | lla EmpresasI llc '''
             
#regla2
def p_EmpresasI(p):
    '''EmpresasI : dp pa Empresas pc'''

#regla
def p_Empresas(p):
    '''Empresas : lla EmpresaE llc'''

#regla
def p_EmpresaE(p):
    '''EmpresaE : EmpresaE
                | Empresa'''

#regla
def p_Empresa(p):
    '''Empresa : lla Nombre_empresa comma Fundacion comma Direccion comma Ingresos_anuales comma Pyme comma Link comma Departamentos llc
               | lla Nombre_empresa comma Fundacion comma Direccion comma Ingresos_anuales comma Pyme comma Departamentos llc'''

#regla
def p_Nombre_empresa(p):
    '''Nombre_empresa : nombre_empresa dp string'''

#regla
def p_direccion(p):
    '''Direccion : lla Calle comma ciudad comma Pais llc
                 | lla Calle comma Pais comma ciudad llc
                 | lla ciudad comma Calle comma Pais llc
                 | lla ciudad comma Pais comma Calle llc
                 | lla Pais comma Calle comma ciudad llc
                 | lla Pais comma ciudad comma Calle llc
                 | lla llc'''

#regla
def p_Departamentos(p):
    '''Departamentos : pa DepartamentoD pc'''

#regla
def p_DepartamentoD(p):
    '''DepartamentoD : DepartamentoD
                     | Departamento'''

#regla
def p_Departamento(p):
    '''Departamento : lla Nombre comma Jefe comma Subdepartamentos llc
                    | lla Nombre comma Subdepartamentos llc
                    | lla Subdepartamentos comma Nombre comma Jefe llc
                    | lla Subdepartamentos comma Nombre llc
                    | lla Jefe comma Nombre comma Subdepartamentos llc
                    | lla Jefe comma Subdepartamentos comma Nombre llc'''   

#regla
def p_Subdepartamentos(p):
    '''Subdepartamentos : pa SubdepartamentoS pc'''

#regla
def p_SubdepartamentoS(p):
    '''SubdepartamentoS : SubdepartamentoS 
                        | Subdepartamento'''

#regla
def p_Subdepartamento(p):
    '''Subdepartamento : lla Nombre comma Jefe comma Empleados llc
                       | lla Nombre llc
                       | lla Nombre comma Jefe llc
                       | lla Nombre comma Empleados llc'''

#regla
def p_Empleados(p):
    '''Empleados : pa EmpleadoE pc
                 | pa pc'''

#regla   
def p_EmpleadoE(p):
    '''EmpleadoE : EmpleadoE 
                 | Empleado'''

#regla
def p_empleado(p):
    '''Empleado : lla nombre comma Edad comma Cargo comma Salario comma Activo comma Fecha_contratacion comma Proyectos llc
                | lla nombre comma Cargo comma Salario comma Activo comma Fecha_contratacion llc
                | lla nombre comma Cargo comma Edad comma Salario comma Activo comma Fecha_contratacion comma Proyectos llc'''

#regla
def p_Proyectos(p):
    '''Proyectos : pa ProyectoP pc
                 | pa pc'''

#regla
def p_ProyectoP(p):
    '''ProyectoP : ProyectoP 
                 | Proyecto'''

#regla
def p_proyecto(p):
    '''Proyecto : lla nombre comma estado comma Fecha_inicio comma Fecha_fin llc
                | lla nombre comma Fecha_inicio llc
                | lla nombre comma Estado comma Fecha_inicio llc'''

#deriva de Sigma
#regla
def p_Version(p):
    '''Version : version dp null
               | version dp string'''

    
#regla
def p_Firma_digital(p):
    '''Firma_digital : firma_digital dp string
                     | firma_digital dp null'''


#regla
def p_Estado(p):
    '''Estado : estado dp ESTADO_PROYECTO
              | estado dp null'''

#regla
def p_Jefe(p):
    '''Jefe : jefe dp null
            | jefe dp string'''

#regla
def p_Link(p):
    '''Link : link dp patron_url
            | link dp null'''

#regla
def p_Fecha_inicio(p):
    '''Fecha_inicio : fecha_inicio dp date'''


#regla
def p_Fecha_fin(p):
    '''Fecha_fin : fecha_fin dp null
                 | fecha_fin dp date'''

#regla
def p_Fecha_contratacion(p):
    '''Fecha_contratacion : fecha_contratacion dp date'''

#regla
def p_Nombre(p):
    '''Nombre : nombre dp string'''

#regla
def p_Pais(p):
    '''Pais : pais dp string'''

#regla
def p_Calle(p):
    '''Calle : calle dp string'''

#regla
def p_Ciudad(p):
    '''Ciudad : ciudad dp string'''

#regla
def p_Fundacion(p):
    '''Fundacion : fundacion dp integer'''

#regla
def p_Activo(p):
    '''Activo : activo dp bool'''

#regla
def p_Pyme(p):
    '''Pyme : pyme dp bool'''

#regla
def p_Ingresos_anuales(p):
    '''Ingresos_anuales : ingresos_anuales dp float'''

#regla
def p_Cargo(p):
    '''Cargo : cargo dp CARGO_EMPLEADO'''

#regla
def p_Salario(p):
    '''Salario : salario dp float'''

#regla
def p_Edad(p):
    '''Edad : edad dp integer'''
    

def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

parser = yacc.yacc()

# Probamos el parser
data = '''{
    "empresas": [
        {
            "nombre_empresa": "Mc Donalds",
            "fundacion": 2005,
            "direccion": {
                "calle": "Calle Falsa 123",
                "ciudad": "Springfield",
                "pais": "USA"
            },
            "ingresos_anuales": 200000.25,
            "pyme": false,
            "link": "https://www.mcdonalds.com.ar",
            "departamentos": [
                {
                    "nombre": "Ventas",
                    "jefe": "Cosme Fulanito",
                    "subdepartamentos": [
                        {
                            "nombre": "Mc Donalds JUC",
                            "jefe": "Krusty",
                            "empleados": [
                                {
                                    "nombre": "Sideshow Mel",
                                    "edad": 30,
                                    "cargo": "Product Analyst",
                                    "salario": 1250.65,
                                    "activo": true,
                                    "fecha_contratacion": "2023-09-10",
                                    "proyectos": [
                                        {
                                            "nombre": "Mc Flurry",
                                            "estado": "In progress",
                                            "fecha_inicio": "2022-01-10",
                                            "fecha_fin": "2025-08-25"
                                        },
                                        {
                                            "nombre": "Mcnifica",
                                            "estado": "Done",
                                            "fecha_inicio": "2020-10-13",
                                            "fecha_fin": "2024-01-01"
                                        }
                                    ]
                                },
                                {
                                    "nombre": "Krusty",
                                    "edad": 45,
                                    "cargo": "Developer",
                                    "salario": 32250.65,
                                    "activo": true,
                                    "fecha_contratacion": "2020-05-15",
                                    "proyectos": [
                                        {
                                            "nombre": "Mc chicken",
                                            "estado": "On hold",
                                            "fecha_inicio": "2022-01-10"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "nombre": "Mc Donalds Chicken",
                            "jefe": "Principal Skinner",
                            "empleados": [
                                {
                                    "nombre": "Principal Skinner",
                                    "edad": 30,
                                    "cargo": "Project Manager",
                                    "salario": 150.65,
                                    "activo": true,
                                    "fecha_contratacion": "2023-09-10",
                                    "proyectos": [
                                        {
                                            "nombre": "Chicken burger",
                                            "estado": "In progress",
                                            "fecha_inicio": "2022-01-10",
                                            "fecha_fin": "2025-08-25"
                                        },
                                        {
                                            "nombre": "Rechicken",
                                            "estado": "Done",
                                            "fecha_inicio": "2020-10-13",
                                            "fecha_fin": "2024-01-01"
                                        }
                                    ]
                                },
                                {
                                    "nombre": "Edna Krabappel",
                                    "edad": 35,
                                    "cargo": "Marketing",
                                    "salario": 350.65,
                                    "activo": false,
                                    "fecha_contratacion": "2020-05-15",
                                    "proyectos": [
                                        {
                                            "nombre": "Chicken roll",
                                            "estado": "Canceled",
                                            "fecha_inicio": "2022-01-10",
                                            "fecha_fin": "2022-02-20"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "nombre": "Compras",
                    "jefe": "Fat Tony",
                    "subdepartamentos": [
                        {
                            "nombre": "Comestibles",
                            "jefe": "Apu Nahasapeemape",
                            "empleados": [
                                {
                                    "nombre": "Apu Nahasapeemape",
                                    "edad": 34,
                                    "cargo": "Product Analyst",
                                    "salario": 250.65,
                                    "activo": true,
                                    "fecha_contratacion": "2023-09-10",
                                    "proyectos": [
                                        {
                                            "nombre": "kwik-e-mart",
                                            "estado": "In progress",
                                            "fecha_inicio": "2022-01-10"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "nombre": "Cobranzas",
                            "empleados": []
                        }
                    ]
                }
            ]
        },
        {
            "nombre_empresa": "Beetroot squad",
            "fundacion": 1990,
            "direccion": {
                "calle": "Calle Falsa 333",
                "ciudad": "shelbyville",
                "pais": "USA"
            },
            "ingresos_anuales": 2000.25,
            "pyme": true,
            "departamentos": [
                {
                    "nombre": "Produccion",
                    "jefe": "Shelbyville Manhattan",
                    "subdepartamentos": [
                        {
                            "nombre": "Desarrollo",
                            "jefe": "Jack Bauer",
                            "empleados": [
                                {
                                    "nombre": "Jack Bauer",
                                    "edad": 30,
                                    "cargo": "Developer",
                                    "salario": 10.65,
                                    "activo": true,
                                    "fecha_contratacion": "1991-09-10",
                                    "proyectos": [
                                        {
                                            "nombre": "Jugo betabel",
                                            "estado": "In progress",
                                            "fecha_inicio": "2022-01-10"
                                        }
                                    ]
                                },
                                {
                                    "nombre": "Shelby",
                                    "edad": 8,
                                    "cargo": "Developer",
                                    "salario": 50.65,
                                    "activo": true,
                                    "fecha_contratacion": "2010-05-15",
                                    "proyectos": null
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "version": "1.0",
    "firma_digital": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}'''

result = parser.parse(data)
print(result)
