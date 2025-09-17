# [기계학습] Machine Learning

**Published:** Wed, 27 Mar 2024 05:01:46 GMT
**Link:** https://velog.io/@heerang/%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5-Machine-Learning

---

<h1 id="💡-머신러닝이란">💡 머신러닝이란?</h1>
<h3 id="인공지능">인공지능</h3>
<ul>
<li>인간의 지능을 기계가 나타내는 것</li>
<li>어떤 문제에 대해 최적 혹은 부최적의 해결책을 제시하는 기계에 의해 나타나는 지능</li>
</ul>
<h3 id="머신러닝">머신러닝</h3>
<ul>
<li>인공지능을 달성하기 위한 접근 방법</li>
<li>명시적으로 프로그래밍되지 않고도 학습할 수 있는 능력</li>
<li>데이터에서 패턴을 자동으로 감지하고, 발견된 패턴을 이용해 미래 데이터를 예측하거나 불확실한 조건 하에서 의사결정을 가능하게 함</li>
</ul>
<h3 id="딥러닝">딥러닝</h3>
<ul>
<li>머신러닝을 구현하기 위한 기술</li>
</ul>


<h3 id="✔-명시적-프로그래밍의-한계">✔ 명시적 프로그래밍의 한계</h3>
<blockquote>
<p><strong>머신러닝</strong>은 Explicit Programming, 즉 <strong><code>명시적 프로그래밍</code>의 한계</strong>에서 착안한 기술</p>
</blockquote>
<ul>
<li>예를 들어, 스팸 필터나 자동 운전과 같은 경우 많은 규칙이 필요!</li>
<li>아서 새무얼(Arthur Samuel, 1959)은 머신러닝을 &quot;명시적인 프로그래밍 없이 컴퓨터가 학습하는 능력을 갖추게 하는 연구 분야&quot;라고 정의</li>
</ul>
<p><span style="color: gray;"><em>🤔 만약 스팸 메일을 필터링 하는 프로그램을 개발해야 하는 상황에서 스펨 메일이 사진으로 오거나 스팸이 아닌 것처럼 가장해서 온다면 필터링에 한계가 있겠지?</em> </span></p>
<p><span style="color: gray;"><em>🧐 머신 러닝은 이러한 명시적 프로그래밍의 한계를 보완하기 위해서 만들어진 기술로 인간이 직접 프로그래밍 하지 않아도 컴퓨터가 알아서 학습 후 필터링해준는 것!</em></span></p>
<hr />
<h1 id="💡-왜-머신러닝을-사용하는가">💡 왜 머신러닝을 사용하는가?</h1>
<p><span style="color: gray;"><em>🧐 위에서 본 스팸 메일 필터링을 예시로 왜 머신러닝을 사용해야 하는지 더 구체적으로 알아보자.</em></span></p>
<h3 id="전통적-프로그래밍-기법에-기반을-둔-스팸-필터">전통적 프로그래밍 기법에 기반을 둔 스팸 필터</h3>
<ul>
<li>전통적인 접근 방법에서는 문제가 어려워지면 규칙이 점점 길고 복잡해지므로 유지 보수하기 매우 힘듦</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/f1002884-6391-447d-b67f-3d694fe47730/image.png" /></p>
<p>1단계 ) 문제 연구: 스팸에 어떤 단어들이 주로 나타나는지 살펴보기
2단계 ) 규칙 작성: 발견한 각 패턴을 감지하는 알고리즘을 작성하여 스팸으로 분류
3단계 ) 평가 및 오차 분석: 프로그램 테스트 및 성능 테스트를 위한 1&amp; 2단계 반복</p>


<h3 id="머신러닝-기법에-기반을-둔-스팸-필터">머신러닝 기법에 기반을 둔 스팸 필터</h3>
<ul>
<li>스팸에 자주 나타나는 패턴을 감지하여 어떤 단어와 구절이 스팸 메일을 판단하는데 좋은 기준인지 자동 학습함</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/582fb501-6886-46b7-9c77-83d194c69f6c/image.png" /></p>
<p>⇀ 프로그램이 간결해지고 유지 보수가 쉬우며 정확도가 높음</p>


<p><span style="color: gray;"><em>🧐 그렇다면 머신러닝이 유용한 또 다른 분야는?.</em></span></p>
<h3 id="전통적인-방식으로는-너무-복잡하거나-알려진-알고리즘이-없는-문제-예-음성인식">전통적인 방식으로는 너무 복잡하거나, 알려진 알고리즘이 없는 문제 (예: 음성인식)</h3>
<ul>
<li>각 단어를 녹음한 샘플을 사용해 스스로 학습하는 알고리즘을 작성하는 것이 현재 가장 좋은 솔루션임</li>
</ul>



