table_data = [["apples", "oranges", "cherries", "banana"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]

word_length = 0
col_width = []
sum_width = 0
result_list = []
result = []

for i in table_data:
    for j in range(len(i)):
        if len(i[j]) > word_length: #and j < len(i):
            word_length = len(i[j])
#        elif len(i[j]) > word_length:
#            word_length = len(i[j])
#    col_width.append(word_length)
#    word_length = 0

#for k in col_width:
#    if sum_width < k:
#        sum_width = k
#print(sum_width)

for l in range(len(table_data[0])):
    for m in range(len(table_data)):
        result_list.append(table_data[m][l].rjust(word_length, " "))
    result.append(result_list)
    result_list = []

for n in result:
       
        print("".join(n))