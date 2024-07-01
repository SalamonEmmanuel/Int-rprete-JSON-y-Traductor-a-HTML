import ply.yacc as yacc
from lexer import tokens
import re
import os
import codecs
import tkinter
from tkinter import filedialog
from tkinter import Entry, Frame,Tk ,Text, filedialog, ttk, messagebox

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
             
def p_EmpresasI(p):
    '''EmpresasI : empresas dp pa Empresas pc'''

def p_Empresas(p):
    '''Empresas : Empresa_list'''

def p_Empresa_list(p):
    '''Empresa_list : Empresa_list comma Empresa
                    | Empresa'''
    
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
    '''Nombre_empresa : nombre_empresa dp string''' ####

# si pongo esto me tira error
def p_Fundacion(p):
    '''Fundacion : fundacion dp integer'''

#regla
def p_direccion(p): ## aca agregué "direccion"
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
    
#regla
def p_Departamento(p):
    '''Departamento : lla Nombre comma Jefe comma Subdepartamentos llc
                    | lla Nombre comma Subdepartamentos llc
                    | lla Subdepartamentos comma Nombre comma Jefe llc
                    | lla Subdepartamentos comma Nombre llc
                    | lla Jefe comma Nombre comma Subdepartamentos llc
                    | lla Jefe comma Subdepartamentos comma Nombre llc'''   

def p_Subdepartamentos(p):
    '''Subdepartamentos : subdepartamentos dp pa Subdepartamento_list pc'''

def p_Subdepartamento_list(p):
    '''Subdepartamento_list : Subdepartamento_list comma Subdepartamento
                            | Subdepartamento'''

#regla
def p_Subdepartamento(p):
    '''Subdepartamento : lla Nombre comma Jefe comma Empleados llc
                       | lla Nombre llc
                       | lla Nombre comma Jefe llc
                       | lla Nombre comma Empleados llc'''

def p_Empleados(p):
    '''Empleados : empleados dp pa Empleado_list pc
                 | empleados dp pa pc'''

def p_Empleado_list(p):
    '''Empleado_list : Empleado_list comma Empleado
                     | Empleado'''

#regla
def p_Empleado(p):
    '''Empleado : lla Nombre comma Edad comma Cargo comma Salario comma Activo comma Fecha_contratacion comma Proyectos llc
                | lla Nombre comma Cargo comma Salario comma Activo comma Fecha_contratacion llc
                | lla Nombre comma Cargo comma Edad comma Salario comma Activo comma Fecha_contratacion comma Proyectos llc'''

def p_Proyectos(p):
    '''Proyectos : proyectos dp pa Proyecto_list pc
                 | proyectos dp pa pc
                 | proyectos dp null'''

def p_Proyecto_list(p):
    '''Proyecto_list : Proyecto_list comma Proyecto
                     | Proyecto'''

#regla
def p_proyecto(p):
    '''Proyecto : lla Nombre comma Estado comma Fecha_inicio comma Fecha_fin llc
                | lla Nombre comma Fecha_inicio llc
                | lla Nombre comma Estado comma Fecha_inicio llc'''

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

#Funcion interactuar con caja de texto superior
def Pantalla():
    global codigo, correcto, textocreado, Arch

    pantalla1.configure(state="normal")
    pantalla1.delete("1.0", "end")
    pantalla1.configure(state="disabled")

    codigo = pantalla.get("1.0", 'end-1c')
   
    correcto = 0

    parser.parse(codigo)

    if codigo != "" and correcto == 0:
        respuesta = messagebox.askquestion("Resultado", "Compilación exitosa.\n¿Desea guardar el código como archivo HTML?", icon="question")

        if respuesta == 'yes':
            if textocreado != "" and correcto == 0:
                if Arch != None:
                    messagebox.showinfo("Resultado", "Elija el lugar para guardar el archivo ;)")
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
    tipos_archivo = [("", "*.txt *.xml")]
    Archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=tipos_archivo)
    Arch = codecs.open(Archivo, "r", encoding="utf-8")
    a = Arch.read()
    pantalla.delete("1.0", "end")
    pantalla.insert('1.0', a)

ventana_principal=Tk()
ventana=Frame(ventana_principal)
ventana_principal.title("Parser G-22")
ventana_principal.resizable(0, 0)

#Caja de texto superior
pantalla= Entry(ventana)
pantalla= Text( width=100, height=20, font=("Helvetica", 10))

#Ubicar caja
pantalla.grid (row=1, column=0, columnspan=4,padx=10,pady=10)

#Caja de inferior
pantalla1= Entry(ventana)
pantalla1= Text(width=100, height=10, font=("Helvetica", 10))
pantalla1.configure(state="disabled")

#Ubicar caja
pantalla1.grid (row=2, column=0, columnspan=4,padx=10,pady=10)

#Boton Abrir archivo
ventana.boton_abrirarchivo= ttk.Button(text="Abrir Archivo", command=OpenArch, width=20).grid(row=3,column=0,pady=15,columnspan=2)

#Boton compilar
ventana.boton_compilar= ttk.Button(text="Compilar", command=Pantalla, width=20).grid(row=3, column=1,padx=10,pady=15,columnspan=2)

#Boton Exit
ventana.boton_cerrar= ttk.Button(ventana_principal,text='Cerrar',command=lambda: ventana_principal.quit(), width=20).grid(row=3, column=2,pady=15, columnspan=2)

ventana_principal.mainloop()
