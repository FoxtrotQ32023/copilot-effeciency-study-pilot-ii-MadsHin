import math
import os

class AirportFinder:

    def __init__(self, input_file):
        with open(input_file, "r", encoding="utf8") as f:
            self.airports_input : list[tuple] = [self.convert_string_to_tuple(i) for i in f.readlines()]


    def optimal_airport_hub(self, airports : list[tuple[float, float]]) -> tuple[float, float]:
        """
        finds the best airport for a set of inputs
        """
        candidates = list()

        for airport_candidate in airports:

            max_distance = 0
            best_airport = tuple()

            for airport in airports:
                distance = self.calculate_distance(airport, airport_candidate)
                if max_distance <= distance:
                    max_distance = distance
                    best_airport = (airport_candidate, max_distance)

            candidates.append(best_airport)

        return sorted(candidates, key=lambda x: float(x[1]))[0][0]
                 
    def calculate_distance(self, point_a: tuple[float, float], point_b: tuple[float, float]) -> float:
        """finds the euclidean norm"""
        return math.sqrt((point_b[0]-point_a[0])**2+(point_b[1]-point_a[1])**2)

    def convert_string_to_tuple(self, input_string: str) -> tuple[float, float]:
        """simple conversion from string to tuple"""
        return tuple(map(float, input_string.split(' ')))

    def find_airport_hubs(self) -> list[(float, float)]:
        """
        Responsible for finding each set of problems in the file
        and returning the list, and make an solution.ans file
        """     
        line_number : int = 0
        airport_hub_list : list[tuple[float, float]] = list()

        while line_number < len(self.airports_input):

            try:
                number_of_airports = int(self.airports_input[line_number][0])

            except IndexError:
                break

            airports = self.airports_input[line_number+1:line_number+number_of_airports+1]
            line_number += number_of_airports+1
            airport_hub_list.append(self.optimal_airport_hub(airports))

        self.output_to_file(airport_hub_list)
        return airport_hub_list

    def output_to_file(self, result_list : list[tuple[float, float]]) -> None:
        with open("outputfile.ans", "w", encoding="utf8") as file:
            for line in result_list:
                file.write(str(line[0]) + " " + str(line[1]) + "\n")
    

