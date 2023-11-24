from django.shortcuts import render
from django.http import HttpResponse


def convert_measurement(value, source_unit, target_unit):
    """conversion logics"""
    conversion_factors = {
        'meter': {'meter': 1, 'kilometer': 0.001, 'mile': 0.000621371},
        'kilometer': {'meter': 1000, 'kilometer': 1, 'mile': 0.621371},
        'mile': {'meter': 1609.34, 'kilometer': 1.60934, 'mile': 1},
    }

    if source_unit in conversion_factors and target_unit in conversion_factors[source_unit]:
        conversion_factor = conversion_factors[source_unit][target_unit]
        result = value * conversion_factor
        return result

def index(request):
    if request.method == 'POST':
        value = float(request.POST['value'])
        source_unit = request.POST['source_unit']
        target_unit = request.POST['target_unit']

        result = convert_measurement(value, source_unit, target_unit)

        return render(request, 'conversion/index.html', {
            'result': result, 
            'value': value, 
            'source_unit': source_unit, 
            'target_unit': target_unit,
            "title":"conversion"
            })

    return render(request, 'conversion/index.html', {
        "title": "conversion"
    })








