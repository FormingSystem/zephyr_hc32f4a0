---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-1
title: zephyr__bluetooth__classic__avrcp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_classic\_\_avrcp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音视频远程控制配置文件（Audio Video Remote Control Profile）的头文件。

查看此文件的源码。

<a id="details"></a>

音视频远程控制配置文件（Audio Video Remote Control Profile）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Favrcp_5Funit_5Finfo_5Frsp"></a>

```c
struct bt_avrcp_unit_info_rsp
```

相关声明：[bt_avrcp_unit_info_rsp](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md)。

<a id="r_bt_5Favrcp_5Fsubunit_5Finfo_5Frsp"></a>

```c
struct bt_avrcp_subunit_info_rsp
```

相关声明：[bt_avrcp_subunit_info_rsp](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md)。

<a id="r_bt_5Favrcp_5Fpassthrough_5Fopvu_5Fdata"></a>

```c
struct bt_avrcp_passthrough_opvu_data
```

相关声明：[bt_avrcp_passthrough_opvu_data](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md)。

<a id="r_bt_5Favrcp_5Fpassthrough_5Fcmd"></a>

```c
struct bt_avrcp_passthrough_cmd
```

相关声明：[bt_avrcp_passthrough_cmd](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md)。

<a id="r_bt_5Favrcp_5Fpassthrough_5Frsp"></a>

```c
struct bt_avrcp_passthrough_rsp
```

相关声明：[bt_avrcp_passthrough_rsp](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md)。

<a id="r_bt_5Favrcp_5Fget_5Fcaps_5Frsp"></a>

```c
struct bt_avrcp_get_caps_rsp
```

相关声明：[bt_avrcp_get_caps_rsp](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md)。

<a id="r_bt_5Favrcp_5Fget_5Ffolder_5Fitems_5Fcmd"></a>

```c
struct bt_avrcp_get_folder_items_cmd
```

相关声明：[bt_avrcp_get_folder_items_cmd](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md)。

获取文件夹条目（GetFolderItems）命令请求。

<a id="r_bt_5Favrcp_5Fitem_5Fhdr"></a>

```c
struct bt_avrcp_item_hdr
```

相关声明：[bt_avrcp_item_hdr](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md)。

获取文件夹条目（GetFolderItems）响应使用的通用条目头（Common Item Header）。

<a id="r_bt_5Favrcp_5Fmedia_5Fplayer_5Fitem"></a>

```c
struct bt_avrcp_media_player_item
```

相关声明：[bt_avrcp_media_player_item](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md)。

媒体播放器条目（Media Player Item），`item_type=0x01`。

<a id="r_bt_5Favrcp_5Ffolder_5Fitem"></a>

```c
struct bt_avrcp_folder_item
```

相关声明：[bt_avrcp_folder_item](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md)。

文件夹条目（Folder Item），`item_type=0x02`。

<a id="r_bt_5Favrcp_5Fmedia_5Fattr"></a>

```c
struct bt_avrcp_media_attr
```

相关声明：[bt_avrcp_media_attr](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md)。

AVRCP 媒体属性（Media Attribute）结构体。

<a id="r_media_5Felement_5Fitem_5Fname"></a>

```c
struct media_element_item_name
```

相关声明：[media_element_item_name](../device_power_control_model_reference/P028_media_element_item_name_结构体.md)。

媒体元素项名称（Media Element Item Name）的结构。

<a id="r_media_5Felement_5Fitem_5Fattr"></a>

```c
struct media_element_item_attr
```

相关声明：[media_element_item_attr](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md)。

媒体元素项属性（Media Element Item Attributes）的结构。

<a id="r_bt_5Favrcp_5Fmedia_5Felement_5Fitem"></a>

```c
struct bt_avrcp_media_element_item
```

相关声明：[bt_avrcp_media_element_item](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md)。

媒体元素条目（Media Element Item），`item_type = 0x03`。

<a id="r_bt_5Favrcp_5Fget_5Ffolder_5Fitems_5Frsp"></a>

```c
struct bt_avrcp_get_folder_items_rsp
```

相关声明：[bt_avrcp_get_folder_items_rsp](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md)。

获取文件夹条目（GetFolderItems）响应。

<a id="r_bt_5Favrcp_5Fchange_5Fpath_5Fcmd"></a>

```c
struct bt_avrcp_change_path_cmd
```

相关声明：[bt_avrcp_change_path_cmd](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md)。

更改路径（ChangePath）命令请求。

<a id="r_bt_5Favrcp_5Fchange_5Fpath_5Frsp"></a>

```c
struct bt_avrcp_change_path_rsp
```

相关声明：[bt_avrcp_change_path_rsp](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md)。

更改路径（ChangePath）响应。

<a id="r_bt_5Favrcp_5Fget_5Fitem_5Fattrs_5Fcmd"></a>

```c
struct bt_avrcp_get_item_attrs_cmd
```

相关声明：[bt_avrcp_get_item_attrs_cmd](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md)。

获取条目属性（GetItemAttributes）命令请求。

<a id="r_bt_5Favrcp_5Fget_5Fitem_5Fattrs_5Frsp"></a>

```c
struct bt_avrcp_get_item_attrs_rsp
```

相关声明：[bt_avrcp_get_item_attrs_rsp](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md)。

获取条目属性（GetItemAttributes）响应。

<a id="r_bt_5Favrcp_5Fplay_5Fitem_5Frsp"></a>

```c
struct bt_avrcp_play_item_rsp
```

相关声明：[bt_avrcp_play_item_rsp](../bluetooth_classic_model_reference/P060_bt_avrcp_play_item_rsp_结构体.md)。

播放条目（PlayItem）响应。

<a id="r_bt_5Favrcp_5Fget_5Ftotal_5Fnumber_5Fof_5Fitems_5Fcmd"></a>

```c
struct bt_avrcp_get_total_number_of_items_cmd
```

相关声明：[bt_avrcp_get_total_number_of_items_cmd](../bluetooth_classic_model_reference/P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md)。

获取条目总数（GetTotalNumberOfItems）命令请求。

<a id="r_bt_5Favrcp_5Fget_5Ftotal_5Fnumber_5Fof_5Fitems_5Frsp"></a>

```c
struct bt_avrcp_get_total_number_of_items_rsp
```

相关声明：[bt_avrcp_get_total_number_of_items_rsp](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md)。

获取条目总数（GetTotalNumberOfItems）响应。

<a id="r_bt_5Favrcp_5Fsearch_5Fcmd"></a>

```c
struct bt_avrcp_search_cmd
```

相关声明：[bt_avrcp_search_cmd](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md)。

搜索（Search）命令请求。

<a id="r_bt_5Favrcp_5Fsearch_5Frsp"></a>

```c
struct bt_avrcp_search_rsp
```

相关声明：[bt_avrcp_search_rsp](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md)。

搜索（Search）响应。

<a id="r_bt_5Favrcp_5Ffolder_5Fname"></a>

```c
struct bt_avrcp_folder_name
```

相关声明：[bt_avrcp_folder_name](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md)。

获取文件夹名称的响应（Get Folder Name Response）。

<a id="r_bt_5Favrcp_5Fset_5Fbrowsed_5Fplayer_5Frsp"></a>

```c
struct bt_avrcp_set_browsed_player_rsp
```

相关声明：[bt_avrcp_set_browsed_player_rsp](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md)。

设置浏览播放器（Set Browsed Player）响应结构体。

<a id="r_bt_5Favrcp_5Fget_5Felement_5Fattrs_5Fcmd"></a>

```c
struct bt_avrcp_get_element_attrs_cmd
```

相关声明：[bt_avrcp_get_element_attrs_cmd](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md)。

获取元素属性（GetElementAttributes）命令请求结构体。

<a id="r_bt_5Favrcp_5Fget_5Felement_5Fattrs_5Frsp"></a>

```c
struct bt_avrcp_get_element_attrs_rsp
```

相关声明：[bt_avrcp_get_element_attrs_rsp](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md)。

获取元素属性（GetElementAttributes）响应结构体。

<a id="r_bt_5Favrcp_5Flist_5Fplayer_5Fapp_5Fsetting_5Fattrs_5Frsp"></a>

```c
struct bt_avrcp_list_player_app_setting_attrs_rsp
```

相关声明：[bt_avrcp_list_player_app_setting_attrs_rsp](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md)。

列出播放器应用设置属性（ListPlayerApplicationSettingAttributes）响应。

<a id="r_bt_5Favrcp_5Flist_5Fplayer_5Fapp_5Fsetting_5Fvals_5Fcmd"></a>

```c
struct bt_avrcp_list_player_app_setting_vals_cmd
```

相关声明：[bt_avrcp_list_player_app_setting_vals_cmd](../bluetooth_classic_model_reference/P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md)。

列出播放器应用设置值（ListPlayerApplicationSettingValues）命令请求。

<a id="r_bt_5Favrcp_5Flist_5Fplayer_5Fapp_5Fsetting_5Fvals_5Frsp"></a>

```c
struct bt_avrcp_list_player_app_setting_vals_rsp
```

相关声明：[bt_avrcp_list_player_app_setting_vals_rsp](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md)。

列出播放器应用设置值（ListPlayerApplicationSettingValues）响应。

<a id="r_bt_5Favrcp_5Fget_5Fcurr_5Fplayer_5Fapp_5Fsetting_5Fval_5Fcmd"></a>

```c
struct bt_avrcp_get_curr_player_app_setting_val_cmd
```

相关声明：[bt_avrcp_get_curr_player_app_setting_val_cmd](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md)。

获取当前播放器应用设置值（GetCurrentPlayerApplicationSettingValue）命令请求。

<a id="r_bt_5Favrcp_5Fapp_5Fsetting_5Fattr_5Fval"></a>

```c
struct bt_avrcp_app_setting_attr_val
```

相关声明：[bt_avrcp_app_setting_attr_val](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md)。

AVRCP 属性值对（Attribute-Value Pair）。

<a id="r_bt_5Favrcp_5Fget_5Fcurr_5Fplayer_5Fapp_5Fsetting_5Fval_5Frsp"></a>

```c
struct bt_avrcp_get_curr_player_app_setting_val_rsp
```

相关声明：[bt_avrcp_get_curr_player_app_setting_val_rsp](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md)。

获取当前播放器应用设置值（GetCurrentPlayerApplicationSettingValue）响应。

<a id="r_bt_5Favrcp_5Fset_5Fplayer_5Fapp_5Fsetting_5Fval_5Fcmd"></a>

```c
struct bt_avrcp_set_player_app_setting_val_cmd
```

相关声明：[bt_avrcp_set_player_app_setting_val_cmd](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md)。

设置播放器应用设置值（SetPlayerApplicationSettingValue）命令请求。

<a id="r_bt_5Favrcp_5Fget_5Fplayer_5Fapp_5Fsetting_5Fattr_5Ftext_5Fcmd"></a>

```c
struct bt_avrcp_get_player_app_setting_attr_text_cmd
```

相关声明：[bt_avrcp_get_player_app_setting_attr_text_cmd](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md)。

获取播放器应用设置属性文本（GetPlayerApplicationSettingAttributeText）命令请求。

<a id="r_bt_5Favrcp_5Fapp_5Fsetting_5Fattr_5Ftext"></a>

```c
struct bt_avrcp_app_setting_attr_text
```

相关声明：[bt_avrcp_app_setting_attr_text](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md)。

音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）的属性文本条目（Attribute Text Entry）。

<a id="r_bt_5Favrcp_5Fget_5Fplayer_5Fapp_5Fsetting_5Fattr_5Ftext_5Frsp"></a>

```c
struct bt_avrcp_get_player_app_setting_attr_text_rsp
```

相关声明：[bt_avrcp_get_player_app_setting_attr_text_rsp](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md)。

获取播放器应用设置属性文本（GetPlayerApplicationSettingAttributeText）响应。

<a id="r_bt_5Favrcp_5Fget_5Fplayer_5Fapp_5Fsetting_5Fval_5Ftext_5Fcmd"></a>

```c
struct bt_avrcp_get_player_app_setting_val_text_cmd
```

相关声明：[bt_avrcp_get_player_app_setting_val_text_cmd](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md)。

