
class Basic_account:
  all_basic_acc={}

  def __init__(self,account_ID,name,num):
    self.account_ID=account_ID
    self.name=name
    self.num=num
    self.credits=0

class Premium_account(Basic_account):
  all_prem_acc={}


def upgrade_membership(id):
  a=Basic_account.all_basic_acc.pop(id)
  Premium_account.all_prem_acc[id]=a
  print('Congratulations. You are now upgraded to a premium member!')
  print(Premium_account.all_prem_acc)



def store_simulation():


  print('\nWelcome user!Purchase our store membership to avail the following benefits:\n\n' )
  print('BASIC MEMBERSHIP:\n .\n * Earn 1 credit on shopping for every 100Rs.\n *Avail these credits to get vouchers and shop more!\n **** Buy Basic membership just with one time payment of 2000Rs. ****')
  print('\n\nPREMIUM MEMBERSHIP:\n *Avail 10% discount every time you shop.\n * Earn 1 credit on shopping for every 50Rs.\n *Avail these credits to get vouchers and shop more! * Also get early access to sales!\n **** Buy premium membership just with Rs.2000 and later pay Rs.1000 per three months to continue with your membership plan. ****\n')

  while(True):

    print("\nwelcome!\n Choose an option: ")
    print('1.) Buy membership')
    print('2.) Access account')
    print('3.) Upgrade membership')
    print('4.) Exit')
    choice=input()
  
    if choice== '1':
      print('Choose type of membership:')
      print('1.) Basic')
      print('2.) Premium')
      membership=input()
      print('Enter your ID')
      id=input()
      print("Enter your name")
      name=input()
      print("Enter your contact no.")
      num=input()

      if membership== '1':
        print('Pay Rs.1500 and become a basic member now!')
        account=Basic_account(id,name,num)
        Basic_account.all_basic_acc[id]=account
        # also add this Id and everything to the database (praney)
        print('Congratulations! You are now a basic member')
        
      if membership=='2':
        print('Pay Rs.2500 and become a premium member now! ')
        
        account=Premium_account(id,name,num)
        Premium_account.all_prem_acc[id]=account
       # also add this Id everything to the database (praney)
        print('Congratulations! You are now a premium member')
    
    if choice == '2':
      print('Enter ID')
      id = input()

      account = None
      if id in Basic_account.all_basic_acc:
          account = Basic_account.all_basic_acc[id]
      elif id in Premium_account.all_prem_acc:
          account = Premium_account.all_prem_acc[id]
      else:
          print('ID not valid')
          continue

      print("Welcome user " + id + ".")
      print('Choose an option: \n1.) Use credits.\n2.) Pay and earn credits.')
      option = input()

      if option == '1':
          print("You have " + str(account.credits) + " credits.")
          amount_to_use = int(input("Enter the number of credits you want to use: "))

          if amount_to_use <= account.credits:
              account.credits -= amount_to_use
              print(str(amount_to_use) + " credits used successfully. Remaining credits: " + str(account.credits))
          else:
              print("Insufficient credits!")

      elif option == '2':
          amount = int(input("Enter the subtotal amount: "))

          if isinstance(account, Basic_account) and not isinstance(account, Premium_account):
              total_payable_amount=amount
              credits_earned = amount // 100
          
          elif isinstance(account, Premium_account):
              credits_earned = amount // 50
              total_payable_amount=0.9*amount
              print('You are a premium member.You get 10% discount on your subtotal amount!')
    
          account.credits += credits_earned
          
          print(f"The net total amount to be paid is Rs.{total_payable_amount}")
          print("You earned " + str(credits_earned) + " credits! Total credits: " + str(account.credits))
      else:
        print("Invalid option. Please try again.")




    if choice=='3':
      print('Enter you member id')
      id=input()
      # Check whether id is already a basic member in the database. (Praney).If not print('You need to be a basic member to proceed for upgradation.). If already a basic member, then:-
      print('Pay Rs.500 to upgrade membership from Basic to premium.')
      upgrade_membership(id)
      
    if choice=='4':
      print('\nGoodbye!')
      break

store_simulation()







