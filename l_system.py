import turtle
#very rudimentary L system
def evaluate_to_n (seed, ruleset,n):
    result = ""
    while(n!=0):
        for cmd in seed:
            try:
               result+=ruleset[cmd] 
            except KeyError:
                result+=cmd
        n-=1
        seed = result
        result=""
    return seed

def run (rules, angle_to_rotate_by):
    turtle.speed(10)
    angle = 0
    position_stack = []
    rotation_stack = []
    for rule in rules:
        if(rule=="+"):
            turtle.left(angle_to_rotate_by)
            angle -=angle_to_rotate_by
        if(rule=="-"):
            turtle.right(angle_to_rotate_by)
            angle+=angle_to_rotate_by
        if(rule=="F" or rule == "A"):
            turtle.fd(5)
        if(rule == "["):
            position_stack.append(turtle.pos())
            rotation_stack.append(angle)
        if(rule == "]"):
            tmp= position_stack.pop()
            turtle.up()
            turtle.goto(tmp[0], tmp[1])
            turtle.down()
            angle = rotation_stack.pop()
            turtle.setheading(angle)
n=10
ruleset={"F":"F+A", "A":"F-A"} #dragon curve
seed = "F"
turtle.up()
turtle.setpos(-100,0)
turtle.down()
run(evaluate_to_n(seed, ruleset, n), 90)