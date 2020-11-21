from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


def main():
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("usage: inputfile.pdf output.pdf [page-range]")
        print("\t[page-range]\t= [firstpage-lastpage]")
        exit()

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # page_range = "1-3,4-6"
    page_range = sys.argv[3]
    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(infile, "rb"))
    output_file = open(outfile, "wb")

    page_ranges = (x.split("-") for x in page_range.split(","))
    range_list = [i for r in page_ranges for i in range(
        int(r[0]), int(r[-1]) + 1)]

    for p in range_list:
        # Subtract 1 to deal with 0 index
        output.addPage(input_pdf.getPage(p - 1))
    output.write(output_file)


if __name__ == "__main__":
    main()
