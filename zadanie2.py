class MyClass:
  def __init__(self):
    self.metr = int(input("Podaj ilość metrów: "))
    self.mile = self.metr * 0.00062137
klasa = MyClass()
print("Metry: ",klasa.metr)
print("Mile: ",klasa.mile)
