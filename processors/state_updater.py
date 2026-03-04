from ..Entities.world import World
class StateUpdater:

    def execute(self, world: World): 
        data = self.compute_state(world)
        self.set_state_data(world, data)

    def set_state_data(self, world: World, data: list):
        state = world.get_state()
        state.turn += 1
        state.animals = data[0]
        state.food = data[1]
        state.avgAE = data[2]
        state.avgET = data[3]
        state.avgH = data[4]
        state.avgV = data[5]
        state.avgML = data[6]
        state.avgL = data[7]
        state.avgFE = data[8]
        state.avgGen = data[9]
        state.maxAE = data[10]
        state.maxET = data[11]
        state.maxH = data[12]
        state.maxV = data[13]
        state.maxL = data[14]
        state.maxFE = data[15]
        state.maxGen = data[16]
        state.minAE = data[17]
        state.minET = data[18]
        state.minH = data[19]
        state.minV = data[20]
        state.minL = data[21]
        state.minFE = data[22]
        state.minGen = data[23]
        state.totalAE = data[24]
        state.totalFE = data[25]
        state.totalE = data[24] + data[25]

    def compute_state(self, world: World) -> list:
        animals = len(world.animals)
        food = len(world.foods)
        avgAE = None
        avgET = 0.0
        avgH = 0.0
        avgV = 0.0
        avgML = 0.0
        avgL = 0.0
        avgFE = None
        avgGen = 0.0
        maxGen = 0
        maxAE = 0
        maxH = 0
        maxV = 0
        maxL = 0
        maxET = 0
        maxFE = 0
        minGen = 10e10
        minAE = 10e10
        minH = 10e10
        minV = 10e10
        minL = 10e10
        minET = 10e10
        minFE = 10e10
        totalAE = 0.0
        totalFE = 0.0

        if animals > 0:
            for a in list(world.get_animal_list().values()):
                totalAE += a.get_energy()
                avgET += a.get_threshold()
                avgH += a.get_hit()
                avgML += a.get_max_life()
                avgL += a.get_max_life()-a.get_life()
                avgV += a.get_vision()
                avgGen += a.get_gen()
                if a.get_gen() < minGen:
                    minGen = a.get_gen()
                if a.get_gen() > maxGen:
                    maxGen = a.get_gen()
                if a.get_energy() < minAE:
                    minAE = a.get_energy()
                if a.get_energy() > maxAE:
                    maxAE = a.get_energy()
                if a.get_hit() > maxH:
                    maxH = a.get_hit()
                if a.get_hit() < minH:
                    minH = a.get_hit()
                if a.get_vision() > maxV:
                    maxV = a.get_vision()
                if a.get_vision() < minV:
                    minV = a.get_vision()
                if a.get_max_life() > maxL:
                    maxL = a.get_max_life()
                if a.get_max_life() < minL:
                    minL = a.get_max_life()
                if a.get_threshold() > maxET:
                    maxET = a.get_threshold()
                if a.get_threshold() < minET:
                    minET = a.get_threshold()
            avgAE = totalAE / animals
            avgET = avgET / animals
            avgH = avgH/animals
            avgV = avgV/animals
            avgML = avgML/animals
            avgGen = avgGen / animals
            avgL = avgL / animals
        else:
            avgAE = 0.0
            avgET = 0.0
            avgH = 0
            avgV = 0
            avgML = 0
            avgGen = 0.0
            maxGen = 0
            maxAE = 0
            maxH = 0
            maxV = 0
            maxL = 0
            maxET = 0
            minGen = 0
            minAE = 0
            minH = 0
            minV = 0
            minL = 0
            minET = 0
            totalAE = 0
            avgL = 0
        
        if food >0:
            for f in list(world.get_food_list().values()):
                totalFE += f.get_energy()
                if f.get_energy() > maxFE:
                    maxFE = f.get_energy()
                if f.get_energy() < minFE:
                    minFE = f.get_energy()
            avgFE = totalFE/food
        else:
            avgFE = 0.0
            maxFE = 0.0
            minFE = 0.0
            totalFE = 0.0
        data = [animals,food,avgAE,avgET,avgH,avgV,
                avgML,avgL,avgFE,avgGen,maxAE,maxET,maxH,
                maxV,maxL,maxFE,maxGen,minAE,minET,
                minH,minV,minL,minFE,minGen,totalAE,totalFE]
        return data

   