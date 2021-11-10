grid = []
points = []

class Cell:
    def __init__(self, corners):
        #top left, top right, bottom right, bottom left
        self.corners = corners
        self.w = corners[2][0] - corners[0][0]
        self.h = corners[2][1] - corners[0][1] 
        
    def show(self):
        stroke(50)
        strokeWeight(3)
        noFill()
        
        rect(self.corners[0][0], self.corners[0][1], self.w, self.h)        
        self.drawLines()
        
    def drawLines(self):        
        stroke(255)
        strokeWeight(3)
        
        #topLeft = self.corners[0]
        #topRight = self.corners[1]
        #bottomRight = self.corners[2]
        #bottomLeft = self.corners[3]
        
        corners = self.corners
        w = self.w
        h = self.h
        x = corners[0][0]
        y = corners[0][1]
        cornerValues = [corners[0][2],corners[1][2],corners[2][2],corners[3][2]]
        
        if cornerValues == [0,0,0,0]:
            #case 0
            pass
        elif cornerValues == [0,0,0,1]:
            #case 1
            line(x, y + h /2, x + w / 2, x + h)
        elif cornerValues == [0,0,1,0]:
            #case 2
            line(x + w / 2, y + h, x + w, y + h / 2)
        elif cornerValues == [0,0,1,1]:
            #case 3
            line(x, y + h /2, x + w, y + h / 2)
        elif cornerValues == [0,1,0,0]:
            #case 4
            line(x + w / 2, y, x + w, y + h / 2)
        elif cornerValues == [0,1,0,1]:
            #case 5
            line(x, y + h / 2, x + w / 2, y)
            line(x + w / 2, y + h, x + w, y + h / 2)
        elif cornerValues == [0,1,1,0]:
            #case 6
            line(x + w / 2, y, x + w / 2, y + h)
        elif cornerValues == [0,1,1,1]:
            #case 7
            line(x, y + h / 2, x + w / 2, y)
        elif cornerValues == [1,0,0,0]:
            #case 8
            line(x, y + h / 2, x + w / 2, y)
        elif cornerValues == [1,0,0,1]:
            #case 9
            line(x + w / 2, y, x + w / 2, y + h)
        elif cornerValues == [1,0,1,0]:
            #case 10
            line(x, y + h /2, x + w / 2, x + h)
            line(x + w / 2, y, x + w, y + h / 2)
        elif cornerValues == [1,0,1,1]:
            #case 11
            line(x + w / 2, y, x + w, y + h / 2)
        elif cornerValues == [1,1,0,0]:
            #case 12
            line(x, y + h / 2, x + w, y + h / 2)
        elif cornerValues == [1,1,0,1]:
            #case 13
            line(x + w / 2, y + h, x + w, y + h / 2)
        elif cornerValues == [1,1,1,0]:
            #case 14
            line(x, y + h /2, x + w / 2, x + h)
        elif cornerValues == [1,1,1,1]:
            #case 15
            pass     
        

def setup():
    size(600,600)
    background(0)
    stroke(255)
    spacing = 60
    for i in range(height // spacing + 1):
        for j in range(width // spacing + 1):
            x = j * spacing
            y = i * spacing
            value = random(2) // 1
            points.append([x,y,value])     
            
    rowLength = width // spacing + 1       
    for i in range(len(points) - rowLength - 1):
        #corners clockwise from top left
        #logic same as pixel indexing i + rowLength = element below i        
        corners = [points[i], points[i+1], points[i + 1 + rowLength] , points[i + rowLength]]
        cell = Cell(corners)
        grid.append(cell)
       
def draw():
    for cell in grid:
        cell.show()
        
    for p in points:
        strokeWeight(10)
        if p[2]:
            stroke(0,0,255)
        else:
            stroke(255,0,0)
        point(p[0],p[1])
        
    
