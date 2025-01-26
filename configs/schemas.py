SCHEMAS = {
    "pet_places": """
- Table name: PET_PLACES
- Description: This table contains detailed information about pet-friendly facilities, including their location, amenities, and rules for pet accommodation.
- Columns:
    - FCLTY_NM (TEXT): Name of the facility.
    - CTGRY_NM (TEXT): Category name of the facility. (동물병원, 동물약국, 문예회관, 미술관, 미용, 박물관, 반려동물용품, 식당, 여행지, 위탁관리, 카페, 펜션, 호텔)
    - CTPRVN_NM (TEXT): Name of the province or metropolitan city where the facility is located.
    - SIGNGU_NM (TEXT): Name of the district (시군구) where the facility is located.
    - LEGALDONG_NM (TEXT): Name of the legal district (동/면/읍).
    - LI_NM (TEXT): Name of the administrative subdivision (리).
    - LC_LA (TEXT): Latitude of the facility location.
    - LC_LO (TEXT): Longitude of the facility location.
    - ZIP_NO (TEXT): Postal code of the facility location.
    - RDNMADR_NM (TEXT): Road name address of the facility.
    - LNM_ADDR (TEXT): Land-lot number address of the facility.
    - TEL_NO (TEXT): Contact phone number of the facility.
    - HMPG_URL (TEXT): Website URL of the facility.
    - RSTDE_GUID_CN (TEXT): Information about facility closure days.
    - OPER_TIME (TEXT): Operating hours of the facility.
    - PARKNG_POSBL_AT (TEXT): Indicates whether parking is available (Y/N).
    - UTILIIZA_PRC_CN (TEXT): Details about usage fees.
    - ENTRN_POSBL_PET_SIZE_VALUE (TEXT): Size limits for pets allowed entry.
    - PET_LMTT_MTR_CN (TEXT): Restrictions or rules for pet accommodation.
    - IN_PLACE_ACP_POSBL_AT (TEXT): Indicates whether pets are allowed indoors (Y/N).
    - OUT_PLACE_ACP_POSBL_AT (TEXT): Indicates whether pets are allowed outdoors (Y/N).
    - FCLTY_INFO_DC (TEXT): Detailed description of the facility.
    - PET_ACP_ADIT_CHRGE_VALUE (TEXT): Additional charges for pet accommodation.
    """,
    "children_places": """
- Table name: CHILDREN_PLACES
- Description: This is the location data of cultural facilities that can be accompanied by family children such as age of entry, parking, nursing room, stroller rental, and kids zone.
- Columns:
    - FCLTY_NM (TEXT): Name of the facility.
    - MRHST_NM (TEXT): Name of the franchise or affiliated business managing the facility.
    - CTGRY_ONE_NM (TEXT): First-level category of the facility ('전시/공연', '문화관광/명소').
    - CTGRY_TWO_NM (TEXT): Second-level category of the facility ('영화/연극/공연', '전시/기념관', '관광지', '명승지').
    - CTGRY_THREE_NM (TEXT): Third-level category of the facility, if applicable. ('N', '기타전시/박물관', '공연/연극/문화센터', '미술관', '대형기념관/묘역', '테마공원/대형놀이공원', '유명관광지', '아쿠아리움/대형수족관', '해수욕장', '대형예술센터', '일반유원지/일반놀이공원', '휴양림/수목원', '성/성터', '식물원', '대형전시/박물관', '궁궐/종묘', '동물원', '컨벤션센터', '대형미술관', '도서관', '글램핑코리아(캠핑)', '일반유원지')
    - CTPRVN_NM (TEXT): Name of the province or metropolitan city where the facility is located.
    - SIGNGU_NM (TEXT): Name of the district (시군구) where the facility is located.
    - LEGALDONG_NM (TEXT): Name of the legal district (동/면/읍) where the facility is located.
    - LI_NM (TEXT): Name of the administrative subdivision (리), if applicable.
    - LNBR_NO (TEXT): Land lot number of the facility.
    - ROAD_NM (TEXT): Road name where the facility is located.
    - BULD_NO (TEXT): Building number of the facility.
    - LC_LA (TEXT): Latitude of the facility location.
    - LC_LO (TEXT): Longitude of the facility location.
    - ZIP_NO (TEXT): Postal code of the facility location.
    - RDNMADR_NM (TEXT): Road name address of the facility.
    - LNM_ADDR (TEXT): Land-lot number address of the facility.
    - TEL_NO (TEXT): Contact phone number of the facility.
    - HMPG_URL (TEXT): Official website URL of the facility.
    - BLOG_URL (TEXT): Blog URL with additional information about the facility.
    - FACEBOOK_URL (TEXT): Facebook page URL of the facility.
    - INSTGRM_URL (TEXT): Instagram page URL of the facility.
    - RSTDE_GUID_CN (TEXT): Information about closure days (e.g., holidays or maintenance).
    - OPER_TIME (TEXT): Operating hours of the facility.
    - FRE_PARKNG_AT (TEXT): Indicates whether free parking is available (Y/N).
    - CHGD_PARKNG_AT (TEXT): Indicates whether paid parking is available (Y/N).
    - ENTRN_PRICE_AT (TEXT): Indicates whether there is an entrance fee (Y/N).
    - ENTRN_POSBL_BN_VALUE (TEXT): Entry age or restrictions (e.g., 연령제한없음).
    - DSPSN_TOILET_AT (TEXT): Indicates whether there is a designated restroom for persons with disabilities (Y/N).
    - NRSGRM_AT (TEXT): Indicates whether a nursing room is available (Y/N).
    - STROLLER_LEND_AT (TEXT): Indicates whether stroller rental is available (Y/N).
    - KIDS_ZONE_AT (TEXT): Indicates whether there is a designated kids' zone (Y/N).
    """
}