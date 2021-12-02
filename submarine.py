import sys

from typing import List
from abc import ABC, abstractmethod


"""
Let's build a submarine!
"""


class BaseDevice(ABC):
    @abstractmethod
    def __init__(self, data_source: str):
        self.data_source = data_source

    @abstractmethod
    def operate(self):
        pass


class Sonar(BaseDevice):
    """
    Day 1 feature
    """

    def __init__(self, data_source: str):
        self.data_source = data_source

    def operate(self):
        print(
            "Basic surrounding analysis: {}".format(self.basic_surroundings_analysis())
        )
        print(
            "Advanced surrounding analysis: {}".format(
                self.advanced_surroundings_analysis()
            )
        )

    def basic_surroundings_analysis(self) -> int:
        basic_depth_analysis = 0
        depths = self._sweep_depths()
        for index in range(len(depths)):
            if index > 0:
                # We want to ignore the first depth
                if depths[index] > depths[index - 1]:
                    basic_depth_analysis += 1
        return basic_depth_analysis

    def advanced_surroundings_analysis(self) -> int:
        advanced_depth_analysis = 0
        depths = self._sweep_depths()
        for index in range(len(depths)):
            if index > 0 and index < len(depths) - 2:
                actual_measurement = depths[index : index + 3]
                previous_measurement = depths[index - 1 : index + 2]
                if sum(actual_measurement) > sum(previous_measurement):
                    advanced_depth_analysis += 1
        return advanced_depth_analysis

    def _sweep_depths(self) -> List:
        with open(self.data_source, "r") as observed_data:
            depths = [int(depth.rstrip()) for depth in observed_data]
            return depths


class Engine(BaseDevice):
    """
    Day 2 feature
    """

    def __init__(self, data_source: str):
        self.data_source = data_source

    def operate(self):
        print("Planned simple course is: {}".format(self._get_simple_planned_course()))
        print(
            "Planned advanced course is: {}".format(self._get_advanced_planned_course())
        )

    def _get_simple_planned_course(self):
        basic_orders = {"up": 0, "down": 0, "forward": 0}
        with open(self.data_source, "r") as orders:
            for order in orders:
                direction, units = order.split()
                basic_orders[direction] = basic_orders[direction] + int(units)
        return (basic_orders["down"] - basic_orders["up"]) * basic_orders["forward"]

    def _get_advanced_planned_course(self):
        advanced_orders = {"forward": 0, "aim": 0, "depth": 0}
        with open(self.data_source, "r") as orders:
            for order in orders:
                direction, units = order.split()
                if direction == "forward":
                    advanced_orders[direction] = advanced_orders[direction] + int(units)
                    advanced_orders["depth"] = (
                        advanced_orders["depth"] + int(units) * advanced_orders["aim"]
                    )
                elif direction == "down":
                    advanced_orders["aim"] = advanced_orders["aim"] + int(units)
                else:
                    advanced_orders["aim"] = advanced_orders["aim"] - int(units)

        return advanced_orders["depth"] * advanced_orders["forward"]


def operate_submarine():
    allowed_operations = {
        "sonar": {"device": Sonar, "data_source": "measurements.txt"},
        "engine": {"device": Engine, "data_source": "movement_orders.txt"},
    }

    if len(sys.argv) > 2:
        print("Only one operation allowed at once.")
        sys.exit(1)

    operation_to_perform = sys.argv[1]

    if operation_to_perform not in allowed_operations:
        print(
            "Not allowed operation: {}. Allowed operations are: {}".format(
                operation_to_perform, " - ".join(allowed_operations)
            )
        )
        sys.exit(1)

    device = allowed_operations[operation_to_perform]["device"](
        allowed_operations[operation_to_perform]["data_source"]
    )
    device.operate()


if __name__ == "__main__":
    operate_submarine()
