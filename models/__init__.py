#!/usr/bin/python3
import models
from models.engine import file_storage

storage = file_storage.FileStorage()

models.storage.reload()
