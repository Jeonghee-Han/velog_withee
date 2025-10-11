# [AI를 위한 Python] Statement

**Published:** Fri, 10 Oct 2025 08:53:46 GMT
**Link:** https://velog.io/@heerang/AI%EB%A5%BC-%EC%9C%84%ED%95%9C-Python-Statement

---

<h2 id="조건문">조건문</h2>
<h3 id="if---elif---else">if - elif - else</h3>
<p>⚠️ python에서는 <code>else if</code>가 아닌 <code>elif</code>임을 주의하자.</p>
<pre><code class="language-python">score = 85

if score &gt;= 90:
    print(&quot;학점: A&quot;)
elif score &gt;= 80:
    print(&quot;학점: B&quot;)
else:
    print(&quot;학점: C&quot;)</code></pre>
<p><br /></p>
<h3 id="match---case">match - case</h3>
<p>Java의 <code>switch-case</code>와 동일하게 사용하지만, <code>default</code> 키워드만 <code>_</code>로 사용한다.</p>
<pre><code class="language-python">month = 6
day = 0

match month:
    case 2:
        day = 28
    case 4 | 6 | 9 | 11:
        day = 31
    case _:
        day = 30
print(day)</code></pre>
<p>⚠️ python <code>match-case</code>구문에서는 <code>break</code>문 없어도 일치하면 자동 break.
<br /></p>
<hr />
<h2 id="반복문">반복문</h2>
<h3 id="for">for</h3>
<ul>
<li><p>순회 가능한 객체의 요소를 하나씩 순회한다.</p>
<pre><code class="language-python">fruits = [&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;]
for fruit in fruits:
    print(fruit)

# range() 함수와 함께 사용하는 for 루프
for i in range(5): # 0부터 4까지 (5는 포함 안됨)
    print(i)

for i in range(2, 11, 2): # 시작 값, 끝 값 (포함 안됨), 스텝
    print(i) # 2부터 10까지 짝수 출력</code></pre>
</li>
<li><p>index랑 같이 사용하고 싶으면 <code>enumerate()</code>로 감싸서 사용한다.</p>
<pre><code class="language-python">list_value = [3, 6, 1, 10]

for index, value in enumerate(list_value):
    print(index, value)</code></pre>
<pre><code>출력 결과

0 3
1 6
2 1
3 10</code></pre></li>
</ul>
<h3 id="while">while</h3>
<p>while문은 조건이 True인 동안 반복하며, 다른 언어와 동일하다.</p>
<pre><code class="language-python">index = 0

while index &lt; 10:
    print(index, '', end='')
    index += 1</code></pre>
<h2 id="brbr"><br /></h2>
<h2 id="리스트-컴프리헨션-list-comprehension-⭐">리스트 컴프리헨션 (List Comprehension) ⭐</h2>
<p>반복문과 조건문을 단 한 줄로 결합해서 새로운 리스트를 생성하는 Python의 매우 강력한 문법이다. Java의 Stream API에서 <code>map</code>이나 <code>filter</code>를 사용하는 개념과 유사하다.</p>
<p>💡데이터 분석 및 AI 분야에서는 대용량 데이터를 빠르고 간결하게 처리해야 하므로, 리스트 컴프리헨션이 일반적인 for 루프보다 가독성과 실행 속도 면에서 선호한다.</p>
<blockquote>
<p><code>[결과_표현식 for 항목 in 순회_가능_객체 if 조건식]</code></p>
</blockquote>
<pre><code class="language-python">print(&quot;\n--- 리스트 컴프리헨션 ---&quot;)
squares = [x**2 for x in range(10)]
print(f&quot;0부터 9까지 제곱: {squares}&quot;)

even_numbers = [x for x in range(20) if x % 2 == 0]
print(f&quot;0부터 19까지 짝수: {even_numbers}&quot;)</code></pre>
<h2 id="brbr-1"><br /></h2>
<h2 id="itertools">itertools</h2>
<p>파이썬 표준 라이브러리로, 반복을 유연하고 강력하게 처리할 수 있도록 도와준다. 특히 조합, 순열, 누적 계산 등 복잡한 반복 패턴을 쉽게 구현할 수 있다.</p>
<h3 id="🔧-주요-함수">🔧 주요 함수</h3>
<ul>
<li>product(): 데카르트 곱 (중첩 반복)</li>
<li>permutations(): 순열 생성</li>
<li>combinations(): 조합 생성</li>
<li>accumulate(): 누적합 계산</li>
<li>groupby(): 조건에 따라 그룹화</li>
</ul>
<pre><code class="language-python">from itertools import product, permutations, combinations, accumulate

# product: 모든 조합 (중첩 반복)
print(&quot;\n--- product ---&quot;)
for p in product([1, 2], ['A', 'B']):
    print(p)

# permutations: 순열
print(&quot;\n--- permutations ---&quot;)
for p in permutations([1, 2, 3], 2):
    print(p)

# combinations: 조합
print(&quot;\n--- combinations ---&quot;)
for c in combinations([1, 2, 3], 2):
    print(c)

# accumulate: 누적합
print(&quot;\n--- accumulate ---&quot;)
import operator
nums = [1, 2, 3, 4]
print(&quot;누적합:&quot;, list(accumulate(nums)))
print(&quot;누적곱:&quot;, list(accumulate(nums, func=operator.mul)))</code></pre>