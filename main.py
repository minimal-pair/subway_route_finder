# RED_LINE_STR = "Red Line"
# BLUE_LINE_STR = "Blue Line"
#
# station_line_map = {
#     "Chiang Kai-shek Memorial Hall": RED_LINE_STR,
#     "NTU Hospital": RED_LINE_STR,
#     "Taipei Main Station": f"{RED_LINE_STR}/{BLUE_LINE_STR}",
#     "Zhongshan": RED_LINE_STR,
#     "Shuanglian": RED_LINE_STR,
#     "Longshan Temple": BLUE_LINE_STR,
#     "Ximen": BLUE_LINE_STR,
#     "Shandao Temple": BLUE_LINE_STR,
#     "Zhongxiao Xinsheng": BLUE_LINE_STR,
#     "Zhongxiao": BLUE_LINE_STR,
#     "Fuxing": BLUE_LINE_STR
# }
#
#
# def route_finder(start, destination):
#     if start not in station_line_map:
#         return f"ERROR: {start} is not a recognized station."
#     elif destination not in station_line_map:
#         return f"ERROR: {destination} is not a recognized station."
#     else:
#         start_line = station_line_map[start]
#         dest_line = station_line_map[destination]
#         if start_line == dest_line:
#             return start_line
#         else:
#             return f"{start_line} => {dest_line} via Taipei Main Station"
#
#
# print(route_finder("Chiang Kai-shek Memorial Hall", "NTU Hospital"))
# print(route_finder("Chiang Kai-shek Memorial Hall", "Zhongxiao"))
# print(route_finder("Taipei Main Station", "Zhongxiao"))
# print(route_finder("Taipei Main Station", "Zhongiao"))

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
ninos_heroes.neighbors = [cuauhtemoc, hospital_general]
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
