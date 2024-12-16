import tkinter as tk
import ctypes


def block_mouse_interactions(window_id):
    """
    Set the window to intercept mouse clicks and stay as an active overlay.
    """
    hwnd = ctypes.windll.user32.GetParent(window_id)

    # Modify the window style to make it transparent but still block mouse clicks
    ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
    ex_style |= 0x80000  # WS_EX_LAYERED
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, ex_style)

    # Set transparency (0x1 = color key transparency mode)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x1)


# Create a fullscreen transparent Tkinter window
root = tk.Tk()
root.title("Transparent Barrier")

# Make the window fullscreen and always on top
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)

# Set a transparent background
root.attributes('-alpha', 0.3)  # Adjust alpha for a "glass" effect

# Disable user interaction with widgets in this window
root.overrideredirect(True)  # Remove title bar and borders

# Make the Tkinter window intercept mouse interactions
root_id = root.winfo_id()
block_mouse_interactions(root_id)

# Start the Tkinter event loop
root.mainloop()
