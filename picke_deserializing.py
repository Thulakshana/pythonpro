import pickle
with open("dict.pickle","rb") as f:
    dict_data=pickle.load(f)
print(dict_data)