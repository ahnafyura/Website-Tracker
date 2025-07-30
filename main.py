from config import USE_OPENAI
import os
if USE_OPENAI:
    os.system("python online_main.py")
else:
    os.system("python offline_main.py")