//Exported by Tool, please don't edit this file directly.

package datatable

type EAPICode int32
const (
	EAPICode_Success EAPICode = 0
	EAPICode_Fail EAPICode = 1
	EAPICode_Error_NotLogin EAPICode = 100
	EAPICode_Error_NoPlayer EAPICode = 101
)

type EAPICode_Login int32
const (
	EAPICode_Login_Success EAPICode_Login = 0
	EAPICode_Login_WrongFormat EAPICode_Login = 1
	EAPICode_Login_WrongUser EAPICode_Login = 2
	EAPICode_Login_Fail EAPICode_Login = 3
)

type EAPICode_Register int32
const (
	EAPICode_Register_Success EAPICode_Register = 0
	EAPICode_Register_WrongFormat EAPICode_Register = 1
	EAPICode_Register_UserExist EAPICode_Register = 2
	EAPICode_Register_Fail EAPICode_Register = 3
)

type EEnumType int32	//Test Enum
const (
	EEnumType_Type_None EEnumType = 0
	EEnumType_Type_1 EEnumType = 2
	EEnumType_Type_2 EEnumType = 3
	EEnumType_Type_Max EEnumType = 4
)

type ERoleType int32
const (
	ERoleType_None ERoleType = 0
	ERoleType_Luoli ERoleType = 1
	ERoleType_LanKongQue ERoleType = 2
	ERoleType_LiangCai ERoleType = 3
	ERoleType_Moli ERoleType = 4
	ERoleType_FeiLing ERoleType = 5
	ERoleType_BaiGuangYing ERoleType = 6
	ERoleType_HeiXiangLing ERoleType = 7
	ERoleType_WangMo ERoleType = 8
	ERoleType_ChenSiSi ERoleType = 9
	ERoleType_JianPeng ERoleType = 10
	ERoleType_ShuYan ERoleType = 11
	ERoleType_QiNa ERoleType = 12
	ERoleType_GaoTaiMing ERoleType = 13
	ERoleType_WenQian ERoleType = 14
	ERoleType_FengYinSha ERoleType = 15
	ERoleType_ShuiWangZi ERoleType = 16
	ERoleType_ManDuoLa ERoleType = 17
	ERoleType_XinLin ERoleType = 18
	ERoleType_BingGongZhu ERoleType = 19
	ERoleType_HuangShi ERoleType = 20
	ERoleType_MoSha ERoleType = 21
	ERoleType_PangZun ERoleType = 22
	ERoleType_YanJue ERoleType = 23
	ERoleType_DuNiangNiang ERoleType = 24
	ERoleType_JinWangZi ERoleType = 25
	ERoleType_LingGongZhu ERoleType = 26
	ERoleType_HuoLingZhu ERoleType = 27
	ERoleType_ShiJianGongZhu ERoleType = 28
)

type EFairyType int32
const (
	EFairyType_None EFairyType = 0
	EFairyType_Luoli EFairyType = 1
	EFairyType_LanKongQue EFairyType = 2
	EFairyType_Moli EFairyType = 3
	EFairyType_LiangCai EFairyType = 4
	EFairyType_FeiLing EFairyType = 5
	EFairyType_HeiXiangLing EFairyType = 6
)

type EDollType int32
const (
	EDollType_None EDollType = 0
	EDollType_Luoli EDollType = 1
	EDollType_LanKongQue EDollType = 2
	EDollType_LiangCai EDollType = 3
	EDollType_Moli EDollType = 4
	EDollType_FeiLing EDollType = 5
	EDollType_BaiGuangYing EDollType = 6
	EDollType_HeiXiangLing EDollType = 7
	EDollType_Max EDollType = 8
)

type ERaceType int32
const (
	ERaceType_None ERaceType = 0
	ERaceType_Human ERaceType = 1
	ERaceType_Fairy ERaceType = 2
)

type EMapType int32
const (
	EMapType_None EMapType = 0
	EMapType_Begin EMapType = 1
	EMapType_Login EMapType = 2
	EMapType_Lobby EMapType = 3
	EMapType_CreatePlayer EMapType = 4
	EMapType_Game EMapType = 5
	EMapType_Story EMapType = 6
	EMapType_Media EMapType = 7
)

