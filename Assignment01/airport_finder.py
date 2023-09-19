import math

class AirportFinder:

    def __init__(self, input_file):
        with open(input_file, "r", encoding="utf8") as f:
            self.airports_input : list[str] = f.readlines()


    def optimal_airport_hub(self, airports : list[tuple[float, float]]):
        

    def calculate_distance(self, a: tuple[float, float], b: tuple[float, float]) -> float:
        return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    
    
    def convert_string_to_tuple(self, input_string: str) -> tuple[float, float]:
        return tuple(map(float, input_string.split(' ')))

    def find_airport_hubs(self) -> list[(float, float)]:
        
        line_number : int = 0
        airport_hub_list : list[tuple[float, float]] = []

        while line_number < len(self.airports_input):

            try:
                number_of_airports = int(self.airports_input[line_number])
                

            except IndexError:
                break

            airports = self.airports_input[line_number+1:line_number+number_of_airports+1]
            converted_airports = [self.convert_string_to_tuple(i) for i in airports]
            
            line_number += number_of_airports+1
            

            
                

        
