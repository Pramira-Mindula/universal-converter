from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        convert_type = request.POST.get("type")
        from_unit = request.POST.get("from_unit")
        to_unit = request.POST.get("to_unit")

        #Currency
        if convert_type == "currency":
            usd = 310
            eur = 362
            aud = 291
            if from_unit == "USD" and to_unit == "LKR":
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
            if from_unit == "meter" and to_unit == "km":
                result = amount / 1000
            elif from_unit == "km" and to_unit == "meter":
                result = amount * 1000

        #Tempe
        elif convert_type == "temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (amount * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (amount - 32) * 5/9

    return render(request, "currency/home.html", {"result": result})