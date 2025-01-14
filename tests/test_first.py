from jacob_os_version_check.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v is not None
    #assert v == "Ubuntu 24.04.1 LTS"
    # 빈문자열이 아닌지
    # 문자열에 LTS가 포함 되었는지
    # 문자열에 문자도 있고, 숫자도 있는지
    # . 이 포함 되어 있는지
    # 기타 등등 ..... 
    # 길이가 적어도 얼마 이상인지 
    # 요구조건을 만족하는 asseert 문을 만들어보기 
    assert len(v) > 0
    assert "LTS" in v
    assert "." in v
    assert v.replace(" ","").replace(".","").isalnum()
    assert len(v) > 5
