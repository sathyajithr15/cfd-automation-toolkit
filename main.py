import os
import json
import argparse
import logging
from core.simulation_runner import SimulationRunner
from datetime import datetime

def load_config(path):
    with open(path, "r") as f:
        return json.load(f)


def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/tool.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"
    )


def parse_arguments():
    parser = argparse.ArgumentParser(description="CFD Batch Automation Tool")
    parser.add_argument(
        "--config",
        required=True,
        help="Path to batch configuration JSON file"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    setup_logging()

    logging.info("Starting CFD Batch Tool")

    config_data = load_config(args.config)

    executed_cases = []

    for sim_config in config_data["simulations"]:
        sim = SimulationRunner(sim_config)
        sim.run()
        executed_cases.append(sim_config.get("case_name", "unknown"))

    # Create batch summary
    os.makedirs("results", exist_ok=True)
    summary_path = os.path.join("results", "batch_summary.txt")

    with open(summary_path, "w") as f:
        f.write("CFD Batch Execution Summary\n")
        f.write("=" * 40 + "\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Total simulations run: {len(executed_cases)}\n")
        f.write("Cases executed:\n")
        for case in executed_cases:
            f.write(f"- {case}\n")

    logging.info("Batch execution completed.")


if __name__ == "__main__":
    main()
