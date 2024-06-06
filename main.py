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
