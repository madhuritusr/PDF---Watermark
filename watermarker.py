import PyPDF2

watermark_file = "wtr.pdf"
writer = PyPDF2.PdfFileWriter()
with open(watermark_file, "rb"):
    watermark = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark.getPage(0)


def pdf_watermark(*pdf_list):
    for pdf in pdf_list:
        with open(pdf, "rb"):
            reader = PyPDF2.PdfFileReader(pdf)
            no_of_pages = reader.numPages
            for page_no in range(no_of_pages):
                page = reader.getPage(page_no)
                page.mergePage(watermark_page)
                writer.addPage(page)
                with open("watermarked.pdf", "wb") as output_file:
                    writer.write(output_file)


pdf_watermark("dummy.pdf", "twopage.pdf")
