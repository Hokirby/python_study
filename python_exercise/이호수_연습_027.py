# # 261

# class Stock():
#     def __init__ (self):
#         pass

# # 262

# class Stock():
#     def __init__ (self, codename, code):
#         self.codename = codename
#         self.code = code

# samsung = Stock("삼성전자", "005930")
# print(samsung.codename, samsung.code)

# # 263

# class Stock():
#     def __init__ (self, codename, code):
#         self.codename = codename
#         self.code = code

#     def nameSet(self, nameSet):
#         self.codename = nameSet

# a = Stock(None, None)
# a.nameSet("삼성전자")
# print(a.codename)

# # 264

# class Stock():
#     def __init__ (self, codename, code):
#         self.codename = codename
#         self.code = code

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet

# a = Stock(None, None)
# a.codeSet("005930")
# print(a.code)

# # 265

# class Stock():
#     def __init__ (self, codename, code):
#         self.codename = codename
#         self.code = code

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet
    
#     def get_name(self):
#         return self.codename
    
#     def get_code(self):
#         return self.code
    
# samsung = Stock("삼성전자", "005930")

# print(f"종목명: {samsung.codename}, 종목코드: {samsung.code}")

# # 266

# class Stock():
#     def __init__ (self, codename, code, PER, PBR, yeildDiv):
#         self.codename = codename
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.yeildDiv = yeildDiv

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet
    
#     def get_name(self):
#         return self.codename
    
#     def get_code(self):
#         return self.code

# # 267

# class Stock():
#     def __init__ (self, codename, code, PER, PBR, yeildDiv):
#         self.codename = codename
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.yeildDiv = yeildDiv

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet
    
#     def get_name(self):
#         return self.codename
    
#     def get_code(self):
#         return self.code

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# print(samsung.yeildDiv)


# # 268

# class Stock():
#     def __init__ (self, codename, code, PER, PBR, yieldDiv):
#         self.codename = codename
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.yeildDiv = yieldDiv

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet
    
#     def PERSet(self, PERSet):
#         self.PER = PERSet

#     def PBRSet(self, PBRSet):
#         self.PBR = PBRSet

#     def yieldSEt(self, yieldSet):
#         self.yieldDiv = yieldSet


#     def get_name(self):
#         return self.codename
    
#     def get_code(self):
#         return self.code


# # 269

# class Stock():
#     def __init__ (self, codename, code, PER, PBR, yieldDiv):
#         self.codename = codename
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.yeildDiv = yieldDiv

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet
    
#     def PERSet(self, PERSet):
#         self.PER = PERSet

#     def PBRSet(self, PBRSet):
#         self.PBR = PBRSet

#     def yieldSEt(self, yieldSet):
#         self.yieldDiv = yieldSet


#     def get_name(self):
#         return self.codename
    
#     def get_code(self):
#         return self.code

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# samsung.PERSet(12.75)
# print(samsung.PER)


# # 270

# class Stock():
#     def __init__ (self, codename, code, PER, PBR, yieldDiv):
#         self.codename = codename
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.yieldDiv = yieldDiv

#     def nameSet(self, nameSet):
#         self.codename = nameSet

#     def codeSet(self, codeSet):
#         self.code = codeSet
    
#     def PERSet(self, PERSet):
#         self.PER = PERSet

#     def PBRSet(self, PBRSet):
#         self.PBR = PBRSet

#     def yieldSEt(self, yieldSet):
#         self.yieldDiv = yieldSet


#     def get_name(self):
#         return self.codename
    
#     def get_code(self):
#         return self.code
    
#     # def stocklist(self):
#     #     stocklist = []
#     #     stocklist.append(self.codename)
#     #     stocklist.append(self.code) 
#     #     stocklist.append(self.PER) 
#     #     stocklist.append(self.PBR) 
#     #     stocklist.append(self.yieldDiv)
#     #     return stocklist

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

# stocklist = []

# stocklist.append(samsung)
# stocklist.append(hyundai)
# stocklist.append(lg)

# for i in stocklist:
#     print(i.code, i.PER)

