from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet,Restarted

class ActionHandle(Action):
   def name(self):
      # type: () -> Text
      return "action_handle"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
      turn = tracker.get_slot("turn")
      if (turn is None):
      #    intent = tracker.latest_message['intent'].get('name')
          dispatcher.utter_message("嗯，因为就是说像有些人，就是说有这种不可抗力的原因导致的，像卡有些是因为这个卡是被盗刷的，不是自己使用这些情况，您这边没有没有这方这些方面的原因呢？")
        #  SlotSet("turn", "1")
          return [SlotSet("turn", "1")]
      if (turn == "1"):
          intent = tracker.latest_message['intent'].get('name')
          if (intent == "confirm"):
              dispatcher.utter_message("嗯，你能再详细描述一下吗？")
          else:
              dispatcher.utter_message("嗯这样的,嗯因为前几天，总行这边呢是把这个相关的这个报案文书直接下发到咱当地要求做这个报案处理，但是的话我们看了一下您这个用卡记录，一直是还是非常不错的，嗯那么所以说今天我打这个电话呢也是联系一下咱这边到底是有没有什么特殊的情况，啊您有没有就是说需要解释的，就是说这个特殊原因导致咱这个款项无法处理的，或者说您这边的话噢自己有什打算，您都可以跟我说一下，在这个嗯报案材料书上呢就说我给您做一下备注，后期的话在正式报案定性的时候可能会对您有帮助。")
          return [SlotSet("turn", "2")]
      if (turn == "2"):
          intent = tracker.latest_message['intent'].get('name')
          if (intent == "cant_pay"):
              dispatcher.utter_message("对于银行来说，也是为了把钱追回来，谁也不想被债务天天追着，你这边最好还是想想办法，这个对于你以后的生活都有影响，对吧。")
          else:
              dispatcher.utter_message("按照刑法第一百九十六条的规定，进行信用卡诈骗的，应予以立案追诉。本条规定的恶意透支，是指持卡人已非法占有为目的，规定超过限额，并且发卡银行两次催收后超过三个月扔不归还的。对于银行来说，也是为了把钱追回来，你这边最好还是想想办法，因为这个对于你以后的生活都有影响，好吧。")
          return [SlotSet("turn", "3")]
      if (turn == "3"):
          dispatcher.utter_message("嗯，你现在结婚了吗？")
          return [SlotSet("turn", "4")]
      if (turn == "4"):
          marriage = tracker.get_slot("marriage")
          house = tracker.get_slot("house")
          car = tracker.get_slot("car")
          if (marriage is None):
              intent = intent = tracker.latest_message['intent'].get('name')
              if (intent == "confirm"):
                  dispatcher.utter_message("嗯，你有房子吗？")
                  return [SlotSet("marriage", "yes")]
              elif (intent == "deny"):
                  dispatcher.utter_message("嗯，你有房子吗？")
                  return [SlotSet("marriage", "no")]
              else:
                  dispatcher.utter_message("嗯？结婚了吗？")
              return []
          elif (house is None):
              intent = intent = tracker.latest_message['intent'].get('name')
              if (intent == "confirm"):
                  dispatcher.utter_message("嗯，车呢，有吗？")
                  return [SlotSet("house", "yes")]
              elif (intent == "deny"):
                  dispatcher.utter_message("嗯，车呢，有吗？")
                  return [SlotSet("house", "no")]
              else:
                  dispatcher.utter_message("嗯？有没有房？")
              return []
          elif (car is None):
              intent = intent = tracker.latest_message['intent'].get('name')
              message_ = ""
              if (marriage == "yes"):
                  message_ = message_ + "你结婚了,以后你孩子上学工作，一些工作像公务员，参军，考军校等，都需要政审之类的，征信报告还是很重要的。>这些记录还是需要处理一下的。"
              if (house == "yes"):
                  message_ = message_ + "你还有房儿,"
              if (intent == "confirm"):
                  message_ = message_ + "你还有车。"
                  if (message_  == ""):
                      dispatcher.utter_message("好的，我备注了你的信息。后续会持续跟进，我还是需要提醒一下，这些通话都是会录音的，后期我们会进行核实>，会作为>立案的依据。")
                      return [SlotSet("turn", "5")]
                  else:
                      message_ = message_ + "这点钱还还不上吗？银行在处理这些问题的时候，也不是什么人都浪费时间去要的，你这不是说单纯的能力有问题，也要看咱这边主观态度，有无还款意愿。后期银行立案的时候，这些都是重要的资料。你如果不还的话，银行可以向法院申请资产冻结，拍卖的时候，到那时候更>难办，就这么点钱，你想好要不要到这一步吧。"
                  dispatcher.utter_message(message_)
                  return [SlotSet("turn", "5")]
              elif (intent == "deny"):
                  if (house == "yes"):
                      message_ = message_ + "这点钱还还不上吗？银行在处理这些问题的时候，也不是什么人都浪费时间去要的，你这不是说单纯的能力有问题，也要看咱这边主观态度，有无还款意愿。后期银行立案的时候，这些都是重要的资料。你如果不还的话，银行可以向法院申请资产冻结，拍卖的时候，到那时候更>难办，就这么点钱，你想好要不要到这一步吧。"
                  if (message_ == ""):
                      message_ = "嗯，我备注了你的信息，本轮电话也会被录音，如果资料有误，要承担提供错误信息的责任。好吧。"
                  dispatcher.utter_message(message_)
                  return [SlotSet("turn", "5")]
              else:
                  dispatcher.utter_message("嗯？有没有车？")
                  return []
      if (turn == "5"):
          dispatcher.utter_message("嗯那就是说您这边的话还有其他疑问吗？如果是没有疑问的话，这个事情我就例行通知到了，嗯您这边的话就是说如果说有疑问，您可以现在可以提可以就说问我，我可以如果能作出回答的话，我可以给您回答一下。") 
          return [SlotSet("turn", "6")]
      if (turn == "6"):
          dispatcher.utter_message("行，您这边如果说能解决的话，您自己联系一下客服个人建议，最好是明天。如果说客户这边没有给你做任何答复，你可以直接联系我，后期我可以能帮的话，我尽可能帮你们去把这个案子给撤一下。嗯，好吧?")
          return [SlotSet("turn", "7")]
      if (turn == "7"):
          dispatcher.utter_message("嗯，行，拜拜")
          return [Restarted()]
      return []
'''
class ActionSearchRestaurants(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
            tracker.get_slot("people"))
        return []


class ActionDefaultFallback(Action):
   def name(self):
      # type: () -> Text
      return "action_default_fallback"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
     # item = tracker.get_slot("item")
      dispatcher.utter_message("嗯？什么意思？")
      return []
'''
