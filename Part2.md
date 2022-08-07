
## 1장(AWS 기초와 VPC)
### 1.1 (개요) 클라우드 컴퓨팅
* 클라우드 컴퓨팅 : 구름처럼 언제 어디서나, 컴퓨팅 자원을 제공할 수 있는 서비스
* 클라우드 컴퓨팅 장점 :
  1. 컴퓨터를 사지 않아도 돼서 초기 비용이 적게 든다
  2. 사용한 만큼만 비용을 지불한다(단점이 될 수도 있음)
  3. 클릭을 통해 서버 구축을 간편하게 할 수 있다.
* 클라우드 컴퓨팅 단점 :
  1. 사용하기 위해서 많은 전문 지식이 필요하다
  2. 서비스 개수가 많아서 파악하기가 힘듬
  
### 1.2 AWS 의 주요 서비스 소개
* 컴퓨팅 서비스
  1. AWS EC2 : 가변 가능한 컴퓨팅 자원을 제공해주는 서비스
  2. AWS Lightsail : EC2 와 동일하나 프라이빗 서버를 제공
  3. AWS Auto Scaling : 서버의 조건에 따라 Auto Scaling 할 수 있도록 하는 서비스
  4. AWS Workspaces : 파일드랍과 같은 문서및 파일을 공통적으로 서버에 보관하게 하는 서비스
  
* 네트워킹 서비스
  1. AWS Route 53 : DNS
  2. AWS VPC : 가상네트워크를 클라우드 내에 제공하는 서비스
  3. AWS Direct Connect : On-Premise(형체가 있는 기존 인프라) <-> AWS 연결하는 네트워킹 서비스
  4. AWS ELB : 로드 밸런싱 서비스
  
* 스토리지/데이터베이스 서비스
  1. AWS S3 : 여러가지 파일 데이터 저장(NAS)
  2. AWS RDS : 가상 RDB 서비스
  3. AWS DynamoDB : 가상 NoSQL DB 서비스
  4. AWS ElastiCache : 인메모리 캐시 서버 서비스
  
* 데이터 분석 & AI
  1. AWS Redshift : 데이터 분석에 특화된 스토리지 서비스
  2. AWS EMR : MapReduce 통한 대량의 데이터 처리 서비스
  3. AWS Sagemaker : 머신러닝&데이터분석 클라우드 환경 서비스
  

### 1.3 네트워킹의 기본
* IP 주소는 네트워크 영역, 호스트 영역으로 나뉜다.
* 다른 네트워크 영역간 통신 시 라우터를 통해야 한다.
* 네트워크 영역의 첫 옥텟 안의 앞 비트를 보고 A,B,C 클래스로 나눈다
* 각 클래스 별로 사용가능한 네트워크 영역, 호스트 영역이 달라진다.  
* 네트워크 안에서 서브넷을 만들 수 있고 서브넷 CIDR 표기법은 111.111.111.0/25 로 시작 주소와 네트워크 비트 길이를 표기해준다.

### 1.4~6 네트워킹의 동작원리
* VPC(Virtual Private Cloud) : AWS 상에서 클릭 몇 번 만으로 네트워크를 구축할 수 있는 서비스, 기존에 물리적으로 생성해서 사용하던
네트워크와 거의 유사하다.
* VPC 의 특징
  1. 서브넷 구성
  2. 보안 설정
  3. VPC Peering(VPC 간의 연결)
  4. IP 대역 지정
  
* VPC 의 구성요소
  1. Availability Zone
     * 데이터 복구(사용성) 위해, 하나의 region 안에 여러개의 일정거리 떨어진 동일한 데이터센터가 존재하는 것
  2. Subnet(CIDR)
     * Subnet 생성 시, Subnet 은 한 AZ 안에만 존재할 수 있음
  3. Internet Gateway
     * VPC <-> 인터넷과의 연결을 위한 Gateway
  4. Network Access Control List/security group
     * AWS 오고 나가는 네트워크에 대한 보안 컨트롤을 담당.
     * NACL : stateless, SG : state
  5. Route Table
     * 한 네트워크 안에서, 어떤 IP 요청이 어디로 가야 하는지 적혀있는 테이블
  6. NAT instance/NAT gateway
     * 외부접근이 불가능한 Private Subnet 에서 외부 접속을 위해 사용하는 장치
     * Private Subnet -> Public Subnet -> NAT(gateway or instance) 를 통해 대리 외부 접속 한다.
     > Bastion host : NAT 의 반대로, 외부 접근자가 Public Subnent 을 통해 Private Subnet 으로 대리 접근 
  7. VPC endpoint
     * Private Network -> AWS 서비스 간 연결 지원
     * 지원 타입
     1. interface endpoint : Private Network 내에 연결 IP 할당
     2. Gateway endpoint : 라우팅 테이블을 통해 연결
    
### 1.7 (VPC) VPC 와 Private, Public Subnet 만들기
* 새로운 VPC 와 그에 대한 public, private subnet 생성
  
