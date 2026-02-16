class SimulationRunner:
    def __init__(self, config):
        self.config = config

    def run(self):
        print("Running simulation with config:", self.config)

    def extract_results(self):
        print("Extracting results...")
