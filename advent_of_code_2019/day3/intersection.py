
def getEndPoints(wire):

    # Process each segment and get point of each turn
    start = (0, 0)
    path = [start]

    current_point = start
    for segment in wire:
        direction = segment[0]
        step_count = int(segment[1:])

        x, y = current_point
        if direction == 'R':
            current_point = (x + step_count, y)
        elif direction == 'L':
            current_point = (x - step_count, y)
        elif direction == 'U':
            current_point = (x, y + step_count)
        elif direction == 'D':
            current_point = (x, y - step_count)

        path.append(current_point)

    return path

def horizontalVerticalIntersect(horiz_start, horiz_end, vert_start, vert_end):
    min_x = min(horiz_start[0], horiz_end[0])
    max_x = max(horiz_start[0], horiz_end[0])

    if (min_x <= vert_start[0] and vert_start[0] <= max_x):
        min_y = min(vert_start[1], vert_end[1])
        max_y = max(vert_start[1], vert_end[1])

        if (min_y <= horiz_start[1] and horiz_start[1] <= max_y):
            return (vert_start[0], horiz_start[1])

    return None

def isVertical(start, end):
    return start[0] == end[0]

def isHorizontal(start, end):
    return start[1] == end[1]

def pathIntersects(first_start, first_end, second_start, second_end):

    if isHorizontal(first_start, first_end) and isVertical(second_start, second_end):
        return horizontalVerticalIntersect(first_start, first_end, second_start, second_end)
    elif isVertical(first_start, first_end) and isHorizontal(second_start, second_end):
        return horizontalVerticalIntersect(second_start, second_end, first_start, first_end)
    return None

def getPointDistance(point):
    return abs(point[0]) + abs(point[1])

def getDistance(start, end):
    return getPointDistance((end[0] - start[0], end[1] - start[1]))

def getIntersections(first_wire, second_wire):

    intersections = []
    steps_to_intersections = []

    # Iterate through each segment of the first against each segment of the other
    first_wire_steps = 0
    for first_start, first_end in zip(first_wire[:-1], first_wire[1:]):

      second_wire_steps = 0
      for second_start, second_end in zip(second_wire[:-1], second_wire[1:]):
          intersect = pathIntersects(first_start, first_end, second_start, second_end)

          if intersect:
              intersections.append(intersect)
              first_wire_steps_to_intersect = first_wire_steps + getDistance(first_start, intersect)
              second_wire_steps_to_intersect = second_wire_steps + getDistance(second_start, intersect)
              steps_to_intersections.append(first_wire_steps_to_intersect + second_wire_steps_to_intersect)

          second_wire_steps += getDistance(second_start, second_end)

      first_wire_steps += getDistance(first_start, first_end)

    return intersections, steps_to_intersections


def getMinDistance(intersections):
    distances = [ getPointDistance(intersect) for intersect in intersections]
    return min(distances)


if __name__ == "__main__":

    with open("paths.txt") as path_file:
        first_wire = path_file.readline().split(",")
        second_wire = path_file.readline().split(",")

    first_wire_path = getEndPoints(first_wire)
    second_wire_path = getEndPoints(second_wire)

    intersections, steps_to_intersections = getIntersections(first_wire_path, second_wire_path)

    min_distance = getMinDistance(intersections)
    print("Min Distance: {}".format(min_distance))

    min_steps = min(steps_to_intersections)
    print("Min Steps: {}".format(min_steps))
