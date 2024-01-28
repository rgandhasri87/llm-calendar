from flask import Flask, request, render_template

app = Flask(__name__, static_folder='staticFiles')

from app import main