获取播放器应用设置值文本（GetPlayerApplicationSettingValueText）命令请求。

<a id="r_bt_5Favrcp_5Fapp_5Fsetting_5Fval_5Ftext"></a>

```c
struct bt_avrcp_app_setting_val_text
```

相关声明：[bt_avrcp_app_setting_val_text](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md)。

音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）的属性文本条目（Attribute Text Entry）。

<a id="r_bt_5Favrcp_5Fget_5Fplayer_5Fapp_5Fsetting_5Fval_5Ftext_5Frsp"></a>

```c
struct bt_avrcp_get_player_app_setting_val_text_rsp
```

相关声明：[bt_avrcp_get_player_app_setting_val_text_rsp](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md)。

获取播放器应用设置值文本（GetPlayerApplicationSettingValueText）响应。

<a id="r_bt_5Favrcp_5Finform_5Fdisplayable_5Fchar_5Fset_5Fcmd"></a>

```c
struct bt_avrcp_inform_displayable_char_set_cmd
```

相关声明：[bt_avrcp_inform_displayable_char_set_cmd](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md)。

通知可显示字符集（InformDisplayableCharacterSet）命令请求。

<a id="r_bt_5Favrcp_5Finform_5Fbatt_5Fstatus_5Fof_5Fct_5Fcmd"></a>

```c
struct bt_avrcp_inform_batt_status_of_ct_cmd
```

相关声明：[bt_avrcp_inform_batt_status_of_ct_cmd](../bluetooth_classic_model_reference/P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md)。

通知控制端电池状态（InformBatteryStatusOfCT）命令请求。

<a id="r_bt_5Favrcp_5Fget_5Fplay_5Fstatus_5Frsp"></a>

```c
struct bt_avrcp_get_play_status_rsp
```

相关声明：[bt_avrcp_get_play_status_rsp](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md)。

获取播放状态（GetPlayStatus）响应。

<a id="r_bt_5Favrcp_5Fregister_5Fnotification_5Fcmd"></a>

```c
struct bt_avrcp_register_notification_cmd
```

相关声明：[bt_avrcp_register_notification_cmd](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md)。

注册通知（RegisterNotification）命令请求。

<a id="r_bt_5Favrcp_5Fset_5Fabsolute_5Fvolume_5Fcmd"></a>

```c
struct bt_avrcp_set_absolute_volume_cmd
```

相关声明：[bt_avrcp_set_absolute_volume_cmd](../bluetooth_classic_model_reference/P064_bt_avrcp_set_absolute_volume_cmd_结构体.md)。

设置绝对音量（SetAbsoluteVolume）命令请求。

<a id="r_bt_5Favrcp_5Fset_5Fabsolute_5Fvolume_5Frsp"></a>

```c
struct bt_avrcp_set_absolute_volume_rsp
```

相关声明：[bt_avrcp_set_absolute_volume_rsp](../bluetooth_classic_model_reference/P065_bt_avrcp_set_absolute_volume_rsp_结构体.md)。

设置绝对音量（SetAbsoluteVolume）响应。

<a id="r_bt_5Favrcp_5Fset_5Faddressed_5Fplayer_5Fcmd"></a>

```c
struct bt_avrcp_set_addressed_player_cmd
```

相关声明：[bt_avrcp_set_addressed_player_cmd](../bluetooth_classic_model_reference/P066_bt_avrcp_set_addressed_player_cmd_结构体.md)。

设置受控播放器（SetAddressedPlayer）命令请求。

<a id="r_bt_5Favrcp_5Fplay_5Fitem_5Fcmd"></a>

```c
struct bt_avrcp_play_item_cmd
```

相关声明：[bt_avrcp_play_item_cmd](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md)。

播放条目（PlayItem）命令请求。

<a id="r_bt_5Favrcp_5Fadd_5Fto_5Fnow_5Fplaying_5Fcmd"></a>

```c
struct bt_avrcp_add_to_now_playing_cmd
```

相关声明：[bt_avrcp_add_to_now_playing_cmd](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md)。

添加到当前播放列表（AddToNowPlaying）命令请求。

<a id="r_bt_5Favrcp_5Fevent_5Fdata"></a>

```c
struct bt_avrcp_event_data
```

相关声明：[bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)。

<a id="r_bt_5Favrcp_5Fct_5Fcb"></a>

```c
struct bt_avrcp_ct_cb
```

相关声明：[bt_avrcp_ct_cb](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md)。

<a id="r_bt_5Favrcp_5Ftg_5Fcb"></a>

```c
struct bt_avrcp_tg_cb
```

相关声明：[bt_avrcp_tg_cb](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gae4e7573280179717124104858629122a"></a>

```c
#define BT_AVRCP_COMPANY_ID_SIZE (3)
```

相关声明：[BT_AVRCP_COMPANY_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae4e7573280179717124104858629122a)。

<a id="r_gae7a97b11a8954a2a25cc401ced566fd2"></a>

```c
#define BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG (0x001958)
```

相关声明：[BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae7a97b11a8954a2a25cc401ced566fd2)。

<a id="r_ga7eee1ffa11a5152a0dd014ac15979605"></a>

```c
#define BT_AVRCP_PASSTHROUGH_GET_STATE(payload)
```

相关声明：[BT_AVRCP_PASSTHROUGH_GET_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7eee1ffa11a5152a0dd014ac15979605)。

<a id="r_ga8c8e1596f92e32781690c0a76196c4c8"></a>

```c
#define BT_AVRCP_PASSTHROUGH_GET_OPID(payload)
```

相关声明：[BT_AVRCP_PASSTHROUGH_GET_OPID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8c8e1596f92e32781690c0a76196c4c8)。

<a id="r_ga4f8014317db642c98d3db9be6db7adea"></a>

```c
#define BT_AVRCP_PASSTHROUGH_SET_STATE_OPID(payload, state, opid)
```

相关声明：[BT_AVRCP_PASSTHROUGH_SET_STATE_OPID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4f8014317db642c98d3db9be6db7adea)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

<a id="r_ga5ecfdd180bc51dc0867e859d1b3a7fbe"></a>

```c
#define BT_AVRCP_MAX_ABSOLUTE_VOLUME 0x7F
```

相关声明：[BT_AVRCP_MAX_ABSOLUTE_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga5ecfdd180bc51dc0867e859d1b3a7fbe)。

音视频遥控配置文件（Audio/Video Remote Control Profile，AVRCP）的最大绝对音量（Maximum Absolute Volume）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_gab9bd888ef5443bd0a3d34a34b972f409"></a>

```c
typedef void(* bt_avrcp_notify_changed_cb_t) (struct bt_avrcp_ct *ct, uint8_t event_id, struct bt_avrcp_event_data *data)
```

相关声明：[bt_avrcp_notify_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab9bd888ef5443bd0a3d34a34b972f409)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)。

AVRCP 事件通知回调（Event Notification Callback），仅用于 CHANGED 通知。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_gac311dc7b5f99162b954271529eeb84ea"></a>

```c
enum bt_avrcp_cap_t { BT_AVRCP_CAP_COMPANY_ID = 0x2 , BT_AVRCP_CAP_EVENTS_SUPPORTED = 0x3 }
```

相关声明：[bt_avrcp_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac311dc7b5f99162b954271529eeb84ea)、[BT_AVRCP_CAP_COMPANY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac311dc7b5f99162b954271529eeb84eaa89fecce56afb09791a2253a7ad840430)、[BT_AVRCP_CAP_EVENTS_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac311dc7b5f99162b954271529eeb84eaa2a7b326aded772c09cf01387145d2802)。

AVRCP 能力标识符（Capability ID）。

<a id="r_gaf55aae17f67a1361279ae208b17e4a75"></a>

```c
enum bt_avrcp_evt_t { BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED = 0x01 , BT_AVRCP_EVT_TRACK_CHANGED = 0x02 , BT_AVRCP_EVT_TRACK_REACHED_END = 0x03 , BT_AVRCP_EVT_TRACK_REACHED_START = 0x04 , BT_AVRCP_EVT_PLAYBACK_POS_CHANGED = 0x05 , BT_AVRCP_EVT_BATT_STATUS_CHANGED = 0x06 , BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED = 0x07 , BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED = 0x08 , BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED = 0x09 , BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED = 0x0a , BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED = 0x0b , BT_AVRCP_EVT_UIDS_CHANGED = 0x0c , BT_AVRCP_EVT_VOLUME_CHANGED = 0x0d }
```

相关声明：[bt_avrcp_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf55aae17f67a1361279ae208b17e4a75)、[BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a892f2928d634b675426f2fe597a45f6d)、[BT_AVRCP_EVT_TRACK_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a25f8e3e08b5988e833eb0d47452d12a9)、[BT_AVRCP_EVT_TRACK_REACHED_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a412a9b7cbb891bc50fb77c1e6de9faaf)、[BT_AVRCP_EVT_TRACK_REACHED_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75af4f9e221522cd57461920d22e7a290b9)、[BT_AVRCP_EVT_PLAYBACK_POS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75afc4ef6f8a80a9067ad9dfd30bf2a6958)、[BT_AVRCP_EVT_BATT_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a9ff1d99bc0c83399961ef23d4a75f9b6)、[BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ae6237555b0051b2395e0bf2287e954c1)、[BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ab2b2287a0db9be97af8c20298bebba2d)、[BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ac0b720defdd8716d757e0c8a7e57db83)、[BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75abd82dd6ba6d5d76cf22a8c703c76c6e0)、[BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ab6fdeacb536067660f754b3c586e073a)、[BT_AVRCP_EVT_UIDS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a8ac593400cda085fbdff36e403bd2a91)、[BT_AVRCP_EVT_VOLUME_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a8d526498fdcb1380e8e3944da2a5ef85)。

AVRCP 通知事件（Notification Events）。

<a id="r_ga2a4c610e00ba9832f954f30bd6b6618e"></a>

```c
enum bt_avrcp_ctype_t { BT_AVRCP_CTYPE_CONTROL = 0x0 , BT_AVRCP_CTYPE_STATUS = 0x1 , BT_AVRCP_CTYPE_SPECIFIC_INQUIRY = 0x2 , BT_AVRCP_CTYPE_NOTIFY = 0x3 , BT_AVRCP_CTYPE_GENERAL_INQUIRY = 0x4 }
```

相关声明：[bt_avrcp_ctype_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga2a4c610e00ba9832f954f30bd6b6618e)、[BT_AVRCP_CTYPE_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04)、[BT_AVRCP_CTYPE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce)、[BT_AVRCP_CTYPE_SPECIFIC_INQUIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb)、[BT_AVRCP_CTYPE_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290)、[BT_AVRCP_CTYPE_GENERAL_INQUIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7)。

音视频控制（AV/C）命令类型（Command Types）。

<a id="r_gaba2d8faec2c3baf7403199ea8a509326"></a>

```c
enum bt_avrcp_rsp_t { BT_AVRCP_RSP_NOT_IMPLEMENTED = 0x8 , BT_AVRCP_RSP_ACCEPTED = 0x9 , BT_AVRCP_RSP_REJECTED = 0xa , BT_AVRCP_RSP_IN_TRANSITION = 0xb , BT_AVRCP_RSP_IMPLEMENTED = 0xc , BT_AVRCP_RSP_STABLE = 0xc , BT_AVRCP_RSP_CHANGED = 0xd , BT_AVRCP_RSP_INTERIM = 0xf }
```

相关声明：[bt_avrcp_rsp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaba2d8faec2c3baf7403199ea8a509326)、[BT_AVRCP_RSP_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696)、[BT_AVRCP_RSP_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8)、[BT_AVRCP_RSP_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c)、[BT_AVRCP_RSP_IN_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad)、[BT_AVRCP_RSP_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144)、[BT_AVRCP_RSP_STABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992)、[BT_AVRCP_RSP_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988)、[BT_AVRCP_RSP_INTERIM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88)。

音视频控制（AV/C）响应码（Response Codes）。

<a id="r_ga78ba828636b731b2c43e088a581bfee9"></a>

