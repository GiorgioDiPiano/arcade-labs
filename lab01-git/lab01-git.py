import arcade
# ALtura, anchura y el nombre del dibujo
arcade.open_window(800, 600, "praia de areia", resizable=True, antialiasing=True)
arcade.set_background_color(arcade.color.BLUE_YONDER)
arcade.start_render()
arcade.draw_circle_filled(600, 500, 70, arcade.color.YELLOW)
arcade. draw_arc_outline(200, 500, 90, 100, arcade.color.WHITE, 0, 90)
arcade. draw_arc_outline(290, 500, -90, 100, arcade.color.WHITE, 0, 90)

arcade.finish_render()
arcade.run()