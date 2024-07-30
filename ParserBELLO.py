import ply.yacc as yacc
from lexerFunciona import tokens
import os
import codecs
import tkinter
from tkinter import filedialog
from tkinter import Entry, Frame, Tk, Text, filedialog, ttk, messagebox, Label
from ttkthemes import ThemedTk 
import json

# Definición de la gramática

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

# control de errores
def p_error(p):
    global correcto
    correcto=1
    pantalla1.configure(state="normal")
    pantalla1.insert('1.0', "Error en la línea "+str(p.lineno)+"\nVerifique la cadena "+str(p.value)+"\n\n")
    pantalla1.configure(state="disabled")

parser = yacc.yacc()

textocreado = ""
correcto=0

codigo = ""
Arch = None


def json_to_html(data):
    html_output = []

    def process_company(company):
        html_output.append('<div style="border:1px solid gray; padding:20px; margin-bottom:20px;">')
        html_output.append(f'<h1>{company["nombre_empresa"]}</h1>')

        if "link" in company and company["link"] is not None:
            html_output.append(f'<a href="{company["link"]}">Link</a>')

        for dept in company.get("departamentos", []):
            process_department(dept)

        html_output.append('</div>')

    def process_department(department):
        html_output.append('<div style="margin-left:20px;">')
        html_output.append(f'<h2>{department["nombre"]}</h2>')

        for subdept in department.get("subdepartamentos", []):
            process_subdepartment(subdept)

        html_output.append('</div>')

    def process_subdepartment(subdepartment):
        html_output.append('<div style="margin-left:40px;">')
        html_output.append(f'<h3>{subdepartment["nombre"]}</h3>')

        for emp in subdepartment.get("empleados", []):
            process_employee(emp)

        html_output.append('</div>')

    def process_employee(employee):
        html_output.append('<div style="border:1px solid blue; padding:10px; margin-left:60px; margin-bottom:10px;">')
        html_output.append(f'<h4>{employee["nombre"]}</h4>')

        if "proyectos" in employee:
            html_output.append('<table border="1" style="width:100%; margin-top:10px;">')
            html_output.append('<tr><th>Nombre</th><th>Estado</th><th>Fecha Inicio</th><th>Fecha Fin</th></tr>')
            for proj in employee["proyectos"] or []:
                html_output.append('<tr>')
                html_output.append(f'<td>{proj["nombre"]}</td>')
                html_output.append(f'<td>{proj.get("estado", "")}</td>')
                html_output.append(f'<td>{proj.get("fecha_inicio", "")}</td>')
                html_output.append(f'<td>{proj.get("fecha_fin", "")}</td>')
                html_output.append('</tr>')
            html_output.append('</table>')

        html_output.append('</div>')

    for empresa in data.get("empresas", []):
        process_company(empresa)

    return '\n'.join(html_output)

def Pantalla():
    global codigo, correcto, textocreado, Arch

    pantalla1.configure(state="normal")
    pantalla1.delete("1.0", "end")
    pantalla1.configure(state="disabled")

    codigo = pantalla.get("1.0", 'end-1c')
   
    correcto = 0

    parser.parse(codigo)

    if codigo != "" and correcto == 0:
        # Traducir a HTML
        try:
            json_data = json.loads(codigo)
            textocreado = json_to_html(json_data)
        except json.JSONDecodeError as e:
            pantalla1.configure(state="normal")
            pantalla1.insert('1.0', f"Error en la traducción JSON a HTML: {str(e)}\n\n")
            pantalla1.configure(state="disabled")
            return

        respuesta = messagebox.askquestion("Resultado", "Compilación exitosa.\n¿Desea guardar el código como archivo HTML?", icon="question")

        if respuesta == 'yes':
            if textocreado != "" and correcto == 0:
                if Arch != None:
                    messagebox.showinfo("Resultado", "Elija el lugar para guardar el archivo")
                    file_path = filedialog.asksaveasfilename(initialfile=os.path.splitext(os.path.basename(Arch.name))[0], defaultextension=".html", filetypes=[("Archivos HTML", "*.html")])
                    if file_path:
                        with open(file_path, "w") as archivo_guardado:
                            archivo_guardado.write(textocreado)
                            messagebox.showinfo("Resultado", "Archivo guardado correctamente como HTML.")
                else:
                    messagebox.showinfo("Resultado", "Asigne un nombre y elija el lugar para guardar el archivo ;)")
                    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("Archivos HTML", "*.html")])
                    if file_path:
                        with open(file_path, "w") as archivo_guardado:
                            archivo_guardado.write(textocreado)
                            messagebox.showinfo("Resultado", "Archivo guardado correctamente como HTML.")
    else:
        textocreado=""
         

#Funcion abrir archivo
def OpenArch():
    global Arch
    tipos_archivo = [("Archivos JSON", "*.json")]
    Archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=tipos_archivo)
    Arch = codecs.open(Archivo, "r", encoding="utf-8")
    ttk.Style().theme_use('vista') 
    a = Arch.read()
    pantalla.delete("1.0", "end")
    pantalla.insert('1.0', a)

#Definición del estilo de la ventana
ventana_principal = ThemedTk(theme="classic")
ventana=Frame(ventana_principal)
ventana_principal.title("Black Mesa Translator")
ventana_principal.resizable(0, 0)

# Configurar el layout de la ventana principal
ventana_principal.columnconfigure(0, weight=1)
ventana_principal.columnconfigure(1, weight=1)

# Color de la ventana principal
ventana_principal.configure(bg="#ED9121")

# Etiqueta para el cuadro de texto izquierdo
label_texto_analizar = Label(ventana_principal, text="Texto a analizar:", font=("Helvetica", 10), bg="#ED9121")
label_texto_analizar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

# Caja de texto izquierda
pantalla = Text(ventana_principal, width=50, height=20, font=("Helvetica", 10), bg="floralwhite", fg="black")
pantalla.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Etiqueta para el cuadro de texto derecho
label_texto_analizar = Label(ventana_principal, text="Errores:", font=("Helvetica", 10), bg="#ED9121")
label_texto_analizar.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")

# Caja de texto derecha
pantalla1 = Text(ventana_principal, width=50, height=20, font=("Helvetica", 10), bg="gainsboro", fg="black")
pantalla1.grid(row=1, column=1, padx=10, pady=10, sticky="nsew") 

# Botón Abrir archivo
boton_abrirarchivo = ttk.Button(ventana_principal, text="Abrir Archivo", command=OpenArch, width=20)
boton_abrirarchivo.grid(row=2, column=0, padx=10, pady=15, sticky="ew")

# Botón Compilar
boton_compilar = ttk.Button(ventana_principal, text="Compilar", command=Pantalla, width=20)
boton_compilar.grid(row=2, column=1, padx=10, pady=15, sticky="ew") 

ventana_principal.mainloop()
