class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    vend1 = VendingMachine()
    # TODO: Purchase input number of drinks
    input1 = int(input())
    vend1.purchase(input1)
    # TODO: Restock input number of bottles
    input2 = int(input())
    vend1.restock(input2)
    # TODO: Report inventory
    vend1.report()