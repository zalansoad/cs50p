from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name, orientation):
        super().__init__(orientation)
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return self.name

    def header(self):
        # Rendering logo:
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def text(self):
        self.set_font("helvetica", "B", 20)
        self.set_xy(20, 110)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{self.name} took CS50", align='C')


def main():
    name = input('Name: ')
    pdf = PDF(name, orientation="portrait")
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=50, w=pdf.epw)
    pdf.text()
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

