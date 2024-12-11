# import textx files
from textx import metamodel_from_file
nono_mm = metamodel_from_file('nnl.tx')

# tkinter for graphics
import tkinter as tk

'''
COMMANDS:
'''

# creates filled out visualization
def visualize(design):
    # design into array
    pattern_str = "\n".join(design.patterns)
    lines = pattern_str.strip().split('\n')
    array_2d = [line.split() for line in lines]

    # TKINTER:
    root = tk.Tk()
    root.title("NONOGRAM (VISUALIZATION)")

    rows = len(array_2d)
    cols = len(array_2d[0])

    # create and place labels in the grid
    for i in range(rows):
        for j in range(cols):
            label = tk.Label(root, text=array_2d[i][j], borderwidth=1, relief="solid", width=4, height=2)
            label.grid(row=i, column=j, padx=1, pady=1)

    root.mainloop()

# generate blank puzzle
def puzzle(design):
    # design into array
    pattern_str = "\n".join(design.patterns)
    lines = pattern_str.strip().split('\n')
    array_2d = [line.split() for line in lines]

    # get row clues
    row_clues = generate_clues(array_2d)
    
    # transpose array to get col clues
    transposed_array = list(map(list, zip (*array_2d)))
    col_clues = generate_clues(transposed_array)

    # TKINTER
    # initialize the main window
    root = tk.Tk()
    root.title("NONOGRAM PUZZLE")

    # nonogram puzzle size
    rows = len(row_clues)
    cols = len(col_clues)

    # create the main frame
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    # display row clues
    for i, clues in enumerate(row_clues):
        label = tk.Label(frame, text=' '.join(map(str, clues)), width=4, height=2, borderwidth=1, relief="solid")
        label.grid(row=i+1, column=0, padx=1, pady=1)

    # display column clues
    for j, clues in enumerate(col_clues):
        label = tk.Label(frame, text=' '.join(map(str, clues)), width=4, height=2, borderwidth=1, relief="solid")
        label.grid(row=0, column=j+1, padx=1, pady=1)

    # create the grid cells
    grid_buttons = []
    for i in range(rows):
        row_buttons = []
        for j in range(cols):
            button = tk.Button(frame, width=4, height=2, borderwidth=1, relief="solid", command=lambda i=i, j=j: toggle_cell(i, j))
            button.grid(row=i+1, column=j+1, padx=1, pady=1)
            row_buttons.append(button)
        grid_buttons.append(row_buttons)

    # function to toggle cell state
    def toggle_cell(i, j):
        button = grid_buttons[i][j]
        if button.config('bg')[-1] == 'black':
            button.config(bg='white')
        else:
            button.config(bg='black')

    # run the main loop
    root.mainloop()

# creates clues
def create_clue(design):
    # print the pattern the user defined
    for p in design.patterns:
        print(p)
    print("\n----------------")
    
    # design into array
    pattern_str = "\n".join(design.patterns)
    lines = pattern_str.strip().split('\n')
    array_2d = [line.split() for line in lines]
    
    # get row clues
    row_clues = generate_clues(array_2d)

    # transpose array to get col clues
    transposed_array = list(map(list, zip (*array_2d)))
    col_clues = generate_clues(transposed_array)

    # prints clues for user
    print("ROW CLUES: ")
    for i, counts in enumerate(row_clues):
        print(f"ROW {i+1} has clues 'X's: {counts}")
    
    print("\nCOLUMN CLUES: ")
    for i, counts in enumerate(col_clues):
        print(f"COLUMN {i+1} has clues 'X's: {counts}")

'''
CLUE FUNCTIONS:
'''
# generates the clues
def generate_clues(array):
    # all clues stored in a list
    clues = []
    for row in array:
        # keeps count of consecutive
        current_consecutive = 0
        # keeps count of consecutives for a row
        consecutive_counts = []
        for element in row:
            if element == "X":
                current_consecutive+= 1
            else:
                if current_consecutive > 0:
                    consecutive_counts.append(current_consecutive)
                    current_consecutive = 0 #reset to 0 once element isn't X
        # adds row consecutives to list
        if current_consecutive > 0:
            consecutive_counts.append(current_consecutive)
        clues.append(consecutive_counts) # adds for entire nonogram
    return clues

class NonoLang:
    # initialize grid to 0x0
    def __init__(self):
        self.row = 0
        self.col = 0
    
    # print what the grid is
    def __str__(self):
        return f"GRID IS {self.row} x {self.col}."
    
    # interpret
    def interpret(self, model):
        # initialize grid
        self.row = model.row
        self.col = model.col
        print(self)
        # parse through pattern and create clue
        for c in model.clues:
            create_clue(c.design)
        # parse through pattern and generate visualization
        for c in model.generate:
            visualize(c.design)
        # parse through and create puzzle
        for c in model.blank:
            puzzle(c.design)

# PROGRAM 1
print("\nPROGRAM #1:")
nono = NonoLang()
nono_model = nono_mm.model_from_file('program.nnl')
nono.interpret(nono_model)
print("----------------")

# PROGRAM 2
print("\nPROGRAM #2:")
nono2 = NonoLang()
nono_model2 = nono_mm.model_from_file('program2.nnl')
nono2.interpret(nono_model2)
print("----------------")

# PROGRAM 3
print("\nPROGRAM #3:")
nono3 = NonoLang()
nono_model3 = nono_mm.model_from_file('program3.nnl')
nono3.interpret(nono_model3)
print("----------------")

# PROGRAM 4
print("\nPROGRAM #4:")
nono3 = NonoLang()
nono_model3 = nono_mm.model_from_file('program4.nnl')
nono3.interpret(nono_model3)
print("----------------")
