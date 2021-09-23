# Pandas as pd 


import pandas as pd 

my_dict = {
    'Dish' : ["Dhokla", "Samosa", "Dosa"],
    'Price' : [12, 10, 30]
}

final_one = pd.DataFrame(my_dict)

print(final_one)