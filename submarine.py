from typing import List


"""
Let's build a sybmarine!
"""


class Sonar:
    """
    Day one feature
    """
    def __init__(self, measurements: str):
        self.basic_depth_analysis = 0
        self.advanced_depth_analysis = 0
        self.measurements = measurements

    def basic_surroundings_analysis(self) -> int:
        depths = self._sweep_depths()
        for index in range(len(depths)):
            if index > 0:
                # We want to ignore the first depth
                if depths[index] > depths[index - 1]:
                    self.basic_depth_analysis += 1
        return self.basic_depth_analysis

    def advanced_surroundings_analysis(self) -> int:
        depths = self._sweep_depths()
        for index in range(len(depths)):
            if index > 0 and index < len(depths) - 2:
                actual_measurement = depths[index : index + 3]
                previous_measurement = depths[index - 1 : index + 2]
                if sum(actual_measurement) > sum(previous_measurement):
                    self.advanced_depth_analysis += 1
        return self.advanced_depth_analysis

    def _sweep_depths(self) -> List:
        with open(self.measurements, "r") as observed_data:
            depths = [int(depth.rstrip()) for depth in observed_data]
            return depths


if __name__ == "__main__":
    sonar = Sonar(measurements="measurements.txt")
    basic_depth_analysis = sonar.basic_surroundings_analysis()
    advanced_surroundings_analysis = sonar.advanced_surroundings_analysis()
    print(f"Basic Analysis: {basic_depth_analysis}")
    print(f"Advanced Analysis: {advanced_surroundings_analysis}")
