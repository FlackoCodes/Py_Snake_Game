from turtle import Turtle
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.segments.append(turtle)
            self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # swapping the position so they can all move together
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            time.sleep(0.1)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        # get the position of the last segment in the snake
        last_segment_position = self.segments[-1].position()

        # create a new Turtle object for the new segment
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_segment_position)

        # add the new segment to the segments list
        self.segments.append(new_segment)


    def up(self):
        """Snake should turn up when the up arrow key is pressed when the heading of the snake is not facing down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Snake should turn down when the down arrow key is pressed when the heading of the snake is not facing up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Snake should turn right when the right arrow key is pressed when the heading of the snake is not facing
        right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Snake should turn left when the left arrow key is pressed when the heading of the snake is not facing left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
