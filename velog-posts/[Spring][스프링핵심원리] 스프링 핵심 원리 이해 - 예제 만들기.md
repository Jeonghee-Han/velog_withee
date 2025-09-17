# [Spring][스프링핵심원리] 스프링 핵심 원리 이해 - 예제 만들기

**Published:** Mon, 25 Mar 2024 05:47:06 GMT
**Link:** https://velog.io/@heerang/Spring%EC%8A%A4%ED%94%84%EB%A7%81%ED%95%B5%EC%8B%AC%EC%9B%90%EB%A6%AC-%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EC%9D%B4%ED%95%B4-%EC%98%88%EC%A0%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0

---

<h1 id="🌱-스프링-핵심-원리-이해---예제-만들기">🌱 스프링 핵심 원리 이해 - 예제 만들기</h1>
<hr />
<h2 id="프로젝트-생성">프로젝트 생성</h2>
<blockquote>
<p><a href="https://start.spring.io/">Spring Initializar</a></p>
</blockquote>
<ul>
<li>Project: Gradle - Groovy Project</li>
<li>Spring Boot: 3.x.x</li>
<li>Language: Java</li>
<li>Packaging: Jar</li>
<li>Java: 17 또는 21</li>
<li>groupId: hello</li>
<li>artifactId: core</li>
<li>Dependencies: 선택 X</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/2b6e26c4-215a-490c-8fe2-2e4948622cd5/image.png" />
<code>스프링 입문</code> 강의에서 IntelliJ 실행 속도를 더 빠르게 하기 위해 Gradle이 아닌 IntelliJ  IDEA로 변경해서 자바를 바로 띄우도록 하면 된다고 했었는데, 해당 내용은 스프링 부트 3.2 이전에만 적용된다고 한다. </p>
<p>심지어 Gradle을 선택하지 않으면 몇가지 오류가 생긴다고 하니 🚨주의🚨
<img alt="" src="https://velog.velcdn.com/images/heerang/post/df9b5ad8-f2fc-46e2-bd96-eaec77599a8f/image.png" /></p>


<hr />
<h2 id="비즈니스-요구사항과-설계">비즈니스 요구사항과 설계</h2>
<h4 id="회원">회원</h4>
<ul>
<li>회원을 가입하고 조회할 수 있다.</li>
<li>회원은 일반과 VIP 두 가지 등급이 있다.</li>
<li>회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있다. ⇒ <code>미확정</code></li>
</ul>
<h4 id="주문과-할인-정책">주문과 할인 정책</h4>
<ul>
<li>회원은 상품을 주문할 수 있다.</li>
<li>회원 등급에 따라 할인 정책을 적용할 수 있다.</li>
<li>할인 정책은 모든 VIP는 1000원을 할인해주는 고정 금액 할인을 적용해달라. (나중에 변경 될 수 있다.)</li>
<li>할인 정책은 변경 가능성이 높다. 회사의 기본 할인 정책을 아직 정하지 못했고, 오픈 직전까지 고민을 미루고 싶다. 최악의 경우 할인을 적용하지 않을 수 도 있다. ⇒ <code>미확정</code></li>
</ul>
<p>요구사항을 보면 미확정 2개가 존재하지만, 개발을 미룰 수 없으니 객체 지향 설계 방법을 떠올리며 인터페이스를 만들고 구현체를 언제든 갈아끼울 수 있도록 설계</p>


<hr />
<h2 id="회원-도메인-설계">회원 도메인 설계</h2>
<blockquote>
<p>회원 요구사항</p>
</blockquote>
<ul>
<li>회원을 가입하고 조회할 수 있다.</li>
<li>회원은 일반과 VIP 두 가지 등급이 있다.</li>
<li>회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있다. ⇒ <code>미확정</code></li>
</ul>
<h4 id="✔-회원-도메인-협력-관계">✔ 회원 도메인 협력 관계</h4>
<blockquote>
<p>기획자들도 볼 수 있는 그림</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/fe9228e5-1995-45cf-8dda-1935cea1004c/image.png" /></p>
<ul>
<li>클라이언트의 역할: 회원 서비스 호출</li>
<li>회원 서비스의 역할: <code>회원가입</code> <code>회원조회</code> 두 기능 제공</li>
<li>회원 저장소의 역할: 세 저장소 중 하나를 통해 회원 관리<ul>
<li>구현: <code>메모리 회원 저장소</code> <code>DB 회원 저장소</code> <code>외부 시스템 연동 회원 저장소</code></li>
</ul>
</li>
</ul>


