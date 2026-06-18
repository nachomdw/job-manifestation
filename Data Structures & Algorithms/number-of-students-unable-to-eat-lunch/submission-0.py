class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        amount = 0

        while (len(sandwiches) != 0) and (amount != len(students)) :
            # While there are remaining sandwhiches and students

            if students[0] == sandwiches[0]:
                # If the first student in line likes the sandwhich remove both
                students.pop(0)
                sandwiches.pop(0)
                amount = 0
            
            elif students[0] != sandwiches[0]:
                # If the student doesn't like the sandwich, go to the back of the line.
                goBack = students.pop(0)
                students.append(goBack)
                amount = amount + 1
       
        return len(students)