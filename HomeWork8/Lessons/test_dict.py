import json

company_json = """ {
"id" : 111,
"isActive" : true,
"createDateTime" : "2022-12-23T14:43:26.713Z",
"lastChangedDateTime" : "2022-12-23T14:43:26.713Z",
"name" : "Барбершоп Цирюьник",
"description" : "Крутые стрижки для кртух шишек"

}
"""

def test_parse_json():
  company = json.loads(company_json)
  assert company["id"]==111