<h3 id="데이터-마이닝data-mining">데이터 마이닝(data mining)</h3>
<ul>
<li>머신러닝 기술을 적용해서 대용량 데이터를 분석하면 겉으로는 보이지 않던 패턴을 발견할 수 있음을 의미하는 개념</li>
</ul>



<h3 id="✅-정리">✅ 정리</h3>
<blockquote>
<p><strong>머신러닝이 뛰어난 분야</strong></p>
</blockquote>
<ul>
<li>기존 솔루션으로는 많은 수동 조정과 규칙이 필요한 문제</li>
<li>전통적인 방식으로는 해결 방법이 없는 복잡한 문제</li>
<li>유동적인 환경: 머신러닝 시스템은 새로운 데이터에 적응할 수 있음</li>
<li>복잡한 문제와 대량의 데이터에서 통찰 얻기</li>
</ul>
<hr />
<h1 id="💡-머신러닝-시스템의-종류">💡 머신러닝 시스템의 종류</h1>
<p><span style="color: gray;"><em>🧐 머신러닝 시스템의 종류는 매우 방대하므로 넓은 범주에서 분류해보자.</em></span></p>
<h4 id="✔-사람-감독-하에-훈련하는-것인지-그렇지-않은-것인지">✔ 사람 감독 하에 훈련하는 것인지 그렇지 않은 것인지</h4>
<p><code>지도학습</code> <code>비지도학습</code> <code>준지도학습</code> <code>강화학습</code></p>
<h4 id="✔-실시간으로-점진적인-학습을-하는지-아닌지">✔ 실시간으로 점진적인 학습을 하는지 아닌지</h4>
<p><code>온라인 학습</code> <code>배치 학습</code></p>
<h4 id="✔-단순하게-알고-있는-데이터-포인트와-새-데이터-포인트를-비교하는-것인지-아니면-과학자들이-하는-것처럼-훈련-데이터에서-패턴을-발견하여-예측-모델을-만드는지">✔ 단순하게 알고 있는 데이터 포인트와 새 데이터 포인트를 비교하는 것인지 아니면 과학자들이 하는 것처럼 훈련 데이터에서 패턴을 발견하여 예측 모델을 만드는지</h4>
<p><code>사례 기반 학습</code> <code>모델 기반 학습</code></p>


<p><span style="color: gray;"><em>🧐 조금 더 자세히 알아보자.</em></span></p>
<h2 id="📍-분류-기준-①---학습하는-동안의-감독-형태나-정보량">📍 분류 기준 ① - 학습하는 동안의 감독 형태나 정보량</h2>
<p><span style="color: red;"><code>지도학습</code> <code>비지도학습</code> <code>준지도학습</code> <code>강화학습</code></span></p>
<h3 id="1-지도학습-supervised-learning">1. 지도학습 (Supervised Learning)</h3>
<blockquote>
<p>알고리즘에 주입하는 훈련 데이터에 <strong>레이블</strong>(= 원하는 답)이 포함</p>
</blockquote>
<p>컴퓨터에게 수많은 <code>문제</code>와 <code>문제에 대한 답</code>을 가르치고, 컴퓨터가 새롭게 습득한 지식을 사용하여 작업을 수행
<img alt="" src="https://velog.velcdn.com/images/heerang/post/c51d75ee-2aeb-49d6-befa-a53f8f6ee930/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/9365827c-d401-4cf8-8388-c75cd2a35a35/image.png" /></p>
<p><span style="color: gray;"><em>🧐 전형적인 지도 학습의 작업에는 분류와 회귀가 있는데 이 둘에 대해 알아보자.</em></span></p>
<blockquote>
<p><strong>분류</strong> (Classification)
전형적인 지도 학습 작업으로 비연속적인 범주형 값을 분류하는 것 (A냐 B냐)</p>
</blockquote>
<ul>
<li>예측하고 싶은 결과가 이름 혹은 문자</li>
<li>예시) 스팸 메일 분류</li>
</ul>
<blockquote>
<p><strong>회귀</strong> (Regression)
예측 변수라 부르는 특성(주행거리, 연식, 브랜드 등)을 사용해 타깃 수치를 예측하는 것</p>
</blockquote>
<ul>
<li>예측하고 싶은 결과가 수치</li>
<li>예시) 중고차 가격 예측</li>
</ul>




