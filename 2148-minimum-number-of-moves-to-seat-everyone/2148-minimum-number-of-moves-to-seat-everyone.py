class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        c=0
        for i in range(len(seats)):
            c+=abs(seats[i]-students[i])
        return c

        