"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         Shixin Wu
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root=tkinter.Tk()
    # root.mainloop()


    # -------------------------------------------------------------------------
    # done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # root.mainloop()
    # -------------------------------------------------------------------------
    # done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    go_forward_button = ttk.Button(frame1, text='Forward')
    go_forward_button.grid()
    # root.mainloop()
    # -------------------------------------------------------------------------
    # done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    print_stuff_button = ttk.Button(frame1, text='Hello')
    print_stuff_button['command'] = (lambda:
                                     print("response"))
    print_stuff_button.grid()

    # root.mainloop()
    # -------------------------------------------------------------------------
    # done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = (lambda:
                                     print_contents(my_entry_box))
    print_entry_button.grid()





    # -------------------------------------------------------------------------
    # done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    # frame2 = ttk.Frame(root, padding=10)
    # frame2.grid()
    my_entry_box2 = ttk.Entry(frame1)
    my_entry_box2.grid()
    x=my_entry_box.get()
    print_entry_button2 = ttk.Button(frame1, text='Integer Entry')
    print_entry_button2['command'] = (lambda: print_contents2(my_entry_box2,my_entry_box))
    print_entry_button2.grid()
    go_for_button = ttk.Button(frame1, text='For')
    go_for_button.grid()

    # -------------------------------------------------------------------------
    # done: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    root.mainloop()
def print_contents(enter):
    x=enter.get()
    if x=="ok":
        print("Hello")
        # return "Hello"
    else:
        print("Goodbye")
        # return ("Goodbye")
    # return x
def print_contents2(enter,enter2):

    y=int(enter.get())
    if y==int:

        for k in range (y):
            print_contents(enter2)
    else:
        print_contents("error")
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
