## first story
* confirm
  - utter_open
> check_1

## 不是本人，同意转告
* deny
  - utter_others_notice_1
* confirm
  - utter_others_notice_2

## 不是本人，不同意转告
* deny
  - utter_others_notice_1
* deny
  - utter_others_notice_deny

## check_1_cant_pay OR confirm OR deny
> check_1
* cant_pay OR confirm OR deny
  - action_handle
> check_1

## check_1_promise_pay
> check_1
* promise_pay
  - utter_specific_time
* confirm OR deny OR goodbye OR thanks OR sharp_answer OR
request_money OR ask_lowest OR instalments OR bargain OR part OR deny_inform OR require_influence OR paid_back OR deny_loan OR cant_pay OR promise_pay OR how_pay OR ask_id OR report
  - utter_second_breach

## check_1_instalments
> check_1
* instalments
  - utter_instalments
> check_1

## check_1_deny_loan
> check_1
* deny_loan
  - utter_deny_loan

## check_1_how_pay
> check_1
* how_pay
  - utter_how_pay
> check_1

## check_1_ask_lowest
> check_1
* ask_lowest
  - utter_ask_lowest
> check_1

## check_1_bargain
> check_1
* ask_bargain
  - utter_bargain
> check_1

## check_1_request_money
> check_1
* request_money
  - utter_request_money
> check_1

## check_1_part
> check_1
* part
  - utter_part
> check_1

## check_1_ask_id
> check_1
* ask_id
  - utter_ask_id
> check_1

## check_1_report
> check_1
* report
  - utter_report

## check_1_sharp_answer
> check_1
* sharp_answer
  - utter_sharp_answer
> check_1

## fallback story
* out_of_scope
  - action_default_fallback
