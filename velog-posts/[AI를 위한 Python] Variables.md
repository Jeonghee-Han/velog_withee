# [AI를 위한 Python] Variables

**Published:** Fri, 10 Oct 2025 08:34:13 GMT
**Link:** https://velog.io/@heerang/AI%EB%A5%BC-%EC%9C%84%ED%95%9C-Python-Variables

---

<h2 id="variables-변수">Variables (변수)</h2>
<p>⚠️참고로 Python은 변수 선언 시 타입을 명시하지 않는다. (동적 타이핑)</p>
<h3 id="숫자형-numeric-types">숫자형 (Numeric Types)</h3>
<ul>
<li><strong>int</strong> (정수형)<pre><code class="language-python">int_value = 1
print(type(int_value)) # &lt;class 'int'&gt;</code></pre>
</li>
<li><strong>float</strong> (부동소수점형)<pre><code class="language-python">float_value = 1.0
print(type(int_value)) # &lt;class 'float'&gt;</code></pre>
</li>
<li><strong>complex</strong> (복소수)<pre><code class="language-python">complex_value = 2 - 1j
print(type(complex_value)) # &lt;class 'complex'&gt;</code></pre>
</li>
</ul>
<p><br /></p>
<h3 id="논리형-bool-types">논리형 (Bool Types)</h3>
<p><strong>True, Flase</strong> 두 가지 상수 값이 존재하고, Java와 달리 <strong>첫 글자는 대문자</strong>로 표기한다.</p>
<pre><code class="language-python">true_value = True
print(type(true_value)) # &lt;class 'bool'&gt;

false_value = False
print(type(false_value)) # &lt;class 'bool'&gt;</code></pre>
<p><br /></p>
<h3 id="연속형-sequence-types">연속형 (Sequence Types)</h3>
<ul>
<li><strong>list</strong> (배열)<ul>
<li>순서가 있고, 변경 가능한 자료형</li>
<li>다양한 타입의 데이터를 합께 저장 가능<pre><code class="language-python">my_list = [1, 2, 'apple', True]
my_list.append('banana')</code></pre>
</li>
</ul>
</li>
<li><strong>Tuple</strong> (튜플)<ul>
<li>순서가 있지만, 변경 불가능한 자료형</li>
<li>한 번 객체를 생성하면 구성요소를 바꿀 수 X</li>
<li>리스트보다 메모리 효율이 좋고, 안전한 데이터 저장에 적합<pre><code class="language-python">my_tuple = (10, 20, 'cherry')
my_typle[0] = 4     #⚠️ 변경 불가</code></pre>
</li>
<li><strong>range</strong> (범위)<pre><code class="language-python">range_value = range(1, 4) # 1, 2, 3이 해당됨</code></pre>
</li>
</ul>
</li>
</ul>
<p><br /></p>
<h3 id="문자형-text-sequence-type">문자형 (Text Sequence Type)</h3>
<p>Python에서는 문자를 표현할 때 <code>'</code>과 <code>&quot;</code>를 이용하여 표현.
<br /></p>
<h3 id="집합형-set-types">집합형 (Set Types)</h3>
<ul>
<li><strong>Set</strong> (세트)<ul>
<li>순서가 없고, 중복 허용 X</li>
<li>집합 개념 (합집합, 교집합, 차집합 등)<pre><code class="language-python">my_set = {1, 2, 3, 2, 1}
my_set.add(4)
print(my_set)   #⚠️ 중복이 제거됨을 확인</code></pre>
</li>
</ul>
</li>
</ul>
<p><br /></p>
<h3 id="매핑형-mapping-type">매핑형 (Mapping Type)</h3>
<ul>
<li><strong>Dict</strong> (딕셔너리)<ul>
<li>key와 value 한 쌍으로 데이터 관리</li>
<li>순서가 없고, key는 중복되지 않고, 나중에 추가한 값으로 갱신<pre><code class="language-python">my_dict = {'name': '김영희', 'age': 25, 'city': '서울'}</code></pre>
</li>
</ul>
</li>
</ul>
<blockquote>
<p>** 🎮 빌트인 딕셔너리**</p>
</blockquote>
<ol>
<li>defaultdict : 기본값을 지정할 수 있는 딕셔너리</li>
<li>Counter: 리스트나 문자열 등 반복 가능한 객체의 요소 개수를 자동으로 세어주는 딕셔너리</li>
</ol>
<p><br /></p>
<h3 id="none-type">None Type</h3>
<p>다른 언어의 <code>null</code>과 동일하며 0, <code>' '</code>과는 다르게 사용</p>