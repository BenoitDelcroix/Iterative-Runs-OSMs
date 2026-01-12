# Iterative-Runs-OSMs

Iterative-Runs-OSMs is a Python-based script for running batch simulations of EnergyPlus building models (.idf) in a parallel and programmatic way. It leverages Dask for distributed computing, automates simulation runs, and organizes results for post-processing (post-processing not yet implemented).

## Features
- Batch simulation of multiple EnergyPlus models
- Parallel execution using Dask
- Automated results organization
- Error logging for missing files

## Directory Structure

```
├── main.py                # Main script to run batch simulations
├── pyproject.toml         # Project dependencies and metadata
├── README.md              # Project documentation
├── results/               # Output folders for simulation results
│   └── <model_name>/      # Results for each building model
├── test-models/           # Input building models and folders
│   ├── <model_name>.osm   # OpenStudio Model files
│   └── <model_name>/      # Folders for each building model
```

## Requirements
- Python >= 3.11
- EnergyPlus (must be installed and available in PATH) - in the current config, EnergyPlus is included in the devcontainer  
- Dask  
- Note: all requirements are included in the devcontainer (for more details, look at the configuration files provided in the folder ".devcontainer")

## Usage

1. Place your building model folders and .osm files in the `test-models/` directory. The idf files should be placed in the folder "run" in each building model folder (as it is commonly the case when using OpenStudio). 
2. Ensure your EnergyPlus IDF and weather files are correctly referenced in each model folder.
3. Run the main script:

```bash
python main.py
```

Simulation results will be saved in the `results/` directory, organized by model name.

## How It Works
- The script scans `test-models/` for building folders.
- For each folder, it runs EnergyPlus with the specified IDF and weather file.
- Results and error logs are saved in `results/<model_name>/`.
- Dask is used to parallelize simulations and post-processing.

## Notes
- Ensure EnergyPlus is installed and accessible from the command line.
- Weather files should be placed in the expected location within each building folder.
- Post-processing is currently a placeholder for future development.

## License
MIT License

## Author
Benoit Delcroix


