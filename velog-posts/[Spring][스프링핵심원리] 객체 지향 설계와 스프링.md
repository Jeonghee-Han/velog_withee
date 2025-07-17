<h1 id="🌱-객체-지향-설계와-스프링">🌱 객체 지향 설계와 스프링</h1>
<hr />
<h2 id="java의-추운-겨울과-spring봄의-탄생">JAVA의 추운 겨울과 Spring(봄)의 탄생</h2>
<p>✔ 2000년 초반 JAVA 표준 기술 <strong><code>EJB</code></strong>(Enterprise Java Beans)</p>
<p>당시 EJB는 분산 기능이 탁월하다는 장점이 있었지만, 오픈 소스가 아니라서 값비싼 Server를 구매해야 했고 또한 개발자들이 사용하기에 복잡하고 느리다는 치명적인 단점을 가지고 있었음</p>
<p>마틴 파울러는 단순한 자바 오브젝트에 도메인 로직을 사용하는 것이 더 좋은데, 그 평범한 자바 오프젝트를 대체할 용어가 없어서 사람들이 사용하지 않는 것이라 판단하여 해당 오브젝트에 POJO(Plan Old Java Object)라는 명칭을 부여</p>
<p>하지만 POJO로 돌아가는 것은 로우 레벨을 다루자는 말이라서 적절한 대안이 필요했고, 이때 두명의 개발자가 POJO 프레임워크를 개발함</p>
<h4 id="📌-rod-johnson---spring">📌 Rod Johnson - Spring</h4>
<p>EJB보다 단순하고 편리하게 사용할 수 있도록 만든 기술</p>
<h4 id="📌-gavin-king---hibernate">📌 Gavin King - Hibernate</h4>
<p>EJB Entity Bean 기술을 대체하여 JPA(Java Persistence API)의 새로운 표준을 정의한 기술
</p>
<hr />
<h2 id="스프링이란">스프링이란</h2>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/6601892a-bd14-4fcf-97cf-7a63765e9c3e/image.png" /></p>
<h3 id="⭐-spring-framework">⭐ Spring Framework</h3>
<ul>
<li><strong>✔ 스프링의 핵심 기술: 스프링 DI 컨테이너, AOP, 이벤트 등</strong></li>
<li>웹 기술: 스프링 MVC, 스프링 WebFlux</li>
<li>데이터 접근 기술: 트랜잭션, JDBC, ORM 지원, XML 지원</li>
<li>기술 통합: 캐시. 임일, 원격접근, 스케줄링</li>
<li>테스트: 스프링 기반 테스트 지원</li>
<li>언어: 코틀린, 그루비</li>
</ul>
<blockquote>
<p>최근에는 <strong>Spring Boot</strong>를 통해서 Spring Framework의 기술들을 편리하게 사용</p>
</blockquote>
<h3 id="spring-boot">Spring Boot</h3>
<ul>
<li>스프링을 편리하게 사용할 수 있도록 지원, 최근에는 기본으로 사용</li>
<li>(+) Tomcat 같은 <strong>웹 서버를 내장</strong>해서 별도의 웹 서버를 설치하지 않아도 OK</li>
<li>(+) <strong>단독</strong>으로 실행할 수 있는 스프링 웹 애플리케이션을 <strong>쉽게</strong> 생성</li>
<li>(+) 라이브러리를 쓸 때 여러 개를 묶어서 가져왔어야 했는데 이제는 <strong>starter 종속성을 제공하여 빌드 구성이 쉬움</strong></li>
<li>(+) <strong>스프링과 외부 라이브러리를 자동으로 구성</strong>해줘서 개발자가 이 둘이 맞는 버전을 따로 고려하지 않아도 됨</li>
<li>(+) 메트릭, 상태 확인, 외부 구성 같은 프로덕션 준비 기능 제공</li>
<li>(+) 관례에 의한 간결한 설정</li>
</ul>


<h3 id="spring🤔❓">Spring🤔❓</h3>
<blockquote>
<p>스프링이라는 단어는 문맥에 따라 다르게 사용됨</p>
</blockquote>
<ul>
<li>스프링 DI 컨테이너 기술</li>
<li>스프링 프레임워크</li>
<li><strong>스프링 부트, 스프링 프레임 워크 등을 모두 포함한 스프링 생태계</strong>

