# we will now create the property agent class

class PropertyAgent():
    def __init__(self, registration_number, property_agency_name, joining_year, commission_sharing_rate=0.70):
        self.registration_number = registration_number
        self.property_agency_name = property_agency_name
        self.joining_year = joining_year
        self.commission_sharing_rate = commission_sharing_rate
        self.hold_properties = []
        self.sold_properties = []

    def add_property(self, property):
        self.hold_properties.append(property)

    def sell_property(self, property):
        if property in self.hold_properties:
            self.hold_properties.remove(property)
            self.sold_properties.append(property)
        else:
            print("invalid_input_for_property")

    def earnings_per_anum(self):
        earnings_per_anum = 0
        for property in self.sold_properties:
            earnings_per_anum += property.valuation * property.commission_rate * self.commission_sharing_rate
        return earnings_per_anum


# testing class

new_agent = PropertyAgent('1212', 'SPICY STICKS', '2018')
print(new_agent.property_agency_name)    # SPICY STICKS
print(new_agent.joining_year)            # 2018

# for test purpose we will add a new property "India House" as a string to the agent list of hold properties.
# we are adding the property as a string to keep things simple here because in order to add a real property, we will have to import
#class of property and add that to the agent here.

new_agent.add_property("India House")
print("List of hold properties of the agent: " + str(new_agent.hold_properties))