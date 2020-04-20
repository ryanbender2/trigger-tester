from breezypythongui import EasyFrame


class TextAreaDemo(EasyFrame):

    def __init__(self):
        super().__init__('Investment Calculator')
        self.addLabel(text='Initial amount', row=0, column=0)
        self.addLabel(text='Number of years', row=1, column=0)
        self.addLabel(text='Interest rate in %', row=2, column=0)
        self.amount = self.addFloatField(value=0.0, row=0, column=1)
        self.period = self.addIntegerField(value=0, row=1, column=1)
        self.rate = self.addIntegerField(value=0, row=2, column=1)

        self.outputArea = self.addTextArea(' ', row=4, column=0, columnspan=2, width=50, height=15)
        self.compute = self.addButton(text='Compute', row=3, column=0, columnspan=2, command=self.compute)
        self.cb = self.addCheckbutton('something', 7, 0)
        self.addButton('print', 7, 1, command=self.pri)
    
    
    def pri(self):
        print(str(self.cb.isChecked()))

    def compute(self):
        startBalance = self.amount.getNumber()
        rate = self.rate.getNumber() / 100
        years = self.period.getNumber()

        if startBalance == 0 or rate == 0 or years == 0:
            return

        result = '%4s%18s%10s%16s\n' % ('Year', "Starting balance", "Interest", "Ending balance")

        for year in range(1, years + 1):
            totalInterest = 0
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % \
                      (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest

            result += "Ending balance: $%0.2f\n" % endBalance
            result += "Total interest earned: $%0.2f\n" % totalInterest

            self.outputArea["state"] = "normal"
            self.outputArea.setText(result)
            self.outputArea["state"] = "disabled"


def main():
    TextAreaDemo().mainloop()


if __name__ == "__main__":
    main()