```c
enum bt_avrcp_subunit_type_t { BT_AVRCP_SUBUNIT_TYPE_PANEL = 0x09 , BT_AVRCP_SUBUNIT_TYPE_UNIT = 0x1f }
```

相关声明：[bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)、[BT_AVRCP_SUBUNIT_TYPE_PANEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga78ba828636b731b2c43e088a581bfee9a6db3104fa9727594b842b4ae9b64a605)、[BT_AVRCP_SUBUNIT_TYPE_UNIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga78ba828636b731b2c43e088a581bfee9a8be8c211cd26a849c1c89e482aa10030)。

音视频控制（AV/C）子单元类型（Subunit Type），也用于单元类型（Unit Type）。

<a id="r_ga3c997d96028343a0a5a4948dabe19b84"></a>

```c
enum bt_avrcp_opid_t { BT_AVRCP_OPID_SELECT = 0x00 , BT_AVRCP_OPID_UP = 0x01 , BT_AVRCP_OPID_DOWN = 0x02 , BT_AVRCP_OPID_LEFT = 0x03 , BT_AVRCP_OPID_RIGHT = 0x04 , BT_AVRCP_OPID_RIGHT_UP = 0x05 , BT_AVRCP_OPID_RIGHT_DOWN = 0x06 , BT_AVRCP_OPID_LEFT_UP = 0x07 , BT_AVRCP_OPID_LEFT_DOWN = 0x08 , BT_AVRCP_OPID_ROOT_MENU = 0x09 , BT_AVRCP_OPID_SETUP_MENU = 0x0a , BT_AVRCP_OPID_CONTENTS_MENU = 0x0b , BT_AVRCP_OPID_FAVORITE_MENU = 0x0c , BT_AVRCP_OPID_EXIT = 0x0d , BT_AVRCP_OPID_0 = 0x20 , BT_AVRCP_OPID_1 = 0x21 , BT_AVRCP_OPID_2 = 0x22 , BT_AVRCP_OPID_3 = 0x23 , BT_AVRCP_OPID_4 = 0x24 , BT_AVRCP_OPID_5 = 0x25 , BT_AVRCP_OPID_6 = 0x26 , BT_AVRCP_OPID_7 = 0x27 , BT_AVRCP_OPID_8 = 0x28 , BT_AVRCP_OPID_9 = 0x29 , BT_AVRCP_OPID_DOT = 0x2a , BT_AVRCP_OPID_ENTER = 0x2b , BT_AVRCP_OPID_CLEAR = 0x2c , BT_AVRCP_OPID_CHANNEL_UP = 0x30 , BT_AVRCP_OPID_CHANNEL_DOWN = 0x31 , BT_AVRCP_OPID_PREVIOUS_CHANNEL = 0x32 , BT_AVRCP_OPID_SOUND_SELECT = 0x33 , BT_AVRCP_OPID_INPUT_SELECT = 0x34 , BT_AVRCP_OPID_DISPLAY_INFORMATION = 0x35 , BT_AVRCP_OPID_HELP = 0x36 , BT_AVRCP_OPID_PAGE_UP = 0x37 , BT_AVRCP_OPID_PAGE_DOWN = 0x38 , BT_AVRCP_OPID_POWER = 0x40 , BT_AVRCP_OPID_VOLUME_UP = 0x41 , BT_AVRCP_OPID_VOLUME_DOWN = 0x42 , BT_AVRCP_OPID_MUTE = 0x43 , BT_AVRCP_OPID_PLAY = 0x44 , BT_AVRCP_OPID_STOP = 0x45 , BT_AVRCP_OPID_PAUSE = 0x46 , BT_AVRCP_OPID_RECORD = 0x47 , BT_AVRCP_OPID_REWIND = 0x48 , BT_AVRCP_OPID_FAST_FORWARD = 0x49 , BT_AVRCP_OPID_EJECT = 0x4a , BT_AVRCP_OPID_FORWARD = 0x4b , BT_AVRCP_OPID_BACKWARD = 0x4c , BT_AVRCP_OPID_ANGLE = 0x50 , BT_AVRCP_OPID_SUBPICTURE = 0x51 , BT_AVRCP_OPID_F1 = 0x71 , BT_AVRCP_OPID_F2 = 0x72 , BT_AVRCP_OPID_F3 = 0x73 , BT_AVRCP_OPID_F4 = 0x74 , BT_AVRCP_OPID_F5 = 0x75 , BT_AVRCP_OPID_VENDOR_UNIQUE = 0x7e }
```

相关声明：[bt_avrcp_opid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga3c997d96028343a0a5a4948dabe19b84)、[BT_AVRCP_OPID_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f)、[BT_AVRCP_OPID_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9)、[BT_AVRCP_OPID_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537)、[BT_AVRCP_OPID_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba)、[BT_AVRCP_OPID_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2)、[BT_AVRCP_OPID_RIGHT_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63)、[BT_AVRCP_OPID_RIGHT_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745)、[BT_AVRCP_OPID_LEFT_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779)、[BT_AVRCP_OPID_LEFT_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366)、[BT_AVRCP_OPID_ROOT_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87)、[BT_AVRCP_OPID_SETUP_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372)、[BT_AVRCP_OPID_CONTENTS_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472)、[BT_AVRCP_OPID_FAVORITE_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574)、[BT_AVRCP_OPID_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3)、[BT_AVRCP_OPID_0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade)、[BT_AVRCP_OPID_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0)、[BT_AVRCP_OPID_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566)、[BT_AVRCP_OPID_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459)、[BT_AVRCP_OPID_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c)、[BT_AVRCP_OPID_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5)、[BT_AVRCP_OPID_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a)、[BT_AVRCP_OPID_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff)、[BT_AVRCP_OPID_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06)、[BT_AVRCP_OPID_9](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb)、[BT_AVRCP_OPID_DOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf)、[BT_AVRCP_OPID_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae)、[BT_AVRCP_OPID_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2)、[BT_AVRCP_OPID_CHANNEL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586)、[BT_AVRCP_OPID_CHANNEL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de)、[BT_AVRCP_OPID_PREVIOUS_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e)、[BT_AVRCP_OPID_SOUND_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b)、[BT_AVRCP_OPID_INPUT_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c)、[BT_AVRCP_OPID_DISPLAY_INFORMATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef)、[BT_AVRCP_OPID_HELP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b)、[BT_AVRCP_OPID_PAGE_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321)、[BT_AVRCP_OPID_PAGE_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a)、[BT_AVRCP_OPID_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358)、[BT_AVRCP_OPID_VOLUME_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487)、[BT_AVRCP_OPID_VOLUME_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62)、[BT_AVRCP_OPID_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1)、[BT_AVRCP_OPID_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b)、[BT_AVRCP_OPID_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60)、[BT_AVRCP_OPID_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a)、[BT_AVRCP_OPID_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27)、[BT_AVRCP_OPID_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8)、[BT_AVRCP_OPID_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f)、[BT_AVRCP_OPID_EJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344)、[BT_AVRCP_OPID_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e)、[BT_AVRCP_OPID_BACKWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23)、[BT_AVRCP_OPID_ANGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2)、[BT_AVRCP_OPID_SUBPICTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98)、[BT_AVRCP_OPID_F1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5)、[BT_AVRCP_OPID_F2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4)、[BT_AVRCP_OPID_F3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40)、[BT_AVRCP_OPID_F4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283)、[BT_AVRCP_OPID_F5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d)、[BT_AVRCP_OPID_VENDOR_UNIQUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d)。

AVRCP 透传命令（Passthrough Commands）使用的 AV/C 操作标识符（Operation IDs）。

<a id="r_ga15f9f868b056f17ea12d96530b7da881"></a>

```c
enum bt_avrcp_button_state_t { BT_AVRCP_BUTTON_PRESSED = 0 , BT_AVRCP_BUTTON_RELEASED = 1 }
```

相关声明：[bt_avrcp_button_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga15f9f868b056f17ea12d96530b7da881)、[BT_AVRCP_BUTTON_PRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3)、[BT_AVRCP_BUTTON_RELEASED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706)。

AVRCP 按钮状态标志（Button State Flag）。

<a id="r_ga52368f4cc655bab75f96da80ddaaabe0"></a>

```c
enum bt_avrcp_status_t { BT_AVRCP_STATUS_INVALID_COMMAND = 0x00 , BT_AVRCP_STATUS_INVALID_PARAMETER = 0x01 , BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR = 0x02 , BT_AVRCP_STATUS_INTERNAL_ERROR = 0x03 , BT_AVRCP_STATUS_OPERATION_COMPLETED = 0x04 , BT_AVRCP_STATUS_UID_CHANGED = 0x05 , BT_AVRCP_STATUS_INVALID_DIRECTION = 0x07 , BT_AVRCP_STATUS_NOT_A_DIRECTORY = 0x08 , BT_AVRCP_STATUS_DOES_NOT_EXIST = 0x09 , BT_AVRCP_STATUS_INVALID_SCOPE = 0x0a , BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS = 0x0b , BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE = 0x0c , BT_AVRCP_STATUS_MEDIA_IN_USE = 0x0d , BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL = 0x0e , BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED = 0x0f , BT_AVRCP_STATUS_SEARCH_IN_PROGRESS = 0x10 , BT_AVRCP_STATUS_INVALID_PLAYER_ID = 0x11 , BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE = 0x12 , BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED = 0x13 , BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS = 0x14 , BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS = 0x15 , BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED = 0x16 , BT_AVRCP_STATUS_IN_TRANSITION = 0xfd , BT_AVRCP_STATUS_NOT_IMPLEMENTED = 0xfe , BT_AVRCP_STATUS_SUCCESS = BT_AVRCP_STATUS_OPERATION_COMPLETED }
```

相关声明：[bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)、[BT_AVRCP_STATUS_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a14e183c33a64cdac271ee7f320796bd6)、[BT_AVRCP_STATUS_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a8a767466ac8069e20f6d9e0f30c33420)、[BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a7cba04973b3753b50f63e6b0bc205638)、[BT_AVRCP_STATUS_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0af48dcc2c65e4af461c1a6ece622a2f5a)、[BT_AVRCP_STATUS_OPERATION_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0ad3a41ce04f27cc349c7466aae18bcee2)、[BT_AVRCP_STATUS_UID_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a0e77e1782b5a0f88f4d45b6560df2b09)、[BT_AVRCP_STATUS_INVALID_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a448e1c0383e4e4b5fc3c0c80e2040af9)、[BT_AVRCP_STATUS_NOT_A_DIRECTORY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a6fee8c927f897fff59b7690c3e1732c2)、[BT_AVRCP_STATUS_DOES_NOT_EXIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a9f552377c6bb93b3e52b29228a6feaa5)、[BT_AVRCP_STATUS_INVALID_SCOPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0aaddaf4f6439aa6a52e3a4fdbb3f0c071)、[BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a81094560261826c16be6ebba9d99081c)、[BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a2f8ca7c1fe4ba52a1a418612c094158a)、[BT_AVRCP_STATUS_MEDIA_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0ae63cf3ffada01f268498151d88c3a3ec)、[BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a359810fbbdf875adb89a192deaae6a6d)、[BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a4ee781cc845d8b1211217f8338b97023)、[BT_AVRCP_STATUS_SEARCH_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a402038758703ee9f8543ad546681a3c5)、[BT_AVRCP_STATUS_INVALID_PLAYER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a5cd415ba8d307dc5153a9a0b2f9958e3)、[BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a28925d094d4c3e55b259a55440a5c044)、[BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a3dfa01e069c517e7e466fa6edcc1c9cb)、[BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a033e10d03bf56df95ec1e888a07cedf9)、[BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a5544c22cad94dadb9eccf47669fabafb)、[BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a43e59407a44f87d85fa71cdb627524e3)、[BT_AVRCP_STATUS_IN_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0af72a55b60fda9c157cdef8b1c6038780)、[BT_AVRCP_STATUS_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a14868dd213f59e09dbdb066d5ca39c96)、[BT_AVRCP_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0afbff25149bb9c35756dfb7bb6f2516c3)。

AVRCP 状态码与错误码（Status and Error Codes）。

