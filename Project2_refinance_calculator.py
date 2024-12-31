from tkinter import *

class RefiEval:
    def __init__(self):
        self.window = Tk()
        self.window.title("Refinance Evaluator")

        # Labels
        Label(self.window, text="Loan Amount").grid(row=1, column=1, sticky=W)
        Label(self.window, text="Interest Rate").grid(row=2, column=1, sticky=W)
        Label(self.window, text="Term (years)").grid(row=3, column=1, sticky=W)

        # Output labels
        Label(self.window, text="Payment:").grid(row=5, column=1, sticky=W)
        Label(self.window, text="Total Payments:").grid(row=6, column=1, sticky=W)

        # Variables to store input
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

        self.pmt = StringVar()
        self.total = StringVar()

        # Entry fields
        Entry(self.window, textvariable=self.pv, justify=RIGHT).grid(row=1, column=2, padx=(0, 5))
        Entry(self.window, textvariable=self.interest_rate, justify=RIGHT).grid(row=2, column=2, padx=(0, 5))
        Entry(self.window, textvariable=self.term, justify=RIGHT).grid(row=3, column=2, padx=(0, 5))

        # Output labels for Payment and Total Payments
        Label(self.window, textvariable=self.pmt, font="Helvetica 12 bold", justify=RIGHT).grid(row=5, column=2, sticky=E)
        Label(self.window, textvariable=self.total, font="Helvetica 12 bold", justify=RIGHT).grid(row=6, column=2, sticky=E)

        # Calculate button with adjusted row and padding to make it visible
        Button(self.window, text="Calculate Payment", command=self.calcPayment, font="Helvetica 14").grid(row=7, column=2, padx=(20, 5), pady=10)

        # Refinance variables
        self.old_pmt = StringVar()
        self.time_left = StringVar()
        self.refi_cost = StringVar()

        # Refinance Labels
        Label(self.window, text="Current Payment", font="Helvetica 16").grid(row=8, column=1)
        Label(self.window, text="Time Remaining", font="Helvetica 16").grid(row=9, column=1)
        Label(self.window, text="Refi Cost", font="Helvetica 16").grid(row=10, column=1)

        # Evaluation Entries
        Entry(self.window, textvariable=self.old_pmt, justify=RIGHT).grid(row=8, column=2, padx=(0, 5))
        Entry(self.window, textvariable=self.time_left, justify=RIGHT).grid(row=9, column=2, padx=(0, 5))
        Entry(self.window, textvariable=self.refi_cost, justify=RIGHT).grid(row=10, column=2, padx=(0, 5))

        # Output variables for evaluation
        self.monthly_savings = StringVar()
        self.payback = StringVar()
        self.overall_savings = StringVar()

        # Output Labels
        Label(self.window, text="Monthly Savings", font="Helvetica 16").grid(row=11, column=1)
        Label(self.window, text="Payback in Months", font="Helvetica 16").grid(row=12, column=1)
        Label(self.window, text="Overall Savings", font="Helvetica 16").grid(row=13, column=1)

        # Output Entries
        Label(self.window, textvariable=self.monthly_savings, font="Helvetica 12 bold", justify=RIGHT).grid(row=11, column=2, sticky=E)
        Label(self.window, textvariable=self.payback, font="Helvetica 12 bold", justify=RIGHT).grid(row=12, column=2, sticky=E)
        Label(self.window, textvariable=self.overall_savings, font="Helvetica 12 bold", justify=RIGHT).grid(row=13, column=2, sticky=E)

        # Refinance Evaluation Button
        Button(self.window, text="Eval Refi", font="Helvetica 14", command=self.evalRefi).grid(row=14, column=2)

        # Start main loop
        self.window.mainloop()

    def calcPayment(self):
        try:
            # Get user input values
            pv = float(self.pv.get())  # Loan Amount
            rate = float(self.interest_rate.get())  # Interest Rate
            term = int(self.term.get())  # Term in Years

            # Calculate monthly interest rate and number of payments
            r = rate / 1200  # Monthly interest rate
            n = term * 12    # Total number of payments (months)

            if r == 0:  # Handle case for zero interest rate (simple division)
                pmt = pv / n
            else:
                # Standard loan payment formula
                pmt = pv * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

            # Calculate total payments
            total = pmt * n

            # Update the output labels with the calculated values
            self.pmt.set("$" + format(pmt, "5,.2f"))
            self.total.set("$" + format(total, "8,.2f"))
        except ValueError:
            # Handle invalid input (non-numeric values)
            self.pmt.set("Invalid input")
            self.total.set("Invalid input")

    def evalRefi(self):
        try:
            # Get refinance input values
            old_pmt = float(self.old_pmt.get())  # Current Payment
            time_left = int(self.time_left.get())  # Time Remaining (months)
            refi_cost = float(self.refi_cost.get())  # Refinance Cost

            # Calculate new monthly payment and total savings
            new_pmt = float(self.pmt.get()[1:].replace(",", ""))  # Get calculated payment from previous step
            monthly_savings = old_pmt - new_pmt
            overall_savings = monthly_savings * time_left - refi_cost
            payback = refi_cost / monthly_savings if monthly_savings > 0 else 0

            # Update the output labels with the calculated values
            self.monthly_savings.set("$" + format(monthly_savings, "5,.2f"))
            self.payback.set(f"{payback:.1f} months")
            self.overall_savings.set("$" + format(overall_savings, "8,.2f"))
        except ValueError:
            # Handle invalid input (non-numeric values)
            self.monthly_savings.set("Invalid input")
            self.payback.set("Invalid input")
            self.overall_savings.set("Invalid input")

# Create an instance of the RefiEval class
RefiEval()
