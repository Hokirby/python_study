# # 271

# class Account:
#     def  __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
        #   self.bankname = "SC은행"
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         print(f"계좌번호: {fstNumber}-{sndNumber}-{thdNumber}")
#         return fstNumber, sndNumber, thdNumber

# myacnt = Account("hosu",3500)
# print(myacnt.bankname)
# myacnt.accountNumber()

# 272

# class Account:
#     # class variable
#     objectNumbers = 0

#     def  __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         print(f"계좌번호: {fstNumber}-{sndNumber}-{thdNumber}")
#         return fstNumber, sndNumber, thdNumber

# myacnt = Account("이호수", 3500)
# other = Account("김민수", 1000)
# theother = Account("이민수", 2000)
# print(Account.objectNumbers)


# # 273

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
# myacnt = Account("이호수", 3500)
# print(myacnt.accountNumber())
# print(myacnt.accountCount())

# # 274

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
#     def deposit(self, amount):
#         if (amount<1):
#             print("입금은 최소 1원 이상만 가능합니다.")
#         else:
#             self.balance += amount
#         return self.balance
    
# myacnt = Account("이호수", 3500)
# print(myacnt.deposit(1000))

# # 275

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
#     def deposit(self, amountD):
#         if (amountD<1):
#             print("입금은 최소 1원 이상만 가능합니다.")
#         else:
#             self.balance += amountD
#         return self.balance
    
#     def withdraw(self, amountW):
#         if (amountW > self.balance):
#             print("계좌의 잔소 이상으로 출금할 수 없습니다.")
#         else:
#             self.balance -= amountW
#         return self.balance

# myacnt = Account("이호수", 1000)
# myacnt.withdraw(1500)
# myacnt.deposit(1000)
# myacnt.withdraw(1500)
# print(myacnt.balance)


# # 276

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1

#     def infoDisplay(self):
#         print(f"은행이름: {self.bankname}")
#         print(f"예금주: {self.holder}")
#         print(f"계좌번호: {self.accountNumber()}")
#         print("잔고: {:,}원".format(self.balance))
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
#     def deposit(self, amountD):
#         if (amountD<1):
#             print("입금은 최소 1원 이상만 가능합니다.")
#         else:
#             self.balance += amountD
#         return self.balance
    
#     def withdraw(self, amountW):
#         if (amountW > self.balance):
#             print("계좌의 잔소 이상으로 출금할 수 없습니다.")
#         else:
#             self.balance -= amountW
#         return self.balance

# myacnt = Account("이호수", 1000)
# myacnt.infoDisplay()

# # # 277

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.depositCount = 0
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1

#     def infoDisplay(self):
#         print(f"은행이름: {self.bankname}")
#         print(f"예금주: {self.holder}")
#         print(f"계좌번호: {self.accountNumber()}")
#         print("잔고: {:,}원".format(self.balance))
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
#     def deposit(self, amountD):
#         if (amountD<1):
#             print("입금은 최소 1원 이상만 가능합니다.")
#         else:
#             self.balance += amountD
#             self.depositCount += 1
        
#         if self.depositCount % 5 == 0:
#             self.balance += self.balance*0.01
        
#         return self.balance
    
#     def withdraw(self, amountW):
#         if (amountW > self.balance):
#             print("계좌의 잔소 이상으로 출금할 수 없습니다.")
#         else:
#             self.balance -= amountW
#         return self.balance

# myacnt = Account("이호수", 100)
# myacnt.deposit(1000)
# myacnt.deposit(1000)
# myacnt.deposit(1000)
# myacnt.deposit(1000)
# myacnt.deposit(1000)
# myacnt.deposit(1000)
# print(myacnt.balance)

# # # 278

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.depositCount = 0
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1

#     def infoDisplay(self):
#         print(f"은행이름: {self.bankname}")
#         print(f"예금주: {self.holder}")
#         print(f"계좌번호: {self.accountNumber()}")
#         print("잔고: {:,}원".format(self.balance))
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
#     def deposit(self, amountD):
#         if (amountD<1):
#             print("입금은 최소 1원 이상만 가능합니다.")
#         else:
#             self.balance += amountD
#             self.depositCount += 1
        
