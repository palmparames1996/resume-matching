from app.resume import MatchPercentageText
import pytest

def preparing_class(val):
    if val >= 80:
        class_val = 0
    else:
        class_val = 10
    return class_val

@pytest.mark.parametrize("text1, text2, expect, model_id", [("HDFS","hdfs",0,1),("HD","hdfs",10,1)])
def test_matcher(text1, text2, expect, model_id):
  val = MatchPercentageText(text1,text2,model_id)
  class_val = preparing_class(val)
  assert class_val == expect