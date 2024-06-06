# now we will create property agency director class inherited from property agent class
# in addition to inheriting constructors and methods from the parent class, we will add additional method of commission sharing from agents under his management

# we will need to define PropertyAgent class before creating it's child class in order to avoid any errors.

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

# after creating the parent class, we can now create the child class

class PropertyAgencyDirector(PropertyAgent):
    def __init__(self, registration_number, property_agency_name, joining_year, commission_sharing_rate=0.75,
                 bonus=0.05):
        super().__init__(registration_number, property_agency_name, joining_year, commission_sharing_rate)
        self.bonus = bonus
        self.agent_under_management = []

    def set_bonus(self, bonus):
        if 0.05 <= bonus <= 0.15:
            self.bonus = bonus
        else:
            print("invalid input for bonus rate. Please enter bonus rate between 5% to 15%.")

    def set_commission_sharing_rate(self, commission_sharing_rate):
        if 0.75 <= commission_sharing_rate <= 0.90:
            self.commission_sharing_rate = commission_sharing_rate
        else:
            print("invalid input for commission sharing rate. Please enter commission sharing rate between 75% to 90%.")

    def add_agent(self, agent):
        self.agent_under_management.append(agent)

    def earnings_per_anum(self):
        earnings_per_anum = 0
        for property in self.sold_properties:
            earnings_per_anum += property.valuation * property.commission_rate * self.commission_sharing_rate
        total_bonus = 0
        for agent in self.agent_under_management:
            total_bonus += agent.earnings_per_anum() * self.bonus
        total_earnings_per_anum = earnings_per_anum + total_bonus
        return total_earnings_per_anum

# Testing class

new_agency_director = PropertyAgencyDirector('0005', 'SPICY_MOMOS', '20002')

print("The registration number: " + str(new_agency_director.registration_number))    # 0005
print("The property agency name: " + str(new_agency_director.property_agency_name))   # SPICY_MOMOS
