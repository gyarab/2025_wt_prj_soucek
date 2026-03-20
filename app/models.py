from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    objednavka = models.ForeignKey(Objednavka, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Recenze(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Recenze by {self.user.name}: {self.text[:20]}"
    
class Produkt(models.Model):
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    recenze = models.ForeignKey(Recenze, on_delete=models.SET_NULL, null=True)

class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev
    
class Objednavka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    datum_objednavky = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Objednavka by {self.user.name} for {self.produkt.cena}"
    
class Mnozstvi(models.Model):
    objednavka = models.ForeignKey(Objednavka, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    mnozstvi = models.PositiveIntegerField()

    def __str__(self):
        return f"Mnozstvi for {self.objednavka} is {self.mnozstvi}"