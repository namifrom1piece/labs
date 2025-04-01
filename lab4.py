# %% [markdown]
# # APS106 - Lab 4
# This week you will practice manipulating strings by writing four separate functions to extract experimental information from strings. 
# 
# ## Lab Objectives
# * Extract substrings from strings using indexing and string methods
# * Use operations and string methods to generate new strings
# * Convert between variable types
# * Utilize while loops to repeat segments of code until a condition is satisfied
# * Practice writing and debugging boolean expressions, conditionals, and loops
# * Understand how to convert between notebooks and .py files
# 
# ## Lab Deliverables
# The following files must be submitted to Gradescope prior to the assignment deadline:
# 1. `lab4.ipynb`
# 2. `lab4.py`
# 
# **Important**: Even though you are submitting both files, only `lab4.py` will be graded
# by the autograder. See below for further details.
# 
# Your `lab4.py` submission should contain the following functions:
# 1. `extract_name_from_email`
# 2. `calculate_site_average`
# 3. `generate_summary`
# 
# ## Gradescope reminders
# Your assignment will be graded using 10 test cases on Gradescope. You will be able to see the results of all of these tests before the deadline.
# However, you will only be able to see the inputs of the first **five** test cases before the submission deadline. 
# If you are not passing any of the test cases, there is an error (bug) in your submission that you will need to identify and correct. 
# 
# **IMPORTANT**: 
# * Do not change the file name or function names
# * Do not use input() inside your program
# 

# %% [markdown]
# ## Problem
# This week, we will imagine you are an engineer working on a treatment process for wastewater from a mine. To evaluate whether your design is effectively desalinating the wastewater, you hire several technicians to measure the pH of treated water at multiple locations around the mine every day.
# Everyday, the measurements from each technician are recorded and uploaded to a database as a string with the following format:
# *Technician email, date, site name, pH measurement, site name, pH measurement, site name, pH measurement, …*
# where:
# * *technician email* is the email of the technician
# * *date* is the day the measurements were taken, formatted as DD/MM/YY.
# * *site name* is the name of the site where a measurement was taken
# * *pH measurement* is the measured pH at that site. The measurements are taken to 2 decimal points.
# Note that there are multiple site-measurement pairs. The number of measurements can vary each day.
# 
# ### Example strings
# 1. `"dina.dominguez@company.com, 28/11/24, A, 4.20, B, 6.74, Control, 7.10, B, 6.45, Control, 7.88, Control, 6.38, A, 3.95"`
# 2. `"jamie.riggs@company.com, 15/12/23, B, 5.67, Control, 5.56, Db, 3.22, Control, 6.15, Control, 5.99"`
# 
# The first string contains measurements by Dina Dominguez from Nov. 28, 2024. There are a total of seven measurements from three sites (A, B, and Control). The second string contains measurements by Jamie Riggs from Dec. 15, 2023. There are a total of five measurements from three sites (B, Db, and Control).
# 
# ## Programming task
# You are interested in extracting the following information from each string:
# 1.	The date the measurements were taken
# 1.	The name of the technician
# 1.	The average pH measurement at specific sites
# 
# After a few weeks, there are hundreds of measurements being added to the database every day and you are finding that manually analyzing and extracting information is very inefficient. Luckily, you have programming skills from APS106 that will help you efficiently extract the information you need. So you decide to write a program to extract the information you need from each string and generate new stings that can be analyzed quickly!
# 
# ## Special instructions for completing this lab
# In this lab you will get experience with using both Jupyter notebooks (this file) and `.py` files in the PyCharm IDE.
# Knowing how to use both types of files is an important part of your Python programming toolkit. Luckily, as you'll get to see in this lab, the differences are not
# too complicated and transferring Python code between the two formats is simple. 
# 
# **Instructions**:
# 1. Follow the instructions in this notebook file to complete the functions required for this lab.
# 1. Once your functions are complete, follow the instructions at the end of the Notebook to transfer your code to the `lab4.py` file. This is the file that will be graded by Gradescope.
# 
# As always, your TAs are available to help you!
# 
# 
# 
# 

