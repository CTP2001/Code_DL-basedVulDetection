## coding: utf-8

import pickle
import os

def dedouble(Hashpath,Deletepath):
    for filename in os.listdir(Hashpath):
        hashpath = os.path.join(Hashpath,filename)
        f = open(hashpath,'rb')
        hashlist = pickle.load(f)
        f.close()
        datalist = []
        delete_list  = []
        hash_index = -1
        for data in hashlist:
            hash_index += 1
            if data not in datalist:
                datalist.append(data)
            else:
                delete_list.append(hash_index)  #index of slices to delete
        with open(os.path.join(Deletepath,filename),'wb') as f:
            pickle.dump(delete_list,f)
        f.close()

if __name__ == '__main__':
    hashpath = '/home/ubuntu/SySeVR/Implementation/data_preprocess/data/hash_slices/'
    deletepath = '/home/ubuntu/SySeVR/Implementation/data_preprocess/data/delete_list/'

    dedouble(hashpath,deletepath)