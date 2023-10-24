import gradio as gr


# def greet(name):
#     return "Hello " + name + "!"
# Testing Replit
def greet(name, is_morning, temperature):
    salutation = "Good Morning" if is_morning else "Good Evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


# text, image, audio, label
demo = gr.Interface(
    # fn=greet, inputs=gr.Textbox(lines=2, placeholder="Name here"), outputs="text"
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=[
        "text",
        "number",
    ],
)
demo.launch()
