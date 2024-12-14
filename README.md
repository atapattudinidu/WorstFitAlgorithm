# WorstFitAlgorithm
Developed by Dinidu Atapattu
Reg no: 221436939

This is a Worst Fit Memory Allocation Simulator to simulate the algorithm

User Guide for the Worst Fit Memory Allocation Simulator
The Worst Fit Memory Allocation Simulator is an intuitive tool designed to help users understand and simulate the Worst Fit memory allocation strategy. Follow these steps to use the application:

Step 1: Launch the Application
•	Open the Python script (WorstFitSimulator.py) file in your Python environment or open WorstFitSimulator.exe
•	Run the script to launch the GUI interface.

Step 2: Provide Input Data
1.	Enter Memory Block Sizes:
o	Use the provided input field to enter the sizes of available memory blocks.
o	Input format: Comma-separated integers (e.g., 100, 200, 300, 400).
2.	Enter Process Requirements:
o	Use the second input field to enter the memory requirements for processes.
o	Input format: Comma-separated integers (e.g., 250, 50, 400, 100).
3.	Validate Inputs:
o	Ensure all inputs are positive integers and follow the correct format.

Step 3: Simulate Allocation
1.	Start Allocation:
o	Click the "Simulate Allocation" button to run the Worst Fit algorithm.
o	The algorithm will allocate each process to the largest available block that fits its requirement.
2.	View Results:
o	The results will appear in the output area, displaying:
	Which process was allocated to which memory block.
	Remaining sizes of memory blocks after each allocation.
	Any processes that could not be allocated due to insufficient memory.

Step 4: Interpret Outputs
•	Allocation Details:
o	For each process, the output will show the memory block it was assigned to (if successful).
•	Unallocated Processes:
o	If a process could not be allocated, it will be listed under "Unallocated Processes."
•	Remaining Memory:
o	Remaining sizes of each memory block after the allocation process will be displayed.

Step 5: Reset and Restart
•	To clear all inputs and start a new simulation:
o	Click the "Clear All" button.
o	Enter new data and repeat the steps above.
