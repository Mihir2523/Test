from fastapi import FastAPI
import numpy as np
import pandas as pd
app = FastAPI()

@app.get("/")
def a():
    b = np.array(range(100))
    c = pd.DataFrame({
            "a":[1,2,3,4,5],
            "b":[6,7,8,9,10]
        })
    e = c['a']
    return {"data" : list(range(100)),"sum":b.sum(),"temp":e.tolist()}