# Taller 2
# Procesamiento de imagenes y visión
# Manuela Bravo Soto

# IMPORTACIONES
import numpy as np # Del módulo numpy
import cv2 # Del módulo opencv-python
import math # Del módulo math

#CLASE imageShape
class imageShape:

    # CONSTRUCTOR
    # Recibe como parámetros el ancho y el alto de la imagen
    def __init__(self, width, height):
        self.width = width # Se guarda el ancho de la imagen en self
        self.height = height # Se guarda el ancho de la imagen en self
        # Se crea una imagen negra cuyas dimensiones corresponden a las ingresadas por el usuario
        # Si no se genera ninguna figura, la imagen es un fondo negro
        self.shape = np.zeros((self.height, self.width), np.uint8)
        self.name = 'Image' # Se crea el nombre de la imagen

    # MÉTODO PARA GENERAR FIGURA
    def generateShape(self):
        # Se crea una imagen negra cuyas dimensiones corresponden a las ingresadas por el usuario
        # Se vuelve a crear para generar una nueva imagen si se llama dos veces el método
        self.shape = np.zeros((self.height, self.width), np.uint8)
        self.shape = cv2.cvtColor(self.shape, cv2.COLOR_GRAY2BGR) # Se convierte la imagen del espacio de color gris al espacio de color BGR para generar la figura a color
        self.rand = np.random.randint(0, 4, None) # Se genera un número aleatorio uniformemente distribuido entero que toma los valores desde 0 hasta 3

        # Si el número aleatorio es 0 se obtiene un triángulo equilatero
        if self.rand == 0:
            self.lado = min(self.height, self.width)/2 # El lado de la figura será la mitad del mínimo entre las dimensiones del fondo
            self.altura = math.sqrt((self.lado)**2-(self.lado/2)**2) # Se calcula la altura del triángulo con pitágoras
            self.vert1 = (int(self.width/2 - self.lado/2), int(self.height/2 + self.altura/2)) # Se ubica el punto de la esquina inferior izquierda del triángulo en el plano para que esté centrado en el fondo de la imagen
            self.vert2 = (int(self.width/2 + self.lado/2), int(self.height/2 + self.altura/2)) # Se ubica el punto de la esquina inferior derecha del triángulo en el plano para que esté centrado en el fondo de la imagen
            self.vert3 = (int(self.width/2), int(self.height/2 - self.altura/2)) # Se ubica la punta del triángulo en el plano para que esté centrado en el fondo de la imagen
            self.color = (255, 255, 0) # Se identifica el color cyan de la figura
            self.triangle = np.array([self.vert1, self.vert2, self.vert3]) # Se crea un arreglo con los puntos de los vértices del triángulo
            self.shape = cv2.drawContours(self.shape, [self.triangle], 0, self.color, -1) # Se dibujan los contornos sobre el fondo negro entre los puntos de los vértices del triángulo y se rellena la figura de color cyan
            self.name = 'triangle' # Se le asigna el nombre de triángulo a la figura

        # Si el número aleatorio es 1 se obtiene un cuadrado
        elif self.rand == 1:
            self.lado = min(self.height, self.width)/2 # El lado de la figura será la mitad del mínimo entre las dimensiones del fondo
            self.startPoint = (int(self.width/2-self.lado/2), int(self.height/2-self.lado/2)) # Se obtienen las coordenadas de inicio del cuadrado para que esté centrado en el fondo de la imagen
            self.endPoint = (int(self.width/2+self.lado/2), int(self.height/2+self.lado/2)) # Se obtienen las coordenadas de finalización del cuadrado para que esté centrado en el fondo de la imagen
            self.color = (255, 255, 0) # Se identifica el color cyan de la figura
            self.shape = cv2.rectangle(self.shape, self.startPoint, self.endPoint, self.color, -1) # Se dibuja un rectángulo sobre el fondo negro descrito entre las coordenadas de inicio y de fin, y se rellena la figura de color cyan
            self.rotate = cv2.getRotationMatrix2D((self.width//2, self.height//2), 45, 1) # Se genera una matriz de rotación en 2D, que rota el punto central 45°
            self.shape = cv2.warpAffine(self.shape, self.rotate, (self.width, self.height)) # A partir de la matriz de rotación, ee rota 45° el cuadrado generado sobre su punto central
            self.name = 'square' # Se le asigna el nombre de cuadrado a la figura

        # Si el número aleatorio es 2 se obtiene un rectangulo
        elif self.rand == 2:
            self.lado_horizontal = self.width/2 # El lado horizontal de la figura será la mitad del ancho del fondo
            self.lado_vertical = self.height/2 # El lado vertical de la figura será la mitad del alto del fondo
            self.startPoint = (int(self.lado_horizontal - self.lado_horizontal/2), int(self.lado_vertical - self.lado_vertical/2)) # Se obtienen las coordenadas de inicio del cuadrado para que esté centrado en el fondo de la imagen
            self.endPoint = (int(self.lado_horizontal + self.lado_horizontal/2), int(self.lado_vertical + self.lado_vertical/2)) # Se obtienen las coordenadas de finalización del cuadrado para que esté centrado en el fondo de la imagen
            self.color = (255, 255, 0) # Se identifica el color cyan de la figura
            self.shape = cv2.rectangle(self.shape, self.startPoint, self.endPoint, self.color, -1) # Se dibuja un rectángulo sobre el fondo negro descrito entre las coordenadas de inicio y de fin, y se rellena la figura de color cyan
            # Si la longitud ingresada por el usuario del ancho y alto del fondo son iguales, la figura generada será un cuadrado
            if self.lado_horizontal == self.lado_vertical:
                self.name = 'square' # Se le asigna el nombre de cuadrado a la figura
            # De lo contrario, será un rectángulo
            else:
                self.name = 'rectangle' # Se le asigna el nombre de rectangulo a la figura

        # Si el número aleatorio es 3 se obtiene un circulo
        elif self.rand == 3:
            self.center = (int(self.width/2), int(self.height/2)) # El punto central del circulo será la mitad de las dimensiones del fondo
            self.radius = int(min(self.width, self.height)/4) # El radio del circulo será la cuarta parte del mínimo entre las dimensiones del fondo
            self.color = (255, 255, 0) # Se identifica el color cyan de la figura
            self.shape = cv2.circle(self.shape, self.center, self.radius, self.color, -1) # Se dibuja un circulo sobre el fondo negro en el punto central con el radio calculado, y se rellena la figura de color cyan
            self.name = 'circle' # Se le asigna el nombre de circulo a la figura

    # MÉTODO QUE MUESTRA LA FIGURA POR 5 SEGUNDOS
    # Si no se generó ninguna figura, muestra el fondo negro generado en el constructor con el nombre de 'Image'
    def showShape(self):
        cv2.imshow(self.name, self.shape) # Mostrar la imagen con el nombre de la imagen correspondiente
        cv2.waitKey(5000) # Mostrar en pantalla la imagen por 5 segundos

    # MÉTODO QUE RETORNA LA IMAGEN GENERADA Y EL NOMBRE
    def getShape(self):
        return self.shape, self.name

    # MÉTODO QUE CLASIFICA LA FIGURA GENERADA
    def whatShape(self):
        self.shape_gray = cv2.cvtColor(self.shape, cv2.COLOR_BGR2GRAY) # Se convierte la imagen del espacio de color BGR al espacio de color gris
        self.ret, self.shape_threshold = cv2.threshold(self.shape_gray, 150, 255, cv2.THRESH_BINARY) # Se binariza la imagen utilizando un umbral de 150
        self.shape_threshold_not = cv2.bitwise_not(self.shape_threshold) # Se realiza un NOT lógico a la imagen binarizada
        self.contours, self.hierarchy = cv2.findContours(self.shape_threshold_not, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # Se encuentran los contornos de la imagen binarizada luego de aplicar el NOT lógico
        # Para cada contorno se aproxima el polígono y se dibuja dicho contorno sobre la imagen BGR
        for self.idx in self.contours:
            self.shape_approx = cv2.approxPolyDP(self.idx, 0.01*cv2.arcLength(self.idx, True), True) # Se aproxima cada contorno al perímetro del polígono para obtener los vértices de la figura de contorno cerrado
            # Si la cantidad de vértices es 3, se clasifica como un triángulo
            if len(self.shape_approx) == 3:
                return 'triangle' # Retorna un string con el nombre de tipo de figura resultante
            # Si la cantidad de vértices es 4, se clasifica como un rectangulo o un cuadrado
            elif len(self.shape_approx) == 4:
                self.horizontal = self.shape_approx[2][0][0]-self.shape_approx[3][0][0] # Se calcula la longitud del lado horizontal de la figura
                self.vertical = self.shape_approx[3][0][1]-self.shape_approx[0][0][1] # Se calcula la longitud del lado vertical de la figura
                # Si el lado vertical y horizontal de la figura son diferentes en su longitud, la figura se clasifica como un rectangulo
                if self.horizontal != self.vertical:
                    return 'rectangle' # Retorna un string con el nombre de tipo de figura resultante
                # De lo contrario, la figura se clasifica como un cuarado
                else:
                    return 'square' # Retorna un string con el nombre de tipo de figura resultante
            # Si la cantidad de vértices es mayor a 4, se clasifica como un circulo
            elif len(self.shape_approx) > 4:
                return 'circle' # Retorna un string con el nombre de tipo de figura resultante