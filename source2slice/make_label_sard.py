## coding:utf-8
import os
import pickle

def make_label(path, _dict):
    print(path)
    f = open(path, 'r')
    slicelists = f.read().split('------------------------------')[:-1]
    f.close()
    
    labels = {}
    if slicelists[0] == '':
        del slicelists[0]
    if slicelists[-1] == '' or slicelists[-1] == '\n' or slicelists[-1] == '\r\n':
        del slicelists[-1]
    
    for slicelist in slicelists:
        sentences = slicelist.split('\n')
            
        if sentences[0] == '\r' or sentences[0] == '':
            del sentences[0]
        if sentences == []:
            continue
        if sentences[-1] == '':
            del sentences[-1]
        if sentences[-1] == '\r':
            del sentences[-1]
            
        slicename = sentences[0].replace('\r', '')
        key = slicename.split(' ')[1]
        sentences = sentences[1:]
        label = 0
        
        if key not in _dict.keys():
	    labels[slicename] = 0
            continue
        else:
            vulline_nums = _dict[key]
            for sentence in sentences:
                if (is_number(sentence.split(' ')[-1])) is False:
		     continue
                linenum = int(sentence.split(' ')[-1])
                if linenum not in vulline_nums:
                    continue
                else:
                    label = 1
                    labels[slicename] = 1
                    break
        if label == 0:
            labels[slicename] = 0
    
    return labels
       
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def load(dec_path, list):
    d = {}
    with open(dec_path, 'rb') as f:
        while True:
            try:
                a = pickle.load(f)
            except EOFError:
                break
            else:
                d.update(a)
    f.close()
    d.update(list)
    with open(dec_path, 'wb') as f:
        pickle.dump(d, f)
    f.close()
            

def main():
    f = open("/home/ubuntu/SySeVR/Data/SARD/contain_all.txt", 'r')
    vullines = f.read().split('\n')
    f.close()

    _dict = {}
    for vulline in vullines:
        key = vulline.split(' ')[0]
        linenum = int(vulline.split(' ')[-1])
        if key not in _dict.keys():
            _dict[key] = [linenum]
        else:
            _dict[key].append(linenum)
    
    lang = '/home/ubuntu/data/SARD/slices/'
    leng = '/home/ubuntu/data/label/'
    
    path = os.path.join(lang, 'api_slices.txt')
    list_all_apilabel = make_label(path, _dict)
    dec_path = os.path.join(leng, 'api_slices_label.pkl')
    load(dec_path, list_all_apilabel)
    #f = open(dec_path, 'ab')
    #pickle.dump(list_all_apilabel, f)
    #f.close()
    
    path = os.path.join(lang, 'arraysuse_slices.txt')
    list_all_arraylabel = make_label(path, _dict)
    dec_path = os.path.join(leng, 'arraysuse_slices_label.pkl')
    load(dec_path, list_all_arraylabel)
    #f = open(dec_path, 'ab')
    #pickle.dump(list_all_arraylabel, f)
    #f.close()
    
    path = os.path.join(lang, 'pointersuse_slices.txt')
    list_all_pointerlabel = make_label(path, _dict)
    dec_path = os.path.join(leng, 'pointersuse_slices_label.pkl')
    load(dec_path, list_all_pointerlabel)
    #f = open(dec_path, 'ab')
    #pickle.dump(list_all_pointerlabel, f)
    #f.close()
 
    path = os.path.join(lang, 'integeroverflow_slices.txt')
    list_all_exprlabel = make_label(path, _dict)
    dec_path = os.path.join(leng, 'integeroverflow_slices_label.pkl')
    load(dec_path, list_all_exprlabel)
    #f = open(dec_path, 'ab')
    #pickle.dump(list_all_exprlabel, f)
    #f.close()
    

if __name__ == '__main__':
    main()
