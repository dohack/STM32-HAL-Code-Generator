import tkinter as tk
from tkinter import ttk

class STM32CodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("STM32 Device Driver Generator")  # Updated title

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12))  # Customize label font
        self.style.configure('TEntry', font=('Arial', 12))  # Customize entry font
        self.style.configure('TButton', font=('Arial', 12))  # Customize button font

        self.checklist_frame = ttk.Frame(self.root)
        self.checklist_frame.pack(padx=20, pady=20)

        self.checklist = ttk.Checkbutton(self.checklist_frame, text="LED", variable=tk.BooleanVar())
        self.checklist.grid(row=0, sticky=tk.W, padx=10, pady=5)

        self.delay_label = ttk.Label(self.checklist_frame, text="Delay (ms):")
        self.delay_label.grid(row=1, sticky=tk.W, padx=10, pady=5)
        self.delay_entry = ttk.Entry(self.checklist_frame)
        self.delay_entry.grid(row=1, column=1, padx=10, pady=5)

        self.port_label = ttk.Label(self.checklist_frame, text="Port:")
        self.port_label.grid(row=2, sticky=tk.W, padx=10, pady=5)
        self.port_entry = ttk.Entry(self.checklist_frame)
        self.port_entry.grid(row=2, column=1, padx=10, pady=5)

        self.pin_label = ttk.Label(self.checklist_frame, text="Pin:")
        self.pin_label.grid(row=3, sticky=tk.W, padx=10, pady=5)
        self.pin_entry = ttk.Entry(self.checklist_frame)
        self.pin_entry.grid(row=3, column=1, padx=10, pady=5)

        self.generate_button = ttk.Button(self.root, text="Generate Code", command=self.generate_code)
        self.generate_button.pack(pady=10)

    def generate_code(self):
        led_selected = self.checklist.instate(['selected'])
        delay = self.delay_entry.get()
        port = self.port_entry.get()
        pin = self.pin_entry.get()

        code = ""

        if led_selected:
            code += f"// LED Initialization\n"
            code += f"HAL_GPIO_WritePin(GPIO{port.upper()}, GPIO_PIN_{pin}, GPIO_PIN_RESET);\n"
            code += f"HAL_Delay({delay});\n"
            code += f"HAL_GPIO_WritePin(GPIO{port.upper()}, GPIO_PIN_{pin}, GPIO_PIN_SET);\n"
            code += f"HAL_Delay({delay});\n\n"

        # Add code for other peripherals here...

        print(code)

if __name__ == "__main__":
    root = tk.Tk()
    app = STM32CodeGenerator(root)
    root.mainloop()