<h3 id="2-비지도학습-unsupervised-learning">2. 비지도학습 (Unsupervised Learning)</h3>
<blockquote>
<p>훈련 데이터에 레이블(= 원하는 답) 없이 시스템이 아무런 도움 없이 학습</p>
</blockquote>
<p>컴퓨터 스스로 어떻게 해야 하는지를 학습하게 하고, 이를 통해 데이터 내의 구조와 패턴을 파악</p>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/77a0fb41-f03b-4a8e-8e24-f71bc4498791/image.png" /></p>





<h3 id="3-준지도학습-semi-supervised-learning">3. 준지도학습 (Semi-supervised Learning)</h3>
<blockquote>
<p>일부 타겟 출력이 누락된 훈련 데이터 세트를 사용 (레이블이 일부만 있는 데이터)</p>
</blockquote>
<p>지도 학습과 비지도 학습의 중간 형태로, 일부 레이블이 지정된 데이터와 그렇지 않은 데이터 모두를 활용</p>




<h3 id="4-강화-학습-reinforcement-learning">4. 강화 학습 (Reinforcement Learning)</h3>
<blockquote>
<p>상호작용을 통해 학습하는 계산 접근 방식</p>
</blockquote>
<p>시행착오를 통해 목표를 달성하기 위한 최적의 행동 양식을 스스로 찾아내며, 이 과정에서 보상 시스템을 통해 학습을 가속화</p>
<ul>
<li>예시: 쥐가 미로를 탈출하는 게임에서 쥐의 행동에 따라 값으로 지정된 보상과 벌점을 주며 보상이 많은 쪽으로 학습을 시키는 것</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/01b9af78-09e8-4c99-b803-6974bbb49e36/image.png" /></p>


<h2 id="📍-분류-기준-②---입력-데이터의-스트림으로부터-점진적으로-학습할-수-있는지-여부">📍 분류 기준 ② - 입력 데이터의 스트림으로부터 점진적으로 학습할 수 있는지 여부</h2>
<p><span style="color: red;"><code>배치학습</code> <code>온라인학습</code></span></p>
<h3 id="1-배치-학습-batch-learning">1. 배치 학습 (Batch Learning)</h3>
<blockquote>
<p>점진적 학습 <strong>불가능</strong>! 가용한 데이터를 모두 사용해 훈련시켜야 함</p>
</blockquote>
<p>시간과 자원을 많이 소모하므로 일반적으로 오프라인에서 수행되는 오프라인 학습</p>
<p>✔ 특징</p>
<ul>
<li><p>가용한 데이터를 모두 사용해서 훈련해야 하므로 시스템이 <strong>전체적으로 학습</strong>되며 <strong>점진적으로 학습할 수 없음</strong></p>
</li>
<li><p>(-) 새로운 데이터에 대해 학습하려면 추가적인 학습을 진행하는 것이 아닌 전체 데이터를 사용하여 시스템의 새로운 버전을 처음부터 다시 학습</p>
</li>
<li><p>(-) 전체 데이터셋을 사용해 훈련한다면 많은 컴퓨팅 자원이 필요함</p>
</li>
</ul>




<h3 id="2-온라인-학습-online-learning">2. 온라인 학습 (Online Learning)</h3>
<blockquote>
<p>데이터를 순차적으로 한 개씩 또는 미니배치(mini-batch)라 부르는 작은 묶음 단위로 주입하여 시스템을 훈련시킴</p>
</blockquote>
<p>✔ 특징</p>
<ul>
<li>(+) 매 학습 단계가 빠르고 비용이 적게 들어 시스템은 데이터가 도착하는 대로 즉시 학습할 수 있음</li>
<li>(+) 연속적으로 데이터를 받고 (like 주식가격) 빠른 변화에 스스로 적응해야 하는 시스템에 적합함</li>
<li>(+) 컴퓨팅 자원이 제한된 경우에도 효율적인 학습 방법</li>
<li>(- ) 시스템에 나쁜 데이터가 주입되었을 때 시스템 성능이 점진적으로 감소함

</li>
</ul>
<p>🚨** 참고**
<span style="color: gray;"><em>이 경우 전체 프로세스는 보통 실시간 시스템에서 수행되는 것이 아닌, <strong>오프라인</strong>으로 실행!</em></span>
<span style="color: gray;"><em>온라인 학습이라는 이름때문에 헷갈리지 말고 <strong>점진적인 학습</strong>이라고 생각하자.</em></span></p>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/3751298a-58eb-49f0-9905-1739baef39ce/image.png" /></p>


