class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        l=len(students)
        c=0
        while(students and sandwiches):
            if students[0]==sandwiches[0]:
                students=students[1:]
                sandwiches=sandwiches[1:]
            else:
                a=students[0]
                students.pop(0)
                students.append(a)
                c+=1
            if c==3*l:
                break
        return len(students)

        