
## YEOLDY 🤟




## 메인

![yeoldy_main](README.assets/yeoldy_main.gif)






### 🤟YEOLDY의 주요기능
#### **1. 쇼핑(의류 구매) 기능**
👉 사이트 내의 상품들 중 마음에 드는 상품을 찜 또는 장바구니에 담기

👉 장바구니 기능 구현을 통한 원하는 상품 저장 가능

👉 장바구니에 담긴 상품들을 카카오페이로 결제하기

👉 구매 목록 저장 나의 페이지 열람 가능

#### **2. 스타일 공유 기능**
👉 자신이 구매한 상품을 입고 사진을 찍고 글을 써, 다른 유저분들과 스타일 공유하기

#### **3. 상품 리뷰 및 문의하기 기능**

👉 상품 리뷰, 상품 문의

👉 스타일 공유(자신이 구매한 상품을 사용한 스타일 자랑)

👉 자신이 구매한 상품에 대한 리뷰나 문의를 할 수 있는 기능

#### **4. 상담사와 실시간으로 소통하는 기능**

👉 사이트내의 관리자와의 채팅 기능으로 관리자와 실시간으로 소통하기



### 🤟 YEOLDY 사이트 기능소개

#### [ Accounts ]

<img src="README.assets/로그인 캡쳐.png" alt="로그인 캡쳐" style="zoom:50%;" />

![제목없음](README.assets/제목 없음.png)


- 기본 회원 가입을 통한 로그인,  회원 정보 수정, 회원 탈퇴 구현
- 회원 가입 후 바로 로그인 기능 구현 
- 카카오와 네이버 소셜로그인을 구현하였지만, 배포 이후의 오류로 네이버만 성공함

- 로그인과 업데이트 폼에 부트스트랩 폼을 썼을 때 처럼 오류메세지 표시 직접 구현 



##### My page

![마이페이지](README.assets/마이페이지.png)


- 마이 페이지 팔로우 가능( 팔로우,  팔로워  확인가능 )
- 마이 페이지 내가 쓴 리뷰, Qna, 스타일, 좋아요한 스타일, 주문내역, 찜한 상품 확인 가능 

#### [ Cart ]

- 로그인 되었을 때, 해당 유저의 장바구니를 띄움
- product별 수량, 색상, 사이즈를 띄우고, 전체 수량 및 개수도 띄움
- 같은 product여도, 색상 또는 사이즈가 다르면 다른 상품으로 인식하도록 함
- 장바구니에서도 수량이 변경하도록 함
- 카카오페이 테스트 결제 기능과 장바구니를 연동함
- 카카오페이 결제 완료 시, 장바구니에서 삭제 및 결제완료 상품을 따로 데이터베이스에 저장함




#### [ Kakaopay ]




- 장바구니와 카카오페이 테스트 결제 시스템을 연동함
- 결제 창에 2개 이상의 상품이 들어있는 경우는 '~외 몇건' 으로 처리
- 배송 완료 건에 대한 데이터베이스(OrderList)를 구축함
- 결제 전, 배송 정보를 입력받고 이를 임시 데이터베이스에 저장

#### [ Chat ]





#### [ Community ]
- qna 작성/조회/삭제/수정/작성할떄 비밀번호생성/작성자와 관리자만 조회 가능 
- qna생성할떄 관리자가 답변작성
- 상품review 작성/조회/삭제/수정
- 상품 평점 기능

#### [ Products ]

![전체태그](README.assets/전체 태그.png)

![상의태그](README.assets/상의 태그.png)

- 



#### [ Style ]







### 🍽 AWS를 통한 배포







### 🍽 사용한 기술스택





### 🍽 프로젝트 참여자들

<a href="https://github.com/w00ye0l/YEOLDY/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=w00ye0l/YEOLDY" />
</a>



### 🍽 프로젝트 후기

**이우열** : 

**이상욱** :  프론트를 맞아서 진행하면서 프론트에 대해 많이 배우고, 팀원들 모두 자기가 맡은 역할을 열심히 해줘서 만족스러운 결과가 나왔고 재밌었습니다.

**권세빈** : 

**여다영** : 장바구니부터 결제기능까지 연동하려고 하니까 여러 난관들을 마주해서 힘들었지만, 팀원들이 열심히 도와주셔가지고 너무너무 좋았다. 다들 너무 수고했고 열디 짱🤍

**안동우** : 

**이수영** : 디테일한 기능들 까지 구현하려고 노력하면서,  잠도 많이 못자고 힘들었지만 그래도 기술적으로 얻어가는게 많은 프로젝트였습니다. 팀원들과 맘이 잘맞아서 재미있게 프로젝트 마무리 할 수 있었습니다.