from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def main():
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("usage: output_file.pdf input_file1.pdf input_file2.pdf ...\n")
        exit()
    paths = sys.argv[2:]
    output_file = sys.argv[1]
    merge_pdfs(paths, output_file)


if __name__ == '__main__':
    main()
