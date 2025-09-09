def read_text_file(filename,n):
    with open(filename, 'r') as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line.strip())

#print(read_text_file('C:/Python/Python_Bootcamp/FileHandling/sample.txt',2))

data = [{
    "name":"Ravi",
    "age": 45,
    "location":"Pune"
},
{
    "name":"Abhijit",
    "age": 45,
    "location":"kolkata"
},{
    "name":"Rakaesh",
    "age": 45,
    "location":"Delhi"
}
]

 
with open('C:/Python/Python_Bootcamp/FileHandling/sample.txt','w') as f:
    for key, value in data.items():
        f.write(f"{key}:{value}\n")