<h4 id="✔-회원-클래스-다이어그램">✔ 회원 클래스 다이어그램</h4>
<blockquote>
<p>도메인 협력 관계를 바탕으로 개발자가 구체화한 것</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/fa3b33b0-dbd2-48f1-963e-d1e6c3428cda/image.png" /></p>
<ul>
<li>회원 서비스 역할 = MemberService 인터페이스</li>
<li>회원 서비스의 구현체 = MemberServiceImpl</li>
<li>회원 저장소 = MemberRepository 인터페이스</li>
<li>회원 저장소의 구현체 = MemoryMemberRespository와 DbMemberRepository</li>
</ul>


<h4 id="✔-회원-객체-다이어그램">✔ 회원 객체 다이어그램</h4>
<blockquote>
<p>실제 서버에 올라왔을 때 객체간의 메모리 참조를 나타낸 것</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/e9a1efa6-207f-4675-b0c5-52bb6ae03906/image.png" /></p>


<hr />
<h2 id="회원-도메인-개발">회원 도메인 개발</h2>
<h4 id="member">Member</h4>
<pre><code class="language-java">package hello.core.member;

public class Member {
    private Long id;
    private String name;
    private Grade grade;

    // 생성자
    public Member(Long id, String name, Grade grade) {
        this.id = id;
        this.name = name;
        this.grade = grade;
    }

    // getter, setter
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Grade getGrade() {
        return grade;
    }
    public void setGrade(Grade grade) {
        this.grade = grade;
    }
}</code></pre>
<h4 id="💡-생성자를-만드는-이유">💡 생성자를 만드는 이유</h4>
<blockquote>
<p><em>&quot;변수를 모두 정의했는데 생성자를 굳이 왜 만들어야 해 🤔❓&quot;</em></p>
</blockquote>
<p>클래스 내에 선언된 변수의 맨 앞에 붙은 <code>private</code> 을 <strong>접근제어자</strong>라고 하며, 접근 제어자에는 <code>public</code> <code>private</code> <code>protected</code> <code>생략</code> 등이 존재</p>
<p>그 중 <code>private</code>은 클래스 외부에서 이 변수를 마음대로 접근할 수 없게 함</p>
<p>어떤 객체를 인스턴스로 생성할 때 (new Order() 할 때) 이 변수들에 일정한 값을 주며 생성하기 위해서는</p>
<ul>
<li>생성자를 이용하거나</li>
<li>수정자 <code>setter 메소드</code> 를 이용하여 이 변수들에 값을 하나씩 할당</li>
</ul>
<p>또한 <strong>객체 지향 프로그래밍</strong>에서 생성자는 어떤 객체가 생성과 동시에 <strong>유효함</strong>을 보장하는 역할을 함</p>
<pre><code class="language-java">class Person {
    int age;
    int height;
}

Person p = new Person();</code></pre>
<p>현재 Person p는 나이와 키가 모두 0인 상태인데 이러한 유효하지 않은 객체를 해결하기 위해 생성자를 이용</p>
<pre><code class="language-java">class Person {
    int age;
    int height;

    public Person(int age, int height){
        this.age = age;
        this.height = height;
    }
}

Person p = new Person(20, 180);</code></pre>
<p>Person p 는 생성과 동시에 나이 20, 키 180을 가진 유효한 객체가 됨</p>
<p>생성자는 결국 함수의 일종인데, 객체를 새로 생성할 때 최초로 한번 실행되며 그 후에는 사용자가 임의로 호출할 수 없음</p>
<p>그리고 <strong>모든 클래스는 반드시 하나 이상의 생성자를 가져야 함</strong></p>