<a id="r_ga81330413af9eba049da6557b14ae082c"></a>

```c
enum bt_avrcp_charset_t { BT_AVRCP_CHARSET_UTF8 = 0x006a }
```

相关声明：[bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)、[BT_AVRCP_CHARSET_UTF8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga81330413af9eba049da6557b14ae082ca29f70165632222ae40ac3e44554130b0)。

AVRCP 字符集标识符（Character Set IDs）。

<a id="r_gaabab9a4f37b3f9653ca95dd4b5944707"></a>

```c
enum bt_avrcp_scope_t { BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST = 0x00 , BT_AVRCP_SCOPE_VFS = 0x01 , BT_AVRCP_SCOPE_SEARCH = 0x02 , BT_AVRCP_SCOPE_NOW_PLAYING = 0x03 }
```

相关声明：[bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)、[BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a7a388bb84fbe14f8931ab9bf41b9823d)、[BT_AVRCP_SCOPE_VFS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a37002574948081d7b42001a62755636b)、[BT_AVRCP_SCOPE_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a4db7699a5f22c8d5986f6f1ba7219dac)、[BT_AVRCP_SCOPE_NOW_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a7baa6442aafc4d00635df52f44d0d608)。

AVRCP 范围值（Scope Values）。

<a id="r_ga02d67e84b4a48ebecf3b307cbd4bb61c"></a>

```c
enum bt_avrcp_change_path_t { BT_AVRCP_CHANGE_PATH_PARENT = 0x00 , BT_AVRCP_CHANGE_PATH_CHILD = 0x01 }
```

相关声明：[bt_avrcp_change_path_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga02d67e84b4a48ebecf3b307cbd4bb61c)、[BT_AVRCP_CHANGE_PATH_PARENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga02d67e84b4a48ebecf3b307cbd4bb61ca8914559b14b7529fc5f1df764036748d)、[BT_AVRCP_CHANGE_PATH_CHILD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga02d67e84b4a48ebecf3b307cbd4bb61ca5cbd84478163171359044825050dd172)。

AVRCP 更改路径方向（ChangePath Direction）。

<a id="r_ga09d191c490efcfb9f8139975090be0d5"></a>

```c
enum bt_avrcp_folder_type_t { BT_AVRCP_FOLDER_TYPE_MIXED = 0x00 , BT_AVRCP_FOLDER_TYPE_TITLES = 0x01 , BT_AVRCP_FOLDER_TYPE_ALBUMS = 0x02 , BT_AVRCP_FOLDER_TYPE_ARTISTS = 0x03 , BT_AVRCP_FOLDER_TYPE_GENRES = 0x04 , BT_AVRCP_FOLDER_TYPE_PLAYLISTS = 0x05 , BT_AVRCP_FOLDER_TYPE_YEARS = 0x06 }
```

相关声明：[bt_avrcp_folder_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga09d191c490efcfb9f8139975090be0d5)、[BT_AVRCP_FOLDER_TYPE_MIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a06308eb3786579cf5aeb0f19f0ab37ac)、[BT_AVRCP_FOLDER_TYPE_TITLES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a702f9974cf5d51a77757fd7e1ef4ab0f)、[BT_AVRCP_FOLDER_TYPE_ALBUMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5ab33fca5f57f5b80785df367ab788a8fc)、[BT_AVRCP_FOLDER_TYPE_ARTISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a89aaeb11e807c44479ff47164d99c4f7)、[BT_AVRCP_FOLDER_TYPE_GENRES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a0ab0ffb986db900ece2146a347dae06d)、[BT_AVRCP_FOLDER_TYPE_PLAYLISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a708dfb5de11ae783b413d2d99202f9b5)、[BT_AVRCP_FOLDER_TYPE_YEARS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a0a60cb99cd19d203618b1264e2a3cca6)。

AVRCP 文件夹类型（Folder Types），用于文件夹条目。

<a id="r_gac927c7e7c59f6f0e6243ca0887945d5a"></a>

```c
enum bt_avrcp_media_type_t { BT_AVRCP_MEDIA_TYPE_AUDIO = 0x00 , BT_AVRCP_MEDIA_TYPE_VIDEO = 0x01 }
```

相关声明：[bt_avrcp_media_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac927c7e7c59f6f0e6243ca0887945d5a)、[BT_AVRCP_MEDIA_TYPE_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac927c7e7c59f6f0e6243ca0887945d5aa9847baed2a6d09d4ac81039c7302832b)、[BT_AVRCP_MEDIA_TYPE_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac927c7e7c59f6f0e6243ca0887945d5aa76bd7c8c80d6ad9985430148cfd44e82)。

AVRCP 媒体类型（Media Types），用于媒体元素条目。

<a id="r_ga0ebc5d2657688b70119e11ac20d24592"></a>

```c
enum bt_avrcp_media_attr_id_t { BT_AVRCP_MEDIA_ATTR_ID_TITLE = 0x01 , BT_AVRCP_MEDIA_ATTR_ID_ARTIST = 0x02 , BT_AVRCP_MEDIA_ATTR_ID_ALBUM = 0x03 , BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER = 0x04 , BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS = 0x05 , BT_AVRCP_MEDIA_ATTR_ID_GENRE = 0x06 , BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME = 0x07 , BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART = 0x08 }
```

相关声明：[bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)、[BT_AVRCP_MEDIA_ATTR_ID_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592acce73266473e0a14580fa337d2fe53b3)、[BT_AVRCP_MEDIA_ATTR_ID_ARTIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a436c4847edcad7121f7d2ed97169fe61)、[BT_AVRCP_MEDIA_ATTR_ID_ALBUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a2b7e8439c8050cdeda97c43d07774001)、[BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592ac66e18f0843901209f9004a62ab55624)、[BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a3dcfd47034d7890e80a05fd4f600f6bf)、[BT_AVRCP_MEDIA_ATTR_ID_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a8fd312d2869f38b6d7446716a30392b1)、[BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a0ba1f760a733cd00923970d01bb85293)、[BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a958ef736372f39d8e180f8fdeb025121)。

AVRCP 媒体属性标识符（Media Attribute IDs）。

<a id="r_gac02fed37e267996d4de50b06292d0668"></a>

```c
enum bt_avrcp_item_type_t { BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER = 0x01 , BT_AVRCP_ITEM_TYPE_FOLDER = 0x02 , BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT = 0x03 }
```

相关声明：[bt_avrcp_item_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac02fed37e267996d4de50b06292d0668)、[BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668ad8dd8a59776d9d29655cbd083fae6535)、[BT_AVRCP_ITEM_TYPE_FOLDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668aeb7289d0102af72c607d42a8f1c6dfa5)、[BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668aca944e6647d353290b4e5c25fde28bd8)。

AVRCP 条目类型（Item Types），用于浏览操作 GetFolderItems 等。

<a id="r_ga433775fa2758df43ee1d26c78e9122d1"></a>

```c
enum bt_avrcp_playback_status_t { BT_AVRCP_PLAYBACK_STATUS_STOPPED = 0x00 , BT_AVRCP_PLAYBACK_STATUS_PLAYING = 0x01 , BT_AVRCP_PLAYBACK_STATUS_PAUSED = 0x02 , BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK = 0x03 , BT_AVRCP_PLAYBACK_STATUS_REV_SEEK = 0x04 , BT_AVRCP_PLAYBACK_STATUS_ERROR = 0xff }
```

相关声明：[bt_avrcp_playback_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga433775fa2758df43ee1d26c78e9122d1)、[BT_AVRCP_PLAYBACK_STATUS_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a71ddb79b742f9acbd5d14a7639a09fe8)、[BT_AVRCP_PLAYBACK_STATUS_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1ae620f45ad0ecb63be8a8a0b446b5817a)、[BT_AVRCP_PLAYBACK_STATUS_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a2509a9b77091db4ff185448d17d44244)、[BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1ab97050ae05ba6cdff052ac6181eed119)、[BT_AVRCP_PLAYBACK_STATUS_REV_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a5dedf3d49340e3371b118215414aa8d8)、[BT_AVRCP_PLAYBACK_STATUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a05cd93eef7ee39f8e7111d23131de6de)。

AVRCP 播放状态（Playback Status）。

<a id="r_ga128458626d5fe6ffbac7cf97867621aa"></a>

```c
enum bt_avrcp_system_status_t { BT_AVRCP_SYSTEM_STATUS_POWER_ON = 0x00 , BT_AVRCP_SYSTEM_STATUS_POWER_OFF = 0x01 , BT_AVRCP_SYSTEM_STATUS_UNPLUGGED = 0x02 }
```

相关声明：[bt_avrcp_system_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga128458626d5fe6ffbac7cf97867621aa)、[BT_AVRCP_SYSTEM_STATUS_POWER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaaea875986bd59d1da9650c5d5f2de20a2)、[BT_AVRCP_SYSTEM_STATUS_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaa4d4a454f0b8a0a84b557a4075eff1215)、[BT_AVRCP_SYSTEM_STATUS_UNPLUGGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaa1e1ed998f24038e6095f802144e240c2)。

AVRCP 系统状态码（System Status Code）。

<a id="r_ga33825b183b12a2b29d5148a7366c0e77"></a>

```c
enum bt_avrcp_battery_status_t { BT_AVRCP_BATTERY_STATUS_NORMAL = 0x00 , BT_AVRCP_BATTERY_STATUS_WARNING = 0x01 , BT_AVRCP_BATTERY_STATUS_CRITICAL = 0x02 , BT_AVRCP_BATTERY_STATUS_EXTERNAL = 0x03 , BT_AVRCP_BATTERY_STATUS_FULL = 0x04 }
```

相关声明：[bt_avrcp_battery_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga33825b183b12a2b29d5148a7366c0e77)、[BT_AVRCP_BATTERY_STATUS_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77aeaba1597c6c1854d46df1eaaff8862a2)、[BT_AVRCP_BATTERY_STATUS_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a4f7cb6c1917180ca96b10d2c73df9fad)、[BT_AVRCP_BATTERY_STATUS_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77adafb0292944a3d4236608ca13d900c98)、[BT_AVRCP_BATTERY_STATUS_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a2883875f5d5441e7eb7976a38573c178)、[BT_AVRCP_BATTERY_STATUS_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a72880bd811f5cf87fedfa0ff006412b4)。

AVRCP 电池状态码（Battery Status Code）。

<a id="r_ga8047dddc873566ee372e77c6eecd008f"></a>

```c
enum bt_avrcp_player_attr_id_t { BT_AVRCP_PLAYER_ATTR_EQUALIZER = 0x01 , BT_AVRCP_PLAYER_ATTR_REPEAT_MODE = 0x02 , BT_AVRCP_PLAYER_ATTR_SHUFFLE = 0x03 , BT_AVRCP_PLAYER_ATTR_SCAN = 0x04 }
```

相关声明：[bt_avrcp_player_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8047dddc873566ee372e77c6eecd008f)、[BT_AVRCP_PLAYER_ATTR_EQUALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa226313d1f90779c47142ba4966ee968f)、[BT_AVRCP_PLAYER_ATTR_REPEAT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa4cfad017fc5870b099a8d4521e422dca)、[BT_AVRCP_PLAYER_ATTR_SHUFFLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa278d43d52aa33cb54705e7d75ddd98b7)、[BT_AVRCP_PLAYER_ATTR_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa4157b63056caa15282fab2712a855cec)。

AVRCP 播放器应用设置属性标识符（Player Application Setting Attribute IDs）。

<a id="r_gae76f2666d10e6f46a1e5d68327fc7607"></a>

```c
enum bt_avrcp_equalizer_value_t { BT_AVRCP_EQUALIZER_OFF = 0x01 , BT_AVRCP_EQUALIZER_ON = 0x02 }
```

相关声明：[bt_avrcp_equalizer_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae76f2666d10e6f46a1e5d68327fc7607)、[BT_AVRCP_EQUALIZER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggae76f2666d10e6f46a1e5d68327fc7607a31587fdac3ae979f111287a924115d4a)、[BT_AVRCP_EQUALIZER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggae76f2666d10e6f46a1e5d68327fc7607aed029088c6bb73d0928ec19b9029e95e)。