type ELevelNodeType int32
const (
	ELevelNodeType_None ELevelNodeType = 0
	ELevelNodeType_Begin ELevelNodeType = 1
	ELevelNodeType_Dialog ELevelNodeType = 2
	ELevelNodeType_Branch ELevelNodeType = 3
	ELevelNodeType_Game ELevelNodeType = 4
	ELevelNodeType_Media ELevelNodeType = 5
	ELevelNodeType_SelectFairy ELevelNodeType = 6
	ELevelNodeType_CreatePlayer ELevelNodeType = 7
	ELevelNodeType_LookAround ELevelNodeType = 8
)

type EGameType int32
const (
	EGameType_None EGameType = 0
	EGameType_Manduola EGameType = 1
	EGameType_BeatManduola EGameType = 2
	EGameType_FindFragments EGameType = 3
	EGameType_MovePieces EGameType = 4
	EGameType_ChopVineman EGameType = 5
	EGameType_AdjustClock EGameType = 6
)

type EAttrType int32
const (
	EAttrType_Charm EAttrType = 0
	EAttrType_EnvirPro EAttrType = 1
	EAttrType_Wisdom EAttrType = 2
	EAttrType_Magic EAttrType = 3
)

type EStringType int32
const (
	EStringType_None EStringType = 0
	EStringType_Valid EStringType = 101010000
)

type ECareerType int32
const (
	ECareerType_Student ECareerType = 0
	ECareerType_CivilServants ECareerType = 1
	ECareerType_CorporateEmployees ECareerType = 2
	ECareerType_BusinessManagement ECareerType = 3
	ECareerType_PrivateOwners ECareerType = 4
	ECareerType_Teacher ECareerType = 5
	ECareerType_Soldier ECareerType = 6
	ECareerType_Freelance ECareerType = 7
	ECareerType_Other ECareerType = 8
	ECareerType_Max ECareerType = 9
)

type EDialogType int32
const (
	EDialogType_None EDialogType = 0
	EDialogType_Aside EDialogType = 1
	EDialogType_Inside EDialogType = 2
	EDialogType_Self EDialogType = 3
	EDialogType_Other EDialogType = 4
)

type EDialogPlayMode int32
const (
	EDialogPlayMode_Hand EDialogPlayMode = 0
	EDialogPlayMode_AutoX1 EDialogPlayMode = 1
	EDialogPlayMode_AutoX2 EDialogPlayMode = 2
)

type EGameSoundType int32
const (
	EGameSoundType_None EGameSoundType = 0
	EGameSoundType_Voice EGameSoundType = 1
	EGameSoundType_Effect EGameSoundType = 2
	EGameSoundType_BGM EGameSoundType = 3
)

type EBackgroundType int32
const (
	EBackgroundType_None EBackgroundType = 0
	EBackgroundType_Image EBackgroundType = 1
	EBackgroundType_Media EBackgroundType = 2
	EBackgroundType_Widget EBackgroundType = 3
)

type EMediaOperateType int32
const (
	EMediaOperateType_None EMediaOperateType = 0
	EMediaOperateType_Open EMediaOperateType = 1
	EMediaOperateType_Play EMediaOperateType = 2
	EMediaOperateType_Pause EMediaOperateType = 3
)

type ESceneActorAttrType int32
const (
	ESceneActorAttrType_None ESceneActorAttrType = 0
	ESceneActorAttrType_Widget ESceneActorAttrType = 1
	ESceneActorAttrType_Spine ESceneActorAttrType = 2
	ESceneActorAttrType_Particle ESceneActorAttrType = 3
	ESceneActorAttrType_WidgetMeidia ESceneActorAttrType = 4
)

type ESceneActorType int32
const (
	ESceneActorType_None ESceneActorType = 0
	ESceneActorType_Background ESceneActorType = 1
	ESceneActorType_Spine ESceneActorType = 2
	ESceneActorType_Particle ESceneActorType = 3
)

type ESameTypePlaceHolder int32
const (
	ESameTypePlaceHolder_None ESameTypePlaceHolder = 0
	ESameTypePlaceHolder_0 ESameTypePlaceHolder = 1
	ESameTypePlaceHolder_1 ESameTypePlaceHolder = 2
	ESameTypePlaceHolder_3 ESameTypePlaceHolder = 3
	ESameTypePlaceHolder_Max ESameTypePlaceHolder = 4
)

