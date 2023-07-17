import fusionengine as fusion

main = fusion.Main()

window = main.window.new_window("Fusion Engine", 800, 600)

@main.window.loop
def loop():
    main.draw.set_background_color(window, (main.color.BLUE))
    button = main.ui.button.new_button(
        window,
        "Hello World",
        25,
        25,
        200,
        100,
        main.fonts.NUNITO_LIGHT,
        "default",
        0,
        main.color.WHITE
    )
    @button.button_pressed
    def button_pressed():
        print("Hello World")
    # print("loop")