AVRCP 播放器应用的均衡器设置值（Player Application Setting Values for Equalizer）。

<a id="r_ga22bf1b16b383ef473624769ae6ae893a"></a>

```c
enum bt_avrcp_repeat_mode_value_t { BT_AVRCP_REPEAT_MODE_OFF = 0x01 , BT_AVRCP_REPEAT_MODE_SINGLE_TRACK = 0x02 , BT_AVRCP_REPEAT_MODE_ALL_TRACKS = 0x03 , BT_AVRCP_REPEAT_MODE_GROUP = 0x04 }
```

相关声明：[bt_avrcp_repeat_mode_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga22bf1b16b383ef473624769ae6ae893a)、[BT_AVRCP_REPEAT_MODE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa4192bdec6c45e76769ca55ee6a3ab190)、[BT_AVRCP_REPEAT_MODE_SINGLE_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa24914c843056b7fc58f534aec1693948)、[BT_AVRCP_REPEAT_MODE_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aabf4b962a513c908baa7fac9454511aaa)、[BT_AVRCP_REPEAT_MODE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa926fe6e1fc4fee9bb108c9b0c2e46c9a)。

AVRCP 播放器应用的重复模式设置值（Player Application Setting Values for Repeat Mode）。

<a id="r_ga8e6ce46ba46268c2c80f4ec7570859c8"></a>

```c
enum bt_avrcp_shuffle_value_t { BT_AVRCP_SHUFFLE_OFF = 0x01 , BT_AVRCP_SHUFFLE_ALL_TRACKS = 0x02 , BT_AVRCP_SHUFFLE_GROUP = 0x03 }
```

相关声明：[bt_avrcp_shuffle_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8e6ce46ba46268c2c80f4ec7570859c8)、[BT_AVRCP_SHUFFLE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8aac7dce4d43e84c3d80f9eb0791db7a8d)、[BT_AVRCP_SHUFFLE_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8ab36d34793768772409794570f740964a)、[BT_AVRCP_SHUFFLE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8a11a1b2613018ad24861a72313af4189a)。

AVRCP 播放器应用的随机播放设置值（Player Application Setting Values for Shuffle）。

<a id="r_ga4426612c49f8456f2543f373db72d3f2"></a>

```c
enum bt_avrcp_scan_value_t { BT_AVRCP_SCAN_OFF = 0x01 , BT_AVRCP_SCAN_ALL_TRACKS = 0x02 , BT_AVRCP_SCAN_GROUP = 0x03 }
```

相关声明：[bt_avrcp_scan_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4426612c49f8456f2543f373db72d3f2)、[BT_AVRCP_SCAN_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2ae12700ce9b55f758572b0fbfab18ea90)、[BT_AVRCP_SCAN_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2a0819f5ffd937f0d4a379ae5e7b9a2ebf)、[BT_AVRCP_SCAN_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2abde23c31bbb6ab1c7daf85e3cd977cf9)。

AVRCP 播放器应用的扫描设置值（Player Application Setting Values for Scan）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_ga6a212dd4765adc82eda6e35cd9742f0c"></a>

```c
int bt_avrcp_connect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga6a212dd4765adc82eda6e35cd9742f0c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

建立 AVRCP 连接（Connect）。

<a id="r_ga7ec468b9a50413ba478186c88728e13b"></a>

```c
int bt_avrcp_disconnect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7ec468b9a50413ba478186c88728e13b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

断开 AVRCP 连接（Disconnect）。

<a id="r_gac3ccb5386c756bc2688ee5d4499aa29b"></a>

```c
struct net_buf * bt_avrcp_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_avrcp_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac3ccb5386c756bc2688ee5d4499aa29b)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 AVRCP 协议数据单元（PDU）发送分配 `net_buf`，并为 AVRCP、AVRCTP（原文写作 AVRCTP）、L2CAP 和 ACL 头部预留空间（Headroom）。

<a id="r_gad0207b2d16d616b628e7bd2dd7fe4e41"></a>

```c
struct net_buf * bt_avrcp_create_vendor_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_avrcp_create_vendor_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad0207b2d16d616b628e7bd2dd7fe4e41)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 AVRCP 厂商相关协议数据单元（Vendor-Dependent PDU）发送分配 `net_buf`；除 AVRCP、AVCTP、L2CAP 和 ACL 头部外，还为厂商 PDU 头部预留空间（Headroom）。

<a id="r_gac66d9b3fc6352e66716da3e10b25ccdb"></a>

```c
int bt_avrcp_browsing_connect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_browsing_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac66d9b3fc6352e66716da3e10b25ccdb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

连接 AVRCP 浏览通道（Browsing Channel）。

<a id="r_gaa00ea2046f2fe87676fe990e0d34de8b"></a>

```c
int bt_avrcp_browsing_disconnect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_browsing_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaa00ea2046f2fe87676fe990e0d34de8b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

断开 AVRCP 浏览通道（Browsing Channel）。

<a id="r_ga7129d3dc93ea77140ae192099f4a4f92"></a>

```c
int bt_avrcp_ct_register_cb (const struct bt_avrcp_ct_cb *cb)
```

相关声明：[bt_avrcp_ct_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7129d3dc93ea77140ae192099f4a4f92)、[bt_avrcp_ct_cb](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md)。

注册回调（Callback）。

<a id="r_ga311233e84ef1c0fc8c28baacbb77b831"></a>

```c
int bt_avrcp_ct_get_caps (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t cap_id)
```

相关声明：[bt_avrcp_ct_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga311233e84ef1c0fc8c28baacbb77b831)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 AVRCP 能力（Capabilities）。

<a id="r_ga0d59de3bbcfd036f267354fa4ee290dd"></a>

```c
int bt_avrcp_ct_get_unit_info (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_get_unit_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0d59de3bbcfd036f267354fa4ee290dd)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 AVRCP 单元信息（Unit Info）。

<a id="r_ga4ddceec722d768a0f0c86b3701e0e693"></a>

```c
int bt_avrcp_ct_get_subunit_info (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_get_subunit_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ddceec722d768a0f0c86b3701e0e693)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 AVRCP 子单元信息（Subunit Info）。

<a id="r_ga16f8e224bc80ed0bca5ce04a93670320"></a>

```c
int bt_avrcp_ct_passthrough (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t opid, uint8_t state, const uint8_t *payload, uint8_t len)
```

相关声明：[bt_avrcp_ct_passthrough](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga16f8e224bc80ed0bca5ce04a93670320)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 AVRCP 透传命令（Pass Through Command）。

<a id="r_gab0886ea325dddc67167bed86ec6c31e9"></a>

```c
int bt_avrcp_ct_set_browsed_player (struct bt_avrcp_ct *ct, uint8_t tid, uint16_t player_id)
```

相关声明：[bt_avrcp_ct_set_browsed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab0886ea325dddc67167bed86ec6c31e9)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置要浏览的播放器（Browsed Player）。

<a id="r_gab2e6565627deefd8dc5c79a08d02aa85"></a>

```c
int bt_avrcp_ct_register_notification (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t event_id, uint32_t interval, bt_avrcp_notify_changed_cb_t cb)
```

相关声明：[bt_avrcp_ct_register_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab2e6565627deefd8dc5c79a08d02aa85)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_avrcp_notify_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab9bd888ef5443bd0a3d34a34b972f409)。

通过回调注册 AVRCP 变化通知（Changed Notifications）。

<a id="r_gadfafc60888e73a92c1d16fe9696565df"></a>

```c
int bt_avrcp_ct_list_player_app_setting_attrs (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_list_player_app_setting_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadfafc60888e73a92c1d16fe9696565df)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `LIST_PLAYER_APP_SETTING_ATTRS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga11f34256317663cec599d7cb1b250243"></a>

```c
int bt_avrcp_ct_list_player_app_setting_vals (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t attr_id)
```

相关声明：[bt_avrcp_ct_list_player_app_setting_vals](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga11f34256317663cec599d7cb1b250243)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `LIST_PLAYER_APP_SETTING_VALS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga232182eaa8d04921d85a68e35268212e"></a>

```c
int bt_avrcp_ct_get_curr_player_app_setting_val (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_curr_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga232182eaa8d04921d85a68e35268212e)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_CURR_PLAYER_APP_SETTING_VAL` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga962f7727f10ca2827c60d4d9a5dd2bde"></a>

```c
int bt_avrcp_ct_set_player_app_setting_val (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_set_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga962f7727f10ca2827c60d4d9a5dd2bde)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `SET_PLAYER_APP_SETTING_VAL` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga197fc46b498c5d4f52e4868bb85480b9"></a>

```c
int bt_avrcp_ct_get_player_app_setting_attr_text (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_player_app_setting_attr_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga197fc46b498c5d4f52e4868bb85480b9)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gaccbb023e5051601e27ab1ca193152f7b"></a>

```c
int bt_avrcp_ct_get_player_app_setting_val_text (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_player_app_setting_val_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaccbb023e5051601e27ab1ca193152f7b)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_PLAYER_APP_SETTING_VAL_TEXT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gab268d545750bd22b0625779d735d344a"></a>

```c
int bt_avrcp_ct_inform_displayable_char_set (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_inform_displayable_char_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab268d545750bd22b0625779d735d344a)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `INFORM_DISPLAYABLE_CHAR_SET` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gae8cb7f3d8dbb8ae91167916e5c99ec39"></a>

```c
int bt_avrcp_ct_inform_batt_status_of_ct (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t battery_status)
```

相关声明：[bt_avrcp_ct_inform_batt_status_of_ct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae8cb7f3d8dbb8ae91167916e5c99ec39)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `INFORM_BATT_STATUS_OF_CT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga27b0a9e2d86fcc91d2e7b19f1bc5df2d"></a>

```c
int bt_avrcp_ct_set_absolute_volume (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t absolute_volume)
```

相关声明：[bt_avrcp_ct_set_absolute_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga27b0a9e2d86fcc91d2e7b19f1bc5df2d)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送设置绝对音量命令（Set Absolute Volume），用于控制方（CT）。

<a id="r_gaf5b49460a1037b0f146e7b16d89215e1"></a>

```c
int bt_avrcp_ct_get_element_attrs (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_element_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf5b49460a1037b0f146e7b16d89215e1)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_ELEMENT_ATTRS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga014c353ff7f2fc54eefad6a6e20112ec"></a>

```c
int bt_avrcp_ct_get_play_status (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_get_play_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga014c353ff7f2fc54eefad6a6e20112ec)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `GET_PLAY_STATUS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga69561453ade3e8ba07b2122efcddcfad"></a>

```c
int bt_avrcp_ct_set_addressed_player (struct bt_avrcp_ct *ct, uint8_t tid, uint16_t player_id)
```

相关声明：[bt_avrcp_ct_set_addressed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga69561453ade3e8ba07b2122efcddcfad)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送 `SET_ADDRESSED_PLAYER` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gab8d46ac46d35b711209f9a8572c1f8bd"></a>

```c
int bt_avrcp_ct_play_item (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_play_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8d46ac46d35b711209f9a8572c1f8bd)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `PLAY_ITEM` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga7e997ce46f322887227623b43e84ff28"></a>

```c
int bt_avrcp_ct_add_to_now_playing (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_add_to_now_playing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7e997ce46f322887227623b43e84ff28)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `ADD_TO_NOW_PLAYING` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gad77454a6d56942ffe57d5b716f7aa39d"></a>

```c
int bt_avrcp_ct_get_folder_items (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_folder_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad77454a6d56942ffe57d5b716f7aa39d)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取文件夹条目（Get Folder Items）。

<a id="r_gab8730a40ab9bc208a53a035243b8cb1b"></a>

```c
int bt_avrcp_ct_change_path (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_change_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8730a40ab9bc208a53a035243b8cb1b)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

更改路径（Change Path）。

<a id="r_ga4ae38864d35a66a306ced13544e442d4"></a>

```c
int bt_avrcp_ct_get_item_attrs (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_item_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ae38864d35a66a306ced13544e442d4)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取条目属性（Get Item Attributes）。

