# Import necessary libraries
#import pandas as pd
import subprocess
#import json
import os #,sys
#from pathlib import Path
from dask.distributed import LocalCluster, Client, progress #, performance_report # dask for parallel processing

def batch_building_simulation(building_dir):
	"""_summary_
     
	Args:
		building_dir (_type_): _description_
	"""
	# Define the command to run the EnergyPlus simulation
	CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
	IDF_FILE = os.path.join(building_dir,"run","in.idf")
	WEATHER_FILE = os.path.join(building_dir,"files",
							 "2020s_CAN_QC_Montreal-Trudeau.Intl.AP.716270_CWEC2016_modified.epw")
	RESULTS_DIR = os.path.join(CURRENT_PATH,"results",os.path.basename(building_dir))
	
	subprocess.run(["energyplus",IDF_FILE,
				    "-w",WEATHER_FILE,
					"--output-directory",RESULTS_DIR])

	return

def postprocess_results(building_dir):
	"""_summary_
	NOT YET IMPLEMENTED

	Args:
		building_dir (_type_): _description_
	"""
	return

def main():
	# Define paths
	CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
	MODELS_DIR = os.path.join(CURRENT_PATH, "test-models")
	
	# List all folders in the models directory
	building_folders = [f.path for f in os.scandir(MODELS_DIR) if f.is_dir()]

	# Create the folder "results" if it doesn't exist
	RESULTS_PATH = os.path.join(CURRENT_PATH, "results")
	if not os.path.exists(RESULTS_PATH):
		os.makedirs(RESULTS_PATH)
	
	# Create subfolders in "results" for each building model
	for building in building_folders:
		building_name = os.path.basename(building)
		building_results_path = os.path.join(RESULTS_PATH, building_name)
		if not os.path.exists(building_results_path):
			os.makedirs(building_results_path)

	# Set up Dask local cluster
	cluster = LocalCluster(n_workers=5)
	client = Client(cluster)
	print("Dask cluster created with the following details:")
	print(client)

	# Print the number of simulations to run
	print(f"Running simulations for {len(building_folders)} buildings with 5 workers...")
	# Submit batch simulations to Dask
	futures = client.map(batch_building_simulation, building_folders)
	# Monitor progress
	progress(futures)
	# Execute the futures and gather results
	client.gather(futures)

	# Parallel result post-processing
	# Submit post-processing tasks to Dask 
	postprocess_futures = client.map(postprocess_results, building_folders)
	# Monitor progress
	progress(postprocess_futures)
	# Execute the futures and gather results
	client.gather(postprocess_futures)

	# Close the Dask client and cluster
	client.close()	
	cluster.close()

if __name__ == "__main__":
    main()
