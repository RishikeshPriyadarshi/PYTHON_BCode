def display_invoice(username,amount ,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on:{due_date}")
    

display_invoice("Depp", 42.50,"04/05")    