### 1.8 (VPC) Internet Gateway과 라우팅 테이블 생성
* 인터넷 게이트웨이(IGW) 생성
* public subnet 의 라우팅 테이블을 추가하여 IGW 에 연결될 수 있도록 설정

### 1.9~10 (VPC) NACL 설정하기
* AWS 의 네트워크 보안은 NACL 이나, Security Group 을 통해 설정한다. NACL 은 stateless, Secytiry Group 은 Stateful 하다
* stateful : 서버 outbound 설정이 전부 막혀있어도, inbound 로 온 요청에 대한 응답 outbound 는 허용
* stateless : 서버 outbound 설정이 전부 막혀있으면, outbound 미허용
* fastcampus-vpc 의 각 public, private subnet 에 NACL 을 통해 인/아웃바운드 설정
* public, private subnet 에 EC2 인스턴스 추가

### 1.11 (VPC) Bastion Host 만들기
* public/private ec2 를 만들고 public ec2 -> private ec2 로 ssh 접속해본다
* Bastion Host 는 따로 만드는 것은 아니고, 개념적으로 우회접속 할 때 사용하는 말인것으로 보임

### 1.12 (VPC) NAT Gateway 만들기
* private ec2 에서, 외부로 나가는 접속을 허용해주기 위해, NAT 게이트웨이를 public ec2에 만들고, private ec2 는 라우팅 테이블을 통해 NAT 게이트웨이를 보게 만든다.

### 1.13 (VPC) VPC EndPoint 만들기
* NAT Gateway 는 public 쪽을 타서 외부로 나가므로, AWS 에서 제공하는 VPC EndPoint 를 설정해서 더 안전하게 private ec2 안에서 다른 서비스(s3) 등을 접근할 수 있게 한다.

## 2장(소규모 아키텍트)

### 2.1 (개요) 모놀리식 아키텍처 vs 마이크로서비스 아키텍처
* 모놀리식 아키텍처 : 서비스를 한 개의 큰 프로그램으로 설계된 구조
  * 장점 : 엔드 투 엔드 테스트가 용이하다, 빠르게 간단한 서비스를 만들 수 있다.
  * 단점 : 일부 오류에도 전체 서비스에 영향을 미침, 개발 언어가 통일되어야 함

* 마이크로서비스 아키텍처 : 서비스를 기능별 작은 규모 단위의 프로그램이 모여서 구성하는 것
    * 장점 : 일부의 장애가 있어도 서비스에 영향을 주지 않음, 개발언어가 자유로움
    * 단점 : 모니터링이 힘듬, 엔드 투 엔드 테스트가 불편
    
### 2.2 (개요) 프로젝트 개요(온라인 주문 어플리케이션)
* 온라인 주문 어플리케이션의 요구 사항 
* 여러 개발 언어 및 서비스(Django, AWS 서비스 등) 을 이용해서 온라인 주문 어플리케이션 개발

### 2.3 (설계) 도메인 주도 설계 개요
* 기존 제품(서비스) 의 개발 방식은, 기획, 마케팅, 개발 간의 소통이 잘 되지 않았다. 서로 쓰는 언어가 다르고 관점이 다르기 때문
* 관점과 언어를 도메인에 가장 근접하게 통일해서 설계하자 -> 도메인 주도 설계
* 전략적 설계 : 전쟁의 전략과 같이 큰 틀에서 설계하는 부분, 도메인 내의 큰 틀을 분리하여 상호작용을 나타낸다
* 전술적 설계 : 전쟁의 전략안의 세부 전술을 뜻하는 것처럼, 도메인 내부의 상세 설계(모델 디자인) 등을 구현
* 도메인 주도 설계는 어떤 entity, value, aggregate 라기보단, 설계 프로세스에 대한 철학을 뜻함

### 2.4 (설계) 어플리케이션 이벤트스토밍
* 이벤트 스토밍 : 여러 사람이 서비스에 대한 이벤트를 같이 논의하고, 결국에는 이벤트를 특정 그룹으로 묶는 것
* 단계 : 
    1. Domain Event 정의 :  발생할 수 있는 이벤트들을 여러개 생각 후 추가
    2. 프로세스 그룹핑 : 동일한 비즈니스 주제로, 이벤트들을 그룹핑
    3. Command 정의 : 이벤트에 대한 Command(사용자의 행위) 를 이벤트에 할당
    4. Trigger 정의 : 이벤트를 발생시키는 행위자를 정의
    5. Aggregate 정의 : Command 수행을 위해서 CRUD 해야 하는 데이터 객체 정의
    6. Bounded Context 정의 : 앞에서 부가한 이벤트 정보들을 바탕으로 그룹핑
    7. Context Map 작성 : Bounded Context 에 대한 도식화(상호작용)
    
### 2.5~7 (백엔드) Django 기초
* Django 튜토리얼을 수행하며 기본적인 투표 페이지 제작

