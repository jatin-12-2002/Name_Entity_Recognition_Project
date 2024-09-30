from fastapi import FastAPI
from uvicorn import run as app_run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from train import training as start_training
from ner.constants import *

start_training()