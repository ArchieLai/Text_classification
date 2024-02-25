from pathlib import Path
import pandas as pd

def MovieReviews():
  data_path = Path("./data/rt-polaritydata/positive.txt")
  with open(data_path, mode='r', encoding='latin-1') as file:
      ps = file.readlines()
  pos = [1 for _ in range(len(ps))]
  df = pd.DataFrame(list(zip(ps, pos)), columns=["text", "category"])

  data_path2 = Path("./data/rt-polaritydata/negative.txt")
  with open(data_path2, mode='r', encoding='latin-1') as file2:
      ns = file2.readlines()
  neg = [0 for _ in range(len(ns))]
  df = pd.concat([df, pd.DataFrame({"text": ns, "category": neg})], axis=0, ignore_index=True)
  
  return df