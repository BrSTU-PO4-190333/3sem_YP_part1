class MyClass:
    def __init__(self):
        self.arr = [
            {
                'number': '№',
                'name_surname_middlename': ['', 'Прозвішча', 'Імя', 'Імя'],
                'surname': 'Прозвішча',
                'name': 'Імя',
                'middlename': 'Імя',
                'age': ' Возвраст',
                'group': ' Група'
            }
        ]

    def get_array_from_csv_file(self, path): # Task 2
        f = open(path, 'r')
        fileString = f.read()
        f.close()

        if fileString == '':
            print('file is empty')
            return

        # Каждая строчка в список
        arr = fileString.split('\n')
        for i in range(len(arr)):
            arr[i] = arr[i].split(',')
        
        # В каждом элементе словарь 
        for i in range(len(arr)):
            data = {}
            data['number'] = arr[i][0]
            data['name_surname_middlename'] = arr[i][1]
            data['name_surname_middlename'] = data['name_surname_middlename'].split(' ')
            
            data['surname'] = data['name_surname_middlename'][1]
            data['name'] = data['name_surname_middlename'][2]
            data['middlename'] = data['name_surname_middlename'][3]

            data['age'] = arr[i][2]
            data['group'] = arr[i][3]
            arr[i] = data
        self.arr = arr

    def print_table(self):
        for i in self.arr:
            print("|%-4s|%-16s|%-16s|%-16s|%-24s|%-8s|" % (
                i['number'],
                i['surname'],
                i['name'], 
                i['middlename'], 
                i['age'], 
                i['group']
            ))
        print()

    def sort_by_field_surname(self):
        arr = self.arr

        for i in range(1, len(arr)):
            for j in range(1, len(arr)):
                if arr[i]['surname'] < arr[j]['surname']:
                    arr[i], arr[j] = arr[j], arr[i]

        self.arr = arr
        print('sorting by surname field surname are done\n')

    def age_degrement(self):
        print('age = age - 1\n')
        for i in range(1, len(self.arr)):
            self.arr[i]['age'] = int(self.arr[i]['age']) - 1
        
    def save_to_csv_file(self, path):
        f = open(path, 'w')
        arr = self.arr
        for i in range(len(arr)):
            f.write('%s, %s %s %s, %s, %s' % (
                arr[i]['number'],
                arr[i]['surname'],
                arr[i]['name'], 
                arr[i]['middlename'], 
                arr[i]['age'], 
                arr[i]['group']
            ))
            if i != len(arr) - 1:
                f.write('\n')
        f.close()
        print('array saved on file %s' % path)

obj = MyClass()

print('Task 2')
obj.get_array_from_csv_file('files/students.csv') # Task 2. Open file
obj.print_table()
obj.sort_by_field_surname() # Task 2. Sort by field surname
obj.print_table()

print('Task 3')
obj.age_degrement() # Task 3. Age = Age - 1
obj.print_table()

print('Task 4-5')
obj.save_to_csv_file('files/result.csv') # Task 4-5. Save CSV file