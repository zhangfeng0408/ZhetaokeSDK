from ztk.api import TbkScInvitecodeGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkScInvitecodeGetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.relation_app = "common" # 渠道推广的物料类型，通常为common 
req.code_type = 1 # 邀请码类型，1 - 渠道邀请，2 - 渠道裂变，3 -会员邀请

result = req.get_response()
print(result)
