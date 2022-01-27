from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(background='grey')
mi_frame = Frame(root, background='#424242')
root.title('Calculadora')
root.geometry('323x372')
root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)
mi_frame.pack()
operaciones = ''
resultado = 0
reset_pantalla = False
el_numero = 0
contador_resta = 0
contador_multiplicacion = 0
contador_division = 0
contador_modulo = 0
contador_reset_todo = 0
contador_reset = 0
contador_eliminar = 0


# ------------------------------------------------------------------------ Barra Menu

barra_menu = Menu(root)
root.config(menu=barra_menu)

def salir_calculadora():
    valor = messagebox.askokcancel('Exit', 'Do you wanna leave?')
    if valor == True:
        root.destroy()

def info_adicional():
    messagebox.showinfo('Calculadora', 'Version 2022\nAlbanochicharroaltur@gmail.com')


archivo_menu = Menu(barra_menu, tearoff=0)

archivo_menu.add_command(label='About', command=info_adicional)
archivo_menu.add_command(label='Exit', command=salir_calculadora)

barra_menu.add_cascade(label='Menu', menu=archivo_menu)


# ------------------------------------------------------------------------ Pantalla

numero_pantalla = StringVar()
pantalla = Entry(mi_frame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=5, pady=10, columnspan=4)
pantalla.config(background='black', fg='white', justify='right', width=14, font=('Helvetica', 30, 'bold'))


# ------------------------------------------------------------------------ def Numero Pulsado

def numero_pulsado(numero):

    global operaciones
    global reset_pantalla

    if operaciones != '':
        numero_pantalla.set(numero)
        reset_pantalla = False
    else:
        numero_pantalla.set(numero_pantalla.get() + numero)


# ------------------------------------------------------------------------ Def El Resultado

def resultado_igual():

    global resultado
    global contador_resta
    global contador_multiplicacion
    global contador_division
    global contador_modulo
    global contador_reset_todo

    if operaciones == 'suma':

        numero_pantalla.set(resultado + int(numero_pantalla.get()))
        resultado = 0

    elif operaciones == 'resta':

        numero_pantalla.set(int(resultado) - int(numero_pantalla.get()))
        resultado = 0
        contador_resta = 0

    elif operaciones == 'multiplicacion':

        numero_pantalla.set(int(resultado) * int(numero_pantalla.get()))
        resultado = 0
        contador_multiplicacion = 0

    elif operaciones == 'division':

        numero_pantalla.set(float(resultado) / float(numero_pantalla.get()))
        resultado = 0
        contador_division = 0

    elif operaciones == 'modulo':

        numero_pantalla.set(int(resultado) % int(numero_pantalla.get()))
        resultado = 0
        contador_modulo = 0


    elif operaciones == 'reset_todo':

        numero_pantalla.set(int(resultado) + int(numero_pantalla.get()))
        resultado = 0
        contador_reset_todo = 0

    elif operaciones == 'reset':

        numero_pantalla.set(int(resultado) + int(numero_pantalla.get()))
        resultado = 0
        contador_reset_todo = 0

    else:
        'Error, please restart the app'


# ------------------------------------------------------------------------ Def Suma


def suma(numero):

    global operaciones
    global resultado
    global reset_pantalla
    resultado += int(numero)
    operaciones = 'suma'
    reset_pantalla = True
    numero_pantalla.set(resultado)


# ------------------------------------------------------------------------ Def Resta


