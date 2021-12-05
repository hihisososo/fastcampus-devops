
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