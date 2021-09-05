def create(order):
    file = open('./Assignements/sales.txt' , 'w')
    file.write("Biggies\nPatia Bhubaneswar- 751023" + '\n' + '---------------------------------------'+'\n\n')
    total = 0
    for item, price in order.items():
        file.write('- ' + item + ' ' + format(price, '.2f') + '\n')
        total += price
    sgst = cgst = (total * 9)/100
    total += cgst + sgst
    
    file. write('\n          S.G.S.T @7.5% = ' + format(sgst,'.2f')+ '\n')
    file. write('          C.G.S.T @8% = ' + format(cgst,'.2f')+ '\n')
    file. write('             Subtotal = ' + format(total,'.2f')+ '\n\n\n')
    
    file.write('---------------------------------------' + '\n' + 'Thank you for coming !! ')
    file.close()
    
my_dict={'Chicken  Burger ': 200 , 'Chessy Fries            ': 90 , 'Veggie Rolls        ': 65, 'Cappucino           ': 85 , 'Grilled Sandwich       ': 350 ,'Blue Mohito          ': 180}
create(my_dict)
