# [ErrorLog] UnsupportedClassVersionError - 클래스 파일 버전 불일치

**Published:** Wed, 05 Nov 2025 01:46:39 GMT
**Link:** https://velog.io/@heerang/ErrorLog-UnsupportedClassVersionError-%ED%81%B4%EB%9E%98%EC%8A%A4-%ED%8C%8C%EC%9D%BC-%EB%B2%84%EC%A0%84-%EB%B6%88%EC%9D%BC%EC%B9%98

---

<h3 id="에러로그">에러로그</h3>
<pre><code class="language-java">Exception in thread &quot;main&quot; java.lang.UnsupportedClassVersionError:
org/springframework/context/ApplicationContext has been compiled by a more recent version of the Java Runtime (class file version 61.0),
this version of the Java Runtime only recognizes class file versions up to 52.0</code></pre>
<hr />
<h3 id="원인분석">원인분석</h3>
<ul>
<li>pom.xml은 JDK 17로 수정했지만, IDE에 반영되지 않음</li>
<li>즉, “빌드된 클래스 파일 버전”과 “실행 JVM 버전” 불일치</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/2935f5c3-c53f-45f1-9969-4d0df54b0b60/image.png" />
<code>xml</code>에서 JDK 버전 17로 변경해두고 <strong>Maven Project Update</strong> 안함</p>
<hr />
<h3 id="해결방법">해결방법</h3>
<p>pom.xml 수정 후
👉 Ctrl + Shift + O (Maven Reload)</p>