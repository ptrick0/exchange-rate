from django.db import models

class UsdQuotation(models.Model):
    date = models.DateField(unique=True)
    euro_rate = models.FloatField()
    real_rate = models.FloatField()
    yen_rate = models.FloatField()

    class Meta():
        verbose_name = "Cotação do dólar"

    def __str__(self):
        return self.date

    def get_rate(self, currency):
        currencies = {  "BRL": self.real_rate, 
                        "EUR": self.euro_rate, 
                        "JPY": self.yen_rate    }

        return currencies[currency]
        