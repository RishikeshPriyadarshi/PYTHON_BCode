#EX: kwargs(it allows us to pass multiple keyword-arguments)

def print_address(**kwargs):
    #print(type(kwargs)) # it will print class of kwargs is dict i.e. dictionary

    #NOTE: within this funcn "we can treat kwargs as if it is a dictionary "
    #      there r lot of built-in methods
        

print_address(street="123 Fake St.",
               city="Abyss",
               state="Corrupt",
               zip="54321")

