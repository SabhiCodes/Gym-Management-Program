import CustomerProgram
import EquipProgram
import EmpProgram
import Menus

Menus.title()
while True:
    Menus.choice()
    choose = input('Enter the number to initiate the program: ')
    if choose == '1':
        print('Customer management program launched')
        while True:
            Menus.menu()
            inp = input('Enter your choice ')
            if inp == '1':
                CustomerProgram.Cust_write()
            elif inp == '2':
                CustomerProgram.read()
            elif inp == '3':
                CustomerProgram.search_edit()
            elif inp == '4':
                CustomerProgram.delete()
            elif inp == '5':
                CustomerProgram.edit()    
            elif inp == '6':
                print('The program is being closed')
                break
            else:
                continue
    elif choose == '2':
        print('Equipment mangement program launched')
        while True:
            Menus.menu()
            inp = input('Enter your choice')
            if inp == '1':
                EquipProgram.Equip_write()
            elif inp == '2':
                EquipProgram.Equip_read()
            elif inp == '3':
                EquipProgram.Equip_search_edit()
            elif inp == '4':
                EquipProgram.delete()
            elif inp == '5':
                EquipProgram.edit()    
            elif inp == '6':
                print('The program is being closed')
                break
            else:
                continue
    elif choose == '3':
        print('Employee management program launched')
        while True:
            Menus.sql_menu()
            inp = input('Enter your choice')
            if inp == '1':
                EmpProgram.emp_write()
            elif inp == '2':
                EmpProgram.emp_search()
            elif inp == '3':
                EmpProgram.emp_del()
            elif inp == '4':
                print('The program is being closed')
                break
            else:
                continue
    else:
        break 
