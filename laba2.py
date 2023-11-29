import tkinter as tk


def calculate():
    w = ew.get().replace(" ", "")
    s = int(em.get())

    t1 = ''.join(w[i] for i in range(1, len(w), 2))
    t2 = ''.join(w[i] for i in range(1, len(w), 3))
    t3 = ''.join(w[i] for i in range(2, len(w), 4))
    t4 = ''.join(w[i] for i in range(3, len(w), 5))

    if s == 1:
        rl.config(text="Через одну букву: " + t1)
    elif s == 2:
        rl.config(text="Через дві букви: " + t2)
    elif s == 3:
        rl.config(text="Через три букви: " + t3)
    else:
        rl.config(text="Через чотири букви: " + t4)


r = tk.Tk()
r.title("Чистокол")

wl = tk.Label(r, text="Введіть слово:")
wl.grid(row=0, column=0, sticky="w")

ew = tk.Entry(r)
ew.grid(row=0, column=1)

nl = tk.Label(r, text="Введіть число через скільки буде братися буква:")
nl.grid(row=1, column=0, sticky="w")

em = tk.Entry(r)
em.grid(row=1, column=1)

cb = tk.Button(r, text="Результат!", command=calculate)
cb.grid(row=2, column=0, columnspan=2, pady=10)

rl = tk.Label(r, text="")
rl.grid(row=3, column=0, columnspan=2)

r.mainloop()