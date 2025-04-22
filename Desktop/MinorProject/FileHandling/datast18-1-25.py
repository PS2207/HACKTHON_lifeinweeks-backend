Algorithms for searching in an Array:-
|Aarav | Aish | Dhruv | Isha | Jai | Meera | Rohan |Tanvi |

Asymptotic Notation:
Performance of an algorithm is often described as a function, say f(n) where n denotes the size of the input problem.
1. Start from the first element in the array.
2. Repeat step 3-5 until the end of the array.
3. Copmare the current name with x.
4. If the current name is same as x, output yes & Stop. 
5. If the current name is not same as x, goto the next element in the array.
6. Output no, & stop 
  

For x=Manoj & if size of the array is 'n'
Time taken by the algorithm is 2n+2.
This is bcz the element is not present in the array, so we need to look into each cell to see whether it exists there or not. 
1 + n + n + 1= (2n + 2)
f(n)= O(n)

f(n)= 2n² + 3n + 1
f(n)= O(n cube) where n= g(n)

1.Big O notation:
f(n)=25
f(n)= O(n) g(n)=1
f(n) <= c.g(n) c=26
25 <= 26.1

2.Big Omega notation:
f(n)= Omega(g(n))
f(n) = 2ncube
f(n) =3n² 

3.0(Theta) Notation
f(n)= 2ncube
f(n)= 0(n3) true,  but not 0(n²) or 0(n4)...
c1.g(n) <= f(n) <= c2.g(n)
1n3 <= 2n3 <= 3n3

f(n) = 0(n4)
c1n4 <= 2n3 <= c2.n4
c.n4 <= 2n3
if f(n) O(g(n)) & omega(g(n)), then f(n) =0(g(n))

f(n) n/2
f(n)= 0(n) or 0(rootn) or    
    
f(n) is a function big O is notation for figuring out how much time does an algorithm need to run.










