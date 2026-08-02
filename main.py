import turtle as t

t.tracer(0)
def draw_board():
    for i in range(12):
        t.penup()
        t.goto(-240, 390-i*60)
        t.pendown()
        t.fd(480)

    t.right(90)
    for i in range(9):
        t.penup()
        t.goto(-240+i*60, 390)
        t.pendown()
        t.fd(300)
        if i > 0 and i <8:
            t.penup()

        t.fd(60)
        t.pendown()
        t.fd(300)

    t.penup()
    t.goto(-240+3*60, 390)
    t.pendown()
    t.goto(-240+5*60, 390-2*60)


    t.penup()
    t.goto(-240+5*60, 390)
    t.pendown()
    t.goto(-240+3*60, 390-2*60)

    t.penup()
    t.goto(-240+3*60, 390-11*60)
    t.pendown()
    t.goto(-240+5*60, 390-11*60+2*60)

    t.penup()
    t.goto(-240+5*60, 390-11*60)
    t.pendown()
    t.goto(-240+3*60, 390-11*60+2*60)

    t.penup()
    t.goto(0, 45)
    t.write("楚河"+" "*38+"汉界", font=("Micro", 17, "normal"), align="center")
    t.ht()
    t.update()
        
board = ['黑军','黑马','黑相','黑士','黑帅','黑士','黑相','黑马','黑军',
         '',    '',    '',    '',   '',    '',    '',   '',     '',
         '',    '',    '',    '',   '',    '',    '',   '',     '',
         '','黑炮',   '',    '',    '',    '',    '','黑炮',    '',
         '黑兵',    '','黑兵',    '','黑兵',    '','黑兵',    '','黑兵',
         '',    '',    '',    '',   '',    '',    '',   '',     '',
         '',    '',    '',    '',   '',    '',    '',   '',     '',
         '红兵',    '','红兵',    '','红兵',    '','红兵',    '','红兵',
         '','红炮',    '',    '',    '',    '',    '','红炮',    '',
         '',    '',    '',    '',   '',    '',    '',   '',     '',
         '',    '',    '',    '',   '',    '',    '',   '',     '',
         '红军','红马','红相','红士','红帅','红士','红相','红马','红军']

def get_board(x, y):
    return board[x+y*9]

pen = t.Pen()
pen.ht()
pen.pensize(3)
pen.speed(0)

move_pen = t.Pen()
move_pen.penup()
move_pen.color("light green")

def draw_piece(piece, x, y):
    if piece.startswith("红"):
        pen.color("red")
    if piece.startswith("黑"):
        pen.color("black")
    pen.penup()
    pen.goto(-240+x*60,390-60*y-27)
    pen.pendown()
    pen.begin_fill()
    pen.circle(27)
    pen.end_fill()

    pen.penup()
    pen.sety(pen.ycor()+5)
    pen.color("white")
    pen.write(piece[-1], font=("Micro", 22, "normal"), align="center")
    

def draw_selected_piece(piece, x, y):
    draw_piece(piece, x, y)
    pen.color("light green")
    pen.sety(pen.ycor()-5)
    pen.pendown()
    pen.circle(27)

def draw_pieces():
    for i, piece in enumerate(board):
        if piece:
            if selected and selected[0]+selected[1]*9 == i:
                draw_selected_piece(piece, i%9, i//9)
            else:
                draw_piece(piece, i%9, i//9)
                t.update()

def possible_moves(x, y):
    piece = get_board(x, y)
    if piece.endswith("炮"):
        return cannon_moves(x, y)
    else:
        return []

def cannon_moves(x, y):
    moves = []
    middle = None
    for i in range(x-1, -1, -1):
        if not middle and get_board(i, y) == '':
            moves.append((i, y))
        else:
            middle = i
            break
    if middle:
        for i in range(middle-1, -1, -1):
            piece = get_board(i, y)
            if  piece == '':
                continue
            else:
                if piece.startswith(opponent(turn)):
                    moves.append((i, y))
                break

    middle = None
    for i in range(x+1, 9):
        if get_board(i, y) == '':
            pass
            
    return moves

        
        

def click(x, y):
    global selected
    x = round((x+240)/60)
    y = round((390-y)/60)
    if 0 <= x < 9 and 0 <= y < 12:
        piece = get_board(x, y)
        if piece and piece.startswith(turn):
            selected = (x, y)
            move_pen.clear()
            pen.clear()
            draw_pieces()
        if selected:
            moves = possible_moves(x, y)
            for mx, my in moves:
                move_pen.goto(-240+mx*60,390-60*my)
                move_pen.dot(10)
                
            
                
t.onscreenclick(click)

turn = "红"
selected = None

draw_board()
draw_pieces()

t.done()
