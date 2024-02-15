import excel_to_db as excel_to_db
import doc.paths as doc
import create_file_links_list_from_db as cf
import make_screen as m
import create_report as c


if __name__=='__main__':

    #  Load data from xls to db.
    file_excel_report = doc.excel_report # Excel-document path.
    
    
    excel_to_db.load(file_excel_report)

    #  Fill in the form current report.
    company = doc.company 
    report_month = doc.report_month
    date_start = doc.date_start
    date_end = doc.date_end



    ###  Create stg-tables.
    # cf.create_STG_tables(company, date_start, date_end)

    ###  Make screen.
    path_for_screens = doc.path_for_screens
    # m.make_screen(path_for_screens)

    ###  Create report.
    c.get_report(company, report_month, path_for_screens)

    print("DONE")
