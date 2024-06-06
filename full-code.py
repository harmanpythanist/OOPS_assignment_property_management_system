# we will start with making different classes for property, commercial property, property agent, property agency director and commission slip
# building the property class

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


# Above we have created a parent class Property. Now we will create a child class CommercialProperty
# CommercialProperty will inherit attributes and methods from property class

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


# now we will create property agency director class inherited from property agent class
# in addition to inheriting constructors and methods from the parent class, we will add additional method of commission sharing from agents under his management

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


# now we will create the class commissionslip which should show a detailed break down of the commission
# in case of director it should show the bonus earned from other agents as well


class CommissionSlip:
    def __init__(self, agent):
        self.agent = agent

    def generate_commission_slip(self):
        total_commission = 0
        commission_breakdown = []

        # Calculate commissions for properties sold by the agent
        for properties in self.agent.sold_properties:
            commission = properties.commission_of_property()
            shared_commission = commission * self.agent.commission_sharing_rate
            commission_breakdown.append((properties, commission, shared_commission))
            total_commission += shared_commission

        director_commission_breakdown = []
        total_overriding_commission = 0

        if isinstance(self.agent, PropertyAgencyDirector):
            for agent in self.agent.agent_under_management:
                agent_commission = 0
                agent_overriding_commission = 0
                for properties in agent.sold_properties:
                    commission = properties.commission_of_property()
                    shared_commission = commission * agent.commission_sharing_rate
                    agent_commission += shared_commission
                    overriding_commission = shared_commission * self.agent.bonus
                    agent_overriding_commission += overriding_commission
                    total_overriding_commission += overriding_commission

                director_commission_breakdown.append((agent, agent_commission, agent_overriding_commission))

        # Display the commission slip
        self.display_commission_slip(commission_breakdown, total_commission, director_commission_breakdown,
                                     total_overriding_commission)

    def display_commission_slip(self, commission_breakdown, total_commission, director_commission_breakdown,
                                total_overriding_commission):
        print("Commission Slip for " + str(self.agent.registration_number))
        print("Company: " + str(self.agent.property_agency_name))
        print("Year Started: " + str(self.agent.joining_year))
        print("")

        print("Commission Breakdown:")
        for properties, commission, shared_commission in commission_breakdown:
            print("---Property: " + properties.address)
            print("---Property Valuation: $" + str(properties.valuation))
            print("---Commission Rate: " + str(properties.commission_rate * 100) + "%")
            print("---Commission: $" + str(commission))
            print("---Shared Commission (Rate: " + str(self.agent.commission_sharing_rate * 100) + "%): $" + str(
                shared_commission))
            print("")

        if not isinstance(self.agent, PropertyAgencyDirector):
            print("Total Commission Earned: $" + str(total_commission))
            print("")

        if isinstance(self.agent, PropertyAgencyDirector):
            print("Overriding Commission Breakdown:")
            for agent, agent_commission, agent_overriding_commission in director_commission_breakdown:
                print("---Agent registration number: " + agent.registration_number)
                print("---Agent's Total Commission: $" + str(agent_commission))
                print("---Overriding Commission (Rate: " + str(self.agent.bonus * 100) + "%): $" + str(
                    agent_overriding_commission))
                print("")

            print("Total Overriding Commission Earned: $" + str(total_overriding_commission))
            print("Total Income Earned: $" + str(total_commission + total_overriding_commission))
            print("")


# Create directors and their agents
# we will import random to create a function for creating properties, agents, directors and commission slip
import random


def create_random_properties(num_properties):
    properties_list = []
    for properties in range(num_properties):
        address = str(random.randint(100, 999)) + "panipuri Street"
        postal_code = random.randint(100000, 999999)
        tenure = random.choice(["Owned", "Lease", "Rented"])
        completion_year = random.randint(1947, 2024)
        property_type = random.choice(["House", "Plot", "Grey_structure"])
        area = random.randint(500, 3000)
        valuation = random.randint(300000, 2000000)
        commission_rate = random.uniform(0.01, 0.03)
        property = Property(address, postal_code, tenure, completion_year, property_type, area, valuation,
                            commission_rate)
        properties_list.append(property)
    return properties_list


def create_random_commercial_properties(num_properties):
    commercial_properties_list = []
    for _ in range(num_properties):
        address = str(random.randint(100, 999)) + "Indian Market Street"
        postal_code = random.randint(100000, 999999)
        tenure = random.choice(["Owned", "Lease", "Rented"])
        completion_year = random.randint(1947, 2024)
        property_type = random.choice(["Shop", "Gym", "Restaurant"])
        area = random.randint(1000, 5000)
        valuation = random.randint(500000, 3000000)
        commission_rate = random.uniform(0.01, 0.03)
        commercial_property_type = random.choice(["Office", "Flatted Factory", "Factory"])
        commercial_property = CommercialProperty(address, postal_code, tenure, completion_year, property_type, area,
                                                 valuation, commercial_property_type, commission_rate)
        commercial_properties_list.append(commercial_property)
    return commercial_properties_list


directors = []

for i in range(2):
    director = PropertyAgencyDirector("Director " + str(i + 1), "India Estate Company", random.randint(1947, 2024))
    for j in range(3):
        agent = PropertyAgent("Agent " + str(j + 1), "India Estate Company", random.randint(1947, 2024))
        hold_properties = create_random_properties(5) + create_random_commercial_properties(5)
        sold_properties = create_random_properties(random.randint(4, 5)) + create_random_commercial_properties(
            random.randint(3, 5))

        for property in hold_properties:
            agent.add_property(property)
        for property in sold_properties:
            agent.add_property(property)
            agent.sell_property(property)
        director.add_agent(agent)
    directors.append(director)

# now we will print commission slip for each director and agent in India Estate Company
for director in directors:
    for agent in director.agent_under_management:
        print("Commission Slip for " + agent.registration_number + ":")
        commission_slip = CommissionSlip(agent)
        commission_slip.generate_commission_slip()

    print("Commission Slip for " + director.registration_number + ":")
    commission_slip = CommissionSlip(director)
    commission_slip.generate_commission_slip()


