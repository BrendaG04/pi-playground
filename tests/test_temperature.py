from agent.temperature import classify_temp

def test_classify_temp_normal():
	assert classify_temp(40.0) == "NORMAL"

def test_classify_temp_warm_lower__bound():
	assert classify_temp(55.0) == "WARM"

def test_classify_temp_warm_upper_bound():
	assert classify_temp(70.0) == "WARM"

def test_classify_temp_hot():
	assert classify_temp(70.1) == "HOT"
