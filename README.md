# Smart Learning Platform - 스마트 학습 문제 생성 플랫폼 🎯

![Flask](https://img.shields.io/badge/Flask-3.1.1-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap_5-purple)

> "AI가 만드는 맞춤형 학습 경험"

Smart Learning Platform은 인공지능 기반의 맞춤형 학습 문제 생성 및 관리 시스템입니다. 다양한 주제와 난이도의 문제를 자동으로 생성하여 개인 맞춤형 학습 경험을 제공합니다.

## 📚 주요 기능

### 1. 스마트 문제 생성
- 문법, 어휘, 독해 등 다양한 카테고리의 문제 제공
- 초급(Beginner), 중급(Intermediate), 고급(Advanced) 난이도 선택
- AI 기반 동적 문제 생성으로 매번 새로운 학습 콘텐츠

### 2. 실시간 피드백 시스템
- 문제별 즉시 정답 확인
- 상세한 해설 및 오답 분석
- 관련 개념 설명 및 학습 팁 제공

### 3. 학습 진도 관리
- 개인별 문제 풀이 기록 추적
- 최근 학습 활동 대시보드
- 학습 패턴 분석 및 통계

### 4. 사용자 친화적 인터페이스
- 직관적이고 깔끔한 웹 인터페이스
- 모바일 반응형 디자인
- 실시간 문제 생성 및 풀이 시스템

## 🚀 시작하기

### 시스템 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)

### 🚀 빠른 시작

#### 로컬 개발 환경
```bash
# 1. 저장소 클론
git clone https://github.com/lhg96/smart-learning-platform.git
cd smart-learning-platform

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 데이터베이스 초기화
flask db upgrade

# 5. 개발 서버 실행
flask run
```

#### Docker 실행 (예정)
```bash
docker-compose up -d
```

웹 브라우저에서 http://localhost:5000 으로 접속하여 서비스를 이용할 수 있습니다.

## 🏷️ 프로젝트 태그

`flask` `python` `education` `ai` `learning-platform` `quiz-generator` `web-application` `sqlite` `bootstrap` `educational-technology` `adaptive-learning` `question-generation`

## 📦 기술 스택

### Backend
- **Framework**: Flask 3.1.1 (Python 웹 프레임워크)
- **Database**: SQLite (SQLAlchemy ORM)
- **Authentication**: Flask-Login
- **Migration**: Flask-Migrate
- **Forms**: Flask-WTF

### Frontend
- **Templates**: Jinja2 템플릿 엔진
- **Styling**: Bootstrap 5 (반응형 CSS 프레임워크)
- **Scripts**: Vanilla JavaScript

### 데이터베이스 설계
- **User**: 사용자 정보 관리
- **Problem**: 문제 데이터 저장
- **Attempt**: 문제 풀이 기록 추적

## 🌟 주요 특징

- **즉시 사용 가능**: 복잡한 설정 없이 바로 문제 생성 및 풀이
- **반응형 디자인**: 모바일, 태블릿, 데스크톱 모든 기기 지원
- **실시간 피드백**: 문제 제출 즉시 정답 여부 및 해설 확인
- **카테고리별 학습**: 문법, 어휘 등 목적에 맞는 학습 가능
- **난이도 조절**: 학습자 수준에 맞는 문제 난이도 선택
- **학습 기록**: 개인별 문제 풀이 이력 자동 저장

## 📱 서비스 화면

### 🏠 메인 대시보드
- 최근 학습 현황 확인
- 추천 문제 제공
- 학습 통계 확인

![메인 대시보드](screenshots/dashboard.png)

### 📚 학습하기
- 카테고리별 문제 선택
- 난이도별 문제 생성
- 상세한 해설 제공

![학습 페이지](screenshots/practice.png)

### 🧩 주요 기능 미리보기
- 직관적인 사용자 인터페이스
- 반응형 디자인으로 모든 기기에서 최적화
- 한글 지원으로 편리한 사용

## 📊 프로젝트 현황

![Development Status](https://img.shields.io/badge/Development-Active-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0--beta-orange)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-blue)

### ✅ 구현 완료된 기능
1. **핵심 인프라**
   - Flask 웹 애플리케이션 프레임워크 구축
   - SQLAlchemy 기반 데이터베이스 모델 설계
   - 사용자 인증 시스템 (Flask-Login)
   - 데이터베이스 마이그레이션 시스템

2. **사용자 인터페이스**
   - Bootstrap 5 기반 반응형 웹 디자인
   - 메인 대시보드, 학습 페이지, 문제 풀이 페이지
   - 사용자 등록/로그인 시스템
   - 에러 처리 페이지 (404, 500)

3. **문제 관리 시스템**
   - 문제 생성 및 저장 기능
   - 카테고리별, 난이도별 문제 분류
   - 객관식 문제 형태 지원
   - 문제별 상세 해설 기능

4. **학습 추적 시스템**
   - 사용자별 문제 풀이 기록
   - 정답/오답 통계
   - 최근 학습 활동 추적

### 🏗️ 현재 개발 상태
1. **문제 생성 로직**
   - 현재: 하드코딩된 샘플 문제 템플릿 사용
   - 계획: AI 모델 연동을 통한 동적 문제 생성

2. **사용자 경험 개선**
   - 현재: 기본적인 문제 풀이 플로우 구현
   - 계획: 개인 맞춤형 추천 시스템

3. **AI 통합**
   - 준비 단계: OpenAI API 연동 준비
   - 목표: GPT 기반 문제 자동 생성 시스템

### 📝 향후 개발 계획

#### Phase 1: 기능 고도화 (2025 Q3)
- [ ] 사용자 프로필 시스템 개선
  - 학습 목표 설정
  - 학습 일정 관리
  - 성취도 배지 시스템
- [ ] 문제 생성 AI 모델 통합
  - OpenAI GPT API 연동
  - 문제 품질 검증 시스템
  - 사용자 피드백 반영

#### Phase 2: 소셜 기능 추가 (2025 Q4)
- [ ] 학습 그룹 시스템
  - 그룹 학습 기능
  - 실시간 학습 경쟁
  - 그룹 채팅
- [ ] 커뮤니티 기능
  - 질문 게시판
  - 학습 팁 공유
  - 멘토링 시스템

#### Phase 3: 플랫폼 확장 (2026 Q1)
- [ ] 모바일 앱 개발
  - iOS/Android 네이티브 앱
  - 푸시 알림 시스템
  - 오프라인 학습 지원
- [ ] API 서비스 제공
  - REST API 개발
  - SDK 개발
  - API 문서화

### ⚠️ 알려진 이슈
1. 데이터베이스 최적화 필요
   - 대량의 문제 생성 시 성능 저하
   - 캐싱 시스템 필요

2. UI/UX 개선 필요
   - 모바일 화면에서 일부 레이아웃 깨짐
   - 다크 모드 지원 필요

3. 보안 강화 필요
   - API 엔드포인트 보안 강화
   - 사용자 데이터 암호화 강화

## 🤝 프로젝트 참여하기

![GitHub Issues](https://img.shields.io/github/issues/lhg96/smart-learning-platform)
![GitHub Stars](https://img.shields.io/github/stars/lhg96/smart-learning-platform)
![GitHub Forks](https://img.shields.io/github/forks/lhg96/smart-learning-platform)

### 개발 환경 설정
1. 개발 도구
   - VS Code 또는 PyCharm 권장
   - Python 3.8 이상
   - Git

2. 코드 컨벤션
   - PEP 8 준수
   - Black 포맷터 사용
   - Type hints 사용

3. 테스트
   - pytest 사용
   - 테스트 커버리지 80% 이상 유지

### 기여 가이드라인
- 이슈 생성 전 먼저 검색
- 풀 리퀘스트 전 테스트 실행
- 커밋 메시지는 명확하게 작성
- 문서화 필수

## 📄 라이센스

![License](https://img.shields.io/badge/License-MIT-yellow)

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👥 기여하기

프로젝트에 기여하고 싶으시다면 다음 절차를 따라주세요:

1. 이 저장소를 Fork 합니다.
2. 새로운 Branch를 생성합니다 (`git checkout -b feature/AmazingFeature`)
3. 변경사항을 Commit 합니다 (`git commit -m 'Add some AmazingFeature'`)
4. Branch에 Push 합니다 (`git push origin feature/AmazingFeature`)
5. Pull Request를 생성합니다.

## � 학습 자료 출처

### 기본 문제 소스
1. 공신력 있는 영어 시험 문제
   - TOEIC 기출 문제 패턴
   - TOEFL 문제 구조
   - 수능 영어 기출 문제
   - Cambridge English Exams

2. 실용 영어 자료
   - BBC Learning English
   - VOA Learning English
   - TED Talks 스크립트
   - The New York Times Learning Network

3. AI 문제 생성을 위한 프롬프트 템플릿
   - 문법 문제 생성 패턴
   - 어휘 문제 변형 규칙
   - 독해 지문 난이도 조절
   - 발음/듣기 문제 생성 기준

### 해설 및 설명 자료
1. 영문법 참고 자료
   - Cambridge Grammar
   - Oxford Practice Grammar
   - Betty Azar's Understanding and Using English Grammar

2. 어휘 학습 자료
   - Oxford Collocations Dictionary
   - Longman Dictionary of Contemporary English
   - Academic Word List

### AI 모델 활용 계획
1. OpenAI GPT 모델
   - 문제 생성 및 변형
   - 맥락에 맞는 예문 생성
   - 상세 해설 작성

2. Google BERT 모델
   - 텍스트 난이도 분석
   - 문장 구조 분석
   - 어휘 수준 평가



## 📞 문의하기

[![Email](https://img.shields.io/badge/Email-hyun.lim@okkorea.net-red)](mailto:hyun.lim@okkorea.net)
[![Website](https://img.shields.io/badge/Website-okkorea.net-blue)](https://www.okkorea.net)

개발 관련 컨설팅 및 외주 받습니다.

프로젝트 관리자 연락처:
- name: 임현근 (Hyun-Keun Lim)
- Email: hyun.lim@okkorea.net
- homepage: https://www.okkorea.net

---

<div align="center">

**⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요! ⭐**

![GitHub Repo stars](https://img.shields.io/github/stars/lhg96/smart-learning-platform?style=social)

</div>