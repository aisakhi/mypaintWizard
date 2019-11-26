# Created by Charlie Cook, Aishwarya Vissom 
# [Insert your name here if you also work on this]
# on Nov. 24th, 2019

#Import tkinter modules
import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox as mbx

#Initialize main tk window
base = tk.Tk()
base.title("MyPaint Configuration Wizard")
base.resizable(False, False)

#Declare a font
fontNormal = tkf.Font(family = "Courier New", size = 12)

#Declare a main frame to contain all wizard pages
frameMain = tk.Frame(base, bd = 3, relief = "raised")
#Pack the main frame
frameMain.pack(padx = 4, pady = 4)

#Delcare subframes a.k.a. pages of the wizard
frameP1 = tk.LabelFrame(frameMain, bd = 0, text = "Page 1")
frameP2 = tk.LabelFrame(frameMain, bd = 0, text = "Page 2")
frameP3 = tk.LabelFrame(frameMain, bd = 0, text = "Page 3")
frameP4 = tk.LabelFrame(frameMain, bd = 0, text = "Page 4")
frameP5 = tk.LabelFrame(frameMain, bd = 0, text = "Page 5")

#Page Change Button Functions
def nextPage(n):
                if n == 1:
                        frameP1.pack_forget()
                        frameP2.pack()
                elif n == 2:
                        frameP2.pack_forget()
                        frameP3.pack()
                elif n == 3:
                        frameP3.pack_forget()
                        updatePage4()
                        frameP4.pack()
                elif n == 4:
                                frameP4.pack_forget()
                                updatePage5()
                                frameP5.pack()

def prevPage(n):
                        if n == 5:
                                frameP5.pack_forget()
                                frameP4.pack()
                        elif n == 4:
                                frameP4.pack_forget()
                                frameP3.pack()
                        elif n == 3:
                                frameP3.pack_forget()
                                frameP2.pack()
                        elif n == 2:
                                frameP2.pack_forget()
                                frameP1.pack()

#Declare next/prev buttons
buttonNext1 = tk.Button(frameP1, text = "Next >", font = fontNormal, command = lambda : nextPage(1), cursor = "hand2")

buttonPrev2 = tk.Button(frameP2, text = "< Previous", font = fontNormal, command = lambda : prevPage(2), cursor = "hand2")
buttonNext2 = tk.Button(frameP2, text = "Next >", font = fontNormal, command = lambda : nextPage(2), cursor = "hand2")
buttonPrev3 = tk.Button(frameP3, text = "< Previous", font = fontNormal, command = lambda : prevPage(3), cursor = "hand2")
buttonNext3 = tk.Button(frameP3, text = "Next >", font = fontNormal, command = lambda : nextPage(3), cursor = "hand2")
buttonPrev4 = tk.Button(frameP4, text = "< Previous", font = fontNormal, command = lambda : prevPage(4), cursor = "hand2")
buttonNext4 = tk.Button(frameP4, text = "Next >", font = fontNormal, command = lambda : nextPage(4), cursor = "hand2")
buttonPrev5 = tk.Button(frameP5, text = "< Previous", font = fontNormal, command = lambda : prevPage(5), cursor = "hand2")

#Grid-arrage the buttons
buttonNext1.grid(row = 12, column = 2)
buttonPrev2.grid(row = 12, column = 1)
buttonNext2.grid(row = 12, column = 2)
buttonPrev3.grid(row = 12, column = 1)
buttonNext3.grid(row = 12, column = 2)
buttonPrev4.grid(row = 12, column = 1)
buttonNext4.grid(row = 12, column = 2)
buttonPrev5.grid(row = 12, column = 1)

#Decorate page 1
imageWizard = tk.PhotoImage(file = "secretlondon_Wizard_s_Hat.png")
imagePaint = tk.PhotoImage(file = "johnny_automatic_paint_can_and_brush.png")
labelWizard = tk.Label(frameP1, image = imageWizard)
labelPaint = tk.Label(frameP1, image = imagePaint)
labelWizard.grid(row = 1, column = 1)
labelPaint.grid(row = 1, column = 2)

labelGreeting = tk.Label(frameP1, text = "Hello there! This wizard will assist you in setting up all the various widgets, menus, and tools MyPaint has to offer. There are three sections that you will see shortly: Brushes, Colors, and Tool Settings. Click \"Next >\" to proceed to the Brushes page.", font = fontNormal, wraplength = 640, justify = tk.LEFT)
labelGreeting.grid(row = 2, column = 1, columnspan = 2)