<h4 id="memorymemberrepository">MemoryMemberRepository</h4>
<pre><code class="language-java">package hello.core.member;

import java.util.HashMap;
import java.util.Map;

public class MemoryMemberRepository implements MemberRepository{
    private static Map&lt;Long, Member&gt; store = new HashMap&lt;&gt;();

    @Override
    public void save(Member member) {
        store.put(member.getId(), member);
    }

    @Override
    public Member findById(Long memberId) {
        return store.get(memberId);
    }
}</code></pre>
<h4 id="💡-hashmap-vs-concurrenthashmap">💡 HashMap VS ConcurrentHashMap</h4>
<blockquote>
<p><em>&quot; <code>HashMap</code> 은 동시성 이슈가 발생할 수 있어서 이런 경우 <code>ConcurrentHashMap</code>을 사용하라는데 무슨 차이 🤔❓&quot;</em></p>
</blockquote>
<p><strong>동시성</strong>: 하나의 CPU에서 여러 개의 작업이 일어나는 것처럼 보이는 것</p>
<p>동시성을 고려하지 않으면 멀티쓰레드 환경에서 하나의 변수에 여러 개의 쓰레드가 동시에 접근할 경우 그 변수 값은 원하는 값으로 반환되지 않음</p>
<p><strong>✔ <code>HashMap</code></strong></p>
<ul>
<li>Tread-safety 보장 X</li>
<li>null 값 허용</li>
</ul>
<p><strong>✔ <code>ConcurrentHashMap</code></strong></p>
<ul>
<li>Tread-safety 보장 O</li>
<li>선택적으로 bucket에 synchronized(동기화)를 선언<ul>
<li>put 메소드 실행 시 CAS(Compare and Swap)을 사용하여 선택적으로 bucket에 lock을 검</li>
<li>get 메소드 실행 시 synchronized 사용 X</li>
</ul>
</li>
<li>즉, put은 하나의 쓰레드만, get은 여러 개의 쓰레드가 접근 가능</li>
<li>여러 쓰레드에서 ConcurrentHashMap 객체에 동시에 데이터를 삽입, 참조하더라도 그 데이터가 다른 세그먼트에 위치하면 서로 락을 얻기 위해 경쟁하지 않음</li>
<li>null 값 허용 X</li>
</ul>
<blockquote>
<p>✅ 멀티 쓰레드 환경에서는 <code>ConcurrentHashMap</code>, 단일 쓰레드에서는 <code>HashMap</code> 사용</p>
</blockquote>


<hr />
<h2 id="회원-도메인-실행과-테스트">회원 도메인 실행과 테스트</h2>
<blockquote>
<p><strong>Junit</strong> Test Framework 사용</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/12ff72f6-ad32-4ba6-b94c-d94c0cfdda13/image.png" />
✔ 나중에 빌드해서 나갈 때 main에 대한 코드만 나가고 test 코드는 배포되지 않음</p>
<h4 id="memberservicetest">MemberServiceTest</h4>
<pre><code class="language-java">package hello.core.member;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

public class MemberServiceTest {
    MemberService memberService = new MemberServiceImpl();

    @Test
    void join() {
        //given
        Member member = new Member(1L, &quot;heerang&quot;, Grade.VIP);

        //when
        memberService.join(member);
        Member findMember = memberService.findMember(1L);

        //then
        Assertions.assertThat(member).isEqualTo(findMember);
    }
}</code></pre>
<h4 id="💡-검증-작업을-편리하게-해주는-assertions">💡 검증 작업을 편리하게 해주는 Assertions?</h4>
<blockquote>
<p><em>&quot; <code>Assertions</code> 에 편리한 API가 많다는데 이건 뭐고, <code>assertThat</code>는 또 뭐지? 🤔❓&quot;</em></p>
</blockquote>
<p>** Assertions**: 테스트 코드에서 사용되며 특정 조건이 참이어야 테스트가 계속 진행되도록 하는 기능</p>
<p>** assertThat**</p>
<ul>
<li><p><code>.inEqualTo()</code> : 대상 A가 기댓값 B와 값이 같은지 <strong>값</strong>을 통해 확인하는 메서드 (↔ <code>isNotEqualTo()</code>)</p>
<pre><code class="language-java">Assertions.assertThat(A).isEqualTo(B);</code></pre>
</li>
<li><p><code>.isSameAs()</code> : 대상 A가 기댓값 B와 같은 대상인지 <strong>주소값</strong>을 통해 확인하는 메서드</p>
<pre><code class="language-java">Assertions.assertThat(A).isSameAs(B);

