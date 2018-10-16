"""
Rubique has a unique logic to rate its customers basis the CIBIL score and the RISK score. Following is the algorithm used to rate and sort the customers.


1. The customer with higher CIBIL score will be on the top.
2. If CIBIL score of two customer matches then the customer with lower RISK score will come above.
3. If both CIBIL and RISK score matches, then the customers are sorted in descending order of their names.
4. If all three value matches then it will remain in the same order as input.

Task is to find the  customer from the top in the sorted list of customers starting from 1;

NAME contain only alphabets without any space.

Input

 : Total number of test cases. In each test, the first line indicates the number of customers 
The  lines following it contain  space separated data  i.e NAME, CIBIL, NEGATIVE INDEX. The  line contains value of .
  

Output
Print two space separated value i.e NAME and CIBIL of the  customer
For each test case, output should be in a different line.

https://www.hackerearth.com/challenge/competitive/rubique-finhack/algorithm/cibil-score/

2
6
Ayush 640 100
Prateek 670 80
Suraj 670 70
Sameer 620 50
Sahil 630 20
Sumit 640 90
3
6
Ayush 640 100
Prateek 670 80
Suraj 670 70
Sameer 620 50
Sahil 630 20
Sumit 640 90
3

"""


def tier_bubble_sort(data):
    for i in range(0,len(data)-1):
        for j in range(i,len(data)):
            if(data[i][1]<data[j][1]):
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
            if (data[i][1] == data[j][1]):
                if(data[i][2] > data[j][2]):
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
                if (data[i][2] == data[j][2]):
                    if (data[i][0] < data[j][0]):
                        temp = data[i]
                        data[i] = data[j]
                        data[j] = temp


if __name__=="__main__":
    no_inputs=0
    data=[]
    temp=[]
    while no_inputs:
        string = input()
        if string is "":
            break
        temp.append(string.split())
        data.append(temp)
        temp.clear()
        string = ""

    """data = [["Ayush", 640, 100],
            ["Prateek", 670, 80],
            ["Suraj", 670, 70],
            ["Sameer", 620, 50],
            ["Sahil", 630, 20],
            ["Sumit", 640, 90]]
    """

    print(data)
    tier_bubble_sort(data)
    print(data)

"""
data =[  ["Ayush", 640, 100],
["Prateek", 670, 80],
["Suraj", 670, 70],
["Sameer", 620, 50],
["Sahil", 630, 20],
["Sumit", 640, 90]]
print(data)
"""
tier_bubble_sort(data)







