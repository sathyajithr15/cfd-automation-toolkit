# CFD Batch Automation Tool

A modular CLI-based automation framework for running CFD simulations in batch mode using JSON configuration.

## Features

- Config-driven batch execution
- Object-oriented architecture
- Per-case result generation
- Structured logging
- Batch summary reporting
- CLI-based execution with argument parsing

## Project Structure

cfd_batch_tool/
│
├── main.py
├── config/
│   └── batch_config.json
├── core/
│   ├── simulation_runner.py
│   └── report_generator.py
├── logs/
└── results/

## How to Run

```bash
py main.py --config config/batch_config.json
