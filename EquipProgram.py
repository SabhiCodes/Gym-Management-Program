import pickle
from tabulate import tabulate

def Equip_write():
    table = [['S.no.','Name of equipment','Type of equipment','Responsibility holder','Name of reponsibility holder','Cost']]
    a = int(input('How many enteries you want to make in the database:'))
    count = 0
    for i in range(count, a):
        b = input('Enter the name of the Equipment: ')
        c = input('Enter the typw of equipment: ')
        d = input('Is there a reponsibility holder? ')
        e = input('Name of the responsibility holder (Leave this empty if no)')
        f = input('Cost of the equipment')
        count+=1
        data = [count,b,c,d,e,f]
        table.append(data)
    print('The table formed is:-')
    print(tabulate(table,headers='firstrow', tablefmt='fancy_grid'))
    with open('Equipment_data.bin','wb') as file:
        pickle.dump(table, file)

def Equip_read():
    with open('Equipment_data.bin','rb') as file:
        data = pickle.load(file)
    print(tabulate(data,headers='firstrow', tablefmt='fancy_grid'))

def Equip_search_edit():
    with open('Equipment_data.bin','rb') as fp:
        data = pickle.load(fp)
    print('The table loaded for the task is:-')
    print(tabulate(data, headers= 'firstrow', tablefmt='fancy_grid'))
    info = int(input('What do you want to search??, Enter the S.no of the required data:'))
    head = [['S.no.','Name of equipment','Type of equipment','Responsibility holder','Name of reponsibility holder','Cost']]
    body = data[info]
    head.append(body)
    print('The table requested is:-')
    print(tabulate(head, headers= 'firstrow', tablefmt= 'fancy_grid'))
    ask = input('Do you want to edit the data?')
    if ask == 'yes':
        while True:
            print('Enter the coloumn which you wanted to edit')
            print('Enter the coloumn number in which you want to make changes')
            print('For eg. to edit the Name of equipment then enter 1')
            ohh = int(input())
            soo = input('Enter the detail which you want to update ')
            head[1][ohh] = soo
            print('The update data is:-')
            print(tabulate(head, headers='firstrow', tablefmt='fancy_grid'))
            now = input('Do you still wanted to make any more changes??')
            if now == 'yes':
                print('The program is being continued')
                continue
            else:
                break
        del head[0]
        data[info] = head[0]
        with open('Equipment_data.bin','wb') as fp:
            pickle.dump(data, fp)         
    else:
        print('The function is being terminated')

def delete():
    print(''' 
    The delete function has been launched''')
    with open('Equipment_data.bin','rb') as fp:
        data = pickle.load(fp)
    print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
    option = int(input('Enter the S.no which you want to delete :'))
    ask = input('Do you really want to delete the selected row? ')
    if ask == 'yes':
        print('The selected option is being deleted ')
        del data[option]
        print('The new data is:-')
        print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
        with open('Equipment_data.bin','wb') as fp:
            pickle.dump(data, fp)
        print('The data has been successfully edited and stored')
    else:
        print('The function being terminated')

def edit():
    with open('Equipment_data.bin','rb') as fp:
        edittable = pickle.load(fp)
    what = input('Do you want to enter more than 1 data?')
    if what == 'yes':
        hmm = int(input('How many new entreies you want to make?'))
        lencount = len(edittable)
        for i in range(hmm):
            b = input('Enter the name of the Equipment: ')
            c = input('Enter the typw of equipment: ')
            d = input('Is there a reponsibility holder? ')
            e = input('Name of the responsibility holder (Leave this empty if no)')
            f = input('Cost of the equipment')
            data = [lencount,b,c,d,e,f]
            lencount+=1
            edittable.append(data)
        print('The table formed is:-')
        print(tabulate(edittable,headers='firstrow', tablefmt='fancy_grid'))
        with open('Equipment_data.bin','wb') as fp:
            pickle.dump(edittable, fp)
    else:
        b = input('Enter the name of the Equipment: ')
        c = input('Enter the typw of equipment: ')
        d = input('Is there a reponsibility holder? ')
        e = input('Name of the responsibility holder (Leave this empty if no)')
        f = input('Cost of the equipment')
        data = [len(edittable),b,c,d,e,f]
        edittable.append(data)
    print('The table formed is:-')
    print(tabulate(edittable,headers='firstrow', tablefmt='fancy_grid'))
    with open('Equipment_data.bin','wb') as fp:
        pickle.dump(edittable, fp)