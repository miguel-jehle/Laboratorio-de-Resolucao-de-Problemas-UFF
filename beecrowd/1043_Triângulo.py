pontos = list(map(float,input().split()))
ordem = sorted(pontos)
if ordem[2] < ordem[1] + ordem[0]:
    print(f"Perimetro = {pontos[0]+pontos[1]+pontos[2]}")
else:
    print(f"Area = {(pontos[0]+pontos[1])*pontos[2]/2}")