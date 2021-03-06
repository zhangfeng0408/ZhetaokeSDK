# 折淘客 Python3 SDK
淘宝联盟-折淘客(www.zhetaoke.com) - Python3 SDK （非官方）

2020-05-24 所有接口已经更新为最新版，SDK接口与上一代有变化，不能通用，更新前请进行测试。

阿里妈妈已经无法申请到转链、订单等API权限，但可以用第三方接口使用到这些权限。
本SDK基于官方SDK修改得到的，提供折淘客的所有API功能，使用方法可见demo目录。
运行demo时需要将config.sample.py重命名为config.py，并填入自己的信息，同时将ztk目录放入demo目录中。

**注：淘客账号授权、淘宝客渠道备案还未完善**

### API列表

| 折淘客API | SDK类名 |
| ------ | ------------ |
| 高佣转链（商品ID）| TbkPrivilegeGetRequest |
| 高佣转链（淘口令）| TbkTpwdConvertRequest |
| 订单查询 | TbkScOrderGetRequest |
| 解析商品编号 | ZtkItemIdConvertRequest |
| 淘客账号授权 | ZtkAuthorizeRequest |
| 获取账户授权列表 | ZtkAuthorisationGetRequest |
| 淘宝短链转换 | TbkSpreadGetRequest |
| 淘口令生成 | TbkTpwdCreateRequest |
| 淘宝客邀请码生成 | TbkScInvitecodeGetRequest |
| 淘宝客渠道备案 | TbkScPublisherInfoSave |
| 淘宝客渠道信息查询 | TbkScPublisherInfoGet |
| 全网商品详情 | TbkItemInfoGetRequest |
| 淘宝联盟官方活动推广 | TbkScActivitylinkToolgetRequest |
| 支付宝代付 | ZtkAlipayAgentPayRequest |
| 店铺链接转换 | TbkScShopConvertRequest |
