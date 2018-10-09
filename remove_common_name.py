import pandas as pd


def read_data(pathFile = './Company_names_2018_10_06.csv'):
    return pd.read_csv(pathFile)

def remove_common(str):
    library = ['co.','co.,','c.','ltd.','company limited',\
                  'private limited','jsc','etc']
    for word in library:
        if str.find(word) != -1:
            str = str.replace(word, '')
    str = str.rstrip(' ')
    str = str.rstrip(',')
    return str

def processing(dataframe):
    lst_company_id = list(dataframe['company_id'])
    lst_company_name = list(dataframe['company_name'])
    for i in range(len(lst_company_name)):
        lst_company_name[i] = remove_common(lst_company_name[i])
    
    dct = {}
    for i in range(0, len(lst_company_id)):
        dct[lst_company_id[i]] = lst_company_name[i]
    return dct

def print_dic(dct):
    for key in dct:
        print(key, dct[key])


def main():    
    print(read_data())
    dct = processing(read_data())
    print_dic(dct)

if __name__ == '__main__':
    main()
