# Taller 2
# Procesamiento de imagenes y visión
# Manuela Bravo Soto

# IMPORTACIONES
from imageShape_class import imageShape # De la clase imageShape

if __name__ == '__main__':
    # DATOS INGRESADOS POR EL USUARIO
    width = int(input('Ingrese el ancho de la imagen: '))  # Solicitud al usuario del ancho de la imagen ej: 500
    height = int(input('Ingrese el alto de la imagen: '))  # Solicitud al usuario del alto de la imagen ej: 300

    # OBJETO
    # Se crea el objeto Image pasando como parámetro los datos ingresados por el usuario
    # Los atributos de este objeto son los de la clase imageShape
    Image = imageShape(width, height)

    Image.generateShape() # Generación de la figura
    Image.showShape() # Mostrar figura en pantalla por 5 segundos
    img, str = Image.getShape() # Obtención de la imagen y del nombre de la figura creada
    str1 = Image.whatShape() # Clasificación de la figura en 1 de las 4 clases
    print('La clase a la que pertenece es:', str1) # Mostrar resultado de la clasificación en pantalla
    # Si el nombre de la figura creada es el mismo que el resultado de la clasificación, la clasificación es correcta
    if str == str1:
        print('La clasificación es correcta')
    # De lo contrario, la clasificación es incorrecta
    else:
        print('La clasificación es incorrecta')