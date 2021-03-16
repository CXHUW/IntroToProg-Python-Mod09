# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# C. Halim,3..16.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

strFileName = 'EmployeeData.txt'
lstOfEmp = []


# Main Body of Script  ---------------------------------------------------- #
# Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts

try:
    lstOfEmp = Fp.read_data_from_file(strFileName)
    while True:
        # Show a menu of options
        Eio.print_menu_items()
        # Get user's menu option choice
        strChoice = Eio.input_menu_options()
        if strChoice.strip() =='1':
            # Show user current data in the list of employee objects
            Eio.print_current_list_items(lstOfEmp)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of employee objects
            empObj = Eio.input_employee_data()
            lstOfEmp.append(empObj)
            print(empObj)
            print('New input of employee information')
            continue
        elif strChoice.strip() =='3':
            # let user save current data to file
            Fp.save_data_to_file(strFileName, lstOfEmp)
            print('Data saved')
            continue
        elif strChoice.strip() == '4':
            # Let user exit program
            print ('Good Bye')
            break
except Exception as e:
    print(e)