#         if self.depositCount % 5 == 0:
#             self.balance += self.balance*0.01
        
#         return self.balance
    
#     def withdraw(self, amountW):
#         if (amountW > self.balance):
#             print("계좌의 잔소 이상으로 출금할 수 없습니다.")
#         else:
#             self.balance -= amountW
#         return self.balance

# alist = []

# kims = Account("kim", 150)
# lees = Account("Lee", 100)
# parks = Account("Park", 200)

# alist.append(kims)
# alist.append(lees)
# alist.append(parks)

# print(alist)

# # 279

# class Account:
#     # class variable
#     objectNumbers = 0
#     accountNumbers = 0

#     def  __init__(self, holder, balance):
#         self.depositCount = 0
#         self.holder = holder
#         self.balance = balance
#         self.bankname = "SC은행"
#         Account.objectNumbers += 1

#     def infoDisplay(self):
#         print(f"은행이름: {self.bankname}")
#         print(f"예금주: {self.holder}")
#         print(f"계좌번호: {self.accountNumber()}")
#         print("잔고: {:,}원".format(self.balance))
    
#     def accountNumber(self):
#         from random import randrange
#         fstNumber = randrange(1,1000)
#         sndNumber = randrange(1,100)
#         thdNumber = randrange(1,1000000)
#         accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
#         Account.accountNumbers += 1
#         return accountNumber
    
#     def accountCount(cls):
#         return cls.accountNumbers # Account.accountNumbers
    
#     def deposit(self, amountD):
#         if (amountD<1):
#             print("입금은 최소 1원 이상만 가능합니다.")
#         else:
#             self.balance += amountD
#             self.depositCount += 1
        
#         if self.depositCount % 5 == 0:
#             self.balance += self.balance*0.01
        
#         return self.balance
    
#     def withdraw(self, amountW):
#         if (amountW > self.balance):
#             print("계좌의 잔소 이상으로 출금할 수 없습니다.")
#         else:
#             self.balance -= amountW
#         return self.balance

# alist = []

# kims = Account("kim", 1500)
# lees = Account("Lee", 1000)
# parks = Account("Park", 2000)

# alist.append(kims)
# alist.append(lees)
# alist.append(parks)

# print(alist)

# for i in alist:
#     if i.balance >= 1500:
#         i.infoDisplay()


# # 280

class Account:
    # class variable
    objectNumbers = 0
    accountNumbers = 0

    def  __init__(self, holder, balance):
        self.depositCount = 0
        self.holder = holder
        self.balance = balance
        self.bankname = "SC은행"
        Account.objectNumbers += 1

    def infoDisplay(self):
        print(f"은행이름: {self.bankname}")
        print(f"예금주: {self.holder}")
        print(f"계좌번호: {self.accountNumber()}")
        print("잔고: {:,}원".format(self.balance))
    
    def accountNumber(self):
        from random import randrange
        fstNumber = randrange(1,1000)
        sndNumber = randrange(1,100)
        thdNumber = randrange(1,1000000)
        accountNumber = str(fstNumber) + "-" + str(sndNumber) + "-" + str(thdNumber)
        Account.accountNumbers += 1
        return accountNumber
    
    def accountCount(cls):
        return cls.accountNumbers # Account.accountNumbers
    
    def deposit(self, amountD):
        if (amountD<1):
            print("입금은 최소 1원 이상만 가능합니다.")
        else:
            self.balance += amountD
            self.depositCount += 1
        
        if self.depositCount % 5 == 0:
            self.balance += self.balance*0.01
        
        return self.balance
    
    def withdraw(self, amountW):
        if (amountW > self.balance):
            print("계좌의 잔소 이상으로 출금할 수 없습니다.")
        else:
            self.balance -= amountW
        return self.balance
    
    def historyDeposit(self):
        for i in self.depositcount:
            i