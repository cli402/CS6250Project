import sys
import timeit

"""
How to call the function:
get_path(graph, cutoff)

Input: The graph represent the datastructure graph, and cutoff the max number of hop on the path
The details of how the graph looks like, please go to the function get_path() and check the example.

Output: the optimal path of result, like a array: [1 2 3 4 5]
        the first one is the source, in this example is 1
		the last one is the dest, in this example is 5
		Also it will open a file in the same dir named "result.txt", and the formate of this file is:

source
dest
weight string
result string
run time

If the "result.txt" is already exsite, then each time it will append new data like above into this file.

"""

def calculatePath(graph, cutoff, start, end):
    total_weight = [sys.float_info.max]
    result = []
    path = []
    dfs(graph, start, end, path, total_weight, 0, result, cutoff)
    #print result[0]
    return result[0]

def dfs(graph, start, end, path, total_weight, w, result, cutoff):
    path = path + [start]
    if start == end:
        if w < total_weight[0] and len(path) < cutoff:

            #print total_weight[0]
            total_weight[0] = w
            #print path, w
            if len(result) == 1:
                result.pop()
            result.append(path)
            #print result
            return
    print graph[start] 
    for node, weight in graph[start].items():
        if node not in path:
            dfs(graph, node, end, path,total_weight, w + weight, result, cutoff)
    path.pop()


def get_path(graph, source, dest, cutoff):

    # convert the weight into a string
    ss = ""
    for key, value in graph.items():
        for node, weight in value.items():
            ss = ss + str(weight) + ","

    # call function to calculate and measure the time
    start = timeit.timeit()
    result = calculatePath(graph, cutoff, source, dest)
    end = timeit.timeit()
    run_time = end - start

    # convert the result into a string
    s = ""
    for i in result:
        s = s + str(i) + ","
	
    # write into file
    foo = open("result.txt", "ab")
    foo.write(result[0])
    foo.write("\n")
    foo.write(result[-1])
    foo.write("\n")
    foo.write(ss)
    foo.write("\n")
    foo.write(s)
    foo.write("\n")
    foo.write(str(run_time))
    foo.write("\n")
    foo.close()
    
    return result


if __name__ == "__main__":
    # Main function to use it
    graph = {'e': {'b': 5.0, 'c': 8.0}, 'b':{'e': 5.0, 'd': 12.0}, 'c': {'e': 8.0, 'd': 2.0}, 'd':{'b':12.0,'c': 8.0}}
    cutoff = 4
    sourse = 'e'
    dest = 'd'
    get_path(graph, sourse, dest, cutoff)
