import tkinter as tk
from tkinter import messagebox

class WorstFitSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Worst Fit Memory Allocation")

        # Input fields for memory blocks and processes
        self.blocks_label = tk.Label(root, text="Enter memory block sizes (comma-separated):")
        self.blocks_label.pack()
        self.blocks_entry = tk.Entry(root, width=50)
        self.blocks_entry.pack()

        self.processes_label = tk.Label(root, text="Enter process memory requirements (comma-separated):")
        self.processes_label.pack()
        self.processes_entry = tk.Entry(root, width=50)
        self.processes_entry.pack()

        # Buttons for allocation and reset
        self.allocate_button = tk.Button(root, text="Simulate Allocation", command=self.simulate_allocation)
        self.allocate_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Clear All", command=self.clearAll)
        self.reset_button.pack(pady=5)

        # Output box for results
        self.output_label = tk.Label(root, text="Results:")
        self.output_label.pack()
        self.output_text = tk.Text(root, width=70, height=15, state=tk.DISABLED)
        self.output_text.pack()

    def simulate_allocation(self):
        try:
            # Parse input
            blocks = list(map(int, self.blocks_entry.get().split(',')))
            processes = list(map(int, self.processes_entry.get().split(',')))

            if not blocks or not processes:
                raise ValueError("Input cannot be empty.")

            allocation = [-1] * len(processes)  # To store the block allocated to each process

            # Display results
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)

            # Worst Fit Allocation logic
            for i in range(len(processes)):

                lagestBlockIndex = 0
                # find largest block
                for j in range(len(blocks)):
                    if blocks[j] > blocks[lagestBlockIndex]:
                        lagestBlockIndex = j

                # allocating processes into blocks
                if blocks[lagestBlockIndex] >= processes[i]:
                    allocation[i] = lagestBlockIndex
                    #reduce the block size by process size to get remaining size of the block
                    blocks[lagestBlockIndex] -= processes[i] 
                else:
                    #when cannot allocate due to process size is huge
                    allocation[i] = -1


            # Final result display
            self.output_text.insert(tk.END, "Final Memory Allocation Results:\n")

            for i in range(len(processes)):
                if allocation[i] != -1:
                    self.output_text.insert(
                        tk.END, f"Process {i+1} ({processes[i]} KB) allocated to Block {allocation[i]+1}\n"
                    )
                else:
                    self.output_text.insert(
                        tk.END, f"Process {i+1} ({processes[i]} KB) could not be allocated\n"
                    )

            self.output_text.insert(tk.END, "\nRemaining Block Sizes:\n")
            for i, size in enumerate(blocks):
                self.output_text.insert(tk.END, f"Block {i+1}: {size} KB\n")

            self.output_text.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid comma-separated integers.")

    def clearAll(self):
        self.blocks_entry.delete(0, tk.END)
        self.processes_entry.delete(0, tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = WorstFitSimulator(root)
    root.mainloop()