from tabnanny import check
class ShoppingCart:
    def __init__(self):
        self.items=[]
    def addItems(self,item_name,qty,unit_price):
        self.items.append((item_name,qty,unit_price))
#adding a tuple to a list
    def remove_item(self,item_name):
        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break
    def calculate_total(self)->float:
        total=0.0
        for name,qty,price in self.items:
            total+=qty*price
        return total
    def summary(self):
        print("Cart Contents")
        for name,qty,price in self.items:
            print(f"{name}:{qty}@Ksh{price:.3f}each")
        print(f"Total:Ksh{self.calculate_total():.2f}\n")

if __name__=="__main__":
    cart=ShoppingCart()
    cart.addItems("kiwi",50,79.2)
    cart.addItems("papaya",30,40.3)
    cart.addItems("Guava",50,20.3)
    cart.addItems("Mango",40,7.6)
    cart.summary()
