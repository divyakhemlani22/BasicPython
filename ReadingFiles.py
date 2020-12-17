employee_file = open("employees.txt", "r")
# few types
# read (r)-> Only reading
# write (w) -> Only writing
# append (a) -> Add to the end of the file
# r+ -> Read and write
for employee in employee_file.readlines():
    print(employee)
# readline = reading one line
# readlines = reading lines using index in the array
employee_file.close()

# To add a new employee
employee_file = open("employees.txt", "w")
employee_file.write("<p>Hello This is my company. These are my employees:</p>")
employee_file.write("\nKelly - Customer Service")
# always use \n for new line
# if you use w - it will overwrite everything




