import streamlit as st


# --------------------------------------------------
# 페이지 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="YSH의 MBTI 포켓몬 추천👍 나와 딱 맞는 몬스터는?",
    page_icon="⚡",
    layout="centered",
)


# --------------------------------------------------
# MBTI별 포켓몬 추천 데이터
# --------------------------------------------------
POKEMON_DATA = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧬",
        "type": "에스퍼",
        "title": "냉철한 전략가",
        "description": (
            "높은 지능과 독립적인 성향을 지닌 뮤츠는 "
            "논리적으로 상황을 분석하고 자신만의 계획을 세우는 INTJ와 잘 어울립니다."
        ),
        "strength": "분석력, 독립성, 장기적인 계획",
    },
    "INTP": {
        "pokemon": "후딘",
        "emoji": "🥄",
        "type": "에스퍼",
        "title": "끝없이 탐구하는 사색가",
        "description": (
            "뛰어난 두뇌와 강한 호기심을 가진 후딘은 "
            "복잡한 원리를 탐구하고 새로운 아이디어를 즐기는 INTP와 닮았습니다."
        ),
        "strength": "논리적 사고, 지적 호기심, 문제 해결",
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥",
        "type": "불꽃·비행",
        "title": "강력한 지휘관",
        "description": (
            "강한 존재감과 목표 지향적인 성격을 가진 리자몽은 "
            "주도적으로 사람들을 이끌고 성과를 만들어 내는 ENTJ와 잘 맞습니다."
        ),
        "strength": "리더십, 결단력, 목표 달성",
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "👻",
        "type": "고스트·독",
        "title": "재치 있는 아이디어 뱅크",
        "description": (
            "예측하기 어려운 행동과 장난기 넘치는 팬텀은 "
            "새로운 가능성을 발견하고 토론을 즐기는 ENTP와 어울립니다."
        ),
        "strength": "창의성, 순발력, 유쾌한 도전 정신",
    },
    "INFJ": {
        "pokemon": "루기아",
        "emoji": "🌊",
        "type": "에스퍼·비행",
        "title": "깊은 통찰력을 가진 수호자",
        "description": (
            "조용하지만 강한 힘과 책임감을 지닌 루기아는 "
            "사람들의 내면을 이해하고 더 나은 방향을 고민하는 INFJ와 닮았습니다."
        ),
        "strength": "통찰력, 책임감, 깊은 공감",
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🦊",
        "type": "노말",
        "title": "무한한 가능성을 품은 이상주의자",
        "description": (
            "다양한 모습으로 성장할 가능성을 지닌 이브이는 "
            "자신만의 가치와 가능성을 소중히 여기는 INFP와 잘 어울립니다."
        ),
        "strength": "상상력, 진정성, 유연한 가능성",
    },
    "ENFJ": {
        "pokemon": "가디안",
        "emoji": "✨",
        "type": "에스퍼·페어리",
        "title": "따뜻한 카리스마의 조력자",
        "description": (
            "소중한 사람을 적극적으로 보호하는 가디안은 "
            "타인의 성장을 돕고 공동체를 이끄는 ENFJ와 잘 맞습니다."
        ),
        "strength": "공감 능력, 헌신, 긍정적인 영향력",
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "type": "전기",
        "title": "활기찬 분위기 메이커",
        "description": (
            "밝고 친근하며 모험을 즐기는 피카츄는 "
            "호기심과 열정으로 주변 사람에게 에너지를 주는 ENFP와 닮았습니다."
        ),
        "strength": "열정, 친화력, 새로운 경험",
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🐢",
        "type": "물",
        "title": "믿음직한 원칙주의자",
        "description": (
            "단단한 방어력과 안정적인 전투 능력을 지닌 거북왕은 "
            "책임감이 강하고 맡은 일을 정확하게 처리하는 ISTJ와 어울립니다."
        ),
        "strength": "책임감, 신뢰성, 체계적인 실행",
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "emoji": "💗",
        "type": "노말",
        "title": "다정한 치유자",
        "description": (
            "다른 포켓몬을 돌보고 회복시키는 해피너스는 "
            "주변 사람을 세심하게 챙기고 헌신하는 ISFJ와 잘 맞습니다."
        ),
        "strength": "배려, 인내심, 세심한 지원",
    },
    "ESTJ": {
        "pokemon": "괴력몬",
        "emoji": "💪",
        "type": "격투",
        "title": "실행력 강한 관리자",
        "description": (
            "강한 힘과 꾸준한 훈련 능력을 가진 괴력몬은 "
            "현실적인 기준을 세우고 효율적으로 일을 추진하는 ESTJ와 닮았습니다."
        ),
        "strength": "실행력, 조직력, 현실적인 판단",
    },
    "ESFJ": {
        "pokemon": "님피아",
        "emoji": "🎀",
        "type": "페어리",
        "title": "사랑받는 관계 중심형",
        "description": (
            "부드럽고 친근한 분위기의 님피아는 "
            "사람들과 조화를 이루며 따뜻한 관계를 만드는 ESFJ와 잘 어울립니다."
        ),
        "strength": "친화력, 협력, 세심한 배려",
    },
    "ISTP": {
        "pokemon": "루카리오",
        "emoji": "🥋",
        "type": "격투·강철",
        "title": "침착한 실전 전문가",
        "description": (
            "상대의 움직임을 감지하고 정확하게 대응하는 루카리오는 "
            "상황을 빠르게 파악하고 직접 해결책을 찾는 ISTP와 닮았습니다."
        ),
        "strength": "상황 판단, 실용성, 위기 대응",
    },
    "ISFP": {
        "pokemon": "세레비",
        "emoji": "🌿",
        "type": "에스퍼·풀",
        "title": "자유로운 감성 탐험가",
        "description": (
            "자연과 조화를 이루며 자유롭게 시간을 여행하는 세레비는 "
            "섬세한 감성과 자신만의 삶의 방식을 중시하는 ISFP와 어울립니다."
        ),
        "strength": "감수성, 유연성, 자연스러운 표현",
    },
    "ESTP": {
        "pokemon": "에이스번",
        "emoji": "⚽",
        "type": "불꽃",
        "title": "대담한 행동파",
        "description": (
            "빠른 움직임과 화려한 기술을 자랑하는 에이스번은 "
            "즉각적으로 행동하고 경쟁과 도전을 즐기는 ESTP와 잘 맞습니다."
        ),
        "strength": "행동력, 순발력, 도전 정신",
    },
    "ESFP": {
        "pokemon": "푸린",
        "emoji": "🎤",
        "type": "노말·페어리",
        "title": "즐거움을 전하는 엔터테이너",
        "description": (
            "노래로 모두의 관심을 사로잡는 푸린은 "
            "풍부한 표현력과 밝은 에너지로 분위기를 살리는 ESFP와 닮았습니다."
        ),
        "strength": "표현력, 사교성, 낙천적인 에너지",
    },
}


