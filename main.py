import random
global auc_item
global highest_bid
global id_of_bids #each nth element corresponds to the respective item in auc_item, so that is id_of_bids[0] is equal to 101 then auc_item[0][0] ie Item 1's highest bidder has the unique id of 101
id_of_bids=['' for i in range(15)] #place holder vals
highest_bid=[0 for i in range(15)]
auc_item= [["Item "+ str(i+1),0,"desc",random.randint(1,100),i+1] for i in range(15)] #generates the list with all of the "auction" things
total_fee=0

def showcase(): #showcases the information in auc_item
  print("Hello to Pete's Auction house!")
  for i in auc_item:
    for s in range(5):
      print(["Item name:","Number of bids:","Description","reserve value:",'Item number:'][s]+' '+str(i[s]))
    print('------------------------------')



def get_item_details(name): #gets specific item details
  index=-1
  for i in range(15):
    if auc_item[i][0]==name: index=i
  while index==-1:
    return index
    break
  for s in range(4):
      print(["Item name:","Number of bids:","Description:","reserve value:",'Item number:'][s]+' '+str(auc_item[index][s]))
  print("Highest bid:"+str(highest_bid[index]))
  print('------------------------------')
  return index


def bid():
  id_bidder=input('Enter your id please!:')
  try:
    id_bidder=int(id_bidder)
  except ValueError:
    print('Please enter a valid id!')
    bid()
    return 0
  print('These are all our items!')
  showcase()
  s=input('Do you want to bid on any of these?(y/n)')
  if s.lower() not in ['y','n','yes','no']:
    print('Please enter a valid input!')
    bid()
    return 0
  s=s.lower()
  if s=='y' or s=='yes':
    item_name=input('Please enter the item name!')
    index=get_item_details(item_name)
    if index==-1:
      print('Please enter a valid thing!')
      print('\n \n')
      bid()
      return 0
    print('Highest bid is--',highest_bid[index])
    amnt=input('Enter how much do you want to bid on it,enter -1 if you dont want to bid on this!')
    try:
      int(amnt)
    except ValueError:
      print('Please enter a valid amnt')
      bid()
      return 0
    amnt=int(amnt)
    if amnt>highest_bid[index]:
      auc_item[index][1]+=1
      highest_bid[index]=amnt
      id_of_bids[index]=id_bidder
      print('Thank you for bidding!')
      print('The highest bid now: ',highest_bid[index])
      print('Number of bids:',auc_item[index][1])
      bid()
      return 0
    elif amnt==-1:
      bid()
      return 0
    else:
      print('Enter a higher amount please!')
      bid()
      return 0
  else:
    contin=input('Do you want to continue?')
    contin=contin.lower()
    if contin not in ['y','n','yes','no']:
      print('Please enter a valid input!')
      bid()
      return 0
    if contin=='y' or contin=='yes':
      bid()
    else:
      print('Thanks for shopping with us!')


bid()

for i,j in zip(highest_bid,auc_item):
  if i>j[3]:
    print('Item ',j[4],' has been sold!')
    total_fee+=0.1*i
    print('Final bid is ',i)
  elif i==0:
    print('Item ',j[4],' has gotten 0 bids!')
  else:  
    print('Item ',j[4],' has been not been sold!')


print('Total fee ',total_fee)
