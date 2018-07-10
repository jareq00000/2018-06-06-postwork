'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle

class Invoker(object):
    def __init__(self):
        self.recording = False
        self.history = []
        
    def record(self):
        print("Recording started")
        self.recording = True
        
    def stop(self):
        print("Recording stopped")
        self.recording = False 
        
    def playback(self):
        print("playback")
        for command in self.history:
            print(f"Performing recorded action: {command}")
            TurtleShell(command)


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        turtle.forward(int(arg))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        turtle.right(int(arg))
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        turtle.left(int(arg))
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        turtle.home()
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        turtle.circle(int(arg))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % turtle.position())
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (turtle.heading(),))
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        turtle.reset()
    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

class Command(object):
    def __init__(self, inv, ts):
        self.inv = inv
        self.ts = ts
        
    def action(self, command_name, param):
        self.command_name = command_name
        if inv.recording == True:
            print (f"saving: {command_name}")
            inv.history.append([command_name, param])
        print (f"performing action: {command_name}")
        getattr(ts, command_name)(param)
    
    
if __name__ == '__main__':
    
    inv = Invoker()
    ts = TurtleShell()
    command = Command(inv, ts)
    command.action("do_home", 0)
    command.action("do_forward", 10)
    inv.record()
    command.action("do_forward", 10)
    command.action("do_circle", 10)
    inv.stop()
    command.action("do_heading", 10)
    inv.playback()

    #TurtleShell().cmdloop() 
