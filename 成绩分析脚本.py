from random import randint
n=input("请输入一段数字")
k=randint(0,len(n))
for i in range(k):
	for j in range(len(n)-1):
		if n[j]>n[j+1]:
			break
		else:
			n=n[:len(n)-1]
			continue
	n=n[:j]+n[j+1:]
print(n)

'''n='p4y2t3h1o9n4'
p=''
for i in n:
	if '0'<=i<='9':
		if p=='':
			p+=i
		elif i>=p[-1]:
			p+=i
		elif i<p[0]:
			p=i
print(p)'''
