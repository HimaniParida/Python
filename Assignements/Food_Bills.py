def create(order):
    file = open('./Assignements/sales.txt' , 'w')
    file.write("Burger King\nPatia Bhubaneswar- 751023" + '\n' + '---------------------------------------'+'\n\n')
    total = 0
    for item, price in order.items():
        file.write('- ' + item + ' ' + format(price, '.2f') + '\n')
        total += price
    sgst = cgst = (total * 9)/100
    total += cgst + sgst
    
    file. write('\n          S.G.S.T @9% = ' + format(sgst,'.2f')+ '\n')
    file. write('          C.G.S.T @9% = ' + format(cgst,'.2f')+ '\n')
    file. write('             Subtotal = ' + format(total,'.2f')+ '\n\n\n')
    
    file.write('---------------------------------------' + '\n' + 'Thank you for coming !! ')
    file.close()
    
my_dict={'Chicken Fiery Burger ': 200 , 'Med Fries            ': 89 , 'Veggie Strips        ': 49 , 'Pepsi Can            ': 60 , 'Grilled Wings        ': 350 ,'Blue Lagoon          ': 180}
create(my_dict)