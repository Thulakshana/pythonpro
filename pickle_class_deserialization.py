import pickle
with open("class_pickele_file.pickle","rb") as f:
    person_data=pickle.load(f)

person_data.display()