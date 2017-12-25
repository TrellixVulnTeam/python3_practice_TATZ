filename = "programming.txt"
"""写入文件"""
with open(filename, 'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love python too.\n")

