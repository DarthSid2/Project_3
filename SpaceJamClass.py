from panda3d.core import * 
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3
from direct.task import Task

class Universe(ShowBase):
    def __init__ (self, loader: Loader, modelPath: str, parentNode: NodePath, NodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
    
        self.modelNode.setName(modelPath)
        tex = loader. loadTexture(texPath)
        self.modelNode.setTexture(tex, 1 )


class Planets(ShowBase):
    
    def __init__ (self, loader: Loader, modelPath: str, parentNode: NodePath, NodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
    
        self.modelNode.setName(modelPath)
        tex = loader. loadTexture(texPath)
        self.modelNode.setTexture(tex, 1 )    

class SpaceDrones(ShowBase):
    droneCount = 0 
   
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1) 

class increment():
    Increment = 0            

class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
    
class SpaceShip_1(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.taskManager = self.taskMgr()



    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'Forward-thrust')
        else:
            self.taskManager.remove('Forward-thrust')

    def ApplyThrust(self, task):
        rate = 7
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont

    def SetkeyBindings(self):
        self.accept("arrow-up", self.Thrust, [1])
        self.accept("arrow-up-up", self.Thrust, [0])

    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'Right-turn')

        else:
            self.taskManager.remove('Right-turn')

    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'Left-turn')

        else:
            self.taskManager.remove('Left-turn')           











class yz():
    circleIncrement = 0

class xy():
     circleIncrement = 0

class xz():
    circleIncrement = 0
