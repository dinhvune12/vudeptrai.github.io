import tkinter as tk

def calculate(event=None):  # Enter để tính
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result_var.set(str(a + b))
    except ValueError:
        result_var.set("Lỗi: nhập số hợp lệ!")

def clear(event=None):  # Esc để xóa
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_var.set("")

# Cửa sổ chính
root = tk.Tk()
root.title("Máy Tính Cộng 2 Số")

# Ô nhập A
tk.Label(root, text="A", font=("Arial", 12)).grid(row=0, column=0, padx=8, pady=8)
entry_a = tk.Entry(root, width=12, font=("Arial", 16), justify="right")
entry_a.grid(row=0, column=1, padx=8, pady=8)

# Ô nhập B
tk.Label(root, text="B", font=("Arial", 12)).grid(row=1, column=0, padx=8, pady=8)
entry_b = tk.Entry(root, width=12, font=("Arial", 16), justify="right")
entry_b.grid(row=1, column=1, padx=8, pady=8)

# Nút tính
btn_eq = tk.Button(root, text="=", width=10, height=2, command=calculate)
btn_eq.grid(row=2, column=0, padx=8, pady=8)

# Nút xóa
btn_clear = tk.Button(root, text="C", width=10, height=2, command=clear)
btn_clear.grid(row=2, column=1, padx=8, pady=8)

# Kết quả
tk.Label(root, text="Kết quả", font=("Arial", 12)).grid(row=3, column=0, padx=8, pady=8)
result_var = tk.StringVar()
entry_result = tk.Entry(root, textvariable=result_var, width=20, font=("Arial", 16),
                        justify="right", state="readonly", readonlybackground="white")
entry_result.grid(row=3, column=1, padx=8, pady=8)

# Phím tắt
root.bind("<Return>", calculate)
root.bind("<Escape>", clear)

# Focus mặc định vào A
entry_a.focus()

root.mainloop()
