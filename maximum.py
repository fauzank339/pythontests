A = list(map(int, input().split()))
def maximum(A):
	for i in range(len(A)):
		if A[i]>A[0]:
			A[0]=A[i]
	return A[i]
print(maximum(A))

				

