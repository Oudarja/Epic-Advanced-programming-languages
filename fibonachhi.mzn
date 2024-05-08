% Use this editor as a MiniZinc scratch book
int: n=20;
array[1..n] of var int:a;
constraint a[1]=1;
constraint a[2]=1;
constraint forall(i in 3..20)( 
a[i]=a[i-1]+a[i-2]
);
