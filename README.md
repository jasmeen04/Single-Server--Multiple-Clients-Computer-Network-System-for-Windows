# Client Server Network outraging Collaborative Document Editor

# Overview

This project implements a basic collaborative document editing server using Python's socket programming and threading capabilities. Multiple clients can connect to the server, view a shared document, and collaboratively edit its content in real-time.

# Features

**Server-Client Architecture**: Uses TCP sockets for communication between the server and multiple clients.

**Real-Time Document Collaboration**: Clients can connect, view, and edit a shared document simultaneously.

**Threaded Client Handling**: Each client connection is handled in a separate thread to ensure concurrent communication without blocking other clients.

**Error Handling**: Includes basic error handling for network operations and client disconnections.

# Requirements
Python 3.x
No additional Python packages are required beyond the standard library.

# Usage
**Clone the Repository**: Clone the repository to your local machine using Git.

**Start the Server**:Run the server script (server.py) to start the collaborative document editing server.

**Connect Clients**:Clients can connect to the server using any TCP client, such as telnet or a custom client application.

**Edit the Document**:Once connected, clients can send text data to the server. The server will update the shared document and broadcast changes to all connected clients.

**Terminate the Server**:To stop the server, use appropriate commands or key combinations in your terminal or command prompt.

# Structure
**server.py**: Contains the server implementation.

**client.py**: Example client script to connect and interact with the server.

# README.md
This file, providing an overview of the project, setup instructions, and usage guidelines.

# Contributing
Contributions to this project are welcome! If you have suggestions for improvements, fork the repository and submit a pull request with your changes.
