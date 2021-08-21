#To separate the mail IDs using spilt function and then finding the number of gmails, yahoos, outlooks etc using 
# dictionaries with gmail, yahoo, outlook as keys and the number of mail IDs corresponding to those as values¶


mails_list=["turboslayer@gmail.com",
"someone@outlook.com",
"crashtv@gov.in",
"blue_defender@gmail.com",
"logan@yahoo.com",
"ironmerc@gov.in",
"steeltitan@outlook.com",
"stealthedefender@yahoo.com",
"blaze_assault@gov.in",
"venom_fate@yahoo.com",
"dark_side@yahoo.com",
"fataldestiny@yahoo.com",
"ultimatebeast@outlook.com",
"masked_titan@gmail.com",
"frozen_gunner@yahoo.com",
"username_copied@gov.in",
"whos_ur_buddy@outlook.com",
"unfinished_sentenc@gov.in",
"all_gone@gov.in",
"something@gmail.com",
"president@gmail.com",
"tinfoilhat@gmail.com",
"anonymouse@yahoo.com",
"definitely_not_an_athlete@outlook.com",
"dropout@gov.in",
"paw_friend@outlook.com",
"test_name_please_ignore@gov.in",
"heyyou@gov.in",
"a_distraction@yahoo.com",
"thegodfatherpart4@gov.in",
"unfriendme@outlook.com",
"doodles@gmail.com",
"fluffycookie@yahoo.com",
"theintolerant@gmail.com",
"fourhour@yahoo.com",
"toastedwithcheese@gmail.com",
"futureking@yahoo.com",
"coolshirtbruh@outlook.com",
"kentucky@yahoo.com",
"chocolate@gmail.com",
"saintbroseph@yahoo.com",
"just_chillin@gmail.com",
"ghostface@gov.in",
"bigfootisreal@yahoo.com",
"newbie@yahoo.com",
"alienware@outlook.com",
"chrishemsworth@outlook.com",
"nachocheesefries@outlook.com",
"reginageorge@gov.in",
"harmless_potato@outlook.com",
"frostedcupcake@outlook.com",
"avocadorable@outlook.com",
"pixie_dust@gmail.com",
"chopsuey@yahoo.com",
"iron_man@gov.in",
"lemon_ade@outlook.com",
"cerial_killer@outlook.com",
"light_year@gov.in",
"phoenix@outlook.com",
"harry_potter@outlook.com"]

my_dict={}
count1,count2,count3,count4=0,0,0,0
for  i in mails_list:
    words=i.split('@')
    if words[1]=='gmail.com':
        count1+=1
    elif words[1]=='outlook.com':
        count2+=1
    elif words[1]=='gov.in':
        count3+=1
    else:
        count4+=1
    my_dict['gmail.com']=count1
    my_dict['outlook.com']=count2
    my_dict['gov.com']=count3
    my_dict['yahoo.com']=count4
    
print(my_dict)