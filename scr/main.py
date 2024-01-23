import excel_to_db as excel_to_db
import doc.paths as doc


if __name__=='__main__':

    #  Load data from xls to db.
    file_excel_report = doc.excel_report # Excel-document path.
    
    
    excel_to_db.load(file_excel_report)
