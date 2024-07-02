#Booklover class
#This is the module
import pandas as pd

class BookLover:
    def __init__(self,name, email,fav_genre,num_books = 0,book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.num_books=num_books
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self,book_name, rating):
        if book_name not in self.book_list['book_name'].values.tolist():
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            #self.num_books+=1
        else:
            print("This book is already in the list!")
     
    
    def has_read(self,book_name):
        if book_name in self.book_list['book_name'].values.tolist():
            return True
        else:
            return False
    
    def num_books_read(self):
        num_books=len(self.book_list)
        return num_books
    

                    
    def fav_books(self):
        #make boolean condition: a list of booleans with true where the ratings area >3
        my_bool=self.book_list['book_rating'] > 3
        #subset the original list with only the values where the boolean condition is true
        fav_books_df=self.book_list[my_bool]
        #return that list
        return fav_books_df