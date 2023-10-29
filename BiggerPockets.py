class RentalProperty:
    def __init__(self):
        self.purchase_price = float(input("Enter the purchase price: "))
        self.rental_income = float(input("Enter the rental income: "))
        self.expenses = float(input("Enter the expenses: "))
        
    def calculate_ROI(self):
        net_income = self.rental_income - self.expenses
        return net_income / self.purchase_price * 100

property1 = RentalProperty()
print(f"The ROI is {property1.calculate_ROI()}%.")

def calculate_roi():
    income = float(input("Enter the total monthly income: "))  
    expenses = float(input("Enter the total monthly expense: "))  
    total_investment = float(input("Enter the total investment: "))  

    annual_cash_flow = (income - expenses) * 12
    roi = (annual_cash_flow / total_investment) * 100
    return roi

roi = calculate_roi()
print(f"The ROI is {roi}%.")