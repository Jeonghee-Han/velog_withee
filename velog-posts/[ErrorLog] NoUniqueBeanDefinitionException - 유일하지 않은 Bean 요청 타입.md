# [ErrorLog] NoUniqueBeanDefinitionException - 유일하지 않은 Bean 요청 타입

**Published:** Wed, 05 Nov 2025 01:53:39 GMT
**Link:** https://velog.io/@heerang/ErrorLog-NoUniqueBeanDefinitionException-%EC%9C%A0%EC%9D%BC%ED%95%98%EC%A7%80-%EC%95%8A%EC%9D%80-Bean-%EC%9A%94%EC%B2%AD-%ED%83%80%EC%9E%85

---

<h3 id="에러로그">에러로그</h3>
<p><code>org.springframework.beans.factory.NoUniqueBeanDefinitionException</code></p>
<ul>
<li>원인 코드: <code>ctx.getBean(Washer.class);</code></li>
<li>상황: Spring 컨테이너(ctx)에게 Washer 타입의 Bean을 달라고 요청</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/8c909608-11ad-4aec-bc87-2d067429fcd2/image.jpg" /></p>
<hr />
<h3 id="원인분석">원인분석</h3>
<p><strong>&quot;요청한 타입의 Bean이 유일(Unique)하지 않다&quot;</strong></p>
<ul>
<li><p>Spring 컨테이너가 Washer 타입의 Bean을 찾으려고 보니, 해당 타입(또는 인터페이스)으로 등록된 Bean이 2개 이상임. (SWasher와 LWasher) </p>
</li>
<li><p>Spring은 타입만으로는 이 둘 중 어떤 것을 정확히 주입해야 할지 모르기 때문에(모호성 발생) 예외를 발생</p>
</li>
</ul>
<hr />
<h3 id="해결방법">해결방법</h3>
<p>getBean() 메소드를 호출할 때, <strong>타입(Washer.class)</strong>뿐만 아니라 Bean의 고유한 이름(ID)(여기서는 &quot;IWasher&quot;)을 문자열로 함께 지정</p>
<p><code>ctx.getBean(&quot;IWasher&quot;, Washer.class);</code>
<img alt="" src="https://velog.velcdn.com/images/heerang/post/827af72b-76a9-4690-b746-dea0d3c7287d/image.jpg" /></p>