# stats.py
# Funciones de estadística descriptiva
# Autor: Tu Nombre
import math

def media(data):
    return sum(data) / len(data)
def mediana(data):
    x = sorted(data)
    n = len(x)
    mid = n // 2
    if n % 2 == 0:
        return (x[mid - 1] + x[mid]) / 2
    else:
        return x[mid]
def moda(data):
    counts = {}
    for v in data:
        counts[v] = counts.get(v, 0) + 1
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]
def varianza(data):
    mu = media(data)
    return sum((x - mu) ** 2 for x in data) / (len(data) - 1)
def desviacion_estandar(data):
    return math.sqrt(varianza(data))
def percentil(data, p):
    x = sorted(data)
    n = len(x)
    k = (n - 1) * p / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return x[int(k)]
    return x[f] + (k - f) * (x[c] - x[f])
def cuartiles(data):
    return (
        percentil(data, 25),
        percentil(data, 50),
        percentil(data, 75)
    )
def rango_intercuartilico(data):
    q1, _, q3 = cuartiles(data)
    return q3 - q1
def desviacion_absoluta_mediana(data):
    med = mediana(data)
    deviations = [abs(x - med) for x in data]
    return mediana(deviations)
def covarianza(x, y):
    mx = media(x)
    my = media(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (len(x) - 1)
def correlacion(x, y):
    return covarianza(x, y) / (desviacion_estandar(x) * desviacion_estandar(y))

