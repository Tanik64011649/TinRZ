from tkinter import*
import tkinter.messagebox

class Interest:

    def __init__(self, root):
        self.root = root
        self.root.title("Interest Rate Calculator")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='Gray')
        """========================================================================Frame=================================================================================="""

        MainFrame = Frame(self.root, bd=20, width=1350, height=700, padx=10, pady=10, bg="medium purple", relief=RIDGE)
        MainFrame.grid()

        LeftFrame = Frame(MainFrame, bd=10, width=600, height=600, padx=10, pady=42, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=10, width=560, height=600, padx=10, pady=10, relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        """========================================================================Frame=================================================================================="""

        LeftFrame0 = Frame(LeftFrame, bd=5, width=712, height=143, padx=5, bg="medium purple", relief=RIDGE)
        LeftFrame0.grid(row=0, column=0)

        LeftFrame1 = Frame(LeftFrame, bd=5, width=712, height=170, padx=5, pady=12, relief=RIDGE)
        LeftFrame1.grid(row=4, column=0)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=712, height=168, padx=5, pady=13, relief=RIDGE)
        LeftFrame2.grid(row=2, column=0)

        RightFrame1 = Frame(RightFrame, bd=5, width= 522, height=280, padx=5, pady=19, relief=RIDGE)
        RightFrame1.grid(row=1, column=0)

        """==============================================================================================================================================================="""

        var1 = StringVar()
        var2 = StringVar()

        """=======================================================================Functions==============================================================================="""

        rate_list = []
        with open("Rate.txt", "r") as file:
            for line in file:
                rate_list.append(line[7:])
        rate1 = int(rate_list[0])
        rate2 = int(rate_list[1])

        
        
        def Reset():
            var1.set("")
            var2.set("")
            self.txtRateTable.delete("1.0", END)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Interest Rate", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def balance(initBalance, rate, NumYears):
            finalBalance = initBalance * ((1 + rate/100) ** NumYears)
            return finalBalance

        def table():
            self.txtRateTable.delete("1.0", END)
            initBalance = float(var1.get())
            NumYears = int(var2.get())

            if 0 < initBalance <= 100000:
                rate = rate1
                b = balance(initBalance, rate, NumYears)
                print("Rate: %2d%%, Balance: %.2f baht " % (rate, b))
                iRate = str(rate)
                iB = str(b)
                self.txtRateTable.insert(END, "\nRate: " + (iRate) + " % " + "Balance: " + ('%.2f baht' % float(iB)) + " \n\nRecommended Bank: SCB, KrungThai, KrungSri, Kbank")
            else:
                rate = rate2
                b = balance(initBalance, rate, NumYears)
                print("Rate: %2d%%, Balance: %.2f baht " % (rate, b))
                iRate = str(rate)
                iB = str(b)
                self.txtRateTable.insert(END, "\nRate: " + (iRate) + " % " + "Balance: " + ('%.2f baht' % float(iB)) + " \n\nRecommended Bank: SCB, KrungThai, LHBank")
            
            


        
        
        """====================================================================Entry and Label============================================================================"""

        self.lblTitle = Label(LeftFrame0, text="Interest Rate Calculator", padx=17, pady=4, bd=1, font=('Times New Roman', 40, 'bold'), bg="medium purple", width=20)
        self.lblTitle.pack()

        self.lblBalance = Label(LeftFrame2, text="Please enter the initial balance:", font=('Times New Roman', 20, 'bold'), bd=2, justify=LEFT)
        self.lblBalance.grid(row=0, column=0, padx=15)
        self.txtBalance = Entry(LeftFrame2, textvariable=var1, font=('Times New Roman', 20, 'bold'), bd=5, width=14, justify=RIGHT)
        self.txtBalance.grid(row=0, column=1, padx=3, pady=10)

        self.lblYear = Label(LeftFrame2, text="Please enter the Number of years:", font=('Times New Roman', 20, 'bold'), bd=2, justify=LEFT)
        self.lblYear.grid(row=1, column=0, padx=15)
        self.txtYear = Entry(LeftFrame2, textvariable=var2, font=('Times New Roman', 20, 'bold'), bd=5, width=14, justify=RIGHT)
        self.txtYear.grid(row=1, column=1, padx=3, pady=10)

        """==============================================================================================================================================================="""

        self.lblRateTable = Label(RightFrame1, font=('Times New Roman', 20, 'bold'), text="\t PayBack").grid(row=0, column=0)
        self.txtRateTable = Text(RightFrame1, height=15, width=52, bd=16, font=('Times New Roman', 12, 'bold'))
        self.txtRateTable.grid(row=1, column=0, columnspan=3)

        """==============================================================================================================================================================="""

        self.btnRate = Button(LeftFrame1, text="Interest Rate", padx=5, pady=2, bd=4, width=12, font=('Times New Roman', 20, 'bold'), height=1, bg="medium purple", command=table)
        self.btnRate.grid(row=3, column=0)

        self.btnReset = Button(LeftFrame1, padx=5, pady=2, bd=4, fg="black", width=12, font=('Times New Roman', 20, 'bold'), 
        height=1, text="Reset", bg="medium purple", command=Reset).grid(row=3, column=1)

        self.btnExit = Button(LeftFrame1, padx=5, pady=2, bd=4, fg="black", width=12, font=('Times New Roman', 20, 'bold'), 
        height=1, text="Exit", bg="medium purple", command=iExit).grid(row=3, column=2)





if __name__ == "__main__":
    root = Tk()
    application = Interest(root)
    root.mainloop()




