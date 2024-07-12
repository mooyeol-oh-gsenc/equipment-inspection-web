# create_tables.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, BLOB, DECIMAL
from sqlalchemy.sql import insert

DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# 테이블 정의
inspection_details = Table(
    'inspection_details', metadata,
    Column('inspection_id', Integer, primary_key=True),
    Column('inspection_type', String, nullable=False),
    Column('user_ip', String),
    Column('equipment_photo', BLOB),
    Column('equipment_type', String),
    Column('inspection_form_id', Integer, ForeignKey('inspection_forms.inspection_form_id')),
    Column('equipment_registration_number', String),
    Column('user_latitude', DECIMAL(9, 6)),
    Column('user_longitude', DECIMAL(9, 6)),
    Column('site_id', Integer, ForeignKey('sites.site_id')),
    Column('inspection_date', DateTime)
)

sites = Table(
    'sites', metadata,
    Column('site_id', Integer, primary_key=True),
    Column('site_name', String, nullable=False),
    Column('site_address', String),
    Column('site_latitude', DECIMAL(9, 6)),
    Column('site_longitude', DECIMAL(9, 6))
)

inspection_forms = Table(
    'inspection_forms', metadata,
    Column('inspection_form_id', Integer, primary_key=True),
    Column('equipment_type', String, nullable=False),
    Column('inspection_type', String, nullable=False)
)

inspection_items = Table(
    'inspection_items', metadata,
    Column('inspection_item_id', Integer, primary_key=True),
    Column('inspection_form_id', Integer, ForeignKey('inspection_forms.inspection_form_id')),
    Column('inspection_item_number', Integer, nullable=False),
    Column('inspection_item_name', String, nullable=False),
    Column('inspection_item_method', String, nullable=False)
)

inspection_item_details = Table(
    'inspection_item_details', metadata,
    Column('inspection_item_detail_id', Integer, primary_key=True),
    Column('inspection_id', Integer, ForeignKey('inspection_details.inspection_id')),
    Column('inspection_item_id', Integer, ForeignKey('inspection_items.inspection_item_id')),
    Column('inspection_item_photo', BLOB),
    Column('inspection_item_result', String),
    Column('inspection_item_remark', String)
)

# 테이블 생성
metadata.create_all(engine)

