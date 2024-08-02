from shapes import Shape


def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("The object must be an instance of Shape or its subclasses")
    return shape.area()
