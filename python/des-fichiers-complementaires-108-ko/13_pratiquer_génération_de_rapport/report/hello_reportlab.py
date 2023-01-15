from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.drawString(100,100,"Bonjour le monde en pdf avec reportlab")
c.save()
