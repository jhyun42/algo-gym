# Find Numbers with Even Number of Digits

## 1. 문제 설명:
정수의 배열이 주어졌을 때, 자릿수가 짝수인 정수의 개수를 반환하라.

## 2. 문제 풀이:
배열의 값들을 확인한다. 
각각의 값을 10으로 나누면서 숫자 개수 count (digit count) 를 할 수 있고,
digit count 를 modular 연산을 통해 짝수인지 홀수인지 확인하여 
짝수면 return 할 count 값을 +1 한다.  

## 3. 시간 복잡도 & 공간 복잡도:
전체 입력 리스트를 한번만 횡단하면 되기 때문에 시간 복잡도는 O(N),  
공간 복잡도는 따로 list 를 생성하거나 하지 않기 때문에 O(1).
 