<a id="r_gadef2624ec50c0bb138d7eae8525784c5"></a>

```c
int bt_avrcp_ct_get_total_number_of_items (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t scope)
```

相关声明：[bt_avrcp_ct_get_total_number_of_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadef2624ec50c0bb138d7eae8525784c5)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取条目总数（Get Total Number Of Items）。

<a id="r_gab8b765fab76ba2585730f328c0abc167"></a>

```c
int bt_avrcp_ct_search (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8b765fab76ba2585730f328c0abc167)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

搜索（Search）。

<a id="r_ga7ba6030ff079e3c47bf6e5838b61ebdb"></a>

```c
int bt_avrcp_tg_register_cb (const struct bt_avrcp_tg_cb *cb)
```

相关声明：[bt_avrcp_tg_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7ba6030ff079e3c47bf6e5838b61ebdb)、[bt_avrcp_tg_cb](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md)。

注册回调（Callback）。

<a id="r_gaecb26512e8b1d267bca0d3ea01438c9b"></a>

```c
int bt_avrcp_tg_send_unit_info_rsp (struct bt_avrcp_tg *tg, uint8_t tid, struct bt_avrcp_unit_info_rsp *rsp)
```

相关声明：[bt_avrcp_tg_send_unit_info_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaecb26512e8b1d267bca0d3ea01438c9b)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_unit_info_rsp](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md)。

发送单元信息响应（Unit Info Response）。

<a id="r_gabc170c5c0aa39827b4efc43880dbf258"></a>

```c
int bt_avrcp_tg_send_subunit_info_rsp (struct bt_avrcp_tg *tg, uint8_t tid)
```

相关声明：[bt_avrcp_tg_send_subunit_info_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gabc170c5c0aa39827b4efc43880dbf258)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送子单元信息响应（Subunit Info Response）。

<a id="r_gad160c86f1647509e10d741284b9bbb03"></a>

```c
int bt_avrcp_tg_get_caps (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad160c86f1647509e10d741284b9bbb03)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_CAPABILITIES` 响应（Response）。

<a id="r_ga1ef0065fd9fa73bcd03491fe700fac65"></a>

```c
int bt_avrcp_tg_notification (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint8_t event_id, struct bt_avrcp_event_data *data)
```

相关声明：[bt_avrcp_tg_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga1ef0065fd9fa73bcd03491fe700fac65)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)。

发送通知响应（Notification Response）。

<a id="r_ga15bf2602f37ef83b3bcefd85920658eb"></a>

```c
int bt_avrcp_tg_set_browsed_player (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_set_browsed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga15bf2602f37ef83b3bcefd85920658eb)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置浏览播放器响应（Set Browsed Player Response）。

<a id="r_gac92854e7f567f6088a5cf3ad3c209343"></a>

```c
int bt_avrcp_tg_send_passthrough_rsp (struct bt_avrcp_tg *tg, uint8_t tid, bt_avrcp_rsp_t result, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_send_passthrough_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac92854e7f567f6088a5cf3ad3c209343)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_rsp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaba2d8faec2c3baf7403199ea8a509326)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 AVRCP 透传响应（Pass Through Response）。

<a id="r_gab442ef3962bebd8dbe0d5681498f8453"></a>

```c
int bt_avrcp_tg_list_player_app_setting_attrs (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_list_player_app_setting_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab442ef3962bebd8dbe0d5681498f8453)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_ATTRS` 对应的响应。

<a id="r_gae8b42aada8be4c9fac13fbd90e751a7b"></a>

```c
int bt_avrcp_tg_list_player_app_setting_vals (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_list_player_app_setting_vals](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae8b42aada8be4c9fac13fbd90e751a7b)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_VALS` 对应的响应。

<a id="r_gab18ce4d9348698272eedff52ddb3052e"></a>

```c
int bt_avrcp_tg_get_curr_player_app_setting_val (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_curr_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab18ce4d9348698272eedff52ddb3052e)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_CURR_PLAYER_APP_SETTING_VAL` 对应的响应。

<a id="r_ga9d471d9a932dfd43b71e894ddec013b4"></a>

```c
int bt_avrcp_tg_set_player_app_setting_val (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_set_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga9d471d9a932dfd43b71e894ddec013b4)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_SET_PLAYER_APP_SETTING_VAL` 对应的响应。

<a id="r_ga123f5528b62f48faaf020f19dcc321c1"></a>

```c
int bt_avrcp_tg_get_player_app_setting_attr_text (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_player_app_setting_attr_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga123f5528b62f48faaf020f19dcc321c1)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_ATTR_TEXT` 对应的响应。

<a id="r_ga8cc324a60a3480524336bc399d62c1ed"></a>

```c
int bt_avrcp_tg_get_player_app_setting_val_text (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_player_app_setting_val_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8cc324a60a3480524336bc399d62c1ed)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_VAL_TEXT` 对应的响应。

<a id="r_gadda57eb5c28f6b77bda5efe9286bc5f4"></a>

```c
int bt_avrcp_tg_inform_displayable_char_set (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_inform_displayable_char_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadda57eb5c28f6b77bda5efe9286bc5f4)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_INFORM_DISPLAYABLE_CHAR_SET` 对应的响应。

<a id="r_gaa2aca5a011a99a20a3bd3fd7154a864a"></a>

```c
int bt_avrcp_tg_inform_batt_status_of_ct (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_inform_batt_status_of_ct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaa2aca5a011a99a20a3bd3fd7154a864a)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_INFORM_BATT_STATUS_OF_CT` 对应的响应。

<a id="r_gad0d937d50eccfbedc81cc575a3e238f2"></a>

```c
int bt_avrcp_tg_absolute_volume (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint8_t absolute_volume)
```

相关声明：[bt_avrcp_tg_absolute_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad0d937d50eccfbedc81cc575a3e238f2)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送设置绝对音量响应（Set Absolute Volume），用于目标方（TG）。

<a id="r_ga81333eaee7ca1838424ce9b513e6e2c5"></a>

```c
int bt_avrcp_tg_get_element_attrs (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_element_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81333eaee7ca1838424ce9b513e6e2c5)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_ELEMENT_ATTRS` 对应的响应。

<a id="r_ga4f37f0c696ea98f44bd5e8ce2905d9f4"></a>

```c
int bt_avrcp_tg_get_play_status (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_play_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4f37f0c696ea98f44bd5e8ce2905d9f4)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAY_STATUS` 对应的响应。

<a id="r_gadcf3f892a1d492a2743cdb4f8d205505"></a>

```c
int bt_avrcp_tg_set_addressed_player (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_set_addressed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadcf3f892a1d492a2743cdb4f8d205505)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_SET_ADDRESSED_PLAYER` 对应的响应。

<a id="r_ga5f72112c0887ed3efc3455ead567126d"></a>

```c
int bt_avrcp_tg_play_item (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_play_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga5f72112c0887ed3efc3455ead567126d)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_PLAY_ITEM` 对应的响应。

<a id="r_gafc84238ea566bef4d2789e7cdba193dd"></a>

```c
int bt_avrcp_tg_add_to_now_playing (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_add_to_now_playing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gafc84238ea566bef4d2789e7cdba193dd)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_ADD_TO_NOW_PLAYING` 对应的响应。

<a id="r_ga6261635bf3925766bb7af10696df6fd5"></a>

```c
int bt_avrcp_tg_get_folder_items (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_folder_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga6261635bf3925766bb7af10696df6fd5)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取文件夹条目响应（Get Folder Items Response）。

<a id="r_ga851b0c30ac0b382658b5ce040d7755eb"></a>

```c
int bt_avrcp_tg_change_path (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint32_t num_items)
```

相关声明：[bt_avrcp_tg_change_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga851b0c30ac0b382658b5ce040d7755eb)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送更改路径响应（Change Path Response）。

<a id="r_ga509746020e487d769f94174a4071b673"></a>

```c
int bt_avrcp_tg_get_item_attrs (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_item_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga509746020e487d769f94174a4071b673)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取条目属性响应（Get Item Attributes Response）。

<a id="r_gaf521ea00d597fced528d86befd9b5bbb"></a>

```c
int bt_avrcp_tg_get_total_number_of_items (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_total_number_of_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf521ea00d597fced528d86befd9b5bbb)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取条目总数响应（Get Total Number Of Items Response）。

<a id="r_ga136fda008bf5d5f7e9cad3855a4173f9"></a>

```c
int bt_avrcp_tg_search (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga136fda008bf5d5f7e9cad3855a4173f9)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送搜索响应（Search Response）。

<a id="r_gaad6d011fe84aaa6cec8665aa87d4cc41"></a>

```c
int bt_avrcp_tg_browsing_general_reject (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_browsing_general_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaad6d011fe84aaa6cec8665aa87d4cc41)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在 AVRCP 浏览通道（Browsing Channel）上发送通用拒绝响应（General Reject Response），用于目标方（TG）。


