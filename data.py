from covid19uncle import GlobalCovid19,ThaiCovid19

thai = ThaiCovid19()
# res = 'อัพเดต: ' + thai['อัพเดต']
# res+= '\nผู้ป่วยสะสม: ' + thai['ผู้ป่วยสะสม']
# res+= '\nผู้ป่วยรายใหม่: ' + thai['ผู้ป่วยรายใหม่']
# res+= '\nผู้ป่วยรุนแรง: ' + thai['ผู้ป่วยรุนแรง']
# res+= '\nผู้ป่วยเสียชีวิต: ' + thai['ผู้ป่วยเสียชีวิต']

def call_back(message):
    message = message.lower()
    res = ''

    if message.find('อัพเดต') > -1 or message.find('update') > -1:
        res = 'อัพเดต: ' + thai['อัพเดต']
        res+= '\nผู้ป่วยสะสม: ' + thai['ผู้ป่วยสะสม']
        res+= '\nผู้ป่วยรายใหม่: ' + thai['ผู้ป่วยรายใหม่']
        res+= '\nผู้ป่วยรุนแรง: ' + thai['ผู้ป่วยรุนแรง']
        res+= '\nผู้ป่วยเสียชีวิต: ' + thai['ผู้ป่วยเสียชีวิต']

    return res

print()
# print('อัพเดต:', thai['อัพเดต'])
# print('ผู้ป่วยสะสม:', thai['ผู้ป่วยสะสม'])
# print('ผู้ป่วยรายใหม่:', thai['ผู้ป่วยรายใหม่'])
# print('ผู้ป่วยรุนแรง:', thai['ผู้ป่วยรุนแรง'])
# print('ผู้ป่วยเสียชีวิต', thai['ผู้ป่วยเสียชีวิต'])

# print('ผู้ป่วยกลับบ้านแล้ว:', thai['ผู้ป่วยกลับบ้านแล้ว'])
# print('ผู้ป่วยเฝ้าระวังสะสม:', thai['ผู้ป่วยเฝ้าระวังสะสม'])
# print('ผู้ป่วยเฝ้าระวังรายใหม่:', thai['ผู้ป่วยเฝ้าระวังรายใหม่'])
# print('รักษาพยาบาลอยู่รพ:', thai['รักษาพยาบาลอยู่รพ.'])
# print('รักษาพยาบาลกลับบ้าน:', thai['รักษาพยาบาลกลับบ้าน'])
# print('รักษาพยาบาลสังเกตอาการ:', thai['รักษาพยาบาลสังเกตอาการ'])

# print('ผู้เดินทางที่คัดกรองสะสมจากสนามบิน:', thai['ผู้เดินทางที่คัดกรองสะสมจากสนามบิน'])
# print('ผู้เดินทางที่คัดกรองสะสมจากท่าเรือ:', thai['ผู้เดินทางที่คัดกรองสะสมจากท่าเรือ'])
# print('ผู้เดินทางที่คัดกรองสะสมจากด่านพรมแดน:', thai['ผู้เดินทางที่คัดกรองสะสมจากด่านพรมแดน'])
# print('ผู้เดินทางที่คัดกรองสะสมจากสตม.แจ้งวัฒนะ:', thai['ผู้เดินทางที่คัดกรองสะสมจากสตม.แจ้งวัฒนะ'])
# print('อ้างอิง', thai['อ้างอิง'])