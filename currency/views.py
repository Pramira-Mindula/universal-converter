from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

TOP_10 = [
    "USD", "EUR", "GBP", "JPY", "AUD",
    "CAD", "CHF", "CNY", "INR", "LKR"
]

def home(request):
    currencies = []

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        data = response.json()
        currencies = [c for c in TOP_10 if c in data["rates"]]
    except:
        currencies = TOP_10

    return render(request, "currency/home.html", {
        "currencies": currencies,   
        "currencies_json": json.dumps(currencies)
    })


def convert(request):
    try:
        amount = float(request.GET.get("amount"))
        convert_type = request.GET.get("type")
        from_unit = request.GET.get("from_unit")
        to_unit = request.GET.get("to_unit")

        if convert_type == "currency":
            url = f"https://open.er-api.com/v6/latest/{from_unit}"
            response = requests.get(url)
            data = response.json()
            rate = data["rates"][to_unit]
            result = round(amount * rate, 2)

        elif convert_type == "length":
            if from_unit == "meter" and to_unit == "km":
                result = amount / 1000
            elif from_unit == "km" and to_unit == "meter":
                result = amount * 1000
            else:
                result = amount

        elif convert_type == "temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (amount * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (amount - 32) * 5/9
            else:
                result = amount

        return JsonResponse({"result": result})

    except:
        return JsonResponse({"error": "Conversion failed"})