## 不是本人，同意转告
* deny
    - utter_others_notice_1
* confirm
    - utter_others_notice_2
    - export

## 不是本人，不同意转告
* deny
    - utter_others_notice_1
* deny
    - utter_others_notice_deny
    - export

## 是本人，承诺还款
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* confirm
    - utter_paid_back
    - export

## 是本人，无法还款，后承诺想办法
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* self_cant_pay
    - utter_cant_pay
* confirm
    - utter_promise_pay
    - export

## 是本人，无法还款，说后还是无法还款
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* self_cant_pay
    - utter_cant_pay
* deny
    - utter_deny_dispute
    - export

## 是本人，已经还款
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* self_paid_back
    - utter_paid_back
    - export

## 是本人，否认欠款
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* self_deny_loan
    - utter_deny_loan
    - export

## 是本人，否认逾期
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* self_deny_overdue
    - utter_deny_overdue
    - export

## 举报
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* report
    - utter_rest
    - export

## Generated Story -4893167485611229992
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* self_cant_pay
    - utter_cant_pay
* self_cant_pay
    - utter_cant_pay
* self_promise_pay
    - utter_promise_pay
    - export

## fallback story
* out_of_scope
  - action_default_fallback
