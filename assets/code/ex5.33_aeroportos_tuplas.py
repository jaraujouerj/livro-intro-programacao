# Aeroportos usando apenas tuplas (sem dicionário)

lat_galeao = (22, 48, 34)
long_galeao = (43, 15, 0)
aeroporto_galeao = ('Rio', 'Galeão', lat_galeao, long_galeao)

lat_guarulhos = (23, 26, 6)
long_guarulhos = (46, 28, 22)
aeroporto_guarulhos = ('São Paulo', 'Guarulhos', lat_guarulhos, long_guarulhos)

aeroportos = (aeroporto_galeao, aeroporto_guarulhos)

for aeroporto in aeroportos:
    cidade, nome, lat, lon = aeroporto
    print(f'Aeroporto {cidade}:')
    print(f'\t{nome}')
    print(f'\tLatitude: {lat[0]}º{lat[1]}\'{lat[2]}"')
    print(f'\tLongitude: {lon[0]}º{lon[1]}\'{lon[2]}"')
