import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals["weight"] > 100].sort_values(ascending=False, by="weight")
    result = animals["name"]
    df = pd.DataFrame(result)
    return df