// A와 B의 값이 같아도 주소값이 다르면 fail</code></pre>
<blockquote>
<p>isEqualTo()와 isSameAs()의 차이점</p>
<ul>
<li>isSameAs()는 두 오브젝트가 same한지 확인 (두 오브젝트가 같은 <strong>reference</strong>를 가지고 있는지 확인)</li>
<li>isEqualTo()는 두 오브젝트가 equal한지 확인 (두 오브젝트가 같은 <strong>value</strong>를 가지고 있는지 확인)</li>
</ul>
</blockquote>
</li>
<li><p><code>.isInstanceOf()</code> : 대상 A가 <strong>클래스 B의 인스턴스인지</strong> 확인하는 메서드</p>
<pre><code class="language-java">Assertions.assertThat(A).isInstanceOf(B.class);</code></pre>
</li>
<li><p><code>.isNull()</code> : 대상 A가 <strong>null인지</strong> 확인하는 메서드 (↔ <code>.isNotNull()</code>)</p>
<pre><code class="language-java">Assertions.assertThat(A).isNull();</code></pre>
<p><del><em>이것들 외에도 매우매우 많으니 참고</em></del></p>
<h3 id="회원-도메인-설계의-문제점">회원 도메인 설계의 문제점</h3>
<blockquote>
<ul>
<li>이 코드의 설계상 문제점은?</li>
<li>다른 저장소로 변경할 때 OCP 원칙 준수?</li>
<li>DIP 원칙 준수?</li>
</ul>
</blockquote>
<h4 id="memberservicetest-1">MemberServiceTest</h4>
<pre><code class="language-java">package hello.core.member;
public class MemberServiceTest implements MemberService{
  private final MemberRepository memberRepository = new MemoryMemberRepository();

  @Override
  public void join(Member member) {
      memberRepository.save(member);
  }

  @Override
  public Member findMember(Long memberId) {
      return memberRepository.findById(memberId);
  }
}
</code></pre>
<p>의존 관계가 인터페이스 뿐만 아니라 구현까지 모두 의존하는 문제점</p>
<blockquote>
<p>즉 <code>MemberRepository</code> 추상화와 <code>MemoryMemberRepository</code> 구체화 모두 의존 ⇀ 🚨DIP 위반🚨</p>
</blockquote>
</li>
</ul>


<hr />
<h2 id="주문과-할인-도메인-설계">주문과 할인 도메인 설계</h2>
<blockquote>
<p>주문과 할인 요구사항</p>
</blockquote>
<ul>
<li>회원은 상품을 주문할 수 있다.</li>
<li>회원 등급에 따라 할인 정책을 적용할 수 있다.</li>
<li>할인 정책은 모든 VIP는 1000원을 할인해주는 고정 금액 할인을 적용해달라. (나중에 변경 될 수 있다.)</li>
<li>할인 정책은 변경 가능성이 높다. 회사의 기본 할인 정책을 아직 정하지 못했고, 오픈 직전까지 고민을 미루고 싶다. 최악의 경우 할인을 적용하지 않을 수 도 있다. ⇒ <code>미확정</code></li>
</ul>


<h4 id="✔-주문-도메인-협력-역할-책임">✔ 주문 도메인 협력, 역할, 책임</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/0a2944f2-ecaf-42eb-9379-0ba57078fd37/image.png" /></p>
<ul>
<li>주문 생성: 클라이언트가 주문 서비스에 주문 생성 요청</li>
<li>회원 조회: 주문 서비스는 회원 저장소에서 회원을 조회</li>
<li>할인 적용: 주문 서비스는 회원 등급에 다라 할인 여부를 할인 정책에 위임</li>
<li>주문 결과 반환: 주문 서비스는 할인 결과를 포함한 주문 결과 반환</li>
</ul>


