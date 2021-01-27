import PySimpleGUI as Sg

# By using short-hand aliases, you can save even more space in your code by using fewer characters. All of the
# Elements have one or more shorter names that can be used. For example, the Text element can be written simply as T.
# The Input element can be written as I and the Button as B. Your single-line window code thus becomes:

# event, values = sg.Window('Window Title', [[sg.T("What's your name?")], [sg.I()], [sg.B('Ok')]]).read(close=True)


import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()