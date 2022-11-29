#########################--Importing Liberaries--################################
from fpdf import FPDF
from datetime import datetime

#########################--Creating Objects--####################################
pdf = FPDF()
# menu items
orderList = [{
  0: 'Pineapple Juice',
  1: 0,
  3: 80
}, {
  0: 'Chocolate Float',
  1: 0,
  3: 160
}, {
  0: 'Fruit Punch Moktail',
  1: 0,
  3: 180
}, {
  0: 'Cappuccino',
  1: 0,
  3: 120
}, {
  0: 'Ice Tea',
  1: 0,
  3: 200
}]


#########################--Checkout generates bills--############################
def checkOut():
  global orderList
  total = 0
  count = 0

  name = input('\nEnter Your Name : ')
  name = name.lower()

  x = datetime.now()
  diff = 3

  pdf.add_page()
  pdf.set_font("Arial", size=25)

  pdf.cell(200, 10, txt=('Customer Name : ' + name), ln=1, align='L')

  pdf.set_font("Arial", size=15)
  pdf.cell(200, 20, txt=str(x), ln=2, align='L')

  for i in range(diff, len(orderList) + diff):
    if (orderList[i - diff][1] != 0):
      t = str(
        orderList[i -
                  diff][1]) + "\tx\t" + orderList[i - diff][0] + "..." + str(
                    orderList[i - diff][3] * orderList[i - diff][1])
      pdf.cell(200, 10, txt=t, ln=i, align='L')
      count += 1
      total += (orderList[i - diff][3] * orderList[i - diff][1])

  pdf.cell(200,
           10,
           txt=('=============================='),
           ln=count,
           align='L')
  pdf.cell(200,
           10,
           txt=('Total To be Paid : ' + str(total)),
           ln=count + 1,
           align='L')

  # customer's name + time stamp and .pdf
  billName = name + str(x) + '.pdf'

  # generating PDF
  pdf.output(billName)

  print('\nDownload Your Invoice From Files')
  print('\nName : ', billName)

  # adding that name to generated bill so, it becomes easy to find
  file1 = open("Generated-Bills.txt", "a")
  file1.write(billName + '\n')
  welcome()


#########################--Searching Bill--######################################
def searchBill():

  orignal_list = []
  duplicate_list = []
  count = 0

  name = input('\nName to Search : ')
  name = name.lower()
  size = len(name)

  file1 = open("Generated-Bills.txt", "r")
  orignal_list = file1.readlines()
  file1.close()

  # creating duplicate list
  for i in range(0, len(orignal_list)):
    duplicate_list.append(orignal_list[i])

  # slicing names in duplicate list
  for i in range(0, len(duplicate_list)):
    duplicate_list[i] = duplicate_list[i][0:size]

  # counting number of bills
  for i in range(0, len(orignal_list)):
    if duplicate_list[i] == name:
      count += 1

  # if not found
  if count == 0:
    print('\nNo Bills Found!')

  # if found
  else:
    print('\n', count, 'Bills\' Found!')
    for i in range(0, len(orignal_list)):
      if duplicate_list[i] == name:
        print(orignal_list[i], end='')


#########################--Adding Items to Order--###############################
def addItem(n, q):
  orderList[n - 1][1] += q
  print('\n', orderList[n - 1][1], orderList[n - 1][0], 'Ordered!')


#########################--Order Menu Printing--#################################
def menu():

  print(
    '\nAvailable Dishes :\n1---Pineapple Juice\t\t\t80/-\n2---Chocolate Float\t\t\t160/-\n3---Fruite Punch Mocktail\t180/-\n4---Cappuccino\t\t\t\t120/-\n5---Lemon Ice Tea\t\t\t200/-\n\n6---Check Out\n'
  )
  choice = int(input("You Choice..."))

  if (choice >= 1 and choice <= 5):
    quantity = int(input("How many?..."))
    addItem(choice, quantity)
  elif choice == 6:
    checkOut()
  else:
    print('\nNot Valid Choice!!')

  menu()


#########################--Main Menu--###########################################
def welcome():
  print('\n#####################################')
  print('\n1---Order\n2---Search Bill\n3---Exit\n')
  choice = int(input('Your Choice...'))

  if choice == 1:
    menu()
  elif choice == 2:
    searchBill()
  elif choice == 3:
    exit(0)
  else:
    print('\nNot Valid Input!!\nTry Again\n')
    welcome()


#########################--Main Program--########################################
print('\n#####################################\n')
print('\t!! Welcome to PY Restro !!')
while True:
  welcome()