</li>
</ul>
<h3 id="스프링을-만든-이유">스프링을 만든 이유</h3>
<blockquote>
<p>✅ 어떤 복잡한 기술도 기술의 <strong>핵심 개념</strong>은 단순!</p>
</blockquote>
<ul>
<li>이 기술을 왜 만들었는가?</li>
<li>이 기술의 핵심 컨셉은?</li>
</ul>
<h4 id="✔-스프링의-핵심-개념은">✔ 스프링의 핵심 개념은?</h4>
<ul>
<li><del>웹 어플리케이션을 편하게 만들고, DB 접근을 편리하게 해주는 기술?</del></li>
<li><del>전자정부 프레임워크에서 쓰는 기술?</del></li>
<li><del>웹 서버도 자동으로 띄워주는 기술?</del></li>
<li><del>클라우드, 마이크로서비스를 위한 기술?</del></li>
</ul>
<h4 id="no-이것들은-결과물일-뿐-진짜-핵심은-아래-⇩">NO 이것들은 결과물일 뿐, 진짜 핵심은 아래 ⇩</h4>
<ul>
<li>스프링은 <strong>자바 언어 기반의 프레임워크</strong></li>
<li>자바 언어의 가장 큰 특징은 <strong>객체 지향</strong> 언어라는 점</li>
<li>스프링은 <strong>객체 지향 언어가 가진 강력한 특징(like 다형성)을 살려내는 프레임워크</strong></li>
<li>스프링은 <strong>좋은 객체 지향 애플리케이션을 개발할 수 있게 도와주는 프레임워크</strong>
</li>
</ul>
<hr />
<h2 id="좋은-객체-지향-프로그래밍">좋은 객체 지향 프로그래밍?</h2>
<blockquote>
<p>✅** 객체 지향 특징**
<code>추상화</code> <code>캡슐화</code>     <code>상속</code> <strong><code>다형성</code></strong></p>
</blockquote>
<blockquote>
<p>✅** 객체 지향 프로그래밍**</p>
</blockquote>
<ul>
<li>컴퓨터 프로그램을 <strong>객체</strong>들의 <strong>모임</strong>으로 파악하고자 하는 것</li>
<li>각각의 <strong>객체</strong>는 <strong>메시지</strong>를 주고받고, 데이터를 처리할 수 있음(<strong>협력</strong>)</li>
<li>프로그램을 <strong>유연</strong>하고 <strong>변경</strong>이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됨</li>
</ul>
<h4 id="유연하고-변경이-용이하다는-건-무슨-뜻일까">유연하고 변경이 용이하다는 건 무슨 뜻일까?</h4>
<p>컴포넌트를 쉽고 유연하게 변경하면서 개발할 수 있는 방법 like 레고 블럭 조립 = <strong>다형성</strong>(Polymorphism)</p>
<h3 id="다형성">다형성</h3>
<p>다형성을 이해하기 위해서 세상을 <strong>역할과 구현으로 구분</strong>하여 비유해보자!</p>
<h4 id="🏴-운전자---자동차-예시">🏴 운전자 - 자동차 예시</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/69f99827-161c-465a-a5ad-0ec6f087de0d/image.png" /></p>
<blockquote>
<p>운전자가 K3를 타다가 아반떼로 차를 바꿔도 운전 가능 ⇀ 자동차라는 역할에 대한 구현만 바뀌었기 때문
즉, 자동차가 바뀌어도 운전자에게 영향 X (운전자는 자동차라는 인터페이스에 대해서만 알고 있으면 운전이 가능)</p>
</blockquote>
<ul>
<li>자동차라는 역할을 만들고 구현을 분리한 것은 운전자를 위한 것</li>
<li>운전자 = 클라이언트</li>
<li>클라이언트에게 영향을 주지 않고 새로운 기능을 제공할 수 있음 (새로운 자동차가 나와도 클라이언트를 바꿀 필요 X)</li>
</ul>
<h4 id="🏴-공연-무대-예시">🏴 공연 무대 예시</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/67a51253-a01f-4483-ac80-5057245baebf/image.png" /></p>
<blockquote>
<p>각 역할이 정해져 있고, 배우는 누가 해도 상관 X ⇀ 배우는 대체가 가능</p>
</blockquote>
<h4 id="✔-역할과-구현을-분리하면-세상이-단순해지고-유연해지며-변경이-편리해짐">✔ 역할과 구현을 분리하면 세상이 단순해지고 유연해지며 변경이 편리해짐</h4>
<ul>
<li>(+) 클라이언트는 <strong>대상의 역할(인터페이스)</strong>만 알면 OK</li>
<li>(+) 클라이언트는 구현 대상의 <strong>내부 구조를 몰라도 OK</strong></li>
<li>(+) 클라이언트는 구현 대상의 <strong>내부 구조가 변경되어도 영향 X</strong></li>
<li>(+) 클라이언트는 <strong>구현 대상 자체를 변경해도 영향 X</strong></li>
</ul>