## 1.6\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_transport_clock_reference/P002_avrcp.h_源码浏览.md)
- [bt_avrcp_unit_info_rsp](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md)
- [bt_avrcp_subunit_info_rsp](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md)
- [bt_avrcp_passthrough_opvu_data](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md)
- [bt_avrcp_passthrough_cmd](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md)
- [bt_avrcp_passthrough_rsp](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md)
- [bt_avrcp_get_caps_rsp](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md)
- [bt_avrcp_get_folder_items_cmd](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md)
- [bt_avrcp_item_hdr](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md)
- [bt_avrcp_media_player_item](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md)
- [bt_avrcp_folder_item](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md)
- [bt_avrcp_media_attr](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md)
- [media_element_item_name](../device_power_control_model_reference/P028_media_element_item_name_结构体.md)
- [media_element_item_attr](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md)
- [bt_avrcp_media_element_item](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md)
- [bt_avrcp_get_folder_items_rsp](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md)
- [bt_avrcp_change_path_cmd](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md)
- [bt_avrcp_change_path_rsp](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md)
- [bt_avrcp_get_item_attrs_cmd](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md)
- [bt_avrcp_get_item_attrs_rsp](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md)
- [bt_avrcp_play_item_rsp](../bluetooth_classic_model_reference/P060_bt_avrcp_play_item_rsp_结构体.md)
- [bt_avrcp_get_total_number_of_items_cmd](../bluetooth_classic_model_reference/P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md)
- [bt_avrcp_get_total_number_of_items_rsp](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md)
- [bt_avrcp_search_cmd](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md)
- [bt_avrcp_search_rsp](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md)
- [bt_avrcp_folder_name](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md)
- [bt_avrcp_set_browsed_player_rsp](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md)
- [bt_avrcp_get_element_attrs_cmd](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md)
- [bt_avrcp_get_element_attrs_rsp](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md)
- [bt_avrcp_list_player_app_setting_attrs_rsp](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md)
- [bt_avrcp_list_player_app_setting_vals_cmd](../bluetooth_classic_model_reference/P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md)
- [bt_avrcp_list_player_app_setting_vals_rsp](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md)
- [bt_avrcp_get_curr_player_app_setting_val_cmd](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md)
- [bt_avrcp_app_setting_attr_val](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md)
- [bt_avrcp_get_curr_player_app_setting_val_rsp](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md)
- [bt_avrcp_set_player_app_setting_val_cmd](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md)
- [bt_avrcp_get_player_app_setting_attr_text_cmd](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md)
- [bt_avrcp_app_setting_attr_text](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md)
- [bt_avrcp_get_player_app_setting_attr_text_rsp](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md)
- [bt_avrcp_get_player_app_setting_val_text_cmd](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md)
- [bt_avrcp_app_setting_val_text](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md)
- [bt_avrcp_get_player_app_setting_val_text_rsp](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md)
- [bt_avrcp_inform_displayable_char_set_cmd](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md)
- [bt_avrcp_inform_batt_status_of_ct_cmd](../bluetooth_classic_model_reference/P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md)
- [bt_avrcp_get_play_status_rsp](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md)
- [bt_avrcp_register_notification_cmd](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md)
- [bt_avrcp_set_absolute_volume_cmd](../bluetooth_classic_model_reference/P064_bt_avrcp_set_absolute_volume_cmd_结构体.md)
- [bt_avrcp_set_absolute_volume_rsp](../bluetooth_classic_model_reference/P065_bt_avrcp_set_absolute_volume_rsp_结构体.md)
- [bt_avrcp_set_addressed_player_cmd](../bluetooth_classic_model_reference/P066_bt_avrcp_set_addressed_player_cmd_结构体.md)
- [bt_avrcp_play_item_cmd](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md)
- [bt_avrcp_add_to_now_playing_cmd](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md)
- [bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)
- [bt_avrcp_ct_cb](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md)
- [bt_avrcp_tg_cb](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md)
- [BT_AVRCP_COMPANY_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae4e7573280179717124104858629122a)
- [BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae7a97b11a8954a2a25cc401ced566fd2)
- [BT_AVRCP_PASSTHROUGH_GET_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7eee1ffa11a5152a0dd014ac15979605)
- [BT_AVRCP_PASSTHROUGH_GET_OPID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8c8e1596f92e32781690c0a76196c4c8)
- [BT_AVRCP_PASSTHROUGH_SET_STATE_OPID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4f8014317db642c98d3db9be6db7adea)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [BT_AVRCP_MAX_ABSOLUTE_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga5ecfdd180bc51dc0867e859d1b3a7fbe)
- [bt_avrcp_notify_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab9bd888ef5443bd0a3d34a34b972f409)
- [bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac311dc7b5f99162b954271529eeb84ea)
- [BT_AVRCP_CAP_COMPANY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac311dc7b5f99162b954271529eeb84eaa89fecce56afb09791a2253a7ad840430)
- [BT_AVRCP_CAP_EVENTS_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac311dc7b5f99162b954271529eeb84eaa2a7b326aded772c09cf01387145d2802)
- [bt_avrcp_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf55aae17f67a1361279ae208b17e4a75)
- [BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a892f2928d634b675426f2fe597a45f6d)
- [BT_AVRCP_EVT_TRACK_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a25f8e3e08b5988e833eb0d47452d12a9)
- [BT_AVRCP_EVT_TRACK_REACHED_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a412a9b7cbb891bc50fb77c1e6de9faaf)
- [BT_AVRCP_EVT_TRACK_REACHED_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75af4f9e221522cd57461920d22e7a290b9)
- [BT_AVRCP_EVT_PLAYBACK_POS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75afc4ef6f8a80a9067ad9dfd30bf2a6958)
- [BT_AVRCP_EVT_BATT_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a9ff1d99bc0c83399961ef23d4a75f9b6)
- [BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ae6237555b0051b2395e0bf2287e954c1)
- [BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ab2b2287a0db9be97af8c20298bebba2d)
- [BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ac0b720defdd8716d757e0c8a7e57db83)
- [BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75abd82dd6ba6d5d76cf22a8c703c76c6e0)
- [BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ab6fdeacb536067660f754b3c586e073a)
- [BT_AVRCP_EVT_UIDS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a8ac593400cda085fbdff36e403bd2a91)
- [BT_AVRCP_EVT_VOLUME_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a8d526498fdcb1380e8e3944da2a5ef85)
- [bt_avrcp_ctype_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga2a4c610e00ba9832f954f30bd6b6618e)
- [BT_AVRCP_CTYPE_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04)
- [BT_AVRCP_CTYPE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce)
- [BT_AVRCP_CTYPE_SPECIFIC_INQUIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb)
- [BT_AVRCP_CTYPE_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290)
- [BT_AVRCP_CTYPE_GENERAL_INQUIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7)
- [bt_avrcp_rsp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaba2d8faec2c3baf7403199ea8a509326)
- [BT_AVRCP_RSP_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696)
- [BT_AVRCP_RSP_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8)
- [BT_AVRCP_RSP_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c)
- [BT_AVRCP_RSP_IN_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad)
- [BT_AVRCP_RSP_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144)
- [BT_AVRCP_RSP_STABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992)
- [BT_AVRCP_RSP_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988)
- [BT_AVRCP_RSP_INTERIM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88)
- [bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)
- [BT_AVRCP_SUBUNIT_TYPE_PANEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga78ba828636b731b2c43e088a581bfee9a6db3104fa9727594b842b4ae9b64a605)
- [BT_AVRCP_SUBUNIT_TYPE_UNIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga78ba828636b731b2c43e088a581bfee9a8be8c211cd26a849c1c89e482aa10030)
- [bt_avrcp_opid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga3c997d96028343a0a5a4948dabe19b84)
- [BT_AVRCP_OPID_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f)
- [BT_AVRCP_OPID_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9)
- [BT_AVRCP_OPID_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537)
- [BT_AVRCP_OPID_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba)
- [BT_AVRCP_OPID_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2)
- [BT_AVRCP_OPID_RIGHT_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63)
- [BT_AVRCP_OPID_RIGHT_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745)
- [BT_AVRCP_OPID_LEFT_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779)
- [BT_AVRCP_OPID_LEFT_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366)
- [BT_AVRCP_OPID_ROOT_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87)
- [BT_AVRCP_OPID_SETUP_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372)
- [BT_AVRCP_OPID_CONTENTS_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472)
- [BT_AVRCP_OPID_FAVORITE_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574)
- [BT_AVRCP_OPID_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3)
- [BT_AVRCP_OPID_0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade)
- [BT_AVRCP_OPID_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0)
- [BT_AVRCP_OPID_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566)
- [BT_AVRCP_OPID_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459)
- [BT_AVRCP_OPID_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c)
- [BT_AVRCP_OPID_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5)
- [BT_AVRCP_OPID_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a)
- [BT_AVRCP_OPID_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff)
- [BT_AVRCP_OPID_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06)
- [BT_AVRCP_OPID_9](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb)
- [BT_AVRCP_OPID_DOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf)
- [BT_AVRCP_OPID_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae)
- [BT_AVRCP_OPID_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2)
- [BT_AVRCP_OPID_CHANNEL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586)
- [BT_AVRCP_OPID_CHANNEL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de)
- [BT_AVRCP_OPID_PREVIOUS_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e)
- [BT_AVRCP_OPID_SOUND_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b)
- [BT_AVRCP_OPID_INPUT_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c)
- [BT_AVRCP_OPID_DISPLAY_INFORMATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef)
- [BT_AVRCP_OPID_HELP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b)
- [BT_AVRCP_OPID_PAGE_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321)
- [BT_AVRCP_OPID_PAGE_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a)
- [BT_AVRCP_OPID_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358)
- [BT_AVRCP_OPID_VOLUME_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487)
- [BT_AVRCP_OPID_VOLUME_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62)
- [BT_AVRCP_OPID_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1)
- [BT_AVRCP_OPID_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b)
- [BT_AVRCP_OPID_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60)
- [BT_AVRCP_OPID_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a)
- [BT_AVRCP_OPID_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27)
- [BT_AVRCP_OPID_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8)
- [BT_AVRCP_OPID_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f)
- [BT_AVRCP_OPID_EJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344)
- [BT_AVRCP_OPID_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e)
- [BT_AVRCP_OPID_BACKWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23)
- [BT_AVRCP_OPID_ANGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2)
- [BT_AVRCP_OPID_SUBPICTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98)
- [BT_AVRCP_OPID_F1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5)
- [BT_AVRCP_OPID_F2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4)
- [BT_AVRCP_OPID_F3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40)
- [BT_AVRCP_OPID_F4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283)
- [BT_AVRCP_OPID_F5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d)
- [BT_AVRCP_OPID_VENDOR_UNIQUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d)
- [bt_avrcp_button_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga15f9f868b056f17ea12d96530b7da881)
- [BT_AVRCP_BUTTON_PRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3)
- [BT_AVRCP_BUTTON_RELEASED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [BT_AVRCP_STATUS_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a14e183c33a64cdac271ee7f320796bd6)
- [BT_AVRCP_STATUS_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a8a767466ac8069e20f6d9e0f30c33420)
- [BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a7cba04973b3753b50f63e6b0bc205638)
- [BT_AVRCP_STATUS_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0af48dcc2c65e4af461c1a6ece622a2f5a)
- [BT_AVRCP_STATUS_OPERATION_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0ad3a41ce04f27cc349c7466aae18bcee2)
- [BT_AVRCP_STATUS_UID_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a0e77e1782b5a0f88f4d45b6560df2b09)
- [BT_AVRCP_STATUS_INVALID_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a448e1c0383e4e4b5fc3c0c80e2040af9)
- [BT_AVRCP_STATUS_NOT_A_DIRECTORY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a6fee8c927f897fff59b7690c3e1732c2)
- [BT_AVRCP_STATUS_DOES_NOT_EXIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a9f552377c6bb93b3e52b29228a6feaa5)
- [BT_AVRCP_STATUS_INVALID_SCOPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0aaddaf4f6439aa6a52e3a4fdbb3f0c071)
- [BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a81094560261826c16be6ebba9d99081c)
- [BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a2f8ca7c1fe4ba52a1a418612c094158a)
- [BT_AVRCP_STATUS_MEDIA_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0ae63cf3ffada01f268498151d88c3a3ec)
- [BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a359810fbbdf875adb89a192deaae6a6d)
- [BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a4ee781cc845d8b1211217f8338b97023)
- [BT_AVRCP_STATUS_SEARCH_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a402038758703ee9f8543ad546681a3c5)
- [BT_AVRCP_STATUS_INVALID_PLAYER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a5cd415ba8d307dc5153a9a0b2f9958e3)
- [BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a28925d094d4c3e55b259a55440a5c044)
- [BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a3dfa01e069c517e7e466fa6edcc1c9cb)
- [BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a033e10d03bf56df95ec1e888a07cedf9)
- [BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a5544c22cad94dadb9eccf47669fabafb)
- [BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a43e59407a44f87d85fa71cdb627524e3)
- [BT_AVRCP_STATUS_IN_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0af72a55b60fda9c157cdef8b1c6038780)
- [BT_AVRCP_STATUS_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a14868dd213f59e09dbdb066d5ca39c96)
- [BT_AVRCP_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0afbff25149bb9c35756dfb7bb6f2516c3)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)
- [BT_AVRCP_CHARSET_UTF8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga81330413af9eba049da6557b14ae082ca29f70165632222ae40ac3e44554130b0)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a7a388bb84fbe14f8931ab9bf41b9823d)
- [BT_AVRCP_SCOPE_VFS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a37002574948081d7b42001a62755636b)
- [BT_AVRCP_SCOPE_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a4db7699a5f22c8d5986f6f1ba7219dac)
- [BT_AVRCP_SCOPE_NOW_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a7baa6442aafc4d00635df52f44d0d608)
- [bt_avrcp_change_path_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga02d67e84b4a48ebecf3b307cbd4bb61c)
- [BT_AVRCP_CHANGE_PATH_PARENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga02d67e84b4a48ebecf3b307cbd4bb61ca8914559b14b7529fc5f1df764036748d)
- [BT_AVRCP_CHANGE_PATH_CHILD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga02d67e84b4a48ebecf3b307cbd4bb61ca5cbd84478163171359044825050dd172)
- [bt_avrcp_folder_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga09d191c490efcfb9f8139975090be0d5)
- [BT_AVRCP_FOLDER_TYPE_MIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a06308eb3786579cf5aeb0f19f0ab37ac)
- [BT_AVRCP_FOLDER_TYPE_TITLES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a702f9974cf5d51a77757fd7e1ef4ab0f)
- [BT_AVRCP_FOLDER_TYPE_ALBUMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5ab33fca5f57f5b80785df367ab788a8fc)
- [BT_AVRCP_FOLDER_TYPE_ARTISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a89aaeb11e807c44479ff47164d99c4f7)
- [BT_AVRCP_FOLDER_TYPE_GENRES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a0ab0ffb986db900ece2146a347dae06d)
- [BT_AVRCP_FOLDER_TYPE_PLAYLISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a708dfb5de11ae783b413d2d99202f9b5)
- [BT_AVRCP_FOLDER_TYPE_YEARS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a0a60cb99cd19d203618b1264e2a3cca6)
- [bt_avrcp_media_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac927c7e7c59f6f0e6243ca0887945d5a)
- [BT_AVRCP_MEDIA_TYPE_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac927c7e7c59f6f0e6243ca0887945d5aa9847baed2a6d09d4ac81039c7302832b)
- [BT_AVRCP_MEDIA_TYPE_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac927c7e7c59f6f0e6243ca0887945d5aa76bd7c8c80d6ad9985430148cfd44e82)
- [bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)
- [BT_AVRCP_MEDIA_ATTR_ID_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592acce73266473e0a14580fa337d2fe53b3)
- [BT_AVRCP_MEDIA_ATTR_ID_ARTIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a436c4847edcad7121f7d2ed97169fe61)
- [BT_AVRCP_MEDIA_ATTR_ID_ALBUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a2b7e8439c8050cdeda97c43d07774001)
- [BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592ac66e18f0843901209f9004a62ab55624)
- [BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a3dcfd47034d7890e80a05fd4f600f6bf)
- [BT_AVRCP_MEDIA_ATTR_ID_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a8fd312d2869f38b6d7446716a30392b1)
- [BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a0ba1f760a733cd00923970d01bb85293)
- [BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a958ef736372f39d8e180f8fdeb025121)
- [bt_avrcp_item_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac02fed37e267996d4de50b06292d0668)
- [BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668ad8dd8a59776d9d29655cbd083fae6535)
- [BT_AVRCP_ITEM_TYPE_FOLDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668aeb7289d0102af72c607d42a8f1c6dfa5)
- [BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668aca944e6647d353290b4e5c25fde28bd8)
- [bt_avrcp_playback_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga433775fa2758df43ee1d26c78e9122d1)
- [BT_AVRCP_PLAYBACK_STATUS_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a71ddb79b742f9acbd5d14a7639a09fe8)
- [BT_AVRCP_PLAYBACK_STATUS_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1ae620f45ad0ecb63be8a8a0b446b5817a)
- [BT_AVRCP_PLAYBACK_STATUS_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a2509a9b77091db4ff185448d17d44244)
- [BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1ab97050ae05ba6cdff052ac6181eed119)
- [BT_AVRCP_PLAYBACK_STATUS_REV_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a5dedf3d49340e3371b118215414aa8d8)
- [BT_AVRCP_PLAYBACK_STATUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a05cd93eef7ee39f8e7111d23131de6de)
- [bt_avrcp_system_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga128458626d5fe6ffbac7cf97867621aa)
- [BT_AVRCP_SYSTEM_STATUS_POWER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaaea875986bd59d1da9650c5d5f2de20a2)
- [BT_AVRCP_SYSTEM_STATUS_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaa4d4a454f0b8a0a84b557a4075eff1215)
- [BT_AVRCP_SYSTEM_STATUS_UNPLUGGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaa1e1ed998f24038e6095f802144e240c2)
- [bt_avrcp_battery_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga33825b183b12a2b29d5148a7366c0e77)
- [BT_AVRCP_BATTERY_STATUS_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77aeaba1597c6c1854d46df1eaaff8862a2)
- [BT_AVRCP_BATTERY_STATUS_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a4f7cb6c1917180ca96b10d2c73df9fad)
- [BT_AVRCP_BATTERY_STATUS_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77adafb0292944a3d4236608ca13d900c98)
- [BT_AVRCP_BATTERY_STATUS_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a2883875f5d5441e7eb7976a38573c178)
- [BT_AVRCP_BATTERY_STATUS_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a72880bd811f5cf87fedfa0ff006412b4)
- [bt_avrcp_player_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8047dddc873566ee372e77c6eecd008f)
- [BT_AVRCP_PLAYER_ATTR_EQUALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa226313d1f90779c47142ba4966ee968f)
- [BT_AVRCP_PLAYER_ATTR_REPEAT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa4cfad017fc5870b099a8d4521e422dca)
- [BT_AVRCP_PLAYER_ATTR_SHUFFLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa278d43d52aa33cb54705e7d75ddd98b7)
- [BT_AVRCP_PLAYER_ATTR_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa4157b63056caa15282fab2712a855cec)
- [bt_avrcp_equalizer_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae76f2666d10e6f46a1e5d68327fc7607)
- [BT_AVRCP_EQUALIZER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggae76f2666d10e6f46a1e5d68327fc7607a31587fdac3ae979f111287a924115d4a)
- [BT_AVRCP_EQUALIZER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggae76f2666d10e6f46a1e5d68327fc7607aed029088c6bb73d0928ec19b9029e95e)
- [bt_avrcp_repeat_mode_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga22bf1b16b383ef473624769ae6ae893a)
- [BT_AVRCP_REPEAT_MODE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa4192bdec6c45e76769ca55ee6a3ab190)
- [BT_AVRCP_REPEAT_MODE_SINGLE_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa24914c843056b7fc58f534aec1693948)
- [BT_AVRCP_REPEAT_MODE_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aabf4b962a513c908baa7fac9454511aaa)
- [BT_AVRCP_REPEAT_MODE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa926fe6e1fc4fee9bb108c9b0c2e46c9a)
- [bt_avrcp_shuffle_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8e6ce46ba46268c2c80f4ec7570859c8)
- [BT_AVRCP_SHUFFLE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8aac7dce4d43e84c3d80f9eb0791db7a8d)
- [BT_AVRCP_SHUFFLE_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8ab36d34793768772409794570f740964a)
- [BT_AVRCP_SHUFFLE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8a11a1b2613018ad24861a72313af4189a)
- [bt_avrcp_scan_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4426612c49f8456f2543f373db72d3f2)
- [BT_AVRCP_SCAN_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2ae12700ce9b55f758572b0fbfab18ea90)
- [BT_AVRCP_SCAN_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2a0819f5ffd937f0d4a379ae5e7b9a2ebf)
- [BT_AVRCP_SCAN_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2abde23c31bbb6ab1c7daf85e3cd977cf9)
- [bt_avrcp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga6a212dd4765adc82eda6e35cd9742f0c)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_avrcp_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7ec468b9a50413ba478186c88728e13b)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_avrcp_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac3ccb5386c756bc2688ee5d4499aa29b)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_avrcp_create_vendor_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad0207b2d16d616b628e7bd2dd7fe4e41)
- [bt_avrcp_browsing_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac66d9b3fc6352e66716da3e10b25ccdb)
- [bt_avrcp_browsing_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaa00ea2046f2fe87676fe990e0d34de8b)
- [bt_avrcp_ct_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7129d3dc93ea77140ae192099f4a4f92)
- [bt_avrcp_ct_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga311233e84ef1c0fc8c28baacbb77b831)
- [bt_avrcp_ct_get_unit_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0d59de3bbcfd036f267354fa4ee290dd)
- [bt_avrcp_ct_get_subunit_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ddceec722d768a0f0c86b3701e0e693)
- [bt_avrcp_ct_passthrough](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga16f8e224bc80ed0bca5ce04a93670320)
- [bt_avrcp_ct_set_browsed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab0886ea325dddc67167bed86ec6c31e9)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_ct_register_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab2e6565627deefd8dc5c79a08d02aa85)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_ct_list_player_app_setting_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadfafc60888e73a92c1d16fe9696565df)
- [bt_avrcp_ct_list_player_app_setting_vals](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga11f34256317663cec599d7cb1b250243)
- [bt_avrcp_ct_get_curr_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga232182eaa8d04921d85a68e35268212e)
- [bt_avrcp_ct_set_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga962f7727f10ca2827c60d4d9a5dd2bde)
- [bt_avrcp_ct_get_player_app_setting_attr_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga197fc46b498c5d4f52e4868bb85480b9)
- [bt_avrcp_ct_get_player_app_setting_val_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaccbb023e5051601e27ab1ca193152f7b)
- [bt_avrcp_ct_inform_displayable_char_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab268d545750bd22b0625779d735d344a)
- [bt_avrcp_ct_inform_batt_status_of_ct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae8cb7f3d8dbb8ae91167916e5c99ec39)
- [bt_avrcp_ct_set_absolute_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga27b0a9e2d86fcc91d2e7b19f1bc5df2d)
- [bt_avrcp_ct_get_element_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf5b49460a1037b0f146e7b16d89215e1)
- [bt_avrcp_ct_get_play_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga014c353ff7f2fc54eefad6a6e20112ec)
- [bt_avrcp_ct_set_addressed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga69561453ade3e8ba07b2122efcddcfad)
- [bt_avrcp_ct_play_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8d46ac46d35b711209f9a8572c1f8bd)
- [bt_avrcp_ct_add_to_now_playing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7e997ce46f322887227623b43e84ff28)
- [bt_avrcp_ct_get_folder_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad77454a6d56942ffe57d5b716f7aa39d)
- [bt_avrcp_ct_change_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8730a40ab9bc208a53a035243b8cb1b)
- [bt_avrcp_ct_get_item_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ae38864d35a66a306ced13544e442d4)
- [bt_avrcp_ct_get_total_number_of_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadef2624ec50c0bb138d7eae8525784c5)
- [bt_avrcp_ct_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8b765fab76ba2585730f328c0abc167)
- [bt_avrcp_tg_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7ba6030ff079e3c47bf6e5838b61ebdb)
- [bt_avrcp_tg_send_unit_info_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaecb26512e8b1d267bca0d3ea01438c9b)
- [bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)
- [bt_avrcp_tg_send_subunit_info_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gabc170c5c0aa39827b4efc43880dbf258)
- [bt_avrcp_tg_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad160c86f1647509e10d741284b9bbb03)
- [bt_avrcp_tg_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga1ef0065fd9fa73bcd03491fe700fac65)
- [bt_avrcp_tg_set_browsed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga15bf2602f37ef83b3bcefd85920658eb)
- [bt_avrcp_tg_send_passthrough_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac92854e7f567f6088a5cf3ad3c209343)
- [bt_avrcp_tg_list_player_app_setting_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab442ef3962bebd8dbe0d5681498f8453)
- [bt_avrcp_tg_list_player_app_setting_vals](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae8b42aada8be4c9fac13fbd90e751a7b)
- [bt_avrcp_tg_get_curr_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab18ce4d9348698272eedff52ddb3052e)
- [bt_avrcp_tg_set_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga9d471d9a932dfd43b71e894ddec013b4)
- [bt_avrcp_tg_get_player_app_setting_attr_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga123f5528b62f48faaf020f19dcc321c1)
- [bt_avrcp_tg_get_player_app_setting_val_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8cc324a60a3480524336bc399d62c1ed)
- [bt_avrcp_tg_inform_displayable_char_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadda57eb5c28f6b77bda5efe9286bc5f4)
- [bt_avrcp_tg_inform_batt_status_of_ct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaa2aca5a011a99a20a3bd3fd7154a864a)
- [bt_avrcp_tg_absolute_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad0d937d50eccfbedc81cc575a3e238f2)
- [bt_avrcp_tg_get_element_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81333eaee7ca1838424ce9b513e6e2c5)
- [bt_avrcp_tg_get_play_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4f37f0c696ea98f44bd5e8ce2905d9f4)
- [bt_avrcp_tg_set_addressed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadcf3f892a1d492a2743cdb4f8d205505)
- [bt_avrcp_tg_play_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga5f72112c0887ed3efc3455ead567126d)
- [bt_avrcp_tg_add_to_now_playing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gafc84238ea566bef4d2789e7cdba193dd)
- [bt_avrcp_tg_get_folder_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga6261635bf3925766bb7af10696df6fd5)
- [bt_avrcp_tg_change_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga851b0c30ac0b382658b5ce040d7755eb)
- [bt_avrcp_tg_get_item_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga509746020e487d769f94174a4071b673)
- [bt_avrcp_tg_get_total_number_of_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf521ea00d597fced528d86befd9b5bbb)
- [bt_avrcp_tg_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga136fda008bf5d5f7e9cad3855a4173f9)
- [bt_avrcp_tg_browsing_general_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaad6d011fe84aaa6cec8665aa87d4cc41)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__pinctrl__ch570-pinctrl.h_文件参考.md)
