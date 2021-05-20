class Category:

  def __init__(self,name):
    self.name=name
    self.ledger=[]

  def deposit(self,amount,description=""):
    self.ledger.append({"amount":amount,"description":description})

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount":amount*-1,"description":description})
      return True
    else:
      return False

  def get_balance(self):
    return sum([item["amount"] for item in self.ledger])

  def transfer(self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to {}".format(category.name))
      category.deposit(amount,"Transfer from {}".format(self.name))
      return True
    else:
      return False

  def check_funds(self,amount):
      if amount<=sum([item["amount"] for item in self.ledger]):
        return True
      else:
        return False

  def __str__(self):
    str1=''
    if len(self.name)%2==0:
      str1="*"*int((30-len(self.name))/2)+self.name+"*"*int((30-len(self.name))/2)
    else:
      str1="*"*int((30-len(self.name))/2)+self.name+"*"*int(((30-len(self.name))/2)-1)
    for item in self.ledger:
      num_len=len("{:.2f}".format(item["amount"]))
      word_len=len(item["description"][:23])
      str1+="\n{}{}{:.2f}".format(item["description"][:23]," "*(30-(num_len+word_len)),item["amount"])
    str1+="\nTotal: {:.2f}".format(sum([item["amount"] for item in self.ledger]))
    return str1

def create_spend_chart(categories):
  str1="Percentage spent by category\n"
  category_balances=[]
  for category in categories:
    category_balances.append(sum([item["amount"] for item in category.ledger]))
  total_balance=sum(category_balances)
  percentages=[int(round((balance/total_balance)*100,-1)) for balance in category_balances]
  intervals=["100|"," 90|"," 80|"," 70|"," 60|"," 50|"," 40|"," 30|"," 20|"," 10|","  0|"]
  percentage_bars=[" "*(len(intervals)-(percentage//10+1))+"0"*(percentage//10+1) for percentage in percentages]
  for i in range(len(intervals)):
    str1+="{} ".format(intervals[i],percentage_bars[0][i],percentage_bars[1][i],percentage_bars[2][i])
    for percentage_bar in percentage_bars:
      str1+="{}  ".format(percentage_bar[i])
    str1.rstrip()
    str1+="\n"
  str1+="    ----------\n"
  longest_word_length=max([len(category.name) for category in categories])
  words=[category.name+" "*(longest_word_length-len(category.name)) for category in categories]
  for i in range(longest_word_length):
    str1+="     "
    for word in words:
      str1+="{}  ".format(word[i])
    str1.rstrip()
    str1+="\n"
  return str1