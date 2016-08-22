import random

class new_character:
    def __init__(self, dice, sides, dropmin=False):
        self.dice=dice
        self.sides=sides
        self.dropmin=dropmin
        
    def roll(self):
        self.rolls = []
        for i in xrange(0,(self.dice)):
            roll = random.randint(1,self.sides)
            self.rolls.append(roll)
            print "roll %1i" %roll
        if self.dropmin==False:
            print "the sum is %2.0i" %sum(self.rolls)
        elif self.dropmin==True:
            self.rolls.remove(min(self.rolls))
            print "the sum is %2.0i" %sum(self.rolls)
        return self
    def new_attribute(self):
        self.rolls = []
        for i in xrange(0,(self.dice)):
            roll = random.randint(1,self.sides)
            self.rolls.append(roll)
        if self.dropmin==False:
            print "the sum is %2.0i" %sum(self.rolls)
        elif self.dropmin==True:
            self.rolls.remove(min(self.rolls))
        return self
    def fullset(self, type='Fighter'):
        
        att = sorted([sum(self.new_attribute().rolls) for i in range(6)], reverse=True)
        
        thenames = ["strength", "dexterity", "constitution", "wisdom", "intelligence", "charisma"]
        
        self.attributes = att
        self.names = thenames
        
        if type=='Fighter':
            print "strength is", att[0]
            print "constitution is", att[1]
            print "dexterity is", att[2]
            print "wisdom is", att[3]
            print "intelligence is", att[5]
            print "charisma is", att[4]
            #print att
            
        elif type=='Rogue':
            print "dexterity is", att[0]
            print "charisma is", att[1]
            print "intelligence is", att[2]
            print "wisdom is", att[3]
            print "constitution is", att[5]
            print "strength is", att[4]
            #print att
            
        elif type=='Generic':
            
            genlist = ["Top", "Second", "Third", "Fourth", "Fifth", "Sixth"]
            
            for i in range(len(att)):
                print genlist[i], "is", att[i]  
            
        elif type=='Random':
            import random
            random.shuffle(thenames)
            
            for i in range(len(att)):
                print thenames[i], att[i]      
            
        return self
    
    def MCsets(self, iters=10000):
        att = sorted([sum(self.new_attribute().rolls) for i in range(6)], reverse=True)
        thenames = ["strength", "dexterity", "constitution", "wisdom", "intelligence", "charisma"]
        
        for name in range(len(thenames)):
            nums=[]
            for i in range(iters):
                
                att = sorted([sum(self.new_attribute().rolls) for i in range(6)], reverse=True)
                nums.append(att[name])
            globals()[thenames[name]]=nums

        self.top = strength
        self.second = dexterity
        self.third = constitution
        self.fourth = wisdom
        self.fifth = intelligence
        self.bottom = charisma
        
        return self
    
        
        
        
       
        
        