type EEffectType int32
const (
	EEffectType_None EEffectType = 0
	EEffectType_FadeIn EEffectType = 1
	EEffectType_FadeOut EEffectType = 2
)

type EMoneyType int32
const (
	EMoneyType_Star EMoneyType = 0
	EMoneyType_Diamond EMoneyType = 1
	EMoneyType_RMB EMoneyType = 2
	EMoneyType_Item EMoneyType = 3
)

type EItemType int32
const (
	EItemType_Star EItemType = 0
	EItemType_Diamond EItemType = 1
	EItemType_RMB EItemType = 2
	EItemType_GiftPack EItemType = 3
	EItemType_Exp EItemType = 4
	EItemType_Favor EItemType = 5
	EItemType_Activity EItemType = 6
	EItemType_Background EItemType = 7
	EItemType_Tittle EItemType = 8
	EItemType_MomentCard EItemType = 9
	EItemType_Avatar EItemType = 10
	EItemType_AvatarFrame EItemType = 11
	EItemType_ExpBottle EItemType = 12
	EItemType_Other EItemType = 13
)

type ELabelType int32
const (
	ELabelType_None ELabelType = 0
	ELabelType_New ELabelType = 1
	ELabelType_Hot ELabelType = 2
)

type EShopType int32
const (
	EShopType_MonthCard EShopType = 0
	EShopType_Recharge EShopType = 1
	EShopType_Star EShopType = 2
	EShopType_Diamond EShopType = 3
	EShopType_GiftPack EShopType = 4
	EShopType_Add EShopType = 5
)

type EMailState int32
const (
	EMailState_Unread EMailState = 0
	EMailState_Read EMailState = 1
	EMailState_Received EMailState = 2
)

type EAddPurchaseType int32
const (
	EAddPurchaseType_Success EAddPurchaseType = 0
	EAddPurchaseType_BeyondLimit EAddPurchaseType = 1
	EAddPurchaseType_NotEnough EAddPurchaseType = 2
	EAddPurchaseType_Error EAddPurchaseType = 3
)

type EFragmentsState int32
const (
	EFragmentsState_None EFragmentsState = 0
	EFragmentsState_OnGround EFragmentsState = 1
	EFragmentsState_InBox EFragmentsState = 2
	EFragmentsState_BeCleanedUp EFragmentsState = 3
	EFragmentsState_PickUpStep1 EFragmentsState = 4
	EFragmentsState_PickUpStep2 EFragmentsState = 5
	EFragmentsState_PickedUp EFragmentsState = 6
)

type EFragmentsType int32
const (
	EFragmentsType_Mirror EFragmentsType = 0
	EFragmentsType_Gem EFragmentsType = 1
	EFragmentsType_Sword EFragmentsType = 2
)

type EPhoneHeaderType int32
const (
	EPhoneHeaderType_ChatList EPhoneHeaderType = 0
	EPhoneHeaderType_Moment EPhoneHeaderType = 1
	EPhoneHeaderType_Address EPhoneHeaderType = 2
	EPhoneHeaderType_Chat EPhoneHeaderType = 3
	EPhoneHeaderType_ChatMore EPhoneHeaderType = 4
	EPhoneHeaderType_ChatRecord EPhoneHeaderType = 5
	EPhoneHeaderType_ChatRecordRole EPhoneHeaderType = 6
	EPhoneHeaderType_ChatCallRecord EPhoneHeaderType = 7
	EPhoneHeaderType_ChatCallBackground EPhoneHeaderType = 8
)

type EChatMessageType int32
const (
	EChatMessageType_End EChatMessageType = 0
	EChatMessageType_Reset EChatMessageType = 1
	EChatMessageType_Target EChatMessageType = 2
	EChatMessageType_Self EChatMessageType = 3
	EChatMessageType_Send EChatMessageType = 4
	EChatMessageType_RedEnvelope EChatMessageType = 5
)

type EUserState int32
const (
	EUserState_Normal EUserState = 0
	EUserState_Disable EUserState = 1
)

