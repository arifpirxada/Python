''' Problem_2: Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014 '''


exam_st_date = (11, 12, 2014)
exam = [repr(exam_st_date[0]),repr(exam_st_date[1]),repr(exam_st_date[2])]
message="The examination will start from : "
print(message+" / ".join(exam))