import math

class AirportFinder:

    def __init__(self, input_file):
        with open(input_file, "r", encoding="utf8") as f:
            self.airports : list[str] = f.readlines()

    def calculate_distance(self, a: tuple[float, float], b: tuple[float, float]) -> float:
        return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    
    
    def find_airport_hubs(self) -> list[(float, float)]:
        


        for line in self.airports:

            if 
            


        
