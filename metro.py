class Metro:
    def __init__(self, station_array):
        self.station_array = station_array

    def calc_route(self, start_station_name, finish_station_name):
        # clear all stations' previous parents
        for station in self.station_array:
            station.parent = ""

        # input validation
        start_station = self.find_station_by_name(start_station_name)
        end_station = self.find_station_by_name(finish_station_name)
        if start_station == "STATION NOT FOUND":
            return f"Starting station: {start_station_name} not found."
        elif finish_station_name == "STATION NOT FOUND":
            return f"Destination station: {finish_station_name} not found."

        # breadth first search
        queue = [start_station]
        explored = set()

        while queue:
            current_node = queue.pop(0)
            if current_node in explored:
                continue

            # if we find the destination station, generate route tracing backwards using station.parent
            if current_node.name.lower().strip() == finish_station_name.lower().strip():
                return self.generate_route_string_to(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in explored:
                    queue.append(neighbor)
                    neighbor.parent = current_node

            explored.add(current_node)

    def generate_route_string_to(self, current_node):
        r_string = ""

        while current_node.parent:
            if hasattr(current_node.parent.parent, "lines"):
                if (len(current_node.parent.lines) > 1) and not (bool(set(current_node.lines) & set(current_node.parent.parent.lines))):
                    r_string = f" (transfer to line <{self.find_common_line(current_node.lines, current_node.parent.lines)}>) => {current_node.name}{r_string}"
                else:
                    r_string = f" => {current_node.name}{r_string}"
            else:
                r_string = f" => {current_node.name}{r_string}"

            current_node = current_node.parent

        r_string = f"{current_node.name}{r_string}"
        return r_string

    def find_station_by_name(self, name):
        for station in self.station_array:
            if station.name.lower().strip() == name.lower().strip():
                return station
        print("STATION NOT FOUND")
        return "STATION NOT FOUND"

    @staticmethod
    def find_common_line(line_list_1, line_list_2):
        for line in line_list_1:
            if line in line_list_2:
                return line
