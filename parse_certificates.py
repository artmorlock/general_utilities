#   Parse_Certificates
#
#  Python script to generate a list of Learning certificates:
#    Use wildcard specification to loop thru a set of PDF files and use the 
#    PDF parser to
#      1.  Get filename
#      2.  Get save date
#      3.  name of course
#      4.  Length of course
#      5.  Author
#      6.  Date of Completions
#      7.  any distinct identifier for course and course session
#      8.  if possible categorize course
#
#        LinkedIn Learning structure
#            Row 3 column2 -Title
#            Row 4 Column 2 - Certificate ID
#            Row 5 column2 Completion Date & Time and elapsed time
#            Row 7 skills covered - multiple columns
#
#    Save certificate list as MS Excel file.
#
#    Author:
#        Art Morlock
#
#  History:
#    Creation: 20250430
#==================================================================================

'''
  import libraries
'''
