import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    return list(players.shape)
    
    # shape = players.shape
    # row = shape[0]
    # col = shape[1]
    # ans = [row,col]
    # return ans