import geometria


lado = 5
print(f"Área quadrado (lado {lado}): {geometria.area_quadrado(lado)}")

raio = 3
area_c = geometria.area_circulo(raio)
print(f"Área círculo (raio {raio}): {area_c:.2f}")

base = 4
altura = 6
peri = geometria.perimetro_retangulo(base, altura)
print(f"Perímetro retângulo (b={base}, h={altura}): {peri}")
