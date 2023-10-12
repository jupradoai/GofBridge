# IMPLEMENTAÇÃO DE INTERFACE DE COR
class Color:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

# IMPLEMENTAÇÃO DE CONCRETAS DE CORES
class RedColor(Color):
    def __init__(self):
        super().__init__("Red")

class BlueColor(Color):
    def __init__(self):
        super().__init__("Blue")

class GreenColor(Color):
    def __init__(self):
        super().__init__("Green")

# IMPLEMENTAÇÃO DE INTERFACE DE FORMA
class Shape:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def draw(self):
        raise NotImplementedError("Este método precisa ser implementado pela subclasse")

# ABSTRAÇÕES REFINADAS
class CircleShape(Shape):
    def draw(self):
        print(f"Desenhando um círculo {self.color.get_color()}.")

class SquareShape(Shape):
    def draw(self):
        print(f"Desenhando um quadrado {self.color.get_color()}.")


class ShapeFactory:
    def createShape(self, color):
        raise NotImplementedError("Este método precisa ser implementado pela subclasse")
    
class CircleShapeFactory(ShapeFactory):
    def createShape(self, color):
        return CircleShape(color)
    
class SquareShapeFactory(ShapeFactory):
    def createShape(self, color):
        return SquareShape(color)
    



# CLIENTE - UTILIZAÇÃO DO MÉTODO
red = RedColor()
blue = BlueColor()
green = GreenColor()

circleShapeFactory = CircleShapeFactory()
squareShapeFactory = SquareShapeFactory()

circle1 = circleShapeFactory.createShape(red)
circle2 = circleShapeFactory.createShape(green)
square1 = squareShapeFactory.createShape(blue)
square2 = squareShapeFactory.createShape(red)

circle1.draw()
circle2.draw()
square1.draw()
square2.draw()