#Pack page 1
frameP1.pack()

#Decorate page 2
labelBrush = tk.Label(frameP2, font = fontNormal, wraplength = 640, justify = tk.LEFT, text = "Choose any of the following brush groups that you want shown persistently on the side docks; Instructions for each will be provided at the conclusion of this wizard:")
page2Vars = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]
checkClassic = tk.Checkbutton(frameP2, font = fontNormal, anchor = tk.W, variable = page2Vars[0], text = "Classic (Default brush group)")
checkExperimental = tk.Checkbutton(frameP2, font = fontNormal, anchor = tk.W, variable = page2Vars[1], text = "Experimental (Esoteric brush group)")
checkSet1 = tk.Checkbutton(frameP2, font = fontNormal, anchor = tk.W, variable = page2Vars[2], text = "Set #1 (Icons show example brush strokes)")
checkSet2 = tk.Checkbutton(frameP2, font = fontNormal, anchor = tk.W, variable = page2Vars[3], text = "Set #2 (Icons show real world brushes and pens)")
checkSet3 = tk.Checkbutton(frameP2, font = fontNormal, anchor = tk.W, variable = page2Vars[4], text = "Set #3 (Features acrylics, oils, and charcoals)")
checkSet4 = tk.Checkbutton(frameP2, font = fontNormal, anchor = tk.W, variable = page2Vars[5], text = "Set #4 (Features digital-style brushes)")
checkBrushSliders = tk.Checkbutton(frameP2, font =fontNormal, anchor = tk.NW, justify = tk.LEFT, wraplength = 600, variable = page2Vars[6], text = "Universal Brush Settings Sliders (controls brush size, opacity, and other features)")

labelBrush.grid(row = 1, column = 1, columnspan = 2)
checkClassic.grid(row = 2, column = 1, columnspan = 2, sticky = tk.W)
checkExperimental.grid(row = 3, column = 1, columnspan = 2, sticky = tk.W)
checkSet1.grid(row = 4, column = 1, columnspan = 2, sticky = tk.W)
checkSet2.grid(row = 5, column = 1, columnspan = 2, sticky = tk.W)
checkSet3.grid(row = 6, column = 1, columnspan = 2, sticky = tk.W)
checkSet4.grid(row = 7, column = 1, columnspan = 2, sticky = tk.W)
checkBrushSliders.grid(row = 8, column = 1, columnspan = 2, sticky = tk.W)

#Decorate page 3

labelColor = tk.Label(frameP3, font = fontNormal, wraplength = 640, justify = tk.LEFT, text = "Choose any of the following options that you want shown persistently on the side docks; Instructions for each will be provided at the conclusion of this wizard:")
page3Vars = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]
ChangeColor1 = tk.Checkbutton(frameP3, font = fontNormal, anchor = tk.W, variable = page3Vars[0], text = " Change from HSY wheel")
ChangeColor2 = tk.Checkbutton(frameP3, font = fontNormal, anchor = tk.W, variable = page3Vars[1], text = "Change from palette")
OptionSet1 = tk.Checkbutton(frameP3, font = fontNormal, anchor = tk.W, variable = page3Vars[2], text = "Set #1 (HSY wheel)")
OptionSet2 = tk.Checkbutton(frameP3, font = fontNormal, anchor = tk.W, variable = page3Vars[3], text = "Set #2 (HSV wheel)")
OptionSet3 = tk.Checkbutton(frameP3, font = fontNormal, anchor = tk.W, variable = page3Vars[4], text = "Set #3 (color palette)")
OptionSet4 = tk.Checkbutton(frameP3, font = fontNormal, anchor = tk.W, variable = page3Vars[5], text = "Set #4 (HSV cube)")
OptionSet5 = tk.Checkbutton(frameP3, font = fontNormal,anchor = tk.W, variable=page3Vars[6], text =" Set #5 (ADD COLOR to palette)")

checkColorSliders = tk.Label(frameP3, text = " The 'Add color'  option helps to add the extra shade from a color wheel or cube to the palette:")