<h4 id="✔-java-언어의-다형성을-활용해서-생각해보자">✔ JAVA 언어의 다형성을 활용해서 생각해보자</h4>
<ul>
<li>역할 = 인터페이스</li>
<li>구현 = 인터페이스를 구현한 클래스, 구현 객체</li>
<li>객체를 설계할 때 역할과 구현을 명확히 분리</li>
<li>객체 설계 시 역할(인터페이스)을 먼저 부여하고, 그 역할을 수행하는 구현 객체 만들기
<img alt="" src="https://velog.velcdn.com/images/heerang/post/7014a113-759e-4b9c-9461-8185268a3159/image.png" /></li>
</ul>
<blockquote>
<p><strong>객체의 협력</strong>이라는 <strong>관계</strong>부터 생각</p>
</blockquote>
<ul>
<li>혼자 있는 객체는 없음</li>
<li><strong>클라이언트는 요청</strong>을 보내고, <strong>서버는 응답</strong>을 주는 협력 관계</li>
</ul>


<h4 id="🏴-java-언어의-다형성-overriding">🏴 Java 언어의 다형성: Overriding</h4>
<blockquote>
<p>오버라이딩(Overriding): 부모-자식 상속 관계에 있는 클래스에서 상위 클래스의 메서드를 하위 클래스에서 재정의하는 것</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/dcf86e80-5bd8-4076-bcff-3f336b5ce26c/image.png" />
결국 Overriding된 Method가 실행되는데, 다형성으로 Interface를 구현한 객체를 실행 시점에 유연하게 변경 가능
<img alt="" src="https://velog.velcdn.com/images/heerang/post/010f4549-7721-4808-b805-861b678f229f/image.png" /></p>
<p>클라이언트는 MemberRepository를 의존 (= <code>의존 관계</code> <code>내가 쟤를 알고 있다</code>)</p>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/e575abde-688e-48c3-ab1d-daa05a8ae5bb/image.png" /></p>
<pre><code class="language-java">public class MemberService {
    private MemberRepository memberRepository = new MemoryMemberRepository();
}</code></pre>
<pre><code class="language-java">public class MemberService {
    private MemberRepository memberRepository = new JdbcMemberRepository();
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/f06e2fe1-da86-43e0-b0ae-27877739f3e0/image.png" />
MemoryMemberRes든 JdbcMemberRes든 부모에 자식을 할당하는 것은 가능하지만, 자식에 부모를 대입하는 것 또는 부모와 전혀 관계가 없는 것은 할당 불가능</p>


<blockquote>
<p>✅ <strong>다형성의 본질</strong></p>
</blockquote>
<ul>
<li>인터페이스를 구현한 객체 인스턴스를 <strong>실행 시점</strong>에 <strong>유연</strong>하게 <strong>변경 가능</strong></li>
<li>다형성의 본질을 이해하려면 <strong>협력</strong>이라는 객체 사이의 관계에서 시작해야 함</li>
<li><strong>클라이언트를 변경하지 않고, 서버의 구현 기능을 유연하게 변경할 수 O</strong></li>
</ul>
<blockquote>
<p>✅ <strong>역할과 구현을 분리하는 다형성의 한계</strong></p>
</blockquote>
<ul>
<li>역할(인터페이스)이 변하면 클라이언트와 서버 모두 큰 변경이 필요
<del>자동차가 비행기로 변한다면?</del> <del>대본 자체가 변경된다면?</del></li>
<li>⇀ <strong>인터페이스를 안정적으로 잘 설계하는 것이 매우 중요</strong></li>
</ul>
<h4 id="스프링과-객체-지향">스프링과 객체 지향</h4>
<p>스프링은 <strong>다형성</strong>을 극대화해서 이요할 수 있도록 도와주며, 스프링에서 이야기하는 제어의 역전(loC), 의존관계 주입(DI)은 다형성을 활용해서 역할과 구현을 편리하게 다룰 수 있도록 도와줌</p>


<hr />
<h2 id="solid">SOLID</h2>
<blockquote>
<p>클린코드로 유명한 로버트 마틴이 좋은 객체 지향 설계의 5가지 원칙을 정리</p>
</blockquote>
<h3 id="원칙-1-srpsingle-responsibility-principle-단일-책임-원칙">원칙 1: SRP(Single Responsibility Principle); 단일 책임 원칙</h3>
<blockquote>
<p><strong><em>&quot;하나의 클래스는 하나의 책임만 가져야 한다.&quot;</em></strong></p>
</blockquote>
<h4 id="하나의-책임">하나의 책임?</h4>
<p>중요한 기준은 <strong>변경</strong>! 변경이 있을 때 파급 효과가 적으면 단일 책임 원칙을 잘 따른 것</p>


<h3 id="⭐-원칙-2-ocpopenclosed-principle-개방-폐쇄-원칙">⭐ 원칙 2: OCP(Open/Closed Principle); 개방-폐쇄 원칙</h3>
<blockquote>
<p><strong><em>&quot;소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.&quot;</em></strong></p>
</blockquote>
<p><del>확장을 하려면 기존 코드를 당연히 변경해야 하는 것 아닌가?</del>
<strong>다형성</strong>을 활용하면 인터페이스를 구현한 새로운 클래스를 하나 만들어서 새로운 기능을 구현하여 위 원칙을 따를 수 O</p>
<h4 id="하지만-ocp-원칙은-분명-문제점이-존재">하지만, OCP 원칙은 분명 문제점이 존재</h4>
<pre><code class="language-java">// 기존 코드
public class MemberService {
    private MemberRepository memberRepository = new MemoryMemberRepository();
}</code></pre>
<pre><code class="language-java">// 변경 코드
public class MemberService {
    private MemberRepository memberRepository = new JdbcMemberRepository();
}</code></pre>
<p>구현 객체를 변경하려면 위와 같이 클라이언트 코드를 변경해야 함
분명 다형성을 사용했지만 OCP 원칙을 따를 수 없는 상황</p>
<h4 id="이-문제를-어떻게-해결할까">이 문제를 어떻게 해결할까</h4>
<p>객체를 생성하고, 연관관계를 맺어주는 별도의 조립, 설정자가 필요 ➡ 스프링 컨테이너의 역할</p>


<h3 id="원칙-3-lspliskov-substitution-principle-리스코프-치환-원칙">원칙 3: LSP(Liskov Substitution Principle); 리스코프 치환 원칙</h3>
<blockquote>
<p><strong><em>&quot;프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.&quot;</em></strong></p>
</blockquote>
<p>즉 다형성에서 하위 클래스는 인터페이스 규약을 다 지켜야 한다는 것</p>
<p>예를 들어, 자동차라는 인터페이스에서 악셀이라는 기능을 구현할 때 악셀은 앞으로 가야한다는 규약이 있는데, 내가 악셀이 뒤로가는 기능을 구현한 클래스를 생성해도 컴파일 오류는 안나지만 다형성을 지원하기 위해 이 원칙을 지켜야 하는 것</p>


<h3 id="원칙-4-ispinterface-segregation-principle-인터페이스-분리-원칙">원칙 4: ISP(Interface Segregation Principle); 인터페이스 분리 원칙</h3>
<blockquote>
<p><strong><em>&quot;특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다.&quot;</em></strong></p>
</blockquote>
<p>자동차라는 인터페이스를 운전과 정비라는 인터페이스로 분리하면, 사용자 클라이언트를 운전자와 정비사 클라이언트로 분리할 수 있음
분리하면 정비 인터페이스 자체가 변해도 운전자 클라이언트에 영향을 주지 않기 때문에 <strong>인터페이스가 명확해지고, 대체 가능성이 높아짐</strong></p>


<h3 id="⭐-원칙-5--dipdependency-inversion-principle-의존관계-역전-원칙">⭐ 원칙 5:  DIP(Dependency Inversion Principle); 의존관계 역전 원칙</h3>
<blockquote>
<p><strong><em>&quot;프로그래머는 추상화에 의존해야지, 구체화에 의존하면 안된다.&quot;</em></strong></p>
</blockquote>
<p>의존성 주입은 이 원칙을 따르는 방법 중 하나</p>
<p>쉽게 말하면, 구현 클래스에 의존하지 말고 인터페이스(=역할)에 의존하라는 뜻
즉 MemberService가 MemberResository 인터페이스만 바라보고 MemoryMemberRepository나 JdbcMemberRepository에 대해서는 몰라야 함</p>
<p>객체 세상도 클라이언트가 인터페이스에 의존해야 유연하게 구현체를 변경할 수 있지, 구현체에 의존하게 되면 변경이 아주 어려움</p>
<h4 id="하지만-ocp에서-설명한-memberservice는-인터페이스에-의존하지만-동시에-구현-클래스도-의존--🚨-dip-위반">하지만, OCP에서 설명한 MemberService는 인터페이스에 의존하지만 동시에 구현 클래스도 의존 &gt; 🚨 DIP 위반</h4>
<pre><code class="language-java">public class MemberService {
    private MemberRepository memberRepository = new MemoryMemberRepository();
}</code></pre>
<p>추상화인 MemberRepository에도 의존하지만, 구체화인 MemoryMemberRepository에도 의존</p>
<h4 id="그럼-뭐-어떻게-해야-해---여기서-잠깐-정리">그럼 뭐 어떻게 해야 해?! - 여기서 잠깐 정리</h4>
<blockquote>
<p>✅ <strong>정리 1</strong></p>
</blockquote>
<ul>
<li>객체 지향의 핵심은 다형성</li>
<li>다형성 만으로는 쉽게 부품을 갈아 끼우듯 개발할 수 X</li>
<li>다형성 만으로는 구현 객체를 변경할 때 클라이언트 코드도 함께 변경됨</li>
<li><strong>다형성 만으로는 OCP, DIP를 지킬 수 X</strong></li>
<li>뭔가 더 필요하다!!!</li>
</ul>


<hr />
<h2 id="다시-스프링-그리고-객체-지향-설계">다시 스프링, 그리고 객체 지향 설계</h2>
<h4 id="스프링-이야기에-왜-객체-지향-이야기가-나오는거지">스프링 이야기에 왜 객체 지향 이야기가 나오는거지?</h4>
<p>스프링은 다음 기술로 다형성과 OCP, DIP를 가능하게 지원해주는 기술</p>
<ul>
<li>DI(Dependency Injection): 의존 관계, 의존성 주입</li>
<li>DI 컨테이너 제공</li>
</ul>
<p>순수하게 Java로 OCP, DIP 원칙들을 지키면서 개발을 해보면 결국 DI 컨테이너를 만들게 됨</p>
<p>DI의 개념은 코드로 짜봐야 필요성을 느끼니까 스프링이 왜 만들어졌는지 다음 시간에 코드로 이해해보자 <del><em>(Coming soon)</em></del></p>



<blockquote>
<p>✅ <strong>정리 2</strong></p>
</blockquote>
<ul>
<li>모든 설계에 역할과 구현을 분리하자</li>
<li>자동차와 공연의 예를 떠올리자</li>
<li>애플리케이션 설계도 공연을 설계하듯 배역만 만들어두고, 배우는 언제든지 <strong>유연하게 변경</strong>할 수 있도록 만드는 것이 좋은 객체 지향 설계</li>
<li>즉 다형성뿐 아니라 OCP, DIP 원칙을 지켜야 하는데, 그렇게 하려면 스프링 DI 컨테이너가 필요</li>
<li>이상적으로는 모든 설계에 인터페이스를 부여하는게 좋지만 추상화라는 비용이 발생</li>
<li>기능을 확장할 가능성이 없다면 구체 클래스를 직접 사용하고 향후 꼭 필요할 때 리펙토링해서 인터페이스를 도입하는 것도 방법</li>
</ul>