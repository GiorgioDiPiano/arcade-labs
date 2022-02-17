import arcade
# ALtura, anchura y el nombre del dibujo
arcade.open_window(800, 600, "praia de areia", resizable=True, antialiasing=True)
# Color de fondo
arcade.set_background_color(arcade.color.BLUE_YONDER)
arcade.start_render()
# Dibuja el sol
arcade.draw_circle_filled(600, 500, 70, arcade.color.YELLOW)
# Dibuja 2 arcos blancos
arcade. draw_arc_outline(200, 500, 90, 100, arcade.color.WHITE, 0, 90)
arcade. draw_arc_outline(290, 500, -90, 100, arcade.color.WHITE, 0, 90)

arcade. draw_arc_outline(100, 400, 90, 80, arcade.color.WHITE, 0, 85)
arcade. draw_arc_outline(190, 400, -90, 80, arcade.color.WHITE, 0, 85)

arcade. draw_arc_outline(60, 480, 90, 60, arcade.color.WHITE, 0, 90)
arcade. draw_arc_outline(150, 480, -90, 60, arcade.color.WHITE, 0, 90)

arcade. draw_arc_outline(300,440,90,100,arcade.color.WHITE,0,100)
arcade. draw_arc_outline(390,440,-90,100,arcade.color.WHITE,0,100)

# Dibuja el mar
arcade.draw_lrtb_rectangle_filled(0,800,330,0,arcade.color.BLUE_SAPPHIRE)
# Dibuja la arena
arcade.draw_lrtb_rectangle_filled(0,800,230,0, arcade.color.SAND)
# Dibuja el rectángulo grande
arcade.draw_rectangle_filled(260,100,250,100,arcade.color.SANDY_TAUPE)
# Dibuja los rectángulos negros
arcade.draw_rectangle_filled(170,180,9,80, arcade.color.BLACK)
arcade.draw_rectangle_filled(260,180,9,80, arcade.color.BLACK)
arcade.draw_rectangle_filled(350,180,9,80, arcade.color.BLACK)
# Dibuja los rectángulos medianos
arcade.draw_rectangle_filled(170,150,60,60, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(260,150,60,60, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(350,150,60,60, arcade.color.SANDY_TAUPE)
# Dibuja los rectángulos pequeños
arcade.draw_rectangle_filled(150,180,10,15, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(169,180,10,15, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(188,180,10,15, arcade.color.SANDY_TAUPE)

arcade.draw_rectangle_filled(240,180,10,15, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(259,180,10,15, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(278,180,10,15, arcade.color.SANDY_TAUPE)

arcade.draw_rectangle_filled(330,180,10,15, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(349,180,10,15, arcade.color.SANDY_TAUPE)
arcade.draw_rectangle_filled(368,180,10,15, arcade.color.SANDY_TAUPE)
# Dibuja los triangulos rojos
arcade.draw_triangle_filled(165,220,165,200,130,210,arcade.color.RED)
arcade.draw_triangle_filled(255,220,255,200,220,210,arcade.color.RED)
arcade.draw_triangle_filled(345,220,345,200,310,210,arcade.color.RED)

arcade.finish_render()
arcade.run()