# --------------------------------------------------
# CSS 디자인
# --------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top left, #fff6c8 0%, transparent 32%),
                radial-gradient(circle at bottom right, #dceeff 0%, transparent 35%),
                #f8fafc;
        }

        .main-title {
            text-align: center;
            font-size: 2.6rem;
            font-weight: 800;
            margin-top: 0.5rem;
            margin-bottom: 0.4rem;
            color: #1f2937;
        }

        .sub-title {
            text-align: center;
            color: #64748b;
            font-size: 1.05rem;
            margin-bottom: 2rem;
        }

        .result-card {
            background-color: rgba(255, 255, 255, 0.94);
            border: 2px solid #e2e8f0;
            border-radius: 24px;
            padding: 2rem;
            margin-top: 1.5rem;
            text-align: center;
            box-shadow: 0 14px 35px rgba(15, 23, 42, 0.10);
        }

        .pokemon-emoji {
            font-size: 5rem;
            margin-bottom: 0.4rem;
        }

        .mbti-label {
            display: inline-block;
            background-color: #fee2e2;
            color: #b91c1c;
            padding: 0.35rem 0.9rem;
            border-radius: 999px;
            font-weight: 700;
            margin-bottom: 0.8rem;
        }

        .pokemon-name {
            font-size: 2.2rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 0.2rem;
        }

        .pokemon-type {
            color: #475569;
            font-size: 1rem;
            margin-bottom: 1.2rem;
        }

        .pokemon-title {
            color: #2563eb;
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .description {
            color: #334155;
            font-size: 1.05rem;
            line-height: 1.8;
            margin-bottom: 1.2rem;
        }

        .strength-box {
            background-color: #f1f5f9;
            border-radius: 14px;
            padding: 0.9rem;
            color: #334155;
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            color: #94a3b8;
            font-size: 0.85rem;
        }

        div.stButton > button {
            width: 100%;
            height: 3rem;
            border-radius: 14px;
            font-size: 1.05rem;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# 화면 구성
# --------------------------------------------------
st.markdown(
    '<div class="main-title">⚡ MBTI 포켓몬 추천소</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">MBTI를 선택하면 성격에 어울리는 포켓몬을 추천합니다.</div>',
    unsafe_allow_html=True,
)

mbti_options = [
    "선택해 주세요",
    "INTJ",
    "INTP",
    "ENTJ",
    "ENTP",
    "INFJ",
    "INFP",
    "ENFJ",
    "ENFP",
    "ISTJ",
    "ISFJ",
    "ESTJ",
    "ESFJ",
    "ISTP",
    "ISFP",
    "ESTP",
    "ESFP",
]

selected_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요.",
    mbti_options,
)

recommend_button = st.button(
    "나와 어울리는 포켓몬 찾기",
    type="primary",
)


# --------------------------------------------------
# 추천 결과 출력
# --------------------------------------------------
if recommend_button:
    if selected_mbti == "선택해 주세요":
        st.warning("먼저 MBTI를 선택해 주세요.")
    else:
        result = POKEMON_DATA[selected_mbti]

        st.markdown(
            f"""
            <div class="result-card">
                <div class="pokemon-emoji">{result["emoji"]}</div>
                <div class="mbti-label">{selected_mbti}</div>
                <div class="pokemon-name">{result["pokemon"]}</div>
                <div class="pokemon-type">타입: {result["type"]}</div>
                <div class="pokemon-title">{result["title"]}</div>
                <div class="description">{result["description"]}</div>
                <div class="strength-box">
                    <strong>공통 강점</strong><br>
                    {result["strength"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.balloons()


# --------------------------------------------------
# 하단 안내
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        이 추천 결과는 재미를 위한 콘텐츠이며 공식적인 성격 분석이 아닙니다.<br>
        Pokémon 관련 명칭과 캐릭터의 권리는 각 권리자에게 있습니다.
    </div>
    """,
    unsafe_allow_html=True,
)
