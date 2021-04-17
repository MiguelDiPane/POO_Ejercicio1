from ClaseEmail import Email
import csv

#Funcion para testear correos validos e invalidos
def test():
    archivo = open('correosTest.csv')
    reader = csv.reader(archivo,delimiter=',')

    for fila in reader:
        print('Test con correo: {}'.format(fila[0]))
        correo = Email()
        correo.crearCuenta(fila[0])
    archivo.close()
    
if __name__ == '__main__':
    #Ejecucion de funcion test
    op = input('Desea ejecutar la funcion test [S/N]: ')
    if(op.lower() == 's'):
        test()
        
    #APARTADO 1
    print('APARTADO 1')
    #Solicito nombre
    nombre = input('Ingrese nombre: ')

    #Creo una cuenta para el usuario
    miCorreo = Email()
    correo = input('Ingrese su correo: ')
    error = miCorreo.crearCuenta(correo)
    while(error):
        correo = input('Ingrese su correo: ')
        error = miCorreo.crearCuenta(correo) 

    #Imprimo mensaje:
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre,miCorreo.retornaEmail()))

    #Apartado 2
    print('APARTADO 2')
    miCorreo.changePass()

    #Apartado 3
    print('APARTADO 3')
    nuevoCorreo = Email()
    nuevoCorreo.crearCuenta('informatica.fcefn@gmail.com')

    #Apartado 4
    print('APARTADO 4')
    archivo = open('correos.csv')
    reader = csv.reader(archivo,delimiter=',')

    dominio = input('Ingrese un dominio: ')
    cont = 0 #contador de dominios
    bandera  = True
    for fila in reader:
        if bandera: #Salto el encabezado del archivo csv
            bandera = False
        else:
            correo = Email()
            correo.crearCuenta(fila[0],fila[1])
            miDominio = correo.getDominio()
            if dominio == miDominio:
                cont += 1
    archivo.close()

    print('{} direcciones de e-mail tienen dominio igual al ingresado ({}).'.format(cont,dominio))
    
    

    
