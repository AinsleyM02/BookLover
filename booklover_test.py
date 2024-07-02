import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("The Historian", 2)
        self.assertIn("The Historian", test_object.book_list["book_name"].values.tolist())
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        test_object.add_book("Dune", 4)
        self.assertEqual(test_object.book_list["book_name"].value_counts()["Dune"], 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("The Historian", 2)
        self.assertTrue(test_object.has_read("The Historian"))
    
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(test_object.has_read("The Scarlett Letter"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Dune", 5)
        test_object.add_book("The Historian", 2)
        self.assertEqual(test_object.num_books_read(),3)
    
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Dune", 5)
        test_object.add_book("The Historian", 2)
        fav_books_df = test_object.fav_books()
        self.assertTrue((fav_books_df["book_rating"] > 3).all())
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
#The last part of the file is crucial: It tells the Python interpreter to 
#run the bit of code at the end if the file is being run directly 
#(and not being imported into another file).