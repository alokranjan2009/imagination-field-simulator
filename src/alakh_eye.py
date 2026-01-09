"""
Alakh Eye – Imagination Field Simulator

This program simulates a symbolic perception field using:
- Particle flow
- Central iris
- Energy-dependent fractal overlays

NOTE:
This is a creative visualization, not a medical or neurological tool.
"""

import tkinter as tk
import random
import math
import threading
import time

class AlakhEye:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alakh Eye – Imagination World Viewer")
        self.root.geometry("900x700")
        self.root.configure(bg="black")
        self.running = True
        self.hr_value = 70  # symbolic heart-rate / energy
        self.active_mode = False

        # Canvas
        self.canvas = tk.Canvas(self.root, width=900, height=700, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Heart-rate slider
        self.hr_slider = tk.Scale(self.root, from_=40, to=120, orient="horizontal",
                                  label="Symbolic Energy Level", bg="#111", fg="white", troughcolor="#333")
        self.hr_slider.set(self.hr_value)
        self.hr_slider.place(relx=0.5, rely=0.9, anchor="center")

        # Instruction
        self.instruction = tk.Label(self.root, text="Press SPACE to activate Imagination Scan",
                                    bg="black", fg="white", font=("Arial", 12))
        self.instruction.place(relx=0.5, rely=0.95, anchor="center")

        # Bind keys
        self.root.bind("<space>", self.toggle_active_mode)

        self.particles = []
        threading.Thread(target=self.animate, daemon=True).start()
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        self.root.mainloop()

    def toggle_active_mode(self, event=None):
        self.active_mode = not self.active_mode

    def stop(self):
        self.running = False
        self.root.destroy()

    def animate(self):
        while self.running:
            self.hr_value = self.hr_slider.get()
            self.canvas.delete("all")
            w = self.canvas.winfo_width()
            h = self.canvas.winfo_height()
            cx, cy = w/2, h/2

            # Draw central iris
            self.draw_iris(cx, cy)

            # Draw particles
            num_particles = int(self.hr_value / 3)
            for _ in range(num_particles):
                self.particles.append(self.create_particle(cx, cy, w, h))

            for p in self.particles[:]:
                self.update_particle(p)
                if p['life'] <=0:
                    self.particles.remove(p)

            # Active Imagination Mode
            if self.active_mode:
                self.draw_fractal_overlay(cx, cy)

            self.canvas.update()
            time.sleep(0.03)

    def draw_iris(self, cx, cy):
        radius = 60 + (self.hr_value/120)*40
        for i in range(5):
            glow = radius + i*10
            color = f"#{random.randint(0,255):02x}{random.randint(50,255):02x}{random.randint(150,255):02x}"
            self.canvas.create_oval(cx-glow, cy-glow, cx+glow, cy+glow, outline=color, width=2)

        self.canvas.create_oval(cx-20, cy-20, cx+20, cy+20, fill="#0ff", outline="#0af", width=3)
        self.canvas.create_text(cx, cy, text="🕉", fill="#a0f", font=("Consolas", 24, "bold"))

    def create_particle(self, cx, cy, w, h):
        angle = random.uniform(0, 2*math.pi)
        speed = random.uniform(1,3)
        return {
            'x': cx,
            'y': cy,
            'vx': math.cos(angle)*speed,
            'vy': math.sin(angle)*speed,
            'size': random.randint(2,6),
            'color': f"#{random.randint(150,255):02x}{random.randint(100,255):02x}{random.randint(200,255):02x}",
            'life': random.randint(60,120)
        }

    def update_particle(self, p):
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['life'] -=1
        self.canvas.create_oval(
            p['x']-p['size'], p['y']-p['size'],
            p['x']+p['size'], p['y']+p['size'],
            fill=p['color'], outline=""
        )

    def draw_fractal_overlay(self, cx, cy):
        layers = 12
        max_radius = 300 + (self.hr_value/120)*200
        for i in range(layers):
            angle = time.time()*0.5 + i*0.52
            x = cx + math.cos(angle*1.7+i)*max_radius*0.5
            y = cy + math.sin(angle*1.3+i)*max_radius*0.5
            size = 20 + i*4
            color = f"#{random.randint(180,255):02x}{random.randint(180,255):02x}{random.randint(0,255):02x}"
            self.canvas.create_oval(x-size, y-size, x+size, y+size, outline=color, width=2)

if __name__=="__main__":
    AlakhEye()
