from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime
import json
from .models import UsdQuotation
from .forms import UsdQuotationForm

from .serializers import UsdQuotationSerializer
from rest_framework import viewsets

class UsdQuotationViewSet(viewsets.ModelViewSet):
  queryset = UsdQuotation.objects.all()
  serializer_class = UsdQuotationSerializer


def index(request):
    return render(request, "quotations/chart_plot.html", context = {})

def quotation_by_dates(request):
    if(request.method == "POST"):
        if request.POST['initialDate'] and request.POST['finalDate'] and request.POST['currency']:
            initial_date = datetime.datetime.strptime(request.POST['initialDate'], '%Y-%m-%d')
            final_date = datetime.datetime.strptime(request.POST['finalDate'], '%Y-%m-%d')
            currency = request.POST['currency']
            days_dif = (final_date-initial_date).days
            quotations = []

            if days_dif <= 5 and days_dif > 1:
                for date_n in (initial_date + datetime.timedelta(days=n) for n in range(days_dif+1)):
                    quotation = UsdQuotation.objects.filter(date=date_n)
                    if quotation:
                        quotation = quotation[0]
                        quotations.append(quotation.get_rate(currency))
                    else:
                        rq = requests.get("https://api.vatcomply.com/rates?base=USD&date="+date_n.strftime('%Y-%m-%d'))
                        result = json.loads(rq.text)["rates"]
                        quotation = UsdQuotationForm({  "date": date_n, 
                                                        "euro_rate": result["EUR"], 
                                                        "real_rate": result["BRL"], 
                                                        "yen_rate": result["JPY"]   })
                        quotation.save()
                        quotations.append(result[currency])

                return HttpResponse(json.dumps(quotations))
            else:
                return HttpResponse(status=500)
        else:
            return HttpResponse(status=500)