<h4 id="✔-주문-도메인-전체">✔ 주문 도메인 전체</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/d8ca87b7-ff43-4e71-b909-7c1eab9a38e0/image.png" /></p>
<p><strong>'역할과 구현을 분리'</strong> 해서 자유롭게 구현 객체를 조립할 수 있게 설계
⇀ 회원 저장소는 물론, 할인 정책도 유연하게 변경 가능</p>


<h4 id="✔-주문-도메인-클래스-다이어그램">✔ 주문 도메인 클래스 다이어그램</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/b925c411-a8f5-472c-a7ca-eff49487b5ba/image.png" /></p>


<h4 id="✔-주문-도메인-객체-다이어그램">✔ 주문 도메인 객체 다이어그램</h4>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/e3d7a094-6342-486e-88d2-8fe432b3d906/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/4b6afc2c-138f-44bc-a1a8-38370c5bd92d/image.png" /></p>
<p>회원을 메모리가 아닌 DB에서 조회하고 정액 할인 정책이 아닌 정률 할인 정책을 적용해도 주문 서비스는 변경하지 않고 협력 관계를 재사용 가능</p>


<hr />
<h2 id="주문과-할인-도메인-개발">주문과 할인 도메인 개발</h2>
<h4 id="orderserviceimpl">OrderServiceImpl</h4>
<pre><code class="language-java">package hello.core.order;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;

public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    private final DiscountPolicy discountPolicy = new FixDiscountPolicy();

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}</code></pre>
<ul>
<li>주문 생성 요청이 오면, 회원 정보를 조회하고, 할인 정책을 적용한 다음 주문 객체를 생성해서 반환</li>
<li>메모리 회원 리포지토리와, 고정 금액 할인 정책을 구현체로 생성</li>
</ul>


<p>✔ 이 부분이 <strong>좋은 객체 지향 설계</strong>  !!</p>
<pre><code class="language-java">        int discountPrice = discountPolicy.discount(member, itemPrice);</code></pre>
<p><del><em>이전에도 위 코드처럼 구성해왔지만, <strong>단일 책임 원칙</strong>에 대해 명확히 알고 다시 코드를 보니 새삼 다르게 느껴지는..</em></del></p>



<h4 id="💡-static-factory-method-pattern">💡 Static Factory Method Pattern</h4>
<blockquote>
<p><em>&quot; Member의 경우 Member클래스의 생성자를 사용해서 생성하는데 Order를 생성할 때는생성자를 사용하지않고 createOrder를 사용하는 이유? 🤔❓&quot;</em></p>
</blockquote>
<p><strong>Static Factory Method</strong> : 객체 생성 역할을 하는 클래스 메서드로 생성자를 통해서가 아닌 Static Method를 통해 객체를 생성하는 역할</p>
<p><a href="https://johngrib.github.io/wiki/pattern/static-factory-method/">정적 팩토리 메서드를 사용하는 이유</a></p>
<p>참고로 Member 처럼 생성이 단순한 경우에는 그냥 생성자를 사용하는게 굳👍</p>


<hr />
<h2 id="주문과-할인-도메인-실행과-테스트">주문과 할인 도메인 실행과 테스트</h2>
<pre><code class="language-java">package hello.core.order;

import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

public class OrderServiceTest {
    MemberService memberService = new MemberServiceImpl();
    OrderService orderService = new OrderServiceImpl();

    @Test
    void createOrder() {
        long memberId = 1L;
        Member member = new Member(memberId, &quot;heerang&quot;, Grade.VIP);
        memberService.join(member);

        Order order = orderService.createOrder(memberId, &quot;itemA&quot;, 10000);
        Assertions.assertThat(order.getDiscountPrice()).isEqualTo(1000);
    }
}</code></pre>
<p>✔ Test Success 👍</p>