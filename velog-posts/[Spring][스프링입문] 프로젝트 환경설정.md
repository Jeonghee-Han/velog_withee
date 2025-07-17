<h1 id="🌱-프로젝트-환경설정">🌱 프로젝트 환경설정</h1>
<hr />
<h2 id="프로젝트-생성">프로젝트 생성</h2>
<p><a href="https://start.spring.io/"><strong>Spring Initializar</strong></a>
SpringBoot 기반으로 프로젝트를 만들어주는 사이트
<img alt="" src="https://velog.velcdn.com/images/heerang/post/214b3e01-b0b1-4e71-af03-cd886afad868/image.png" /></p>
<p><strong>Project</strong> ⇀ 필요한 라이브러리를 불러오고 관리해주는 툴</p>
<ul>
<li>Gradle: 요즘 많이 사용 (Gradle-Groovy)</li>
<li>Maven: 과거에 많이 사용</li>
</ul>
<p><strong>Language</strong>: Java</p>
<p><strong>Spring Boot</strong>: 3.X.X</p>
<ul>
<li>SNAPSHOT, M1과 같은 경우 아직 만들고 있는 버전으로 정식 버전 X</li>
</ul>
<p><strong>Packaging</strong>: Jar</p>
<p><strong>Project Metadata</strong></p>
<ul>
<li>Group ⇀ 기업 도메인 명<ul>
<li>Java의 패키지명 규칙을 따름</li>
</ul>
</li>
<li>Artifact ⇀ 빌드되어 나오는 결과물<ul>
<li>소문자로만 작성</li>
<li>특수문자 사용 X</li>
</ul>
</li>
<li>Name ⇀ 빌드되어 나오는 결과물</li>
</ul>
<p><strong>Dependencies</strong></p>
<ul>
<li>Spring Web</li>
<li>Thymeleaf ⇀ html을 만들어주는 템플릿엔진</li>
</ul>
<blockquote>
<p><strong>(참고) IntelliJ Gradle 대신 자바 직접 실행</strong></p>
</blockquote>
<ul>
<li>최근 IntelliJ 버전은 Gradle을 통해서 실행하는 것이 기본 설정, But 실행 속도가 느림</li>
<li>다음과 같이 설정하면 Gradle을 통하지 않고 Java로 바로 실행해서 실행 속도가 더 빠름
<img alt="" src="https://velog.velcdn.com/images/heerang/post/cfb02490-6702-4bf4-aa43-519eb537bc63/image.png" /></li>
<li><code>IntelliJ</code> → <code>Build, Execution, Deployment</code> → <code>Gradle</code><ul>
<li><code>Build and run using</code> → <code>IntelliJ IDEA</code></li>
<li><code>Run tests using</code> → <code>IntelliJ IDEA</code></li>
</ul>
</li>
</ul>
<hr />
<h2 id="라이브러리-살펴보기">라이브러리 살펴보기</h2>
<blockquote>
<p>Gradle은 의존관계가 있는 라이브러리들을 함께 다운로드</p>
</blockquote>
<p><code>&gt; build.gradle</code></p>
<pre><code class="language-java">plugins {
    id 'java'
    id 'org.springframework.boot' version '3.2.3'
    id 'io.spring.dependency-management' version '1.1.4'
}

group = 'inflearn'
version = '0.0.1-SNAPSHOT'

