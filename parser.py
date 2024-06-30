import ply.yacc as yacc
from lexer import tokens

# Definición de la gramática

def p_sigma(p):
    '''Sigma : lla Empresas comma Version comma Firma_digital llc
             | lla Empresas comma Firma_digital comma Version llc
             | lla Version comma Empresas comma Firma_digital llc
             | lla Version comma Firma_digital comma Empresas llc
             | lla Firma_digital comma Version comma Empresas llc
             | lla Firma_digital comma Empresas comma Version llc
             | lla Empresas comma Version llc
             | lla Empresas comma Firma_digital llc'''

def p_empresas(p):
    '''Empresas : lla EmpresaE llc'''

def p_empresaE(p):
    '''EmpresaE : EmpresaE comma Empresa
                | Empresa'''

def p_empresa(p):
    '''Empresa : lla Nombre_empresa comma fundacion comma Direccion comma ingresos_anuales comma Pyme comma Link comma Departamentos llc
               | lla Nombre_empresa comma fundacion comma Direccion comma ingresos_anuales comma Pyme comma Departamentos llc'''

def p_nombre_empresa(p):
    '''Nombre_empresa : nombre_empresa dp string'''

def p_direccion(p):
    '''Direccion : lla calle comma ciudad comma pais llc
                 | lla calle comma pais comma ciudad llc
                 | lla ciudad comma calle comma pais llc
                 | lla ciudad comma pais comma calle llc
                 | lla pais comma calle comma ciudad llc
                 | lla pais comma ciudad comma calle llc
                 | lla llc'''

def p_departamentos(p):
    '''Departamentos : pa DepartamentoD pc'''

def p_departamentoD(p):
    '''DepartamentoD : DepartamentoD comma Departamento
                     | Departamento'''

def p_departamento(p):
    '''Departamento : lla nombre comma jefe comma Subdepartamentos llc
                    | lla nombre comma Subdepartamentos llc
                    | lla Subdepartamentos comma nombre comma jefe llc
                    | lla Subdepartamentos comma nombre llc
                    | lla jefe comma nombre comma Subdepartamentos llc
                    | lla jefe comma Subdepartamentos comma nombre llc'''   

def p_subdepartamentos(p):
    '''Subdepartamentos : pa SubdepartamentoS pc'''

def p_subdepartamentoS(p):
    '''SubdepartamentoS : SubdepartamentoS comma Subdepartamento
                        | Subdepartamento'''

def p_subdepartamento(p):
    '''Subdepartamento : lla nombre comma jefe comma Empleados llc
                       | lla nombre comma Empleados llc
                       | lla Empleados comma nombre comma jefe llc
                       | lla Empleados comma nombre llc
                       | lla jefe comma nombre comma Empleados llc
                       | lla jefe comma Empleados comma nombre llc'''

def p_empleados(p):
    '''Empleados : pa EmpleadoE pc
                 | pa pc'''
    
def p_empleadoE(p):
    '''EmpleadoE : EmpleadoE comma Empleado
                 | Empleado'''

def p_empleado(p):
    '''Empleado : lla nombre comma edad comma cargo comma salario comma activo comma fecha_contratacion llc
                | lla nombre comma cargo comma salario comma activo comma fecha_contratacion llc
                | lla nombre comma edad comma salario comma activo comma fecha_contratacion llc'''

def p_proyectos(p):
    '''Proyectos : pa ProyectoP pc
                 | pa pc'''

def p_proyectoP(p):
    '''ProyectoP : ProyectoP comma Proyecto
                 | Proyecto'''

def p_proyecto(p):
    '''Proyecto : lla nombre comma estado comma fecha_inicio comma fecha_fin llc
                | lla nombre comma fecha_inicio llc
                | lla nombre comma estado comma fecha_inicio llc'''

def p_firma_digital(p):
    '''Firma_digital : firma_digital dp string'''

def p_version(p):
    '''Version : version dp string'''

def p_pyme(p):
    '''Pyme : pyme dp bool'''

def p_link(p):
    '''Link : link dp patron_url'''

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
