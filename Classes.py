

from turtle import color


class Cookie:
    def __init__(self , color) -> None:
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self , color):
        self.color = color





cookie_one = Cookie('Green')
cookie_two = Cookie('Red')

print(cookie_one.get_color())
print(cookie_two.get_color())

cookie_one.set_color('Wheatish Brown')
print(cookie_one.get_color())
print(cookie_two.get_color())


