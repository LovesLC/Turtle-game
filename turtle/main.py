import turtle
import random


class CuteRobotGame:
    def __init__(self):
        self.grid_size = 5
        self.cell_size = 50
        self.player_position = [1, 1]
        self.computer_position = [1, 1]
        self.player_moves = 0
        self.computer_moves = 0
        self.setup_screen()
        self.draw_grid()
        self.player_robot = self.create_robot("player")
        self.computer_robot = self.create_robot("computer")
        self.move_robot_to_start(self.player_robot, self.player_position)
        self.move_robot_to_start(self.computer_robot, self.computer_position)

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("lightblue")
        self.screen.title("Sequência de Comandos - Jogo de Lógica com Design Fofo de Anime")
        self.screen.setup(width=500, height=500)

    def draw_grid(self):
        grid_drawer = turtle.Turtle()
        grid_drawer.speed(0)
        grid_drawer.color("black")
        grid_drawer.penup()
        for i in range(self.grid_size + 1):
            grid_drawer.goto(-125, 125 - i * self.cell_size)
            grid_drawer.pendown()
            grid_drawer.forward(self.cell_size * self.grid_size)
            grid_drawer.penup()
        grid_drawer.right(90)
        for i in range(self.grid_size + 1):
            grid_drawer.goto(-125 + i * self.cell_size, 125)
            grid_drawer.pendown()
            grid_drawer.forward(self.cell_size * self.grid_size)
            grid_drawer.penup()
        grid_drawer.hideturtle()

    def create_robot(self, robot_type):
        robot = turtle.Turtle()
        robot.shape("turtle")
        if robot_type == "player":
            robot.color("pink")
        else:
            robot.color("blue")
        robot.penup()
        return robot

    def move_robot_to_start(self, robot, position):
        robot.goto(-125 + (position[1] - 1) * self.cell_size + 25, 125 - (position[0] - 1) * self.cell_size - 25)

    def move_robot(self, commands, position, robot):
        moves = 0
        for command in commands:
            if command == 'U' and position[0] > 1:
                position[0] -= 1
            elif command == 'D' and position[0] < self.grid_size:
                position[0] += 1
            elif command == 'L' and position[1] > 1:
                position[1] -= 1
            elif command == 'R' and position[1] < self.grid_size:
                position[1] += 1
            moves += 1
            self.update_robot_position(robot, position)
        return moves

    def update_robot_position(self, robot, position):
        x = -125 + (position[1] - 1) * self.cell_size + 25
        y = 125 - (position[0] - 1) * self.cell_size - 25
        robot.goto(x, y)

    def get_position(self, position):
        return tuple(position)

    def play_game(self):
        player_commands = self.screen.textinput("Comandos do Jogador",
                                                "Insira a sequência de comandos (U para cima, D para baixo, L para esquerda, R para direita):").upper()
        computer_commands = ''.join(random.choices('UDLR', k=random.randint(5, 20)))

        player_moves = self.move_robot(player_commands, self.player_position, self.player_robot)
        computer_moves = self.move_robot(computer_commands, self.computer_position, self.computer_robot)

        self.show_result(player_moves, computer_moves)

    def show_result(self, player_moves, computer_moves):
        result_turtle = turtle.Turtle()
        result_turtle.penup()
        result_turtle.hideturtle()
        result_turtle.goto(0, -200)

        result_turtle.write(f"Movimentos do jogador: {player_moves}", align="center", font=("Arial", 16, "bold"))
        result_turtle.goto(0, -220)
        result_turtle.write(f"Movimentos do computador: {computer_moves}", align="center", font=("Arial", 16, "bold"))

        result_turtle.goto(0, -240)
        if player_moves < computer_moves and self.player_position == [5, 5]:
            result_turtle.color("green")
            result_turtle.write("O jogador venceu a primeira etapa!", align="center", font=("Arial", 16, "bold"))
        elif computer_moves < player_moves and self.computer_position == [5, 5]:
            result_turtle.color("red")
            result_turtle.write("O computador venceu a primeira etapa!", align="center", font=("Arial", 16, "bold"))
        elif self.player_position == [5, 5] and self.computer_position == [5, 5]:
            result_turtle.color("blue")
            result_turtle.write("Empate na primeira etapa!", align="center", font=("Arial", 16, "bold"))


# Função principal
def main():
    game = CuteRobotGame()
    game.play_game()
    turtle.done()


if __name__ == "__main__":
    main()