def resta(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global el_numero
    global contador_resta

    if contador_resta == 0:
        el_numero = int(numero)
        resultado = numero

    else:
        if contador_resta == 1:
            resultado = el_numero - int(numero)

        else:
            resultado = int(resultado) - int(numero)

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_resta += 1
    operaciones = "resta"
    reset_pantalla = True


# ------------------------------------------------------------------------ Def Multiplicacion

def multiplicacion(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global el_numero
    global contador_multiplicacion

    if contador_multiplicacion == 0:
        el_numero = int(numero)
        resultado = numero

    else:
        if contador_multiplicacion == 1:
            resultado = el_numero * int(numero)

        else:
            resultado = int(resultado) * int(numero)

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_multiplicacion += 1
    operaciones = 'multiplicacion'
    reset_pantalla = True


# ------------------------------------------------------------------------ Def Division

def division(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global el_numero
    global contador_division

    if contador_division == 0:
        resultado = float(numero)
        resultado = numero

    else:
        if contador_division == 1:
            resultado = el_numero / float(numero)

        else:
            resultado = float(resultado) / float(numero)

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_division += 1
    operaciones = 'division'
    reset_pantalla = True


# ------------------------------------------------------------------------ Def Modulo

def modulo(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global el_numero
    global contador_modulo

    if contador_modulo == 0:
        resultado = int(numero)
        resultado = numero

    else:
        if contador_modulo == 1:
            resultado = el_numero / int(numero)

        else:
            resultado = int(resultado) % int(numero)

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_modulo += 1
    operaciones = 'modulo'
    reset_pantalla = True


# ------------------------------------------------------------------------ Def Eliminar

def eliminar(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global el_numero
    global contador_eliminar

    if contador_eliminar == 0:
        resultado = int(numero)
        resultado = numero

    else:
        if contador_eliminar == 1:
            resultado = el_numero - int(numero)

        else:
            resultado = int(resultado) - int(numero)

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_eliminar += 1
    operaciones = 'eliminar'
    reset_pantalla = True


# ------------------------------------------------------------------------ Def Reset_Todo

def reset_todo(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global contador_reset_todo

    if contador_reset_todo == 0:
        resultado = int(numero)
        resultado = 0

    else:
        if contador_reset_todo == 1:
            resultado = 0

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_reset_todo += 1
    operaciones = 'reset_todo'
    reset_pantalla = True


# ------------------------------------------------------------------------ Def Reset

def reset(numero):

    global operaciones
    global resultado
    global reset_pantalla
    global contador_reset

    if contador_reset == 0:
        resultado = 0
        resultado = numero

    else:
        if contador_reset == 1:
            resultado = 0

        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_reset += 1
    operaciones = 'reset'
    reset_pantalla = True


# ------------------------------------------------------------------------ Fila 1


boton_ce = Button(mi_frame, text='CE', width=10, height=3, command=lambda: reset_todo(numero_pantalla.get()))
boton_ce.grid(row=2, column=1)
boton_ce.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_c = Button(mi_frame, text='C', width=10, height=3, command=lambda: reset(numero_pantalla.get()))
boton_c.grid(row=2, column=2)
boton_c.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_atras = Button(mi_frame, text='<=', width=10, height=3, command=lambda: eliminar(numero_pantalla.get()))
boton_atras.grid(row=2, column=3)
boton_atras.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_dividir = Button(mi_frame, text='/', width=10, height=3, command=lambda: division(numero_pantalla.get()))
boton_dividir.grid(row=2, column=4)
boton_dividir.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

# ------------------------------------------------------------------------ Fila 2

boton_7 = Button(mi_frame, text='7', width=10, height=3, command=lambda: numero_pulsado('7'))
boton_7.grid(row=3, column=1)
boton_7.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_8 = Button(mi_frame, text='8', width=10, height=3, command=lambda: numero_pulsado('8'))
boton_8.grid(row=3, column=2)
boton_8.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_9 = Button(mi_frame, text='9', width=10, height=3, command=lambda: numero_pulsado('9'))
boton_9.grid(row=3, column=3)
boton_9.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_x = Button(mi_frame, text='X', width=10, height=3, command=lambda: multiplicacion(numero_pantalla.get()))
boton_x.grid(row=3, column=4)
boton_x.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

# ------------------------------------------------------------------------ Fila 3

boton_4 = Button(mi_frame, text='4', width=10, height=3, command=lambda: numero_pulsado('4'))
boton_4.grid(row=4, column=1)
boton_4.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_5 = Button(mi_frame, text='5', width=10, height=3, command=lambda: numero_pulsado('5'))
boton_5.grid(row=4, column=2)
boton_5.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_6 = Button(mi_frame, text='6', width=10, height=3, command=lambda: numero_pulsado('6'))
boton_6.grid(row=4, column=3)
boton_6.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_restar = Button(mi_frame, text='-', width=10, height=3, command=lambda: resta(numero_pantalla.get()))
boton_restar.grid(row=4, column=4)
boton_restar.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

# ------------------------------------------------------------------------ Fila 4

boton_1 = Button(mi_frame, text='1', width=10, height=3, command=lambda: numero_pulsado('1'))
boton_1.grid(row=5, column=1)
boton_1.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_2 = Button(mi_frame, text='2', width=10, height=3, command=lambda: numero_pulsado('2'))
boton_2.grid(row=5, column=2)
boton_2.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_3 = Button(mi_frame, text='3', width=10, height=3, command=lambda: numero_pulsado('3'))
boton_3.grid(row=5, column=3)
boton_3.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_sumar = Button(mi_frame, text='+', width=10, height=3, command=lambda: suma(numero_pantalla.get()))
boton_sumar.grid(row=5, column=4)
boton_sumar.config(background='grey', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

# ------------------------------------------------------------------------ Fila 5

boton_modulo = Button(mi_frame, text='%', width=10, height=3, command=lambda: modulo(numero_pantalla.get()))
boton_modulo.grid(row=6, column=1)
boton_modulo.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_0 = Button(mi_frame, text='0', width=10, height=3, command=lambda: numero_pulsado('0'))
boton_0.grid(row=6, column=2)
boton_0.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_coma = Button(mi_frame, text=',', width=10, height=3, command=lambda: numero_pulsado('.'))
boton_coma.grid(row=6, column=3)
boton_coma.config(background='#424242', fg='white', justify='center', font=('Helvetica', 9, 'bold'))

boton_igual = Button(mi_frame, text='=', width=10, height=3, command=lambda: resultado_igual())
boton_igual.grid(row=6, column=4)
boton_igual.config(background='darkgrey', fg='black', justify='center', font=('Helvetica', 9, 'bold'))

mi_frame.mainloop()
