import arcade

def draw_sea():
    arcade.draw_lrtb_rectangle_filled(0, 800, 330, 0, arcade.color.BLUE_SAPPHIRE)

def draw_beach():
    arcade.draw_lrtb_rectangle_filled(0, 800, 230, 0, arcade.color.SAND)

def draw_flags():
    arcade.draw_rectangle_filled(170, 180, 9, 80, arcade.color.BLACK)
    arcade.draw_rectangle_filled(260, 180, 9, 80, arcade.color.BLACK)
    arcade.draw_rectangle_filled(350, 180, 9, 80, arcade.color.BLACK)
    arcade.draw_triangle_filled(165, 220, 165, 200, 130, 210, arcade.color.RED)
    arcade.draw_triangle_filled(255, 220, 255, 200, 220, 210, arcade.color.RED)
    arcade.draw_triangle_filled(345, 220, 345, 200, 310, 210, arcade.color.RED)
def draw_SandCastle():
    arcade.draw_rectangle_filled(260, 100, 250, 100, arcade.color.SANDY_TAUPE)

    arcade.draw_rectangle_filled(170, 150, 60, 60, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(260, 150, 60, 60, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(350, 150, 60, 60, arcade.color.SANDY_TAUPE)

    arcade.draw_rectangle_filled(150, 180, 10, 15, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(169, 180, 10, 15, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(188, 180, 10, 15, arcade.color.SANDY_TAUPE)

    arcade.draw_rectangle_filled(240, 180, 10, 15, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(259, 180, 10, 15, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(278, 180, 10, 15, arcade.color.SANDY_TAUPE)

    arcade.draw_rectangle_filled(330, 180, 10, 15, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(349, 180, 10, 15, arcade.color.SANDY_TAUPE)
    arcade.draw_rectangle_filled(368, 180, 10, 15, arcade.color.SANDY_TAUPE)
def draw_sun():
    arcade.draw_circle_filled(600, 500, 70, arcade.color.YELLOW)
def draw_birds():
    arcade.draw_arc_outline(200, 500, 90, 100, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(290, 500, -90, 100, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(100, 400, 90, 80, arcade.color.BLACK, 0, 85)
    arcade.draw_arc_outline(190, 400, -90, 80, arcade.color.BLACK, 0, 85)

    arcade.draw_arc_outline(60, 480, 90, 60, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(150, 480, -90, 60, arcade.color.BLACK, 0, 90)

    arcade.draw_arc_outline(300, 440, 90, 100, arcade.color.BLACK, 0, 100)
    arcade.draw_arc_outline(390, 440, -90, 100, arcade.color.BLACK, 0, 100)
def draw_shark(x, y):
    arcade.draw_point(x,y+50,arcade.color.BLACK,5)

    arcade.draw_arc_filled(x, 60 + y, 90, 80, arcade.color.ALICE_BLUE, 0, 150)
    arcade.draw_circle_filled(x - 9, 72 + y, 31, arcade.color.BLUE_SAPPHIRE)

def on_draw(delta_time):
    arcade.start_render()
    draw_sea()
    draw_shark(on_draw.shark1_z, 180)
    draw_beach()
    draw_flags()
    draw_SandCastle()
    draw_sun()
    draw_birds()
    draw_shark(on_draw.shark1_x, 200)
    draw_shark(on_draw.shark1_y-100, 220)
    on_draw.shark1_x += 1
    on_draw.shark1_y += 0.5
    on_draw.shark1_z += 2


on_draw.shark1_x = 80
on_draw.shark1_y = 80
on_draw.shark1_z = 80





def main():
    arcade.open_window(800, 600, "praia de areia", resizable=True, antialiasing=True)
    arcade.set_background_color(arcade.color.BLUE_YONDER)

    arcade.schedule(on_draw, 1 / 60)

    arcade.run()


# Call the main function
main()