# 초기 데이터 삽입
with engine.connect() as conn:
    # inspection_forms 초기 데이터
    conn.execute(insert(inspection_forms), [
        {'inspection_form_id': 0, 'equipment_type': '굴착기', 'inspection_type': '작업시작 전 안전점검'},
        {'inspection_form_id': 1, 'equipment_type': '이동식크레인', 'inspection_type': '작업시작 전 안전점검'}
    ])

    # inspection_items 초기 데이터
    conn.execute(insert(inspection_items), [
        # 굴착기 작업시작 전 안전점검표
        {'inspection_item_id': 0, 'inspection_form_id': 0, 'inspection_item_number': 0, 'inspection_item_name': 'Note', 'inspection_item_method': '1. 관련법 : 산업안전보건기준에 관한 규칙 제35조제2항 관련 [별표3] 작업시작 전 점검사항(제35조제2항 관련) 14. 차량계 건설기계 해당'},
        {'inspection_item_id': 1, 'inspection_form_id': 0, 'inspection_item_number': 1, 'inspection_item_name': '조종장치', 'inspection_item_method': '조종장치는 정상작동 될 것'},
        {'inspection_item_id': 2, 'inspection_form_id': 0, 'inspection_item_number': 2, 'inspection_item_name': '제동장치', 'inspection_item_method': '주차브레이크는 정상작동 될 것'},
        {'inspection_item_id': 3, 'inspection_form_id': 0, 'inspection_item_number': 3, 'inspection_item_name': '비상정지장치', 'inspection_item_method': '버튼은 적색의 수동복귀형일 것 버튼을 누르면 동력이 차단되어 작동이 중지될 것'},
        {'inspection_item_id': 4, 'inspection_form_id': 0, 'inspection_item_number': 4, 'inspection_item_name': '후진경보기/후방카메라', 'inspection_item_method': '후진 경보장치/후방카메라는 정상적으로 작동될 것'},
        {'inspection_item_id': 5, 'inspection_form_id': 0, 'inspection_item_number': 5, 'inspection_item_name': '각종 등화장치', 'inspection_item_method': '전조등, 정지등, 후진등, 방향지시등, 경광등의 기능은 정상작동 될 것'},
        {'inspection_item_id': 6, 'inspection_form_id': 0, 'inspection_item_number': 6, 'inspection_item_name': '안전시설물', 'inspection_item_method': '승강용 발판, 운전석 방호설비 등의 상태가 양호할 것'},
        {'inspection_item_id': 7, 'inspection_form_id': 0, 'inspection_item_number': 7, 'inspection_item_name': '좌석안전띠', 'inspection_item_method': '좌석안전띠는 파손이나 고장이 없고 운전 시에는 반드시 착용할 것'},
        {'inspection_item_id': 8, 'inspection_form_id': 0, 'inspection_item_number': 8, 'inspection_item_name': '조종석 내부', 'inspection_item_method': '운전 중 핸드폰을 이용하여 DMB 시청, 게임은 하지 않을 것 페달 주변 정리정돈 상태가 양호할 것'},

        # 이동식크레인 작업시작 전 안전점검표
        {'inspection_item_id': 9, 'inspection_form_id': 1, 'inspection_item_number': 0, 'inspection_item_name': 'Note', 'inspection_item_method': '1. 관련법 : 산업안전보건기준에 관한 규칙 제35조제2항 관련 [별표3] 작업시작 전 점검사항(제35조제2항 관련) 5. 이동식크레인 해당'},
        {'inspection_item_id': 10, 'inspection_form_id': 1, 'inspection_item_number': 1, 'inspection_item_name': '인디케이터', 'inspection_item_method': '조종석 내 인디케이터의 작업반경, 붐길이, 크레인제원, 정격총하중 정상동작'},
        {'inspection_item_id': 11, 'inspection_form_id': 1, 'inspection_item_number': 2, 'inspection_item_name': '안전장치', 'inspection_item_method': '권과방지장치, 과부화방지장치, 삼색경보등 등 작동에 이상이 없을 것'},
        {'inspection_item_id': 12, 'inspection_form_id': 1, 'inspection_item_number': 3, 'inspection_item_name': '유압장치', 'inspection_item_method': '각종 실린더 등의 누유 및 손상, 마모 등이 없을 것'},
        {'inspection_item_id': 13, 'inspection_form_id': 1, 'inspection_item_number': 4, 'inspection_item_name': '아웃트리거', 'inspection_item_method': '최대확장, 수축방지핀 체결 및, 당사 받침목 기준 준수 확인'},
        {'inspection_item_id': 14, 'inspection_form_id': 1, 'inspection_item_number': 5, 'inspection_item_name': '후크 및 와이어로프', 'inspection_item_method': '후크: 해지장치 정상작동상태 확인 와이어로프: 지름감소(7%이내), 소선파단(10%이내) 등 이상이 없을 것'},
        {'inspection_item_id': 15, 'inspection_form_id': 1, 'inspection_item_number': 6, 'inspection_item_name': '활차', 'inspection_item_method': '활차는 손상이 없고 와이어로프 이탈방지장치는 정상 체결되어 있을 것'},
        {'inspection_item_id': 16, 'inspection_form_id': 1, 'inspection_item_number': 7, 'inspection_item_name': '지반상태', 'inspection_item_method': '크레인 자중(카운터웨이트포함) + 정격총하중의 무게를 충분히 지탱 할 수 있는 충분한 지내력을 확보 할 것'},
        {'inspection_item_id': 17, 'inspection_form_id': 1, 'inspection_item_number': 8, 'inspection_item_name': '조종석 내부', 'inspection_item_method': '운전 중 핸드폰을 이용하여 DMB 시청, 게임은 하지 않을 것 페달 주변 정리정돈 상태가 양호할 것'},
        {'inspection_item_id': 18, 'inspection_form_id': 1, 'inspection_item_number': 9, 'inspection_item_name': '와이어로프 드럼', 'inspection_item_method': '와이어로프 드럼은 난권이 없을 것'}
    ])
