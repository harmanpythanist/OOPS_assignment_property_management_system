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

# teseting class
new_commission_slip = CommissionSlip('Agent 2')
print(new_commission_slip.agent)    # Agent 2

# The main usage of these classes is linked with all other classes which is accessed in main.py file.
# as the CommisionSlip class is linked with all other classes, to test this class we will have to make all other classes as well
# which will be the entire code. That is why the appropriate test case of commision slip is the entire code present in main.py