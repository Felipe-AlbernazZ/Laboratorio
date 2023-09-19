import turtle

# Configurações da tartaruga
turtle.speed(0)
turtle.pencolor("orange")
turtle.pensize(10)
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

# Desenha a letra F
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)

# Espaço entre as letras
turtle.penup()
turtle.forward(50)
turtle.pendown()

# Desenha a letra E
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)

# Espaço entre as letras
turtle.penup()
turtle.forward(50)
turtle.pendown()

# Desenha a letra L
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# Mantém a janela aberta
turtle.done()
