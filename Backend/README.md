# How the backend works!!

## Communication.py
-------------------
This is a wrapper for the database. The base functionality of this should stay the same whether the database is a local file, or a server. It should only be refactored.

## Objects.py
-------------------
This is simply to define objects for easier use in the code.

## Server.py
-------------------
This is the asynchronous backend server, it will host the website and should be the code that is to be run. It will also have the hidden api for the webpage, and apps.