# Create a CRUD dedicated to professors

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Create an instance of Flask

app = Flask(__name__)

# MySQL Connection

app.config['MYSQL_HOST'] = 'localhost'



