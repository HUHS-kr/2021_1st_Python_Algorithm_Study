"""그리디 알고리즘을 사용하면 매 순간 가장 좋아 보이는 것을 선택하며,
현재의 선택이 나중에 미칠 영향을 고려하지 않는다.
따라서 그리디 알고리즘을 통해 도출한 결과가 최적의 해인지 검토할 수 있어야한다.

그리디 알고리즘은 문제 출제의 폭이 매우 넓기 때문에, 단순 암기를 통해 모든 문제를 대처하기는 어렵다.
따라서 많은 문제를 풀어보며 훈련을 해야한다.

그리디 알고리즘은 좋아보이는 기준을 문제에서 알게 모르게 제시해준다.
대체로 이 기준은 정렬 알고리즘을 사용했을때 만족시킬 수 있으므로, 그리디 알고리즘과 정렬 알고리즘은 자주 짝을 이뤄 출제된다.

어떤 코딩테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심하고, 오랜시간을 고민해도 그리디 알고리즘으로 해결방법을 찾을 수 없다면,
다이나믹프로그래밍이나, 그래프 알고리즘 등으로 해결할 수 있는지를 재차 고민해보는 것이 좋다.

다음은 n이 1이 될때가지 k로 나누거나, 1을 빼는 알고리즘을 구현한 것이다. 이때 k로 나누는 방법은 n이 k로 나누어 떨어질때만 사용 가능하다.
눈여겨볼 것은 알고리즘에서 k로 나누어떨어지지 않을때, 1을 한번씩 빼면서 나누어 떨어지게 만들 것인지,
아니면 얼만큼 빼야 나누어떨어지는 지를 미리 알고, 그만큼 한번에 빼버리는지를 선택하는 것이다."""

# n,k 를 공백으로 구분하여 입력받기
n, k = map(int, input()/split())
result = 0

while True:
  #(n == k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
  target = (n//k)*k #만들어야되는 수 ( k로 나누어 떨어지는 수 )
  result += (n-target) #1을 몇번빼야하는지를 결과값에 더하기 (왜냐하면 시행1번에 1만 뺄 수 있기 때문에)
  n = target #위에서 result에 1을 몇번뺐는지 넣었으니 빼진거라고 가정하고 n은 k로 나누어 떨어지는 수가 됨.
  if n<k:
    break # 만약에 나누어 떨어지는 수가 됐는데 target이 k보다 작아진것. 이제 더이상 나눌 수 없어진 것이라서 밑에 있는 나누는 코드로 가지 않아도 됨.
    
  n //= k 
  result += 1 #k로 1회 나눴다고 생각하고 n에다가 k로 나눠준 값을 넣음.
  
result += (n-1) #반복문을 나왔을 때 남은 n이 있다면 1로 만들어줌. n-1번 빼면 1이 되니 n-1번 실행했다고 생각. 또한 만약에  25번째 코드에서 result가 n만큼 더해져버린다면
                # 한번이 추가적으로 빠진 것이므로 result에 -1를 해주는 기능도 수행함.
print(result)



