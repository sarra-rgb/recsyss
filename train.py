import pickle as pkl
import numpy as np
import pandas as pd
from scipy.spatial import KDTree
from time import time

class DummyModel():

    def __init__(self, K = 1, dataframe = None):
        self.kdtree = None
        self.k = K
        self.dataframe = dataframe

    def fit(self, X, leaf_size = 3):
        self.kdtree = KDTree(X, leafsize=leaf_size)
        return self


    def predict(self, x):
        _, neighbors = self.kdtree.query(x, self.k)
        return neighbors


    def map_to_locations(self, neighbors_ids , colname = "location_id"):
        answers = 0 * neighbors_ids
        for id, nid in enumerate(neighbors_ids):
            answers[id] = self.dataframe[colname].values[nid]
        return answers



if __name__ == '__main__':
    K = 10
    test_sample = [{ "lat": 51.50820541381837,"lon": -0.10843700170516969 , "Season": 2 },
                   { "lat": 51.50820541381837,"lon": -0.10843700170516969 , "Season": 3 }]
    #model = DummyModel()
    #pkl.dump(model, open("model.pkl", "wb"))
    input_data = "prefiltereddd.csv"
    columns = ["location_id" , "lat","lon","Season"]
    data_raw = pd.read_csv(input_data)
    data = data_raw[columns].copy()

    data = data.drop_duplicates().reset_index(drop = True)
    print(len(data.groupby(by = ["lat","lon", "Season"])))
    #print(data)
    print(np.std(data.values[:, [1,2]], axis=0))

    X = data.values[:, 1::]


    model = DummyModel(K, data)
    model.fit(X)
    x = pd.DataFrame(test_sample, columns=["lat", "lon", "Season"]).values
    ans = model.map_to_locations(model.predict(x=x))


    pkl.dump(model, open("model.pkl", "wb"))





