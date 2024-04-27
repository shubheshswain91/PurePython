# Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

#chunk1 = sample_list[0:3]
#print(chunk1)

#chunk2 = sample_list[4:6]

#chunk3 = sample_list[6:9]

#chunk1.reverse()
#chunk2.reverse()
#chunk3.reverse()

#print(chunk3)

##   Approach 2

length = len(sample_list)

chunk_size = int(length/3)

start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start, end)

    print(indexes)

    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    #reverse chunk 
    print("After reversing the chunk: ", list(reversed(list_chunk)))

    start = end
    end += chunk_size
