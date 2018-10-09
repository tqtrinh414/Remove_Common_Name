import pandas as pd
import csv

def read_data(pathFile):
    return pd.read_csv(pathFile)

def remove_common(str):
    library = ['co.','co.,','c.','ltd.','company limited',\
                  'private limited','jsc','etc']
    for word in library:
        if str.find(word) != -1:
            str = str.replace(word, ' ')
    str = str.rstrip(' ')
    str = str.rstrip(',')
    return str

def write_dic_csv(dct, pathFo):
    try:
        df = pd.DataFrame.from_dict(dct)
        df.to_csv(pathFo, index=False)
    except IOError:
        print('I/O error')
        return False
    else:
        print('Done!')
        return True

def processing(pathFi, pathFo):
    dataframe = read_data(pathFi)
    lst_company_id = list(dataframe['company_id'])
    lst_company_name = list(dataframe['company_name'])
    for i in range(len(lst_company_name)):
        lst_company_name[i] = remove_common(lst_company_name[i])
    
    dct = {}
    dct['company_id'] = lst_company_id
    dct['company_name'] = lst_company_name
    write_dic_csv(dct, pathFo)



def main():    
    processing('Company_names_2018_10_06.csv','common_name.csv')

if __name__ == '__main__':
    main()
