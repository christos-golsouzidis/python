class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        out = ''
        for _ in range(self.height):
            for _ in range(self.width):
                out += '*'
            out += '\n'
        return out
    
    def get_amount_inside(self, object):
        max_w = self.width
        max_h = self.height
        in_w = object.width
        in_h = object.height

        n = 0
        while max_w >= n * in_w: 
            n += 1
        n -= 1
        m = 0
        while max_h >= m * in_h: 
            m += 1
        m -= 1
        return n * m
    

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    # overriding

    def __str__(self):
        return f'Square(side={self.width})' # also works for self.height

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side