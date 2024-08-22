Network Port Scanner
A simple and user-friendly GUI-based network port scanner written in Python using the Tkinter library. This tool allows you to scan a range of ports on a specified IP address to determine if they are open or closed.

Features
IP Address Input: Specify the IP address you want to scan.
Port Range Selection: Choose the start and end ports to define the range you want to scan.
Real-time Results: View the status of each port as either open or closed in real-time.
Start/Stop Scanning: Easily control the scanning process with start and stop buttons.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/ferid333/Port-Scanner-With-GUI.git
cd port-scanner
Install the required dependencies:
This project requires Python 3.x. You can install the necessary dependencies using pip:

bash
Copy code
pip install -r requirements.txt
(Note: You may need to create a requirements.txt file with the necessary packages if any are needed. Since Tkinter and socket are standard Python libraries, additional packages may not be required.)

Run the Port Scanner:

bash
Copy code
python3 main.py
Usage
Enter the IP Address:

In the IP Address field, enter the IP address of the target device you want to scan.
Specify the Port Range:

Enter the start and end port numbers to define the range of ports you wish to scan.
Start Scanning:

Click the "Start Scanning" button to begin the scan. The results will be displayed in real-time, showing whether each port is open or closed.
Stop Scanning:

If you wish to stop the scan before it completes, click the "Stop Scanning" button.
Example
Here's how to use the scanner:

IP Address: 192.168.1.1
Start Port: 20
End Port: 80
This will scan ports 20 to 80 on the IP address 192.168.1.1, showing whether each port is open or closed.

Contributing
Your contributions are welcome! Here’s how you can help:

Report Bugs: If you find any issues, please report them by opening an issue on GitHub.
Feature Requests: Suggest new features or improvements by opening an issue.
Submit Pull Requests: If you have a code improvement or bug fix, feel free to submit a pull request.
To get started with contributing, you can:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit and push your changes (git push origin feature-branch).
Open a pull request on GitHub.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Future Improvements
Adding more detailed port information.
Implementing different scanning techniques (e.g., SYN scan).
Enhancing the user interface with additional options and feedback.
Contact
If you have any questions or feedback, feel free to reach out by opening an issue on GitHub.# Port-Scanner-With-GUI
