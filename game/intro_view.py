import arcade

INTRO_IMAGE_PATH = "game/images/introimage.jpg"


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.window.default_camera.use()

        # Load intro image as a texture
        self.intro_texture = arcade.load_texture(INTRO_IMAGE_PATH)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.window.width // 2,
            self.window.height // 2,
            self.window.width,
            self.window.height,
            self.intro_texture
        )

        arcade.draw_text(
            "Click to Start",
            self.window.width // 2,
            50,
            arcade.color.WHITE,
            30,
            anchor_x="center"
        )


    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


class GameView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.window.default_camera.use()

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "Game running! (Click or press Esc to quit)",
            20,
            self.window.height - 40,
            arcade.color.WHITE,
            20
        )

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    window = arcade.Window(1280, 720, "Christmas Tree Game")
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
