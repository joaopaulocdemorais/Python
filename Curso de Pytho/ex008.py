n = float(input('Informe uma distância em metros: '))
km = n/1000
Ml = n/1609
Mn = n/1852
Pol = n * 39.37
Mili = n * 1000
Cen = n * 100

print('A medida de {}m corresponde a\n{:.5f}km\n{:.8f}mi\n{:.5f}nm\n{:.5f}pol\n{:.5f}mm\n{:.5f}cm'.format(n, km, Ml, Mn, Pol, Mili, Cen))
