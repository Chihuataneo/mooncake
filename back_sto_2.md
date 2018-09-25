## 是本人，无法还款，通报案情+核资，有房有车结婚了,问各种问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* confirm
    - action_marriage_yes
* confirm
    - action_house_yes
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* require_influence
    - utter_require_influence
* request_money
    - utter_loan
* instalments
    - utter_instalments
* part
    - utter_part
* how_pay
    - utter_how_pay
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，结婚，没房有车，问金额
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* confirm
    - action_marriage_yes
* deny 
    - action_house_no
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* request_money
    - utter_loan
* confirm
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，结婚，没房没车，没问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* confirm
    - action_marriage_yes
* deny
    - action_house_no
* deny
    - action_car_no
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* part
    - utter_part
* confirm
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，结婚，有房没车，没问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* confirm
    - action_marriage_yes
* confirm
    - action_house_yes
* deny
    - action_car_no
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，没结婚，有房没车，没问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* deny
    - action_marriage_no
* confirm
    - action_house_yes
* deny
    - action_car_no
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，没结婚，没房没车，没问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* deny
    - action_marriage_no
* deny
    - action_house_no
* deny
    - action_car_no
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* how_pay
    - utter_how_pay
* confirm
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，结婚，没房有车，没问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* deny
    - action_marriage_no
* deny
    - action_house_no
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye

## 是本人，无法还款，通报案情+核资，没结婚，有房有车，没问题
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* cant_pay
    - utter_other_reason
* deny
    - utter_case_notice
    - utter_credit_investigation
    - utter_prompt
    - utter_law
    - utter_family
    - utter_prompt
* confirm
    - action_ask_marriage
* deny
    - action_marriage_no
* confirm
    - action_house_yes
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye

## 是本人，承诺还款
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* promise_pay
    - utter_specific_time
    - utter_second_breach

## 是本人，要求还一部分
* confirm 
    - utter_self_report
    - utter_loan
    - utter_asked_random
* part
    - utter_part
    - action_ask_marriage
* confirm
    - action_marriage_yes
* deny
    - action_house_no
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye

## 是本人，利息等讨价还价
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* bargain
    - utter_bargain
    - action_ask_marriage
* confirm
    - action_marriage_yes
* deny
    - action_house_no
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye

## 是本人，要求分期
* confirm
    - utter_self_report
    - utter_loan
    - utter_asked_random
* instalments
    - utter_instalments
    - action_ask_marriage
* confirm
    - action_marriage_yes
* deny
    - action_house_no
* confirm
    - action_car_yes
    - action_handle
    - utter_prompt
* confirm
    - utter_question
* deny
    - utter_end
* confirm
    - utter_goodbye


## 不是本人的情况,无关第三方
* deny
    - utter_self_report
    - utter_relationship
* deny
    - utter_others_notice_deny

## 不是本人，相关第三方
* deny
    - utter_self_report
    - utter_relationship
* confirm
    - utter_others_notice_2

## fallback story
* out_of_scope
  - action_default_fallback