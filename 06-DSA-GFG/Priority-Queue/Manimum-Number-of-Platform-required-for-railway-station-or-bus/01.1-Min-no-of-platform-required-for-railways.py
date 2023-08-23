class Find:
    def __init__(self, arrival, departure) -> None:
        self.arr = arrival
        self.dep = departure
        self.timeConvert()
        self.printAnswer = self.findPlatform()
    
    def findPlatform(self):
        n = len(self.arr)
        count = 1
        maximum = 1         # For Minimum
        for i in range(n):
            count = 1
            for j in range(n):
                if i == j:
                    continue
                elif self.arr[j] <= self.arr[i] <= self.dep[j]:
                    count += 1
            maximum = max(maximum, count)
        return maximum
    
    def timeConvert(self):
        arr = []
        for time in self.arr:
            hour, minute = time.split(':')
            minute = int(minute) + int(hour) * 60
            arr.append(minute)
        self.arr = arr
        dep = []
        for time in self.dep:
            hour, minute = time.split(':')
            minute = int(minute) + int(hour) * 60
            dep.append(minute)
        self.dep = dep


if __name__ == '__main__':
    arrival = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
    departure = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']
    # arrival = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
    # departure = ['9:10', '12:00', '10:40', '11:30', '19:00', '20:00']
    answer = Find(arrival, departure)
    print(answer.arr, answer.dep)
    print(answer.printAnswer)