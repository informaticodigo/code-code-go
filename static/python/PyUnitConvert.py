def convertir_kelvin_celsius(kelvin):
    result = kelvin + 273.15
    return result


def convertir_celsius_kelvin(celsius):
    result = celsius - 273.15
    return result


def convertir_fahrenheit_celsius(fahrenheit):
    result = (fahrenheit - 32)/1.8
    return result


def convertir_celsius_fahrenheit(celsius):
    result = (celsius * 1.8) + 32
    return result


def convertir_galones_litros(galones):
    result = galones/0.26417
    return result


def convertir_litros_galones(litros):
    result = litros*0.26417
    return result


def convertir_onzas_litros(onzas):
    result = onzas/33.814
    return result


def convertir_litros_onzas(litros):
    result = litros*33.814
    return result


def convertir_onzas_galones(onzas):
    result = onzas/33.814*0.26417
    return result


def convertir_galones_onzas(galones):
    result = galones/0.26417*33.814
    return result
