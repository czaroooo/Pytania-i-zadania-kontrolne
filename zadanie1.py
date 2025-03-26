class MyClass:
  def __init__(self):
    self.a = int(input("Podaj długość a: "))
    self.b = int(input("Podaj długość b: "))
    self.c = int(input("Podaj długość c: "))
    self.V = (self.a * self.b) * self.c
    self.Pc = ((2 * self.a) * self.b) + ((2 * self.a) * self.c) + ((2 * self.b) * self.c)
    self.Dk = (4 * self.a) + (4 * self.b) + (4 * self.c)
klasa = MyClass()
print("A:", klasa.a)
print("B:", klasa.b)
print("C:", klasa.c)
print("Objętość:", klasa.V)
print("Pole powierzchni całkowitej:", klasa.Pc)
print("Długość wszystkich krawędzi:", klasa.Dk)
