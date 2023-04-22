# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator

#'''
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
#'''

# test it

rect.set_height(10)
rect.set_width(15)
a = rect.get_amount_inside(sq)

e = 6














