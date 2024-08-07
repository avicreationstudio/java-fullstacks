import tkinter as tk
from custom_gui.gui_config import WidgetConfig
from custom_gui.gui_dialogBox import Dialog
from logic import Logic
# # ---------------------------------
# #      BASIC THINGS TO UPDATE
# # ---------------------------------
WINDOW_TITLE = "To-Do List App"
DB_NAME = "todo_list.db"
TABLE_NAME = "task"

## INITIAL CODE to create table
Logic.createTable(DB_NAME, TABLE_NAME)

# # ---------------------------------
# #       YOUR LOGIC
# # ---------------------------------
def add_item():
    task = entry_widget.get()
    if task:
        Logic.insertTable(DB_NAME,TABLE_NAME,"name",task)
        entry_widget.delete(0, tk.END)
        print('added')
        update_list_widget()
    else:
        Dialog.show_warning("You must enter a task.")

def remove_item():
    try:
        task_id = listbox_widget.get(listbox_widget.curselection())[0]
        Logic.deleteTable(DB_NAME,TABLE_NAME,task_id)
        update_list_widget()
    except:
        Dialog.show_warning("You must select a task to remove.")

def update_list_widget():
    listbox_widget.delete(0, tk.END)
    table = Logic.selectTable(DB_NAME,TABLE_NAME)
    for row in table:
        listbox_widget.insert(tk.END, row)

# # ---------------------------------
mainWidget = tk.Tk()
mainWidget.title(WINDOW_TITLE)
# Configure the main window
mainWidget.configure(WidgetConfig.Main.config)

# Create and configure the label
label_widget = tk.Label(mainWidget)
label_widget.pack(**WidgetConfig.Common.padding)
label_widget.configure(WidgetConfig.Label.config, text='Please enter your task in below input box'.upper())

# Create and configure the entry widget
entry_widget = tk.Entry(mainWidget)
entry_widget.pack(**WidgetConfig.Common.padding)
entry_widget.configure(WidgetConfig.Entry.config)

# Create and configure the button
add_btn_widget = tk.Button(mainWidget)
add_btn_widget.pack(**WidgetConfig.Common.padding)
add_btn_widget.configure(WidgetConfig.Button.config, text="ADD ITEM", command=add_item)

# Create and configure the listbox
listbox_widget = tk.Listbox(mainWidget)
listbox_widget.pack(**WidgetConfig.Common.padding)
listbox_widget.configure(WidgetConfig.ListBox.config)

# Create and configure the button
remove_btn_widget = tk.Button(mainWidget)
remove_btn_widget.pack(**WidgetConfig.Common.padding)
remove_btn_widget.configure(WidgetConfig.Button.config, text="REMOVE ITEM", command=remove_item)

# display if any data is present inside the table
update_list_widget()

mainWidget.mainloop()
