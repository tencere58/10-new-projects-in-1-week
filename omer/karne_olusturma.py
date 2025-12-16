import pandas as pd
import numpy as np

data = {
    "Isım": ["Hakan", "Yavuz", "Recep", "Şaban", "Ramazan"],
    "Matematik": [95,55,0,70,10],
    "Fizik": [40,25,30,40,20],
    "Kimya": [80,75,85,70,85],
    "Biyoloji": [100,100,70,85,40]
}

df = pd.DataFrame(data)

df["Ortalama"] = df[["Matematik", "Fizik", "Kimya", "Biyoloji"]].mean(axis=1)

df["Karne"] = np.where(df["Ortalama"] > 50, "Geçti","Kaldı")

print(df)