'''
    Code for the sirajology chagenje on P vs NP and the tsp problem.

    I got the theory on how to solve the problem from: https://youtu.be/SC5CX8drAtU
    and created the following functions based on that.

    * This functions oly work with lists of 2d coordinates
    
    Functions explained:

      distance(x, y):
        Calculates the distance between x = [x,y] and y =[x,y] points.
      
      closest_point(point, points):
        Gets the closest point from a list of points to a given point.(lots of points)

      total_distance(points):
        Gets the total distance of traveling the points in order.

      greedy(points):
        Reorders the array of points going from the first one to the closest one consequently.
        [example = https://youtu.be/SC5CX8drAtU?t=11s]

      opt2(points):
        Swaps 2 random points.
        [example = https://youtu.be/SC5CX8drAtU?t=24s]

      multi_opt2(n, points):
        Runs opt2 n times.

      multi_opt2_anne(n, points):
        Runs opt2 n times, but tries simulated annealing (or the closest I got to that).

      to_xy(points):
        Returns 2 lists of points to be able to plot the points in a graph.

'''

import math
from random import sample



def distance(x, y):
    return math.sqrt( (y[0]-x[0])**2 + (y[1]-x[1])**2 )


def closest_point(point, points):
    closest = [999999, 999999]
    for p in points:
        if p == point:
            continue
        if distance(p, point) < distance(closest, point):
            closest = p
    return closest


def total_distance(points):
    total_distance = 0
    for p in enumerate(points):
        try:
            d = distance(points[p[0]], points[p[0]+1])
            total_distance += d
        except IndexError:
            continue # Last item, has no next
    return total_distance


def greedy(points):
    copy = list(points)
    greedy, cp, starting = [], [], []

    for point in enumerate(points):
        if point[0] == 0:
            starting = point[1]
            copy.remove(point[1])
            cp = closest_point(point[1], copy)
            greedy.append(point[1])
            greedy.append(cp)
        else:
            copy.remove(cp)
            cp = closest_point(cp, copy)
            greedy.append(cp)

    return greedy[:-1] + [starting]


def opt2(points):
    count = [p[0] for p in enumerate(points) if p[0] != 0]
    x, y = 0, 0
    while x > y or x == 0:
        x, y = sample(count, 2)
    new = points[:x] + points[x:y][::-1] + points[y:]
    return new   


def start_end(points):
    if points[0] != points[-1]:
        points.append(points[0])
    return points


def multi_opt2(n, points):
    points = start_end(list(points))
    for r in range(n):
        new = opt2(points)
        if total_distance(new) < total_distance(points):
            points = new

    return points


def multi_opt2_anne(n, points):
    points = start_end(list(points))
    for r in range(n):
        new = opt2(points)
        dnew = total_distance(new)
        dopt = total_distance(points)
        threshold =  math.sqrt(float(r)/n)**.2

        if r < int(n*0.8) and dnew*threshold < dopt:
            points = new
        elif dnew < dopt:
            points = new

    return points


def to_xy(points):
    x, y = [], []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return [x, y]

