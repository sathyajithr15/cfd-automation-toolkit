from core.simulation_runner import SimulationRunner
from utils.logger import setup_logger
import json

def main():
    logger = setup_logger()

    with open("config/config.json") as f:
        config = json.load(f)

    sim = SimulationRunner(config)
    sim.run()
    sim.extract_results()

    logger.info("Simulation completed successfully.")

if __name__ == "__main__":
    main()
