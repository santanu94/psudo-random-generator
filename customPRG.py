#!/usr/bin/python

class customMSM:
    
    seed = 1234567890
    digits = 10
    
    ##Reading seed value from file if exists.
    def get_seed(self):
        try:
            seed_file = open('seed', 'r')
            data = seed_file.readline()
            seed_file.close
            if len(data) > customMSM.digits:
                data = strip(data[:customMSM.digits])
            customMSM.seed = int(data)
        except:
            pass
    
    ##Modification of seed value
    def generate_new_seed(self):
        customMSM.seed = str(customMSM.seed * customMSM.seed)
        while len(customMSM.seed) < customMSM.digits * 2:
            customMSM.seed = '1' + customMSM.seed
        start = int(customMSM.digits / 2)
        end = start + customMSM.digits
        customMSM.seed = int(customMSM.seed[start:end])
    
    ##This function returns a random number between 0 and limit, with 0 inclusive and limit exclusive.
    def random(self, limit):
        self.get_seed()
        for i in range(0,25000):
            self.generate_new_seed()
        selection = customMSM.seed % limit      ##After giving lots of thought I chose % as it maintains equal biasnes towards all the possible output numbers.
        customMSM.seed += selection             ##An addition from my side to try to reduce repeatitive patterns.
        file = open('seed', 'w')                ##Saving seed value to file for more randomized value and to reduce chance of producing same number at each execution with same input condition.
        file.write(str(customMSM.seed))
        file.close
        return selection


