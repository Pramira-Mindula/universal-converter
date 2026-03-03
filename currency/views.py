from django.shortcuts import render

def home(request):
    result = None
    error = None

    if request.method == "POST":

        value = request.POST.get("amount")
        if not value:
            error = "Enter a Numeric Value"
        else:
            try:
                amount = float(value)
                convert_type = request.POST.get("type")
                from_unit = request.POST.get("from_unit")
                to_unit = request.POST.get("to_unit")

                #Currency
                if convert_type == "currency":
                    usd = 310
                    eur = 362
                    aud = 291
                    if value == "":
                        result = amount
                    elif from_unit == "USD" and to_unit == "LKR":
                        result = amount * usd
                    elif from_unit == "EUR" and to_unit == "LKR":
                        result = amount * eur
                    elif from_unit == "AUD" and to_unit == "LKR":
                        result = amount * aud
                    elif from_unit == "LKR" and to_unit == "USD":
                        result = amount / usd
                    elif from_unit == "LKR" and to_unit == "EUR":
                        result = amount / eur
                    elif from_unit == "LKR" and to_unit == "AUD":
                        result = amount / aud


                #Length
                elif convert_type == "length":
                    if from_unit == "Meter" and to_unit == "KM":
                        result = amount / 1000
                    elif from_unit == "KM" and to_unit == "Meter":
                        result = amount * 1000

                #Tempe
                elif convert_type == "temperature":
                    if from_unit == "Celsius" and to_unit == "Fahrenheit":
                        result = (amount * 9/5) + 32
                    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                        result = (amount - 32) * 5/9
            except ValueError:
                error = "Invalid Number"

    return render(request, "currency/home.html", {"result": result, "error": error})