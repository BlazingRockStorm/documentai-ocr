import os
from os.path import join, dirname
from dotenv import load_dotenv
from ocr_process import InvoiceOCR

if __name__ == '__main__' :
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

 
    file_path = "./data/sample_invoice.pdf"
    mime_type = "application/pdf" 

    invoiceOcr = InvoiceOCR()
    ocr_response = invoiceOcr.process_invoice_ocr(file_path, mime_type)
    
    print(ocr_response)

    path_w = 'output/ocr_result.json'

    with open(path_w, mode='w') as f:
        f.write(ocr_response)
