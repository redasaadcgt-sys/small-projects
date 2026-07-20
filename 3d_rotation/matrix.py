from math import sin,cos,degrees
import time

class Matrix:
    def __init__(self, dimention, empty_char):
        matrix = [[[empty_char for _ in range(dimention)] for _ in range(dimention)] for _ in range(dimention)]


        self.dimention = dimention
        self.empty_char = empty_char

        self.matrix = matrix
 
        self.points = []


    def cube(self):
        length = self.dimention/2
        start = int((self.dimention/2) - length/2)
        end = int((self.dimention/2) + length/2)

        for i in range(self.dimention):
            if i >= start and i <= end :
                for j in range(self.dimention):
                    if j >= start and j <= end :
                        for k in range(self.dimention):
                            if k >= start and k <= end :
                                char = self.empty_char

                                # +X face
                                if i == end:
                                    char = ">"

                                # -X face
                                elif i == start:
                                    char = "<"

                                # +Y face
                                elif j == end:
                                    char = "^"

                                # -Y face
                                elif j == start:
                                    char = "*"

                                # +Z face
                                elif k == end:
                                    char = "#"

                                # -Z face
                                elif k == start:
                                    char = "0"

                                self.matrix[i][j][k] = char
                                self.points.append((float(i), float(j), float(k), char))

    def rotate(self, a, b, c):

        new_matrix = [[[self.empty_char for _ in range(self.dimention)] for _ in range(self.dimention)] for _ in range(self.dimention)]

        center = self.dimention / 2

        for px, py, pz, char in self.points:

            x = px - center
            y = py - center
            z = pz - center

            new = [
                y*sin(a)*sin(b)*cos(c)
                - z*cos(a)*sin(b)*cos(c)
                + y*cos(a)*sin(c)
                + z*sin(a)*sin(c)
                + x*cos(b)*cos(c),

                y*cos(a)*cos(c)
                + z*sin(a)*cos(c)
                - y*sin(a)*sin(b)*sin(c)
                + z*cos(a)*sin(b)*sin(c)
                - x*cos(b)*sin(c),

                z*cos(a)*cos(b)
                - y*sin(a)*cos(b)
                + x*sin(b)
            ]

            nx = round(new[0] + center)
            ny = round(new[1] + center)
            nz = round(new[2] + center)

            if 0 <= nx < self.dimention and \
                0 <= ny < self.dimention and \
                0 <= nz < self.dimention:

                new_matrix[nx][ny][nz] = char

        self.matrix = new_matrix

    def animate(self, a, b, c, sleep, iteration):

        A = 0
        B = 0
        C = 0
        
        for amount in range(iteration):
            self.rotate(A,B,C)
            print('\x1b[2J')
            print(self)
            A += a
            B += b
            C += c
    
            time.sleep(sleep)
            

    def __repr__(self):
        matrix = ""        # only show the x/y
        for i in range(len(self.matrix[0])) :
            for j in range(len(self.matrix[1])) :
                value = self.matrix[i][j][0]
                for k in range(len(self.matrix[2])):
                    if self.matrix[i][j][k] != self.empty_char :        # casting z value 
                        value = self.matrix[i][j][k]
                        break
                        
                matrix += f"{value}  "
            matrix += "\n"

        return f"{matrix}"




matrix = Matrix(dimention=30, empty_char=".")
matrix.cube()
matrix.animate(a=0.1,b=0.1,c=0,sleep=0.1, iteration=200)