# %% [markdown]
# ## Part 1 - Extract the technician name from their email address
# To begin, you will write a function `extract_name_from_email` that accepts a string containing an email and returns a string containing the last and first name separated by a comma. You may assume that all input strings will be formatted as `firstname.lastname@domain.com`. The first letter of the first and last name returned by the function should be capitalized. All other letters should be lowercase.
# 
# ### Sample Test Cases
# | **Input** | **Expected output** |
# |-----------|---------------------|
# |`"ada.lovelace@wise.com"` | `"Lovelace,Ada"` |
# |`"guido.vanrossum@python.com"` | `"Vanrossum,Guido"` |
# 
# **Note**: the quotation marks are not part of the input or output strings, we just include them to indicate that they are strings. If you print the strings, there should be no quotation marks.
# 
# Complete the function below and then test your code.

# %%
def extract_name_from_email(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string containing the first and last names separated by a comma.

    Parameters
    ----------
    email : str
        A string with the format "first_name.last_name@domain.com" where
        first_name and last_name are strings of characters with no spaces

    Returns
    -------
    str
        A string with the format "Last_name,First_name" where
        the first and last names are capitalized and separated by a comma
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'Conda,Anna'
    """
    
    # To Do: Complete the function
    
    name = ''
    for character in range(0, len(email)):
        name = email[0:email.find('@')]
        first_name = (name[0:name.find('.')]).capitalize()
        last_name = (name[name.find('.')+1:]).capitalize()
        name = last_name + ',' + first_name
    return name       
        

# %%
## Test the function with a few test cases here

# Test case 1
email = "ada.lovelace@emaildomain.com"
name = extract_name_from_email(email)
print(name) # should print "Lovelace,Ada"

# Test case 2
email = "guido.vanrossum@python.com"
name = extract_name_from_email(email)
print(name) # should print "Vanrossum,Guido"

## Add more of your own test cases below ... (are there any edge cases to consider?)
email = 'NaOmi.ChI@mail.utoronto.ca' 
name = extract_name_from_email(email)
print(name) 

# %% [markdown]
# ## Part 2 - Calculate the average pH at a specific site
# Now complete the function `calculate_site_average` which will compute the average pH measurement from a specified measurement site.
# This function has two input parameters:
# | **Parameter** | **Type** | **Description** |
# |---------------|----------|-----------------|
# |`measurements` | `str`    | Alternating list of measurement sites and corresponding pH measurements.<br>All values are separated by a comma. |
# |`site`         | `str`    | The measurement site for which the average pH measurement should be calculated. |
# 
# The function should return the average pH measurement at the specified site *as a string*. The returned value should be rounded to two decimal places.
# If the measurement site specified by the `site` parameter is not contained within the `measurements` string, then the function should return the string `"NULL"`.
# 
# ### Assumptions and notes
# You can assume each measurement will contain exactly two decimal points of precision.
# However, there is **no guaranteed number of spaces following each comma**. There may be zero, one, or multiple spaces following any comma in the `measurements` string.
# 
# **Hints**:
# 1. Make use of the commas in the `measurements` string to slice the string into smaller components.
# 1. Start by writing the function to extract only the first measurement value from the desired site.
# 1. Once you can extract the first value, add a loop to your function to repeat this procedure for any additional measurements.
# 
# ### Sample test cases
# | `Measurements` | `site` | **Expected output** | **Description** |
# |----------------|--------|---------------------|-----------------|
# | `"Control, 7.40, Control, 7.19, Control, 7.61"` | `"Control"` | `"7.40"` | All measurements are from the same site;<br>All pH values are positive and less than 10 |
# | `"SchruteFarm,  10.25,SchruteFarm,  11.15,    SchruteFarm,9.60"` | `"SchruteFarm"` | `"10.30"` | All three measurements from the same site;<br>Inconsistent spacing after commas;<br>Some pH measurements are greater than 10 |
# | `"A, 4.16, B, 6.7, Control, 7.1, B, -0.2, Control, 7.8, Control, 6.8, A, 3.96"` | `"A"` | `"4.06"` | Measurements from multiple sites;<br>Some negative pH values |

# %%
def calculate_site_average(measurements, site):
    """
    (str, str) -> str
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the average of the site measurements to two decimal places.

    Parameters
    ----------
    measurements : str
        A string of comma separated site-measurement pairs where the site
        is a string and the measurement is a float.
    site : str
        A string representing the site for which the average is to be calculated.

    Returns
    -------
    str
        The average of the site measurements to two decimal places or "NULL"
        if there are no measurements for the specified site.
    
    >>> calculate_site_average("A, 4.23, B, 6.77, Control, 7.10, B, 6.55, Control, 7.82, Control, 6.89, A, 3.93", "Control")
    7.27
    """

    # To Do: Complete the function
    
    measurements = measurements.replace(" ", "")
    pairs = measurements.split(',')
    
    ph_value = []

    for i in range(0, len(pairs), 2):
        if pairs[i] == site:
            ph_value.append(float(pairs[i+1]))

    if not ph_value:
        return 'NULL'
        
    average = sum(ph_value) / len(ph_value)
    return str(round(average, 2))
    


# %%
## Test the function

# Test 1 - All measurements are for the specified site
measurements = "Control, 7.40, Control, 7.19, Control, 7.61"
site = "Control"
avg = calculate_site_average(measurements, site)
print(avg) # should print "7.4"

# Test 2 - Inconsistent spacing and measurements > 10
measurements = "Control, 10.44,    Control,9.99,Control,  12.61"
site = "Control"
avg = calculate_site_average(measurements, site)
print(avg) # should print "11.01"

# Add more of your own test cases below ... (hint: there are edge cases to consider that are not covered above)
measurements = "A, 4.23, B, 6.77, Control, 7.10, B, 6.55, Control, 7.82, Control, 6.89, A, 3.93"
site = 'Control'
avg = calculate_site_average(measurements, site)
print(avg)

# %% [markdown]
# ## Part 3 - Put it all together
# For the final part, complete the function `generate_summary`. This function accepts the following inputs:
# 
# | **Parameter** | **Type** | **Description** |
# |---------------|----------|-----------------|
# | `measurement_info` | `str` | String containing the technician email, date, pH measurements at various sites.<br>Formatted as*Technician email, date, site name, pH measurement, site name, pH measurement, site name, pH measurement, …* |
# | `target_site` | `str` | String specifying the measurement site for which the average pH measurement should be calculated |
# 
# The function should returns a string containing the date of the measurements, the technician's name, a target site name, and average of pH measurements at the target site:
# 
# *Date,Last name,first name,target site name,average of target site pH measurements*
# 
# There should be no spaces before or after the commas. If there is no measurements from the target site in the measurement info string, then the average should be written as `"NULL"`. **This function should call the other functions you created in parts 1-3.**
# 
# ### Sample test case
# | `measurement_info` | `target_site` | **Expected output** |
# |--------------------|---------------|---------------------|
# | `"michael.scott@dundermifflin.com, 05/05/05, Chilis, 4.20, SchruteFarm, 6.71, Control, 7.11, SchruteFarm, 6.59, Control, 7.48, Control, 6.86, Chilis, 3.90"` | `"Chilis`" | `"05/05/05,Scott,Michael,Chilis,4.05"` |
# | `"andrew.bernard@dundermiflinity.com, 04/10/07, Stamford, 1.22,Stamford, 1.23,  Tallahassee, 10.02"` | `"Scranton"` | `"04/10/07,Bernard,Andrew,Scranton,NULL"` |
# 
# ### How to test this function?
# This final function should utilize the other two functions that you wrote earlier in the lab.
# Breaking our code up into smaller functions like this has a few benefits. First, it makes our program easier to read and understand as each function has a clear and distinct task to complete.
# Another significant benefit is that it makes testing and validating the code easier. If you carefully and thoroughly tested the functions in parts 1 and 2, then you can have confidence that they will work correctly when used here. Therefore, all we need to test in our final function is:
# 1. does it use the other functions from parts 1-2 correctly (i.e., passing correct input arguments)?
# 1. does the function correctly concatenate the strings returned by the other functions into the correct output format?
# 
# Because we have reduced the scope of what we need to test for this function by using multiple functions, we have made the testing and debugging process much easier for ourselves!
# 
# 
# 

# %%
def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name and average of control
    site pH level measurements from string of technician measurements. 
    
    Parameters
    ----------
    measurement_info : str
        A string with the format "firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ..."
    site : str
        A string representing the site for which the average is to be calculated.
    
    Returns
    -------
    str
        A string with the format "date,Lastname,Firstname,site,average pH of specified site
 
    >>> generate_summary("michael.scott@dundermifflin.com, 05/05/05, Chilis, 4.20, SchruteFarm, 6.71, Control, 7.11, SchruteFarm, 6.59, Control, 7.48, Control, 6.86, Chilis, 3.90", "Chilis")
    '05/05/05,Scott,Michael,Chilis,4.05'
    """
    
    # To Do: Complete the function
    
    date = measurement_info[measurement_info.find(',')+2:measurement_info.find(',')+10]

    name = str(extract_name_from_email(measurement_info))

    measurement = measurement_info[measurement_info.find(',')+12:]
    avg_ph = str(calculate_site_average(measurement, site))
    output = date + ',' + name + ',' + site + ',' + avg_ph
    return(str(output))
    
  
    


# %%
#alternative code for part 3
#parts = measurement_info.split(', ')
    
#    date = str(parts[1])

#    email = parts[0]
#    name = str(extract_name_from_email(email))

#    measurements = str(parts[2:])
#    avg_ph = str(calculate_site_average(measurements, site))
#    output = date, name, site, avg_ph
#    return(str(output))

# %%
 # test your code here

#test 1
measurement_info = "michael.scott@dundermifflin.com, 05/05/05, Chilis, 4.20, SchruteFarm, 6.71, Control, 7.11, SchruteFarm, 6.59, Control, 7.48, Control, 6.86, Chilis, 3.90"
site = "Chilis" 
output = generate_summary(measurement_info, site)
print(output) # expected: "05/05/05,Scott,Michael,Chilis,4.05"

#test 2
measurement_info = "andrew.bernard@dundermiflinity.com, 04/10/07, Stamford, 1.22,Stamford, 1.23,  Tallahassee, 10.02"
site = "Scranton"
output = generate_summary(measurement_info, site)
print(output) # expected: "04/10/07,Bernard,Andrew,Scranton,NULL"


# %% [markdown]
# ## Notebook to `.py` file
# In the final part of this lab, you will transfer your functions to the `lab4.py` file, run your code in VSCode, and submit to Gradescope.
# 
# First, a brief overview on the differences between notebook (`.ipynb`) and python (`.py`) files.
# Notebooks are more interactive and allow you to run specific sections of code at different times, making them useful for learning and tasks like data exploration and visualization. For example, in this notebook, you can execute the cells with the test code independently of the cells that contain the functions. This means we can run the test cases multiple times without needing to re-run the code that defines the function. Notebooks also allow you to include non-code cells with text.
# 
# Python files (`.py`) are not so interactive like notebooks. Python files can be exeucted in an IDE like VSCode. When you execute a `.py` file, all of the code within the file is run. This makes `.py` files better suited for non-interactive, automated tasks like a program to continuously measure and display speed and other data on a car’s dashboard. 
# 
# Luckily, both types of files use standard Python programming syntax and converting between file types is not too challenging. To move your functions from this notebook to the `lab4.py` file, all you need to do is copy and paste your functions into the `lab4.py` file. Easy as that!
# 
# Once you have done this, try adding your test code to the `.py` and see what happens when you execute the file. You should see that all of your test cases are executed.
# 


