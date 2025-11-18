#No AI was used to generate this code. Authored by Hadil Ghazal on 11/17/25
import pandas as pd
from pathlib import Path

def load_sustainability_data(csv_path: str = "data/sustainability_sections.csv") -> pd.DataFrame:
    #loading the sustainabiliry sections from csv into the pandas dataframe
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find CSV at {path.resolve()}")

    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_sustainability_data()
    print("Loaded sustainability dataset with shape:", df.shape)
    print(df.head())
