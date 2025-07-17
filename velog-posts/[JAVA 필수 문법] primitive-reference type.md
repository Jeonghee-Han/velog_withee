<h3 id="primitive-type과-reference-type">primitive type과 reference type</h3>
<p>JAVA에는 <strong>프리미티브 타입</strong>(int, long, float, double)과 <strong>레퍼런스 타입</strong>(Integer, Long, Float, Double)이 있다. <strong>레퍼런스 타입은</strong> 참조형 변수니까 <strong>연산 속도가 더 느리다.</strong> </p>
<p>다만, <strong>레퍼런스 타입</strong>은 컬렉션 프레임워크(리스트, 스택, 큐, 데크, 해시맵..) 등에서 <strong>정수형</strong> 또는 <strong>부동소수형</strong>을 저장할 때 사용하기 때문에 알고 넘어가야 한다.</p>
<pre><code class="language-java">// 프리미티브 타입 사용법
int i = 0;
long[] longs = new long[10];
float f = 10.5f;
double d = 10 / 3.0;

// 레퍼런스 타입 사용법(꼭 필요한 경우가 아니면 권장하지 않음)
Integer I = 0;
Long[] Longs = new Long[10];
Float F = 10.5f;
Double D = 10 / 3.0;

// 문법 오류 발생
ArrayList&lt;int&gt; arrayList = new ArrayList&lt;&gt;();
Stack&lt;long&gt; stack = new Stack&lt;&gt;();
Queue&lt;float&gt; queue = new Queue&lt;&gt;();
ArrayDeque&lt;double&gt; arrayDeque = new ArrayDeque&lt;&gt;();

// 올바른 코드
ArrayList&lt;Integer&gt; arrayList = new ArrayList&lt;&gt;();
Stack&lt;Long&gt; stack = new Stack&lt;&gt;();
Queue&lt;Float&gt; queue = new ArrayDeque&lt;&gt;();
ArrayDeque&lt;Double&gt; arrayDeque = new ArrayDeque&lt;&gt;();</code></pre>
<p><br /></p>
<h3 id="정수형">정수형</h3>
<p>✅ 양의 정수, 음의 정수, 0</p>
<pre><code class="language-java">int a = 13
int b = 4 

System.out.println(a + b);    // 더하기 / 17
System.out.println(a - b);    // 빼기 / 9
System.out.println(a * b);    // 곱하기 / 52
System.out.println(a / b);    // 나누기 (소수점 버림) / 3
System.out.println(a % b);    // 모듈러 연산 (소수점 버림) / 1

System.out.println(a == b)  # 같은 값인지 비교 / false
System.out.println(a != b)  # 같지 않은 값인지 비교 / true
System.out.println(a &gt; b)   # 왼쪽 값이 더 큰지 비교 / true
System.out.println(a &lt; b)   # 왼쪽 값이 더 작은지 비교 / false
System.out.println(a &gt;= b)  # 왼쪽 값이 더 크거나 같은지 비교 / true
System.out.println(a &lt;= b)  # 왼쪽 값이 더 작거나 같은지 비교 / false  

System.out.println(a &amp; b)   # AND   / 4
System.out.println(a | b)   # OR    / 13
System.out.println(a ^ b)   # XOR   / 9
System.out.println(~a)      # NOT   / -14
System.out.println(a &lt;&lt; 2)  # 왼쪽 시프트 (a에 2^2를 곱한 것과 동일)  / 52
System.out.println(a &gt;&gt; 1)  # 오른쪽 시프트 (a를 2^1로 나눈 것과 동일) / 6 </code></pre>
<p><br /></p>
<h3 id="부동소수형">부동소수형</h3>
<p>✅ 소수를 저장할 때 사용!</p>
<pre><code class="language-java">System.out.println(2.5 + 3.7)   # 더하기   / 6.2
System.out.println(7.9 - 4.2)   # 빼기    / 3.7
System.out.println(1.5 * 4.8)   # 곱하기   / 7.199999999999999
System.out.println(10.0 / 3.2)  # 나누기   / 3.125 
System.out.println(10.0 % 3.2)  # 모듈러   / 0.39999999999999947

double x = 0.5;
double y = 1.2;
double z = 2.0;
System.out.println(x &gt; y &amp;&amp; y &lt; z); // AND 연산 / false
System.out.println(x &lt; y || y &lt; z); // OR 연산 / true
System.out.println(!(x &gt; y));       // NOT 연산 / true</code></pre>
<p>✅ <strong>엡실론을 포함한 연산에 주의할 것</strong>
<em>부동소수형 코드 실행 결과를 보면 10.0 % 3.2 가 0.4가 아닌 0.39999999999999947이다.</em>
JAVA는 데이터를 이진법으로 표현하는데 이 과정에서 오차가 발생하며, 이를 엡실론이라고 한다.</p>
<p><strong>코테에서 부동소수형 데이터를 다룰 일이 생기면 엡실론이라는 요소 때문에 일부 테스트 케이스가 통과하지 못할 수도 있으니 유의하자.</strong>
<br /></p>
<hr />
<h3 id="🍽️오늘의-eat">🍽️오늘의 EAT</h3>
<p><strong>Experience</strong>
각각의 개념은 알고 있었으나, 레퍼런스 타입의 특징과 부동소수형 코드 실행 시 주의할 점에 대해 알지 못하고 코드를 짜왔다.</p>
<p><strong>Awareness</strong>
레퍼런스 타입은 연산 속도가 느릴 뿐만 아니라, 권장되는 경우가 극히 적다는 점과 부동소수형 코드 실행 시 엡실론을 유의하지 않으면 일부 테스트 케이스가 통과하지 못할 수 있다는 점을 알았다.</p>
<p><strong>Take Action</strong>
코테에서 부동소수형 데이터를 다룰 경우 오차 허용 범위를 언급하는 경우가 많다는데, 앞으로 코테 풀 때 유의해서 봐야겠다.</p>