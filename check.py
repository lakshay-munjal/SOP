import os
import pandas as pd

project_dir = os.getenv("PROJECT_DIR")
env = os.getenv("CONDA_DEFAULT_ENV")
iris_csv = os.getenv("IRIS_CSV")

flowers = pd.read_csv(iris_csv)

print(flowers)
print("My project directory is {} and my conda environment is {}".format(project_dir, env))