from metro import Metro
from station import Station

# Stations
# 1
observatorio = Station("Observatorio", ["1"])
tacubaya = Station("Tacubaya", ["1", "7", "9"])
juanacatlan = Station("Juanacatlan", ["1"])
chapultepec = Station("Chapultepec", ["1"])
sevilla = Station("Sevilla", ["1"])
insurgentes = Station("Insurgentes", ["1"])
cuauhtemoc = Station("Cuauhtemoc", ["1"])
balderas = Station("Balderas", ["1", "3"])

# 3
juarez = Station("Juarez", ["3"])
ninos_heroes = Station("Ninos Heroes", ["3"])
hospital_general = Station("Hospital General", ["3"])
centro_medico = Station("Centro Medico", ["3", "9"])


# 7
constituyentes = Station("Constituyentes", ["7"])
san_pedro_de_los_pinos = Station("San Pedro de los Pinos", ["7"])

# 9
patriotismo = Station("Patriotismo", ["9"])
chilpancingo = Station("Chilpancingo", ["9"])

# station array
station_array = [observatorio, tacubaya, chapultepec, sevilla, insurgentes, cuauhtemoc, balderas, juarez, ninos_heroes,
                 hospital_general, constituyentes, juanacatlan, patriotismo, chilpancingo, centro_medico,
                 san_pedro_de_los_pinos]

# Neighbors
# 1
observatorio.neighbors = [tacubaya]
tacubaya.neighbors = [observatorio, constituyentes, juanacatlan, patriotismo, san_pedro_de_los_pinos]
juanacatlan.neighbors = [tacubaya, chapultepec]
chapultepec.neighbors = [juanacatlan, sevilla]
sevilla.neighbors = [chapultepec, insurgentes]
insurgentes.neighbors = [sevilla, cuauhtemoc]
cuauhtemoc.neighbors = [insurgentes, balderas]
balderas.neighbors = [cuauhtemoc, juarez, ninos_heroes]

# 3
juarez.neighbors = [cuauhtemoc]
ninos_heroes.neighbors = [hospital_general, balderas]
hospital_general.neighbors = [ninos_heroes, centro_medico]
centro_medico.neighbors = [hospital_general, chilpancingo]

# 7
constituyentes.neighbors = [tacubaya]
san_pedro_de_los_pinos.neighbors = [tacubaya]

# 9
patriotismo.neighbors = [tacubaya, chilpancingo]
chilpancingo.neighbors = [patriotismo, centro_medico]


test_metro = Metro(station_array)

print(test_metro.calc_route("observatorio", "balderas"))
print(test_metro.calc_route("observatorio", "hospital general"))
print(test_metro.calc_route("centro medico", "chapultepec"))
