import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--host", help="Host to connect to", type=str, default="127.0.0.1")
parser.add_argument("--port", help="Port to connect to", type=int)
parser.add_argument("--share", help="Enable gradio share", action="store_true")

opts, _ = parser.parse_known_args()
