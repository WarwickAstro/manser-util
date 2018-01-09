# cutpoints.py
Requires numpy and matplotlib, and has been used in both python 2.7 and 3.X.

This program will take an input file with x, y, and y_err columns and produce an interactable matplotlib plot. To interact with the plot, simply click and drag, and the program will register the (x,y) locations of your click and release. With this it will delete any points from the spectrum that are within the box defined by (x1, y1), (x2, y2). Once you have finished cutting points, closing the matplotlib figure window will end the interactability, and the program can save the updated data to a new file.

There are a number of options that you can use when you are in the figure window:

Box areas you wish to cut out of the plot.

Press q to deactivate the rectangle selector. This can be activated when you want to interact with the plot without cuttiing any points.
 
Press a to reactivate the rectangle selector. This returns the program to being able to delete points.

Press i to activate removal. This is always on, with no way to turn off. Future updates may allow the user to undo small mistakes, rather than having to start from scratch (see below).

Press u to return to the original data set and start again. If you make a mistake, this will allow you to rectify it without having to start the program again.

Press h to display these commands in the terminal.
