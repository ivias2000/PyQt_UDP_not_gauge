# PyQt_UDP_not_gauge
This code appears to be a Python script for a graphical user interface (GUI) application using PyQt5. The code seems to be part of a learning series related to PyQt5. Here's a description of what this code does:

Imports: The code begins with various import statements to include necessary libraries and modules, including PyQt5, NumPy, pyqtgraph, and more.

Class Definition: The code defines a class named PyShine_THREADS_APP, which appears to be the main application window for the GUI.

Initialization: Inside the class constructor (__init__), the script loads a user interface (UI) from a file named 'adadxyz2.ui' and initializes various components and variables.

Thread Management: The code defines several threads, including ChronometerThread, LoggingThread, and ThreadClass, which are intended for different purposes. These threads handle tasks related to timing, logging, and data processing.

UDP Data Reception: In the ThreadClass, there is a loop that receives data over a UDP socket, processes it, and emits signals to update the GUI with the received data.

Data Processing: The code seems to process received data (phi, psi, d, x, y, z, and timer values) and perform calculations based on these values. It also appends data to a NumPy array called array_data.

GUI Initialization: The GUI is initialized with various widgets, including a real-time plot using pyqtgraph.

CSV Logging: The code includes functionality to log data to a CSV file (data1D.csv) with specific headers.

Application Entry: The script initializes the PyQt5 application, creates an instance of the PyShine_THREADS_APP class, shows the main window, and enters the application's main event loop.

Overall, this code appears to be a part of a PyQt5-based application for receiving, processing, and visualizing data received over UDP, possibly from some external source. It also includes features for logging the received data to a CSV file. The code structure suggests that it may be part of a larger project or tutorial series related to PyQt5 and data visualization.![Untitled](https://github.com/ivias2000/PyQt_UDP_not_gauge/assets/125237611/827cd6eb-0545-403b-96ea-24f47a642d7d)