<h2 id="📍-분류-기준-③---어떻게-일반화되는가">📍 분류 기준 ③ - 어떻게 일반화되는가</h2>
<p><span style="color: red;"><code>사례 기반 학습</code> <code>모델 기반 학습</code></span></p>
<h3 id="1-사례-기반-학습-instance-based-learning">1. 사례 기반 학습 (Instance-based Learning)</h3>
<blockquote>
<p>시스템이 훈련 샘플을 <strong>기억함으로써 학습</strong>하고, <strong>유사도 측정</strong>을 사용해 새로운 데이터와 학습한 샘플을 비교하는 식으로 일반화함</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/5e1ae2d0-bc51-409f-84c2-de965f26a5ca/image.png" /></p>




<h3 id="2-모델-기반-학습-model-based-learning">2. 모델 기반 학습 (Model-based Learning)</h3>
<blockquote>
<p>샘플들의 모델을 만들어 예측에 사용하는 것</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/ba73288d-1c77-4279-82a1-d36108bf1c08/image.png" /></p>
<hr />
<h1 id="💡-머신러닝의-주요-도전-과제">💡 머신러닝의 주요 도전 과제</h1>
<p><span style="color: gray;"><em>🧐 학습 알고리즘을 선택해서 어떤 데이터에 훈련시킬 때 문제가 될 수 있는 것은 나쁜 알고리즘과 나쁜 데이터! <strong>나쁜 데이터</strong>에 대해 먼저 알아보자.</em></span></p>
<h3 id="나쁜-데이터">나쁜 데이터</h3>
<h4 id="✔-충분하지-않는-양의-훈련-데이터">✔ 충분하지 않는 양의 훈련 데이터</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/22b9cd91-5bd9-4b64-89c9-f60f7017d862/image.png" /></p>
<h4 id="✔-대표성-없는-훈련-데이터">✔ 대표성 없는 훈련 데이터</h4>
<blockquote>
<p><strong>샘플링 잡음</strong>(sampling noise) 
샘플이 작을 때 <strong>우연에 의한 대표성 없는 데이터</strong> 존재</p>
</blockquote>
<blockquote>
<p><strong>샘플링 편향</strong>(sampling bias)
샘플이 클 때 <strong>표본 추출 방법이 잘못되면</strong> 대표성을 띠지 못할 수 있음</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/403fef3a-60c8-4421-9802-cd90e7a0b3dd/image.png" /></p>
<h4 id="✔-낮은-품질의-데이터">✔ 낮은 품질의 데이터</h4>
<p>일부 샘플이 <strong>이상치</strong>라는 게 명확하면, 간단히 그것들을 무시하거나 수동으로 잘못된 것을 고치는 것이 좋음</p>
<p>샘플에 특성 몇 개가 빠져있다면, 해당 특성을 모두 무시하거나 / 샘플을 무시하거나 / 빠진 값을 채우거나 / 해당 특성을 넣은 모델과 제외한 모델을 따로 훈련시킬 지  등을 결정해야 함</p>


<h4 id="✔-관련-없는-특성">✔ 관련 없는 특성</h4>
<blockquote>
<p><strong>특성 선택</strong>(feature selection)
훈련에 가장 유용한 특성 선택</p>
</blockquote>
<blockquote>
<p><strong>특성 추출</strong>(feature extraction)
특성을 결합하여 더 유용한 특성을 만듦</p>
</blockquote>


<p><span style="color: gray;"><em>🧐 지금까지 나쁜 데이터의 사례였고, 이제부터 나쁜 알고리즘에 대해 살펴보자.</em></span></p>
<h3 id="나쁜-알고리즘">나쁜 알고리즘</h3>
<h4 id="✔-훈련-데이터-과대적합-overfitting">✔ 훈련 데이터 과대적합 (overfitting)</h4>
<blockquote>
<p>모델이 훈련데이터에 잘 맞지만 일반성이 떨어지는 것</p>
</blockquote>
<ul>
<li>훈련데이터에 있는 잡음의 양에 비해 모델이 너무 복잡할 때 일어남</li>
<li>(-) 과학습, 과분산(high variance), 비슷한 입력에 부정확 반응 결과</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/3f19b0d3-b35a-45b0-b25c-3eb35008125b/image.png" /></p>


<p>🚨 <strong>해결 방법</strong></p>
<ul>
<li>파라미터 수가 적은 모델을 선택하거나 훈련데이터에 있는 특성 수를 줄이거나, 모델에 제약을 가하여 단순화시키기</li>
<li>훈련데이터를 더 많이 모으기</li>
<li>훈련데이터의 잡음을 줄이기</li>
</ul>