labelColor.grid(row = 1, column = 1, columnspan = 2)
ChangeColor1.grid(row = 2, column = 1, columnspan = 2, sticky = tk.W)
ChangeColor2.grid(row = 3, column = 1, columnspan = 2, sticky = tk.W)
OptionSet1.grid(row = 4, column = 1, columnspan = 2, sticky = tk.W)
OptionSet2.grid(row = 5, column = 1, columnspan = 2, sticky = tk.W)
OptionSet3.grid(row = 6, column = 1, columnspan = 2, sticky = tk.W)
OptionSet4.grid(row = 7, column = 1, columnspan = 2, sticky = tk.W)
OptionSet5.grid(row = 8, column = 1, columnspan = 2, sticky = tk.W)
checkColorSliders.grid(row = 9, column = 1, columnspan = 2, sticky = tk.W)


#Decorate page 4
resultString = tk.StringVar()
def updatePage4():
	page2Strings = [ \
		"Classic Brushes: Click the \"Brush\" menu, then \"Brush Groups >\", then \"Classic\". Drag it to anywhere on either dock if you wish.\n", \
		"Experimental Brushes: Click the \"Brush\" menu, then \"Brush Groups >\", then \"Experimental\". Drag it to anywhere on either dock if you wish.\n", \
		"Brushes Set #1: Click the \"Brush\" menu, then \"Brush Groups >\", then \"Set#1\". Drag it to anywhere on either dock if you wish.\n", \
		"Brushes Set #2: Click the \"Brush\" menu, then \"Brush Groups >\", then \"Set#2\". Drag it to anywhere on either dock if you wish.\n", \
		"Brushes Set #3: Click the \"Brush\" menu, then \"Brush Groups >\", then \"Set#3\". Drag it to anywhere on either dock if you wish.\n", \
		"Brushes Set #4: Click the \"Brush\" menu, then \"Brush Groups >\", then \"Set#4\". Drag it to anywhere on either dock if you wish.\n", \
		"Brush Settings Sliders: Click the \"Window\" menu, then \"Tool Options Panel\". Drag it to anywhere on either dock if you wish.\n", \
	]

	resultString.set("")

	
	for v in page2Vars:
		if v.get() == 1:
			resultString.set(resultString.get() + page2Strings[page2Vars.index(v)] + '\n')
			
labelResultsHead = tk.Label(frameP4, font = fontNormal, justify = tk.LEFT, text = "Items to set up:")
labelResultsHead.grid(row = 1, column = 1, sticky = tk.W)
labelResults = tk.Label(frameP4, font = fontNormal, justify = tk.LEFT, wraplength = 640, textvariable = resultString)
labelResults.grid(row = 2, column = 1, columnspan = 2, sticky = tk.W)



#Decorate page 5
results = tk.StringVar()
def updatePage5():
        
        page3Strings = [ \
                "Change from HSV wheel: Click on the \"Color\" menu, then \"click on Change from HSV wheel >\", Then you can choose the any color from the HSV wheel.\n", \
		"Change from palette: Click on the \"Color\" menu, then \"click change from palette>\", Then you can choose from the available colors.\n" , \
                "select HSY: Click on the \"Color\" menu, then \"click on HSY WHEEL>\", You can select the shades of colors from HSY wheel.Drag it to anywhere on either dock if you wish\n", \
                "select HSV: Click on the \"Color\" menu, then \"click on HSV WHEEL>\", You can select the shades of colors from HSV wheel. Drag it to anywhere on either dock if you wish\n", \
                "select COLOR PALETTE: Click on the \"Color\" menu, then \"click on COLOR PALETTE>\", You can select the colors present in the palette. Drag it to anywhere on either dock if you wish\n", \
                "select HSV WHEEL: Click on the \"Color\" menu, then \"click on HSV WHEEL>\", You can select the shades of colors from HSV wheel.Drag it to anywhere on either dock if you wish \n" , \
                " ADD COLOR: Click on the \"Color\" menu, then \"ADD COLOR TO PALETTE>\", You can select any color from one of the color wheels and add it to the palette with this option.Drag it to anywhere on either dock if you wish\n" , \
        ]
        results.set("")

        for n in page3Vars:
                if n.get() == 1:
                        results.set(results.get() + page3Strings[page3Vars.index(n)] + '\n')
	
labelResHead = tk.Label(frameP5, font = fontNormal, justify = tk.LEFT, text = "Items to set up:")
labelResHead.grid(row = 1, column = 1, sticky = tk.W)
labelRes = tk.Label(frameP5, font = fontNormal, justify = tk.LEFT, wraplength = 640, textvariable = results)
labelRes.grid(row = 2, column = 1, columnspan = 2, sticky = tk.W)

#Start the main window
base.mainloop()
