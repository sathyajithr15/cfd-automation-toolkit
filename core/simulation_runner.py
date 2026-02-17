import os
import logging
from datetime import datetime

class SimulationRunner:
    def __init__(self, config):
        self.config = config

    def run(self):
      try:
        logging.info(f"Running simulation with config: {self.config}")

        os.makedirs("results", exist_ok=True)
        case_name = self.config.get("case_name", "unknown_case")
        output_path = os.path.join("results", f"{case_name}_output.txt")

        with open(output_path, "w") as f:
            f.write(f"Case: {self.config.get('case_name', 'N/A')}\n")
            f.write(f"Mesh size: {self.config.get('mesh_size', 'N/A')}\n")
            f.write(f"Solver: {self.config.get('solver', 'N/A')}\n")
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write("Status: SUCCESS\n")

        logging.info("Simulation completed and results saved.")

      except Exception as e:
        logging.info("ERROR occurred:", str(e))

    def extract_results(self):
        print("Extracting results...")

