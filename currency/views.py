from django.shortcuts import render
import requests

TOP_10 = [
    "USD", "EUR", "GBP", "JPY", "AUD",
    "CAD", "CHF", "CNY", "INR", "LKR"
]

def home(request):
    result = None
    error = None
    currencies = []

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        data = response.json()

        # Filter only top 10
        all_currencies = data["rates"].keys()
        currencies = [c for c in TOP_10 if c in all_currencies]

    except:
        error = "Could not load currencies."

    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount"))
            convert_type = request.POST.get("type")
            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")

            if convert_type == "currency":
                url = f"https://open.er-api.com/v6/latest/{from_unit}"
                response = requests.get(url)
                data = response.json()

                rate = data["rates"][to_unit]
                result = round(amount * rate, 2)
                
            elif convert_type == "length":
                    if from_unit == "Meter" and to_unit == "KM":
                        result = amount / 1000
                    elif from_unit == "KM" and to_unit == "Meter":
                        result = amount * 1000

            #Temp
            elif convert_type == "temperature":
                if from_unit == "Celsius" and to_unit == "Fahrenheit":
                    result = (amount * 9/5) + 32
                elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                    result = (amount - 32) * 5/9

        except:
            error = "Conversion failed."

    return render(request, "currency/home.html", {
        "result": result,
        "error": error,
        "currencies": currencies
    })