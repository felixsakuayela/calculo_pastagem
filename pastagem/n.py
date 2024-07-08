import math

# Constants
d = 2  # Distância do ponto ao transmissor em km
D = 5  # Distância total entre as antenas em km
f = 2.5  # Frequência em GHz

# Converter para as unidades corretas
d = d * 10**3  # Converter km para metros
D = D * 10**3  # Converter km para metros
f = f * 10**9  # Converter GHz para Hz

# Velocidade da luz em m/s
c = 3 * 10**8

# Calcular o comprimento de onda
lambda_ = c / f

# Calcular o raio de Fresnel
r0 = math.sqrt((d * (D - d) * lambda_) / D)

# Imprimir o resultado
print(f"O raio de Fresnel a uma distância de 2 km é de {r0:.2f} metros.")