### 2.8 (백엔드) 온라인 주문 어플리케이션 백엔드 Overview
* UI 적 부분은 최소화
* 주문자, 배달기사, 사장님 별 app 을 따로 개발

### 2.9 (백엔드) Models 제작
* manage.py 를 통해 DB 를 생성하고 스키마를 migration
* 주문 GET, POST 요청에 대한 응답 구성 및 csrf 토큰 추가

### 2.10 (백엔드) Order 백엔드 개발1
* 사용자에게 보여줄 shop list, menu list html 생성
* 이벤트를 통해 shop list -> menu list 이동 동작 추가

### 2.11 (백엔드) Order 백엔드 개발2
* 사용자에게 주문을 받는 기능 추가
* 주문 리스트 조회 기능 추가

### 2.12 (백엔드) Order 백엔드 개발3
* 주문 리스트 조회 페이지 html 개선
* 주문시, 주문 리스트 조회 페이지 클릭할 수 있도록 추가

### 2.13 (백엔드) Boss 백엔드 개발1
* 사장님들이 주문 리스트를 볼 수 있는 페이지 구현
* 배달 예상시간 입력 구현

### 2.14 (백엔드) Boss 백엔드 개발2
* 사장님 별로 주문 리스트를 볼 수 있는 페이지 구현

### 2.15 (백엔드) Delivery 백엔드 개발
* 주문 리스트에서 배달 완료 버튼을 누를 수 있는 배달 페이지 구현

### 2.16 (인프라) 데이터베이스 구축(AWS RDS)
* AWS RDS 사용하여 DB 생성 후 현재 APP 과 연동

### 2.17 (인프라) Django 개발 결과를 EC2에 배포하기
* github 과 연동하여 EC2 인스턴스에 소스 배포 및 접속 확인

### 2.18 (인프라) 로드밸런서(L4 , L7) 의 동작원리와 AWS ELB
* 로드밸런싱 : 여러가지 클라이언트가 주는 부하를 분산시키는 방법, 로드밸런서의 종류에는 L4 계층과 L7 계층이 있다
  * L4 
    * 장점 : 로드를 분산해주는 빠르고 산 장비
    * 단점 : 마이크로서비스에 불리, 특정 데이터를 보고 어떤 서버로 보내주는 것이 불가능
  * L7
    * 장점 : 마이크로서비스에 유리함
    * 단점 : 속도가 비교적 느리다(데이터를 확인하므로), 비용이 많이 든다
  
### 2.19 (인프라) ALB 에 인스턴스 연결하여 웹서비스 실행하기
* AWS ELB Application 로드밸런서 생성 후 EC2 주소에 할당

### 2.20 (인프라) ALB Rule 설정하여 인스턴스 분기하기
* ALB Rule : ALB 에서 어떤 특정 요청을 보고, 어느 서비스 그룹으로 요청을 보낼지에 대한 규칙 
* Sticky Session : 로드 밸런싱 되어 각 서비스 군 중 특정 서비스를 통하게 되면 세션 저장이 불가능하기 때문에, 
로드밸런싱 하는 곳에 세션을 저장하는 방법
* Target Group 을 두개 생성한 뒤, ALB 의 규칙을 통해 /delivery 는 특정 그룹, 그 외의 path 는 다른 
그룹으로 밸런싱 되게 하는 설정 적용

### 2.21 (인프라) AWS Route53 과 DNS 의 동작원리
* 도메인 등록 절차 : 등록자 -> 등록 대행자(가비아 등) -> 등록소(.com, .... 등 end url 에 따라 다름) -> ICANN
* 도메인 질의 절차 : fast-devops.com -> ICANN(root name server) -> .com 에 해당하는 등록소로 질의 -> 
등록소에서 ip 조회 -> ICANN 으로 다시 보냄 -> 등록자
* AWS Route53 은 등록대행자의 역할을 함

### 2.22 (인프라) AWS Route53 도메인 등록과 Hosted zone 설정하기
* 도메인을 hihisososo.link 로 구매
* 해당 도메인을 ALB 에 연결시켜 접속 되는지 확인

### 2.23 (인프라) AWS Route53 DNS 기반 인증서 발급과 ALB에 https 설정하기
* Certificate manager 를 통해 인증서 발급 
* ALB 에 인증서를 추가해서 https 접속이 가능하게 설정

### 2.24 (인프라) AWS CloudFront 와 CDN의 동작원리
* Cloudfront : Cache(메인) + CDN(부가)
* 웹 서버의 비용을 감소시킴, 전 세계의 유저를 대상으로 고속으로 웹 서비스를 제공할 수 있음
* 중간 캐시 서버를 둬서 캐시 데이터에서 먼저 질의하는 방식
* CDN(Content Dlivery Network)
  1. 전 세계 어느 위치에서 접속하더라도 빠른 속도로 서비스할 수 있도록 하는 서비스
  2. 전 세계에 흩어져 있는 Edge Location(캐시 서버)을 활용