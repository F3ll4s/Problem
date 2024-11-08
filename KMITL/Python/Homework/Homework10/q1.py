import matplotlib.pyplot as plt

def pie_chart(x):
    x.sort()
    list = []
    count = []
    for i in x:
        if i not in list:
            list.append(i)
    for i in list:
        count.append(x.count(i))
    
    fig, ax = plt.subplots()
    ax.pie(count)
    plt.show()
        
pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])