type EPlayerState int32
const (
	EPlayerState_Normal EPlayerState = 0
	EPlayerState_NoInfo EPlayerState = 1
	EPlayerState_Create EPlayerState = 2
)

type ETokenState int32
const (
	ETokenState_Normal ETokenState = 0
	ETokenState_Disable ETokenState = 1
)

type EServerState int32
const (
	EServerState_Normal EServerState = 0
	EServerState_Busy EServerState = 1
	EServerState_Full EServerState = 2
	EServerState_Maintain EServerState = 3
)

type EWidgetType int32
const (
	EWidgetType_None EWidgetType = 0
	EWidgetType_BackgroundImage EWidgetType = 1
	EWidgetType_BackgroundMedia EWidgetType = 2
	EWidgetType_BackgroundManduola EWidgetType = 3
	EWidgetType_Spine EWidgetType = 4
	EWidgetType_Main EWidgetType = 5
	EWidgetType_RoleStroySelect EWidgetType = 6
	EWidgetType_Mail EWidgetType = 7
	EWidgetType_Welfare EWidgetType = 8
	EWidgetType_Phone EWidgetType = 9
	EWidgetType_Dialog EWidgetType = 10
	EWidgetType_ChapterBegin EWidgetType = 11
	EWidgetType_Branch EWidgetType = 12
	EWidgetType_Game EWidgetType = 13
	EWidgetType_Media EWidgetType = 14
	EWidgetType_StoryGameManduola EWidgetType = 15
	EWidgetType_StoryGameBeatManduola EWidgetType = 16
	EWidgetType_StoryGameAdjustClock EWidgetType = 17
	EWidgetType_LookAround EWidgetType = 18
	EWidgetType_SelectFairy EWidgetType = 19
	EWidgetType_CreatePlayer EWidgetType = 20
	EWidgetType_FindFragments EWidgetType = 21
	EWidgetType_Fragments EWidgetType = 22
	EWidgetType_ChopVineman EWidgetType = 23
	EWidgetType_SmashGate EWidgetType = 24
	EWidgetType_SmashClock EWidgetType = 25
	EWidgetType_StoryGameDescription EWidgetType = 26
	EWidgetType_GameResult EWidgetType = 27
	EWidgetType_ItemSource EWidgetType = 28
	EWidgetType_RoleSelect EWidgetType = 29
	EWidgetType_ShopStore EWidgetType = 30
	EWidgetType_ShopAddPay EWidgetType = 31
	EWidgetType_ShopStorePay EWidgetType = 32
	EWidgetType_ShopStoreGiftPay EWidgetType = 33
	EWidgetType_ShopStoreConfirmPay EWidgetType = 34
	EWidgetType_RolePay EWidgetType = 35
	EWidgetType_GetRole EWidgetType = 36
	EWidgetType_GetItemPanel EWidgetType = 37
	EWidgetType_PhoneCost EWidgetType = 38
	EWidgetType_NetLoading EWidgetType = 39
	EWidgetType_NetError EWidgetType = 40
	EWidgetType_LoginError EWidgetType = 41
	EWidgetType_PopUpText EWidgetType = 42
	EWidgetType_PopUpInfo EWidgetType = 43
	EWidgetType_TouchBegan EWidgetType = 44
	EWidgetType_Transition EWidgetType = 45
	EWidgetType_LevelUpgrade EWidgetType = 46
	EWidgetType_BookCase EWidgetType = 47
	EWidgetType_GrowUpBook EWidgetType = 48
	EWidgetType_DollGrowUp EWidgetType = 49
	EWidgetType_AttributeUp EWidgetType = 50
)

type EUIParamsType int32
const (
	EUIParamsType_None EUIParamsType = 0
	EUIParamsType_ToShopStore EUIParamsType = 1
	EUIParamsType_ItemSource EUIParamsType = 2
	EUIParamsType_RoleSelect EUIParamsType = 3
	EUIParamsType_GetRole EUIParamsType = 4
	EUIParamsType_Fragments EUIParamsType = 5
	EUIParamsType_GameResult EUIParamsType = 6
	EUIParamsType_Spine EUIParamsType = 7
)
