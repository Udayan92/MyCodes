from graphics import *
from wheel import *
def main():
    # Create a new window of 700 width and 500 height
    new_win = GraphWin("A Car", 700, 300)
    # Create a new car object
    car1 = car(Point(50, 50), 15, Point(100, 50), 15, 40)
    # Set colours to the object
    car1.set_color("black", "grey", "red")
    # Draw the car object after setting colours to it
    car1.draw( new_win )
    # Animate the car
    car1.animate(new_win, 2, 2, 100)
    new_win.mainloop()

main()
