class Customer:
    customers=[]
    def __init__(self, first_name, last_name):
        self._first_name=first_name
        self._last_name=last_name
        Customer.customers.append(self)

    def first_name(self):
        return self._first_name
    
    def first_name(self ,new_first_name):
        self._first_name= new_first_name

    
    def last_name (self):
        return self._last_name
    
    def last_name (self ,new_last_name):
        self._last_name=new_last_name

    
    def full_name(self):
        
        return f"{self._first_name} {self._last_name}"
    
    @classmethod
    def all(cls):
        return cls.customers
    
customer1=Customer("Ali", "Musa")
customer3=Customer("Jeff", "Ainestein")
customer4=Customer("John", "Akoth")
customer5=Customer("John5", "Ainestein")
customer6=Customer("John", "Eestein")
customer7=Customer("John", "Dnestein")
customer8=Customer("John", "Ainestein")
customer9=Customer("John", "Ainestein")


customer1._first_name = "Khalid"

customer1.full_name
customers= Customer.all()
for customer in customers:
    print(customer.full_name())




    



        

 