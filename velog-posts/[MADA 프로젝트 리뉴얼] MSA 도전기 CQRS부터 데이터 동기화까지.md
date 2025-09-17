# [MADA 프로젝트 리뉴얼] MSA 도전기: CQRS부터 데이터 동기화까지

**Published:** Tue, 16 Sep 2025 08:50:00 GMT
**Link:** https://velog.io/@heerang/MADA-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%A6%AC%EB%89%B4%EC%96%BC-MSA-%EB%8F%84%EC%A0%84%EA%B8%B0-CQRS%EB%B6%80%ED%84%B0-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%8F%99%EA%B8%B0%ED%99%94%EA%B9%8C%EC%A7%80

---

<h2 id="cqrs-command-query-responsibility-segregation">CQRS: Command Query Responsibility Segregation</h2>
<blockquote>
<p><strong>'명령'과 '조회'의 책임을 분리</strong>하는 설계 패턴</p>
</blockquote>
<ul>
<li><strong>명령 (Command)</strong>
데이터를 생성(Create), 수정(Update), 삭제(Delete)하는 모든 행위
&quot;새로운 목표를 등록한다&quot; 또는 &quot;카테고리 이름을 변경한다&quot; 같은 작업 →  <strong>'Write'</strong>.</li>
<li><strong>조회 (Query)|</strong>
데이터를 <strong>읽어오는(Read)</strong> 모든 행위
&quot;오늘의 할 일 목록을 보여줘&quot; 또는 &quot;캘린더를 보여줘&quot; 같은 작업 →  <strong>'Read'</strong> .</li>
</ul>
<p><br />
<strong><em>→ 🤔 왜 분리할까?</em></strong></p>
<p>쇼핑몰의 '주문'과 '상품 조회'
상품 조회는 수많은 사람이 동시에 하지만, 실제 주문은 그보다 훨씬 적은 횟수로 일어남.</p>
<p>그래서 '쓰기(Write)'와 '읽기(Read)'는 요구되는 성능과 데이터 형태가 다르니까 이 둘을 분리해서 각자에게 최적화된 기술을 사용하자'는 아이디어가 CQRS.</p>
<p>예를 들어, 쓰기 작업은 데이터의 <strong>정확성</strong>이 매우 중요하지만(PostgreSQL 사용), 읽기 작업은 무엇보다 <strong>속도</strong>가 중요하죠(Redis, MongoDB 사용).
<br /></p>
<hr />
<h2 id="db-postgresql-mysql-mongodb-redis">DB: PostgreSQL, MySQL, MongoDB, Redis</h2>
<blockquote>
<p>CQRS 패턴에 따라 Write용 데이터베이스와 Read용 데이터베이스를 다르게 사용</p>
</blockquote>
<p><strong>Write용: PostgreSQL, MySQL</strong></p>
<ul>
<li>이들은 관계형 데이터베이스(RDBMS).
데이터의 <strong>정확성과 일관성</strong>을 보장하는 데 매우 뛰어남 → 사용자의 목표, 카테고리 등 원본 데이터를 안전하게 저장하는 '금고' 역할.</li>
</ul>
<p><strong>Read용: MongoDB, Redis</strong></p>
<ul>
<li><strong>MongoDB</strong>: <strong>문서(Document) 기반 데이터베이스</strong>
데이터를 앱 화면에 보여주기 좋은 형태(JSON과 유사한 구조)로 미리 가공해서 저장. 
예를 들어, '오늘의 캘린더 화면'에 필요한 모든 정보를 미리 계산해서 하나의 문서로 만들어두면, 앱은 그 문서 하나만 읽어서 화면을 매우 빠르게 보여줌.</li>
<li><strong>Redis</strong>: <strong>인-메모리 데이터베이스</strong>
하드디스크가 아닌 메모리에서 데이터를 읽어오기 때문에 속도가 매우 빠름.
자주 바뀌지 않지만 아주 빠르게 접근해야 하는 데이터(예: 사용자 설정, 카테고리 목록)를 저장하거나, '오늘의 데이터'처럼 아주 빈번하게 조회되는 데이터를 임시 저장(캐싱)하는 데 사용됨.</li>
</ul>
<h2 id="brbr"><br /></h2>
<h2 id="데이터-동기화-kafka-cdc">데이터 동기화: Kafka, CDC</h2>
<blockquote>
<p><em>Write DB의 변경을 어떻게 Read DB에 알릴까? 
Write DB(PostgreSQL)에 데이터가 변경되면, 이걸 Read DB(MongoDB, Redis)에 어떻게 빠르고 정확하게 복사할지.</em></p>
</blockquote>
<h3 id="방법-1-kafka-사용">방법 1: Kafka 사용</h3>
<p>Write DB에 변경이 생기면, &quot;목표가 생성됐어!&quot; 같은 <strong>'이벤트(Event)'를 카프카(Kafka)라는 통로로 던져줌.</strong></p>
<p>그러면 다른 서비스가 그 통로를 지켜보다가 이벤트를 받아서 Read DB를 업데이트.</p>
<p>→ 장점: 각 서비스가 독립적으로 움직여서 안정적임</p>
<p>→ 단점: 트래픽이 많을 때 Kafka 시스템이 부담될 수 있고, 별도의 시스템을 운영해야해서 복잡.<br /></p>
<h3 id="방법-2-애플리케이션에서-직접-동기화">방법 2: 애플리케이션에서 직접 동기화</h3>
<p>Write Service가 PostgreSQL에 데이터를 저장하고, <strong>코드(애플리케이션)에서 직접</strong> MongoDB와 Redis에도 데이터를 써주는 방식.</p>
<p>→ 장점: 구조가 비교적 단순.</p>
<p>→ 단점: 만약 PostgreSQL에는 저장이 성공했는데, Redis에 저장하다가 오류가 나면 <strong>데이터 불일치.</strong><br /></p>
<h3 id="방법-3-cdc-change-data-capture-사용">방법 3: CDC (Change Data Capture) 사용</h3>
<p>Write DB(PostgreSQL)의 <strong>변경 내역 로그를 직접 감시</strong>해서, 변화가 생길 때마다 이를 '캡처'해 Read DB에 전달.</p>
<p>→ 장점: Write Service의 코드에 영향을 주지 않고 동기화할 수 있어 매우 깔끔하고 안정적</p>
<p>→ 요즘 많이 사용하는 방식임!!</p>
<h2 id="brbr-1"><br /></h2>
<h2 id="graphql">GraphQL</h2>
<blockquote>
<p>앱(클라이언트)이 <strong>서버에게 데이터를 요청하는 방식</strong>(API) 중 하나</p>
</blockquote>
<p>기존의 REST API와 달리, <strong>앱이 필요한 데이터만 골라서 딱 그만큼만 요청 가능</strong>
예를 들어, '사용자 정보'에서 '이름'과 '프로필 사진'만 필요하다면, GraphQL을 사용해 정확히 그 두 가지만 받아올 수 있어 효율적.</p>
<h2 id="brbr-2"><br /></h2>
<h2 id="firebase-notification">Firebase Notification</h2>
<blockquote>
<p>사용자에게 <strong>푸시 알림</strong>을 보내기 위한 구글의 서비스 </p>
</blockquote>
<p>안드로이드와 iOS에 모두 안정적으로 알림을 보낼 수 있어 사실상 표준처럼 사용됨.</p>
<p>푸시 알림을 보내는 기능만 따로 떼어내 서버 관리 없이 코드만 실행되는 환경(Serverless)에 올려두는 것이 일반적</p>
<h2 id="brbr-3"><br /></h2>
<h2 id="kubernetes-쿠버네티스">Kubernetes (쿠버네티스)</h2>
<blockquote>
<p>여러 개로 쪼갠 서비스(Write 서비스, Read 서비스 등)들을 <strong>'컨테이너'</strong> 라는 단위로 패키징하고, 이 컨테이너들을 효율적으로 관리하고 운영해주는 도구</p>
</blockquote>
<hr />