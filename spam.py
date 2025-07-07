p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
comment=input("enter comment:")
if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
      print("this comment is spam")
else:
      print("this comment is not spam")