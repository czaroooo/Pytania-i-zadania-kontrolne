class MyClass:
  przelicznik = 1.35962

  @staticmethod
  def kw_na_km(kw):
    return kw * MyClass.przelicznik

kw = float(input("Podaj moc w kW: "))
print("Kilowaty:",kw)
print("Konie mechaniczne",MyClass.kw_na_km(kw))
