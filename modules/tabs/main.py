import gradio as gr

from modules.ui import Tab


class Separate(Tab):
    def title(self):
        return "Main"

    def sort(self):
        return 1

    def ui(self, outlet):
        gr.Textbox("Main page")
