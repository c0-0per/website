class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def add(self, car):
         
 
        new_node = Node(None, None, car)
  
        if self.head is None:
            self.head = new_node
 
        elif self.head.data.price >= new_node.data.price:
            new_node.nextNode = self.head
            new_node.nextNode.prevNode = new_node
            self.head = new_node
        else:
            current = self.head
            while ((current.nextNode is not None) and (current.nextNode.data.price <= new_node.data.price)):
                current = current.nextNode
            new_node.nextNode = current.nextNode
            if current.nextNode is not None:
                new_node.nextNode.prevNode = new_node
  
            current.nextNode = new_node
            new_node.prevNode = current
 
    def updateName(self, identification, name):
        node = self.head
        while node:
            if node.data.identification == identification:
                node.data.name = name
                break
            node = node.nextNode
     
    def updateBrand(self, identification, brand):
        node = self.head
        while node:
            if node.data.identification == identification:
                node.data.brand = brand
                break
            node = node.nextNode
 
    def activateCar(self, identification):
        node = self.head
        while node:
            if node.data.identification == identification:
                node.data.active = True
                break
            node = node.nextNode
     
    def deactivateCar(self, identification):
        node = self.head
        while node:
            if node.data.identification == identification:
                node.data.active = False
                break
            node = node.nextNode
 
    def calculatePrice(self):
        node = self.head
        price = 0
        while node:
            if node.data.active:
                price += node.data.price
                print(node.data.brand)
            node = node.nextNode
        return price
 
class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = int(identification)
        self.name = str(name)
        self.brand = str(brand)
        self.price = int(price)
        self.active = bool(active)
 
 
db = LinkedList()
 
 
def init(cars):
    for a in cars:
        db.add(a)
 
 
def add(car):
    db.add(car)
 
 
def updateName(identification, name):
    db.updateName(identification, name)
 
 
def updateBrand(identification, brand):
    db.updateBrand(identification, brand)
 
 
def activateCar(identification):
    db.activateCar(identification)
 
 
def deactivateCar(identification):
    db.deactivateCar(identification)
 
 
def getDatabaseHead():
    return db.head
 
 
def getDatabase():
    return db
 
 
def calculateCarPrice():
    return db.calculatePrice()
 
 
def clean():
    db.head = None