java {
    sourceCompatibility = '17'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

tasks.named('test') {
    useJUnitPlatform()
}

</code></pre>
<h3 id="스프링부트-라이브러리">스프링부트 라이브러리<img alt="" src="https://velog.velcdn.com/images/heerang/post/eba35cb0-b814-4aeb-9f3a-d0dd8bd7815e/image.png" /></h3>
<p><strong>spring-boot-starter-thymeleaf</strong> ⇀ 타임리프 템플릿 엔진(View)</p>
<p> <strong>spring-boot-starter-web</strong></p>
<ul>
<li>spring-webmvc: 스프링 웹 MVC</li>
<li>spring-boot-starter-tomcat: 톰캣(서버)
<img alt="" src="https://velog.velcdn.com/images/heerang/post/cca10a03-4d12-4df3-b293-5252f26b2567/image.png" /></li>
</ul>
<p><strong>spring-boot-starter(공통)</strong>: <code>스프링 부트</code> + <code>스프링 코어</code> + <code>로깅</code></p>
<ul>
<li>spring-boot &gt; spring-core</li>
<li>spring-boot-starter-logging &gt; slf4j, lobgack<ul>
<li>현업에서는 <code>System.out.println</code> 을 사용하지 않고 로그파일을 관리하여 테스트를 진행</li>
<li><code>slf4j</code> = 인터페이스
<code>lobgack</code> = 실제 로그를 어떤 구현체로 출력할지
⇀ 요즘은 이 두 가지 조합으로 활용하는 것이 표준</li>
</ul>
</li>
</ul>
<h3 id="테스트-라이브러리">테스트 라이브러리<img alt="" src="https://velog.velcdn.com/images/heerang/post/013751b2-3bfd-4c16-bf53-4a9627243ae0/image.png" /></h3>
<p><strong>spring-boot-starter-test</strong></p>
<ul>
<li><strong>junit</strong> ⇀ Java에서 주로 사용하는 테스트 프레임워크</li>
<li>spring-test ⇀ 스프링과 통합해서 테스트할 수 있도록 지원하는 라이브러리</li>
<li>mockito ⇀ 목 라이브러리</li>
<li>assertj ⇀ 테스트 코드를 더 편하게 작성하도록 도와주는 라이브러리</li>
</ul>
<hr />
<h2 id="view-환경설정">View 환경설정</h2>
<h3 id="springboot가-제공하는-welcome-page-기능">Springboot가 제공하는 Welcome Page 기능</h3>
<blockquote>
<p>Welcome Page란, 도메인만 누르고 들어왔을 때 나오는 페이지</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/317ab0e8-9309-4f99-b2a7-527077ebfa4b/image.png" /></p>
<pre><code class="language-html">&lt;!DOCTYPE HTML&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Hello&lt;/title&gt;
    &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
&lt;/head&gt;
&lt;body&gt;
Hello
&lt;a href=&quot;/hello&quot;&gt;hello&lt;/a&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<ul>
<li><code>resources</code> &gt; <code>static</code>에서 <code>index.html</code> 파일을 생성하면 Welcome page 기능을 제공</li>
<li>Welcome page는 정적 페이지로 <code>index.html</code>파일을 Web Server가 그대로 웹 브라우저에 던져준 것</li>
<li>But 템플릿 엔진을 사용하면 파일 구조를 원하는대로 바꿀 수 있음</li>
</ul>
<h3 id="thymeleaf-템플릿-엔진">thymeleaf 템플릿 엔진</h3>
<p>thymeleaf 템플릿 엔진 동작 확인 ⇀ <code>localhost:8080/hello</code> 실행
<img alt="" src="https://velog.velcdn.com/images/heerang/post/f4a32602-f63a-4f8d-b483-d46807916367/image.png" /></p>
<ol>
<li>웹 브라우저에서 <code>localhost:8080/hello</code>를 던지면 Springboot에 내장된 Tomcat Server에서 받아서 Spring에 던짐</li>
<li>Spring은 Controller에 있는 hello 메서드를 실행시키고 model에 <code>data:hello!</code>를 넣어줌</li>
<li>Controller에서는 <code>&quot;hello&quot;</code>를 return하므로 templates에 있는 <code>hello.html</code>을 찾아서 템플릿 엔진이 처리해줌</li>
</ol>
<ul>
<li><code>resources:templates/</code> + {ViewName} + <code>.html</code></li>
</ul>
<hr />
<h2 id="빌드하고-실행하기">빌드하고 실행하기</h2>
<p><code>&gt; cmd 창으로 이동</code></p>
<pre><code>E:\inflearn-spring\inflearn-spring&gt;gradlew
</code></pre><blockquote>
<p>🚨 <strong><em>ERROR</em></strong> 
문제: 위 명령어를 실행했더니 아래와 같은 에러 발생
원인: 해당 프로젝트는 JDK 17, Springboot 3.X.X 버전이나 윈도우에 환경변수로 잡힌 JDK 버전은 17이 아닌 11
해결 방법: 환경 변수에서 JDK 버전을 17로 다시 잡고 명령어 실행
참고 문헌: <a href="https://www.inflearn.com/questions/1147739/%EC%9E%90%EB%B0%94-%EB%B2%84%EC%A0%84%EC%9D%B4-%EB%8B%A4%EB%A5%B4%EA%B2%8C-%EB%82%98%EC%98%B5%EB%8B%88%EB%8B%A4">인프런 Q&amp;A</a></p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/648ad32a-e476-48a4-bba7-ad2f89f42ed9/image.png" /></p>
<p><del>다른 프로젝트에서 JKD 11로 서버를 배포하는 과정에 있으므로 환경 변수 재설정 및 빌드 skip</del></p>
<p>빌드 성공 시 build 폴더가 생기는데 그 중 libs에 생성된 <code>hello-spring-0.0.1-SNAPSHOT.jar</code>를 실행시키면 Sprnig이 뜸</p>
<pre><code>cd build/libs
java -jar hello-spring-0.0.1-SNAPSHOT.jar</code></pre><p>추후에 서버 배포 시, jar 파일을 복사해서 서버에 넣고 위 명령어를 실행하면 서버에서도 Spring이 동작</p>