from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250)
   
    def __str__(self):
        return self.name
    
# classe pour les produits
class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateField()
    image = models.ImageField(null=True,blank=True,upload_to='media/')

    class Meta:
        ordering = ['add_date']

    def statut_quantity(self):
        if self.quantity == 0:
            return 'red'
        elif self.quantity <= 10:
            return 'orange'
        else:
            return 'green'
        
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Vente(models.Model):
    produit = models.ForeignKey(Products, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits= 10, decimal_places=2)

    def __str__(self):
        return self.produit

class Facture_client(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    produit = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_achat = models.DateTimeField(auto_now_add=False)
    total_amount = models.ForeignKey(Vente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Le reçu de {self.customer.customer}"
