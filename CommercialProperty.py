# CommercialProperty will inherit attributes and methods from property class
#we will need to define the property class first in order to make it a parent class of commercial property class
class Property:
    def __init__(self, address, postal_code, tenure, completion_year, property_type, area, valuation,
                 commission_rate=0.01):
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.commission_rate = commission_rate
        self.valuation = valuation

    # we can use the above attributes defined under the fn __init__ to access these different properties of the class
    # below we will define functions to bring a change to these attributes. They are commonly known as setters.

    def set_address(self, address):
        self.address = address

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def set_tenure(self, tenure):
        self.tenure = tenure

    def set_completion_year(self, completion_year):
        self.completion_year = completion_year

    def set_property_type(self, property_type):
        self.property_type = property_type

    def set_area(self, area):
        self.area = area

    def set_commission_rate(self, commission_rate):
        self.commission_rate = commission_rate

    def set_valuation(self, valuation):
        self.valuation = valuation

    # below is the function to calculate commission per property
    def commission_of_property(self):
        return self.commission_rate * self.valuation

class CommercialProperty(Property):
    def __init__(self, address, postal_code, tenure, completion_year, property_type, area, valuation,
                 commercial_property_type, commission_rate=0.01):
        super().__init__(address, postal_code, tenure, completion_year, property_type, area, valuation, commission_rate)
        self.commercial_property_type = commercial_property_type

    # defining a function to set the commercial property type after creating an abject
    def set_commercial_property_type(self, commercial_property_type):
        self.commercial_property_type = commercial_property_type

    def commission_of_commercial_property(self):
        return self.commission_rate * self.valuation

# testing our class

commercial_property = CommercialProperty('Delhi','1234', 'Owned', '2004', 'Factory', '2000', '1500000', 'Flatted Factory')
print("The address of commercial property: " + str(commercial_property.address))   # Delhi
print("The valuation of commercial property: " + str(commercial_property.valuation)) #1500000