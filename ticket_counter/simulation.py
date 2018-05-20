from arrays import Array
from linkedqueue import LinkedQueue as Queue
from simpeople import TicketAgent, Passenger
import random


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrive(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)
        self.printResults()

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" %
              len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    # Handles simulation rule #1.
    def _handleArrive(self, curTime):
        if random.randint(0.0, 1.0) <= self._arriveProb:
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.add(passenger)

    # Handles simulation rule #2.
    def _handleBeginService(self, curTime):
        for agent in self._theAgents:
            if agent.isFree():
                if not self._passengerQ.isEmpty():
                    agent.startService(self._passengerQ.pop(), curTime + self._serviceTime)

    # Handles simulation rule #3.
    def _handleEndService(self, curTime):
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger = agent.stopService()
        self._totalWaitTime += len(self._passengerQ)


if __name__ == "__main__":
    pas = TicketCounterSimulation(6, 25, 7, 23)
    pas.run()
