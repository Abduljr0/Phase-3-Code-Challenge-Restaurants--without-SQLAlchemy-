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
    
#customer1=Customer("Ali", "Musa")
#customer3=Customer("Jeff", "Ainestein")
#customer6=Customer("John", "Eestein")
#customer7=Customer("John", "Dnestein")
#customer8=Customer("John", "Ainestein")
#customer9=Customer("John", "Ainestein")




#customer1.full_name
#customers= Customer.all()


class Restaurant:
    restaurants = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.restaurants.append(self)

    def name(self):
        return self._name
    
    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set(review.customer() for review in self._reviews))
    
    def average_star_rating(self):
        if not self._reviews:
            return 0

        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)

    @classmethod
    def all(cls):
        return cls.restaurants
    
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

        Review.all_reviews.append(self)

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

def main():
    customer1 = Customer("Abdulqani", "Adan")
    customer2 = Customer("John", "Okoth")
    customer3 = Customer("Musa", "Masaai")

    restaurant1 = Restaurant("KFC")
    restaurant2 = Restaurant("CJ's")
    restaurant3 = Restaurant("Pizza Hut")

    review1 = Review(customer1, restaurant1, 3)
    review2 = Review(customer2, restaurant2, 4)
    review3 = Review(customer3, restaurant3, 2)

    
    print(customer1.full_name())  
    print(customer2.full_name())

    for review in Review.all():
     print(f"Review - Customer: {review.customer().full_name()}, Restaurant: {review.restaurant().name()}, Rating: {review.rating()}")






    



        

 