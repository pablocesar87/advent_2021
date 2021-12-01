class Sonar:
    def __init__(self):
        self.increasing_depth_times = 0

    def analyze_surroundings(self, measurements: str) -> int:
        with open(measurements, "r") as observed_data:
            depths = [int(depth.rstrip()) for depth in observed_data]
            for index in range(len(depths)):
                if index > 0:
                    # We want to ignore the first depth
                    if depths[index] > depths[index - 1]:
                        self.increasing_depth_times += 1
            return self.increasing_depth_times


if __name__ == "__main__":
    sonar = Sonar()
    increasing_depth_times = sonar.analyze_surroundings(measurements="measurements.txt")
    print(increasing_depth_times)
