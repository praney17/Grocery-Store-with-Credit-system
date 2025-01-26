import mysql.connector

def db_connection():
   return mysql.connector.connect(
      host="localhost",
      user="root",
      password="tiger",
      database="GROCERY_STORE"
   )

class Basic_account:
  def __init__(self,name,num):
    self.name=name
    self.num=num
    self.balance=0
  
  def new_member(self):
     connection = db_connection()
     cursor = connection.cursor()
     cursor.execute ("INSERT INTO members ( member_name, membership_type, credit_balance, pnumber) VALUES (%s, %s, %s, %s)",
                     (self.name, 'Basic', self.balance, self.num))
     connection.commit()
     cursor.close()
     connection.close()

class Premium_account(Basic_account):
  def __init__(self,name, num):
     super().__init__( name, num)
     self.balance=0

  def new_member(self):
     connection = db_connection()
     cursor = connection.cursor()
     cursor.execute ("INSERT INTO members (member_name, membership_type, credit_balance, pnumber) VALUES (%s, %s, %s, %s)",
                     (self.name, 'Premium', self.balance, self.num))
     connection.commit()
     cursor.close()
     connection.close()

def upgrade_membership(account_ID):
   connection = db_connection()
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM members WHERE member_id = %s", (account_ID))
   result = cursor.fetchone()

   if result:
      cursor.execute("UPDATE members SET membership_typ = 'Premium' WHERE member_id = %s", (account_ID))
      connection.commit()
      print("◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈\n\nCONGRATULATIONS!!!!!\nyou've upgraded to premium membership\n\n◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈ ◈")
      
   else:
      print("member id not found")
    
   connection.close()
   
  
def validate_payment():
   x=input('Confirm Payment? (yes/no): ')
   if x=='yes':
    print('Payment successful')
   else: print('Payment rejected')




  

def store_simulation():


  print('\nWelcome user!Purchase our store membership to avail the following benefits:\n\n' )
  print('BASIC MEMBERSHIP:\n * Avail 10% discount every time you shop.\n * Earn 1 credit on shopping for every 100Rs.\n *Avail these credits to get vouchers and shop more!\n **** Buy Basic membership just with one time payment of 2000Rs. ****')
  print('\n\nPREMIUM MEMBERSHIP:\n *Avail 15% discount every time you shop.\n * Earn 1 credit on shopping for every 50Rs.\n *Avail these credits to get vouchers and shop more! * Also get early access to sales!\n **** Buy premium membership just with Rs.2000 and later pay Rs.1000 per three months to continue with your membership plan. ****\n')

  while(True):

    print("\nwelcome!\n Choose an option: ")
    print('1.) Buy membership')
    print('2.) Access account')
    print('3.) Upgrade membership')
    print('4.) Check credits')
    print('5.) Exit')
    choice=input()
  
    if choice=='1':
      print('Choose type of membership:')
      print('1.) Basic')
      print('2.) Premium')
      membership=input()
      print("Enter your name")
      name=input()
      print("Enter your contact no.")
      num=input()

      if membership== '1':
        print('Pay Rs.1500 and become a basic member now!')
        validate_payment()
        account = Basic_account( name, num)
        account.new_member()
        print("Congratulations! You are now a basic member")
        print(f"Your details are: {name} with member id {member_id} and membership type {membership}")
        
      if membership=='2':
        print('Pay Rs.2500 and become a premium member now! ')
        validate_payment()
        account=Premium_account(name,num)
        account.new_member()
        print('Congratulations! You are now a premium member')
        print(f"Your details are: {name} with member id {member_id} and membership type {membership}")
    
    elif choice=='2':
      print('Enter ID')
      member_id=input()
      connection = db_connection()
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
      result = cursor.fetchone()

      if result:
          member_id, name, membership, credits, num = result
          print(f"Welcome {name}! Your membership type is {membership} and you have {credits} credits")
          
          print('Choose an option: \n1.)Use credits.\n2.)Pay and earn credits.')
          option=input()
          
          if option == '1':
             print(f"You have {credits} credits.")
             amount_to_use = int(input("Enter the number of credits you want to use: "))
             
             if amount_to_use <= credits:
                credits -= amount_to_use
                cursor.execute(
                   "UPDATE members SET credit_balance = %s WHERE member_id = %s", (credits, member_id)
                )
                connection.commit()
                print(f"{amount_to_use} credits used successfully. Remaining Credits: {credits}")
             else:
                print("Insufficient credits")
          elif option == '2':
             amount = int(input("Enter the amount you want to pay: "))
             validate_payment()
             if membership.lower() == 'basic':
                credits_earned = amount // 100
             else:
                credits_earned = amount // 50

             credits += credits_earned
             cursor.execute(
                "UPDATE members SET credit_balance = %s WHERE member_id = %s ",
                (credits, member_id)
             )
             connection.commit()
             print(f"You earned {credits_earned} credits! Total credits: {credits}")
      else:
        print("Invalid memberid. Please check again.")
    
      connection.close()
      



    elif choice=='3':
      print('Enter you member id')
      member_id=input()
      print('Pay Rs.500 to upgrade membership from Basic to premium.')
      validate_payment()
      upgrade_membership(member_id)

    
    elif choice == "4":
       print("Enter ID")
       member_id=input()
       connection = db_connection()
       cursor = connection.cursor()
       cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
       result = cursor.fetchone()

       if result:
          member_id, name, membership, credits, num = result
          print(f"Your current credits are {credits}")

       else:
          print("Not a valid ID, please make an account")

    elif choice=='5':
      print('Goodbye!')
      break

store_simulation()
    