<h4 id="✔-훈련-데이터-과소적합-underfitting">✔ 훈련 데이터 과소적합 (underfitting)</h4>
<blockquote>
<p>과대적합의 반대 개념</p>
</blockquote>
<ul>
<li>모델이 단순해서 데이터의 내재된 구조를 학습하지 못할 때 발생</li>
<li>(-) 데이터 해석 능력저하, 과편향(high bias), 여러가지 입력에 제대로 반응불가
<img alt="" src="https://velog.velcdn.com/images/heerang/post/2bf64137-1c33-45d6-afe8-d17e28034c15/image.png" /></li>
</ul>


<p>🚨 <strong>해결 방법</strong></p>
<ul>
<li>모델 파라미터가 더 많은 강력한 모델을 선택</li>
<li>학습 알고리즘에 더 좋은 특성을 제공</li>
<li>모델의 제약을 줄이기</li>
</ul>
<hr />
<h1 id="💡-테스트와-검증">💡 테스트와 검증</h1>
<p><span style="color: gray;"><em>🤔 모델이 새로운 샘플에 잘 일반화 되었는지 어떻게 알지? 실제 서비스에 모델을 넣어 모니터링? 그치만 모델이 나쁘다면?</em></span></p>
<p><span style="color: gray;"><em>🧐 훈련 데이터를 <strong>훈련 세트와 테스트 세트 두 개로 나누는 방법</strong>에 대해 알아보자.</em></span></p>
<h3 id="✔-훈련-및-테스트-데이터-세트로-나누어-검증">✔ 훈련 및 테스트 데이터 세트로 나누어 검증</h3>
<ul>
<li><p>훈련 데이터: 모델을 훈련하는 데 사용</p>
</li>
<li><p>테스트 데이터: 모델을 테스트하는 데 사용</p>
</li>
<li><p>일반화 오차 (또는 외부 샘플 오차): 새로운 샘플에 대한 오류 비율</p>
</li>
</ul>
<blockquote>
<p>테스트 세트에서 모델을 평가함으로써 이 일반화 오차에 대한 <strong>추정값</strong>을 얻고, 이 추정값으로 이전에 본 적 없는 새로운 샘플에 모델이 얼마나 잘 작동할지 예측 가능</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/22b3f93c-8c82-4fd6-bf05-3b3e8d5dd36b/image.png" /></p>
<blockquote>
<p>훈련 오차가 낮지만 일반화 오차가 높다면 이는 모델이 훈련 데이터에 <strong>과대적합</strong>(overfitting) 되었다는 의미</p>
</blockquote>
<p>✔ 참고)  데이터의 80%를 훈련에 20%는 테스트용으로 분리하며, 데이터셋 크기에 따라 비율이 다름</p>


<h3 id="✔-머신러닝-모델-성능-평가-방법">✔ 머신러닝 모델 성능 평가 방법</h3>
<h4 id="홀드아웃-검증-기법-holdout-validation">홀드아웃 검증 기법 (holdout validation)</h4>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/0fd683b3-8653-48f8-a4ea-47a1e74cd414/image.png" />
😨 훈련데이터와 테스트 데이터로만 나눠서 모델 성능을 평가하면 테스트 데이터가 모델의 파라미터 설정에 큰 영향을 미치게 되어 모델이 테스트 데이터에 오버피팅될 가능성이 있게 됨</p>
</blockquote>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/4efcb7c9-6854-466d-9b8e-7a83fde0046f/image.png" />
😎 그래서 훈련 데이터와 테스트 데이터 둘로만 나누지 않고, 훈련 데이터의 일부를 떼어내어 검증 데이터(validation data)라고 하고, 이를 사용해 여러 후보 모델을 평가하고 가장 좋은 하나를 선택!</p>
</blockquote>
<p><strong>훈련셋</strong>을 이용해서 모델을 훈련시키고,
<strong>검증셋</strong>으로 모델의 최적 파라미터들을 찾아가고,
<strong>테스트셋</strong>을 이용해서 모델의 성능을 평가!</p>


<h4 id="교차-검증-기법-cross-validation">교차 검증 기법 (cross-validation)</h4>
<blockquote>
<p>작은 검증 데이터를 여러 개를 사용해 반복적인 검증을 수행</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/83b367b2-e972-487f-9c25-2df8daec85a5/image.png" /></p>
<p>✔ <strong>K-fold 교차검증</strong>
데이터를 K개의 subset으로 분리하고 하나의 subset만 테스트에 사용하고 나머지 k-1개의 subset은 훈련에 사용함 (K번 반복)</p>
<ul>
<li>(+) 모든 모델의 평가를 평균하면 훨씬 정확한 성능을 측정할 수 있음</li>
<li>(- ) 훈련 시간이 검증 세트의 개수에 비례해 늘어남</li>
</ul>