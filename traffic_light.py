import tkinter as tk


class TrafficLight(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Signal Simulation")
        self.geometry("600x600")

        # Create canvas to draw lights, roads, and cars
        self.canvas = tk.Canvas(self, width=600, height=600, bg='grey')
        self.canvas.pack()

        # Draw roads
        self.canvas.create_rectangle(200, 0, 400, 600, fill='darkgrey')  # Vertical road
        self.canvas.create_rectangle(0, 200, 600, 400, fill='darkgrey')  # Horizontal road

        # Draw lane markers
        self.canvas.create_line(300, 0, 300, 200, fill='white', dash=(5, 2))
        self.canvas.create_line(300, 400, 300, 600, fill='white', dash=(5, 2))
        self.canvas.create_line(0, 300, 200, 300, fill='white', dash=(5, 2))
        self.canvas.create_line(400, 300, 600, 300, fill='white', dash=(5, 2))

                # Draw stop lines as per yellow lines in the image
        self.canvas.create_line(200, 200, 300, 200, fill='yellow')
        self.canvas.create_line(200, 200, 400, 200, fill='yellow')
        self.canvas.create_line(000, 000, 000, 000, fill='yellow')
        self.canvas.create_line(200, 200, 400, 200, fill='yellow')
        self.canvas.create_line(400, 400, 400, 400, fill='yellow')
        self.canvas.create_line(000, 000, 000, 000, fill='yellow')
        self.canvas.create_line(000, 000, 000, 000, fill='yellow')
        self.canvas.create_line(200, 400, 400, 400, fill='yellow')

        # Draw red, yellow, and green lights for vertical traffic
        self.red_light_v = self.canvas.create_oval(500, 250, 550, 300, fill='grey')
        self.yellow_light_v = self.canvas.create_oval(500, 200, 550, 250, fill='grey')
        self.green_light_v = self.canvas.create_oval(500, 150, 550, 200, fill='grey')

        # Draw red, yellow, and green lights for horizontal traffic
        self.red_light_h = self.canvas.create_oval(250, 100, 300, 150, fill='grey')
        self.yellow_light_h = self.canvas.create_oval(200, 100, 250, 150, fill='grey')
        self.green_light_h = self.canvas.create_oval(150, 100, 200, 150, fill='grey')

        # Draw cars
        self.cars = [
            self.canvas.create_rectangle(550, 350, 600, 400, fill='blue'),  # Horizontal car
            self.canvas.create_rectangle(350, 550, 400, 600, fill='red'),  # Vertical car
        ]

        self.current_light = 'horizontal_green'

        # Define signal timings
        self.horizontal_green_time = 6000
        self.horizontal_yellow_time = 2000
        self.vertical_green_time = 6000
        self.vertical_yellow_time = 2000

        self.light_cycle()
        self.move_cars()

    def light_cycle(self):
        if self.current_light == 'horizontal_green':
            self.canvas.itemconfig(self.red_light_v, fill='red')
            self.canvas.itemconfig(self.yellow_light_v, fill='grey')
            self.canvas.itemconfig(self.green_light_v, fill='grey')
            self.canvas.itemconfig(self.red_light_h, fill='grey')
            self.canvas.itemconfig(self.yellow_light_h, fill='grey')
            self.canvas.itemconfig(self.green_light_h, fill='green')
            self.current_light = 'horizontal_yellow'
            self.after(self.horizontal_green_time, self.light_cycle)
        elif self.current_light == 'horizontal_yellow':
            self.canvas.itemconfig(self.yellow_light_h, fill='yellow')
            self.canvas.itemconfig(self.green_light_h, fill='grey')
            self.current_light = 'vertical_green'
            self.after(self.horizontal_yellow_time, self.light_cycle)
        elif self.current_light == 'vertical_green':
            self.canvas.itemconfig(self.red_light_h, fill='red')
            self.canvas.itemconfig(self.yellow_light_h, fill='grey')
            self.canvas.itemconfig(self.green_light_h, fill='grey')
            self.canvas.itemconfig(self.red_light_v, fill='grey')
            self.canvas.itemconfig(self.yellow_light_v, fill='grey')
            self.canvas.itemconfig(self.green_light_v, fill='green')
            self.current_light = 'vertical_yellow'
            self.after(self.vertical_green_time, self.light_cycle)
        elif self.current_light == 'vertical_yellow':
            self.canvas.itemconfig(self.yellow_light_v, fill='yellow')
            self.canvas.itemconfig(self.green_light_v, fill='grey')
            self.current_light = 'horizontal_green'
            self.after(self.vertical_yellow_time, self.light_cycle)

    def move_cars(self):
        car_speed = 50
        stop_line_v = 1000# Vertical stop line
        stop_line_h = 200  # Horizontal stop line

        # Move vertical car
        car1_coords = self.canvas.coords(self.cars[1])
        if self.current_light in ['vertical_green', 'vertical_yellow'] or car1_coords[1] > stop_line_v:
            self.canvas.move(self.cars[1], 0, -car_speed)
        if self.current_light == 'horizontal_green' and car1_coords[1] <= stop_line_v:
            self.canvas.move(self.cars[1], 0, 0)
        if car1_coords[1] < 0:
            self.canvas.coords(self.cars[1], 350, 550, 400, 600)

        # Move horizontal car
        car2_coords = self.canvas.coords(self.cars[0])
        if self.current_light in ['horizontal_green', 'horizontal_yellow'] or car2_coords[0] > stop_line_h:
            self.canvas.move(self.cars[0], -car_speed, 0)
        if self.current_light == 'vertical_green' and car2_coords[0] <= stop_line_h:
            self.canvas.move(self.cars[0], 0, 0)
        if car2_coords[0] < 0:
            self.canvas.coords(self.cars[0], 550, 350, 600, 400)

        self.after(50, self.move_cars)


if __name__ == "__main__":
    app = TrafficLight()
    app.mainloop()
