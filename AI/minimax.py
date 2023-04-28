import math

def minmax(curDepth,nodeIndex,maxTurn,scores,targetDepth):
    if(curDepth==targetDepth):
        return scores[nodeIndex]
    if(maxTurn):
        return max(minmax(curDepth+1,nodeIndex*2,False,scores,targetDepth),
                   minmax(curDepth+1,nodeIndex*2+1,False,scores,targetDepth))
    else : 
        return min(minmax(curDepth+1,nodeIndex*2,True,scores,targetDepth),
                   minmax(curDepth+1,nodeIndex*2+1,True,scores,targetDepth))

a=int(input("Enter number of elements : "))
scores=list(map(int,input("Enter numbers in array : ").strip().split()))
treeDepth=math.log(len(scores),2)
print("optimal value : ",minmax(0,0,True,scores,treeDepth))