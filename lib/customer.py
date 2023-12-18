class Customer:
    customers=[]
    def __init__(self, first_name, last_name):
        self._first_name=first_name
        self._last_name=last_name
        Customer.customers.append(self)

    def first_name(self):
        return self._first_name
    
    def last_name (self):
        return self._last_name
     
    def full_name(self):
        
        return f"{self._first_name} {self._last_name}"
    
    def restaurants(self):
        return list(set(review.restaurant() for review in self._reviews))
    
    def add_reviews(self,restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

    def num_reviews(self):
        return len(self._reviews)
    

    @classmethod
    def find_by_name(cls, name):
        return [customer for customer in cls.customers if customer.full_name()==name]
    
    @classmethod
    def find_all_by_given_name(cls, first_name):
        return [customer for customer in cls.customers if customer.first_name() == first_name]


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

#customer1.full_name
#customers= Customer.all()
print(customer3.first_name())




    



        

 