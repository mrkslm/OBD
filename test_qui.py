# import PySimpleGUI as Sg
#
# # By using short-hand aliases, you can save even more space in your code by using fewer characters. All of the
# # Elements have one or more shorter names that can be used. For example, the Text element can be written simply as T.
# # The Input element can be written as I and the Button as B. Your single-line window code thus becomes:
#
# # event, values = sg.Window('Window Title', [[sg.T("What's your name?")], [sg.I()], [sg.B('Ok')]]).read(close=True)
# import PySimpleGUI as sg
#
# choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')
#
# layout = [  [sg.Text('What is your favorite color?')],
#             [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
#             [sg.Button('Ok')]  ]
#
# window = sg.Window('Pick a color', layout)
#
# while True:                  # the event loop
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     if event == 'Ok':
#         if values['-COLOR-']:    # if something is highlighted in the list
#             sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
# window.close()
