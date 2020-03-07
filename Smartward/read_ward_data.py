#this file can later be deleted
import pickle
with open('ward.pickle','rb') as f:
    read=pickle.load(f)
    print(read)
