---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-2
title: 音频_视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_音频\_视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）

<a id="details"></a>

音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）

<a id="header-groups"></a>
<a id="groups"></a>

## 2.1\_主题（Topics）

<a id="r_bt_5Favrcp_5Fcover_5Fart"></a>

相关声明：[音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）](../api_hid_pipeline_topic_reference/P001_音频_视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）.md)。

音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile，AVRCP-CA）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.2\_数据结构（Data Structures）

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

<a id="r_bt_5Favrcp_5Fct"></a>

```c
struct bt_avrcp_ct
```

相关声明：[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)。

AVRCP 控制端（Controller，CT）结构体。

<a id="r_bt_5Favrcp_5Ftg"></a>

```c
struct bt_avrcp_tg
```

相关声明：[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)。

AVRCP 目标端（Target，TG）结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.3\_宏定义（Macros）

<a id="r_gae4e7573280179717124104858629122a"></a>

```c
#define BT_AVRCP_COMPANY_ID_SIZE (3)
```

相关声明：[BT_AVRCP_COMPANY_ID_SIZE](#gae4e7573280179717124104858629122a)。

<a id="r_gae7a97b11a8954a2a25cc401ced566fd2"></a>

```c
#define BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG (0x001958)
```

相关声明：[BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG](#gae7a97b11a8954a2a25cc401ced566fd2)。

<a id="r_ga7eee1ffa11a5152a0dd014ac15979605"></a>

```c
#define BT_AVRCP_PASSTHROUGH_GET_STATE(payload)
```

相关声明：[BT_AVRCP_PASSTHROUGH_GET_STATE](#ga7eee1ffa11a5152a0dd014ac15979605)。

<a id="r_ga8c8e1596f92e32781690c0a76196c4c8"></a>

```c
#define BT_AVRCP_PASSTHROUGH_GET_OPID(payload)
```

相关声明：[BT_AVRCP_PASSTHROUGH_GET_OPID](#ga8c8e1596f92e32781690c0a76196c4c8)。

<a id="r_ga4f8014317db642c98d3db9be6db7adea"></a>

```c
#define BT_AVRCP_PASSTHROUGH_SET_STATE_OPID(payload, state, opid)
```

相关声明：[BT_AVRCP_PASSTHROUGH_SET_STATE_OPID](#ga4f8014317db642c98d3db9be6db7adea)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

<a id="r_ga5ecfdd180bc51dc0867e859d1b3a7fbe"></a>

```c
#define BT_AVRCP_MAX_ABSOLUTE_VOLUME 0x7F
```

相关声明：[BT_AVRCP_MAX_ABSOLUTE_VOLUME](#ga5ecfdd180bc51dc0867e859d1b3a7fbe)。

音视频遥控配置文件（Audio/Video Remote Control Profile，AVRCP）的最大绝对音量（Maximum Absolute Volume）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.4\_类型定义（Typedefs）

<a id="r_gab9bd888ef5443bd0a3d34a34b972f409"></a>

```c
typedef void(* bt_avrcp_notify_changed_cb_t) (struct bt_avrcp_ct *ct, uint8_t event_id, struct bt_avrcp_event_data *data)
```

相关声明：[bt_avrcp_notify_changed_cb_t](#gab9bd888ef5443bd0a3d34a34b972f409)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)。

AVRCP 事件通知回调（Event Notification Callback），仅用于 CHANGED 通知。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.5\_枚举（Enumerations）

<a id="r_gac311dc7b5f99162b954271529eeb84ea"></a>

```c
enum bt_avrcp_cap_t { BT_AVRCP_CAP_COMPANY_ID = 0x2 , BT_AVRCP_CAP_EVENTS_SUPPORTED = 0x3 }
```

相关声明：[bt_avrcp_cap_t](#gac311dc7b5f99162b954271529eeb84ea)、[BT_AVRCP_CAP_COMPANY_ID](#ggac311dc7b5f99162b954271529eeb84eaa89fecce56afb09791a2253a7ad840430)、[BT_AVRCP_CAP_EVENTS_SUPPORTED](#ggac311dc7b5f99162b954271529eeb84eaa2a7b326aded772c09cf01387145d2802)。

AVRCP 能力标识符（Capability ID）。

<a id="r_gaf55aae17f67a1361279ae208b17e4a75"></a>

```c
enum bt_avrcp_evt_t { BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED = 0x01 , BT_AVRCP_EVT_TRACK_CHANGED = 0x02 , BT_AVRCP_EVT_TRACK_REACHED_END = 0x03 , BT_AVRCP_EVT_TRACK_REACHED_START = 0x04 , BT_AVRCP_EVT_PLAYBACK_POS_CHANGED = 0x05 , BT_AVRCP_EVT_BATT_STATUS_CHANGED = 0x06 , BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED = 0x07 , BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED = 0x08 , BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED = 0x09 , BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED = 0x0a , BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED = 0x0b , BT_AVRCP_EVT_UIDS_CHANGED = 0x0c , BT_AVRCP_EVT_VOLUME_CHANGED = 0x0d }
```

相关声明：[bt_avrcp_evt_t](#gaf55aae17f67a1361279ae208b17e4a75)、[BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75a892f2928d634b675426f2fe597a45f6d)、[BT_AVRCP_EVT_TRACK_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75a25f8e3e08b5988e833eb0d47452d12a9)、[BT_AVRCP_EVT_TRACK_REACHED_END](#ggaf55aae17f67a1361279ae208b17e4a75a412a9b7cbb891bc50fb77c1e6de9faaf)、[BT_AVRCP_EVT_TRACK_REACHED_START](#ggaf55aae17f67a1361279ae208b17e4a75af4f9e221522cd57461920d22e7a290b9)、[BT_AVRCP_EVT_PLAYBACK_POS_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75afc4ef6f8a80a9067ad9dfd30bf2a6958)、[BT_AVRCP_EVT_BATT_STATUS_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75a9ff1d99bc0c83399961ef23d4a75f9b6)、[BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75ae6237555b0051b2395e0bf2287e954c1)、[BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75ab2b2287a0db9be97af8c20298bebba2d)、[BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75ac0b720defdd8716d757e0c8a7e57db83)、[BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75abd82dd6ba6d5d76cf22a8c703c76c6e0)、[BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75ab6fdeacb536067660f754b3c586e073a)、[BT_AVRCP_EVT_UIDS_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75a8ac593400cda085fbdff36e403bd2a91)、[BT_AVRCP_EVT_VOLUME_CHANGED](#ggaf55aae17f67a1361279ae208b17e4a75a8d526498fdcb1380e8e3944da2a5ef85)。

AVRCP 通知事件（Notification Events）。

<a id="r_ga2a4c610e00ba9832f954f30bd6b6618e"></a>

```c
enum bt_avrcp_ctype_t { BT_AVRCP_CTYPE_CONTROL = 0x0 , BT_AVRCP_CTYPE_STATUS = 0x1 , BT_AVRCP_CTYPE_SPECIFIC_INQUIRY = 0x2 , BT_AVRCP_CTYPE_NOTIFY = 0x3 , BT_AVRCP_CTYPE_GENERAL_INQUIRY = 0x4 }
```

相关声明：[bt_avrcp_ctype_t](#ga2a4c610e00ba9832f954f30bd6b6618e)、[BT_AVRCP_CTYPE_CONTROL](#gga2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04)、[BT_AVRCP_CTYPE_STATUS](#gga2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce)、[BT_AVRCP_CTYPE_SPECIFIC_INQUIRY](#gga2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb)、[BT_AVRCP_CTYPE_NOTIFY](#gga2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290)、[BT_AVRCP_CTYPE_GENERAL_INQUIRY](#gga2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7)。

音视频控制（AV/C）命令类型（Command Types）。

<a id="r_gaba2d8faec2c3baf7403199ea8a509326"></a>

```c
enum bt_avrcp_rsp_t { BT_AVRCP_RSP_NOT_IMPLEMENTED = 0x8 , BT_AVRCP_RSP_ACCEPTED = 0x9 , BT_AVRCP_RSP_REJECTED = 0xa , BT_AVRCP_RSP_IN_TRANSITION = 0xb , BT_AVRCP_RSP_IMPLEMENTED = 0xc , BT_AVRCP_RSP_STABLE = 0xc , BT_AVRCP_RSP_CHANGED = 0xd , BT_AVRCP_RSP_INTERIM = 0xf }
```

相关声明：[bt_avrcp_rsp_t](#gaba2d8faec2c3baf7403199ea8a509326)、[BT_AVRCP_RSP_NOT_IMPLEMENTED](#ggaba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696)、[BT_AVRCP_RSP_ACCEPTED](#ggaba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8)、[BT_AVRCP_RSP_REJECTED](#ggaba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c)、[BT_AVRCP_RSP_IN_TRANSITION](#ggaba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad)、[BT_AVRCP_RSP_IMPLEMENTED](#ggaba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144)、[BT_AVRCP_RSP_STABLE](#ggaba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992)、[BT_AVRCP_RSP_CHANGED](#ggaba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988)、[BT_AVRCP_RSP_INTERIM](#ggaba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88)。

音视频控制（AV/C）响应码（Response Codes）。

<a id="r_ga78ba828636b731b2c43e088a581bfee9"></a>

```c
enum bt_avrcp_subunit_type_t { BT_AVRCP_SUBUNIT_TYPE_PANEL = 0x09 , BT_AVRCP_SUBUNIT_TYPE_UNIT = 0x1f }
```

相关声明：[bt_avrcp_subunit_type_t](#ga78ba828636b731b2c43e088a581bfee9)、[BT_AVRCP_SUBUNIT_TYPE_PANEL](#gga78ba828636b731b2c43e088a581bfee9a6db3104fa9727594b842b4ae9b64a605)、[BT_AVRCP_SUBUNIT_TYPE_UNIT](#gga78ba828636b731b2c43e088a581bfee9a8be8c211cd26a849c1c89e482aa10030)。

音视频控制（AV/C）子单元类型（Subunit Type），也用于单元类型（Unit Type）。

<a id="r_ga3c997d96028343a0a5a4948dabe19b84"></a>

```c
enum bt_avrcp_opid_t { BT_AVRCP_OPID_SELECT = 0x00 , BT_AVRCP_OPID_UP = 0x01 , BT_AVRCP_OPID_DOWN = 0x02 , BT_AVRCP_OPID_LEFT = 0x03 , BT_AVRCP_OPID_RIGHT = 0x04 , BT_AVRCP_OPID_RIGHT_UP = 0x05 , BT_AVRCP_OPID_RIGHT_DOWN = 0x06 , BT_AVRCP_OPID_LEFT_UP = 0x07 , BT_AVRCP_OPID_LEFT_DOWN = 0x08 , BT_AVRCP_OPID_ROOT_MENU = 0x09 , BT_AVRCP_OPID_SETUP_MENU = 0x0a , BT_AVRCP_OPID_CONTENTS_MENU = 0x0b , BT_AVRCP_OPID_FAVORITE_MENU = 0x0c , BT_AVRCP_OPID_EXIT = 0x0d , BT_AVRCP_OPID_0 = 0x20 , BT_AVRCP_OPID_1 = 0x21 , BT_AVRCP_OPID_2 = 0x22 , BT_AVRCP_OPID_3 = 0x23 , BT_AVRCP_OPID_4 = 0x24 , BT_AVRCP_OPID_5 = 0x25 , BT_AVRCP_OPID_6 = 0x26 , BT_AVRCP_OPID_7 = 0x27 , BT_AVRCP_OPID_8 = 0x28 , BT_AVRCP_OPID_9 = 0x29 , BT_AVRCP_OPID_DOT = 0x2a , BT_AVRCP_OPID_ENTER = 0x2b , BT_AVRCP_OPID_CLEAR = 0x2c , BT_AVRCP_OPID_CHANNEL_UP = 0x30 , BT_AVRCP_OPID_CHANNEL_DOWN = 0x31 , BT_AVRCP_OPID_PREVIOUS_CHANNEL = 0x32 , BT_AVRCP_OPID_SOUND_SELECT = 0x33 , BT_AVRCP_OPID_INPUT_SELECT = 0x34 , BT_AVRCP_OPID_DISPLAY_INFORMATION = 0x35 , BT_AVRCP_OPID_HELP = 0x36 , BT_AVRCP_OPID_PAGE_UP = 0x37 , BT_AVRCP_OPID_PAGE_DOWN = 0x38 , BT_AVRCP_OPID_POWER = 0x40 , BT_AVRCP_OPID_VOLUME_UP = 0x41 , BT_AVRCP_OPID_VOLUME_DOWN = 0x42 , BT_AVRCP_OPID_MUTE = 0x43 , BT_AVRCP_OPID_PLAY = 0x44 , BT_AVRCP_OPID_STOP = 0x45 , BT_AVRCP_OPID_PAUSE = 0x46 , BT_AVRCP_OPID_RECORD = 0x47 , BT_AVRCP_OPID_REWIND = 0x48 , BT_AVRCP_OPID_FAST_FORWARD = 0x49 , BT_AVRCP_OPID_EJECT = 0x4a , BT_AVRCP_OPID_FORWARD = 0x4b , BT_AVRCP_OPID_BACKWARD = 0x4c , BT_AVRCP_OPID_ANGLE = 0x50 , BT_AVRCP_OPID_SUBPICTURE = 0x51 , BT_AVRCP_OPID_F1 = 0x71 , BT_AVRCP_OPID_F2 = 0x72 , BT_AVRCP_OPID_F3 = 0x73 , BT_AVRCP_OPID_F4 = 0x74 , BT_AVRCP_OPID_F5 = 0x75 , BT_AVRCP_OPID_VENDOR_UNIQUE = 0x7e }
```

相关声明：[bt_avrcp_opid_t](#ga3c997d96028343a0a5a4948dabe19b84)、[BT_AVRCP_OPID_SELECT](#gga3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f)、[BT_AVRCP_OPID_UP](#gga3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9)、[BT_AVRCP_OPID_DOWN](#gga3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537)、[BT_AVRCP_OPID_LEFT](#gga3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba)、[BT_AVRCP_OPID_RIGHT](#gga3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2)、[BT_AVRCP_OPID_RIGHT_UP](#gga3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63)、[BT_AVRCP_OPID_RIGHT_DOWN](#gga3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745)、[BT_AVRCP_OPID_LEFT_UP](#gga3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779)、[BT_AVRCP_OPID_LEFT_DOWN](#gga3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366)、[BT_AVRCP_OPID_ROOT_MENU](#gga3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87)、[BT_AVRCP_OPID_SETUP_MENU](#gga3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372)、[BT_AVRCP_OPID_CONTENTS_MENU](#gga3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472)、[BT_AVRCP_OPID_FAVORITE_MENU](#gga3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574)、[BT_AVRCP_OPID_EXIT](#gga3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3)、[BT_AVRCP_OPID_0](#gga3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade)、[BT_AVRCP_OPID_1](#gga3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0)、[BT_AVRCP_OPID_2](#gga3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566)、[BT_AVRCP_OPID_3](#gga3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459)、[BT_AVRCP_OPID_4](#gga3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c)、[BT_AVRCP_OPID_5](#gga3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5)、[BT_AVRCP_OPID_6](#gga3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a)、[BT_AVRCP_OPID_7](#gga3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff)、[BT_AVRCP_OPID_8](#gga3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06)、[BT_AVRCP_OPID_9](#gga3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb)、[BT_AVRCP_OPID_DOT](#gga3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf)、[BT_AVRCP_OPID_ENTER](#gga3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae)、[BT_AVRCP_OPID_CLEAR](#gga3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2)、[BT_AVRCP_OPID_CHANNEL_UP](#gga3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586)、[BT_AVRCP_OPID_CHANNEL_DOWN](#gga3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de)、[BT_AVRCP_OPID_PREVIOUS_CHANNEL](#gga3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e)、[BT_AVRCP_OPID_SOUND_SELECT](#gga3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b)、[BT_AVRCP_OPID_INPUT_SELECT](#gga3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c)、[BT_AVRCP_OPID_DISPLAY_INFORMATION](#gga3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef)、[BT_AVRCP_OPID_HELP](#gga3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b)、[BT_AVRCP_OPID_PAGE_UP](#gga3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321)、[BT_AVRCP_OPID_PAGE_DOWN](#gga3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a)、[BT_AVRCP_OPID_POWER](#gga3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358)、[BT_AVRCP_OPID_VOLUME_UP](#gga3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487)、[BT_AVRCP_OPID_VOLUME_DOWN](#gga3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62)、[BT_AVRCP_OPID_MUTE](#gga3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1)、[BT_AVRCP_OPID_PLAY](#gga3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b)、[BT_AVRCP_OPID_STOP](#gga3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60)、[BT_AVRCP_OPID_PAUSE](#gga3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a)、[BT_AVRCP_OPID_RECORD](#gga3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27)、[BT_AVRCP_OPID_REWIND](#gga3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8)、[BT_AVRCP_OPID_FAST_FORWARD](#gga3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f)、[BT_AVRCP_OPID_EJECT](#gga3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344)、[BT_AVRCP_OPID_FORWARD](#gga3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e)、[BT_AVRCP_OPID_BACKWARD](#gga3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23)、[BT_AVRCP_OPID_ANGLE](#gga3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2)、[BT_AVRCP_OPID_SUBPICTURE](#gga3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98)、[BT_AVRCP_OPID_F1](#gga3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5)、[BT_AVRCP_OPID_F2](#gga3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4)、[BT_AVRCP_OPID_F3](#gga3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40)、[BT_AVRCP_OPID_F4](#gga3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283)、[BT_AVRCP_OPID_F5](#gga3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d)、[BT_AVRCP_OPID_VENDOR_UNIQUE](#gga3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d)。

AVRCP 透传命令（Passthrough Commands）使用的 AV/C 操作标识符（Operation IDs）。

<a id="r_ga15f9f868b056f17ea12d96530b7da881"></a>

```c
enum bt_avrcp_button_state_t { BT_AVRCP_BUTTON_PRESSED = 0 , BT_AVRCP_BUTTON_RELEASED = 1 }
```

相关声明：[bt_avrcp_button_state_t](#ga15f9f868b056f17ea12d96530b7da881)、[BT_AVRCP_BUTTON_PRESSED](#gga15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3)、[BT_AVRCP_BUTTON_RELEASED](#gga15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706)。

AVRCP 按钮状态标志（Button State Flag）。

<a id="r_ga52368f4cc655bab75f96da80ddaaabe0"></a>

```c
enum bt_avrcp_status_t { BT_AVRCP_STATUS_INVALID_COMMAND = 0x00 , BT_AVRCP_STATUS_INVALID_PARAMETER = 0x01 , BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR = 0x02 , BT_AVRCP_STATUS_INTERNAL_ERROR = 0x03 , BT_AVRCP_STATUS_OPERATION_COMPLETED = 0x04 , BT_AVRCP_STATUS_UID_CHANGED = 0x05 , BT_AVRCP_STATUS_INVALID_DIRECTION = 0x07 , BT_AVRCP_STATUS_NOT_A_DIRECTORY = 0x08 , BT_AVRCP_STATUS_DOES_NOT_EXIST = 0x09 , BT_AVRCP_STATUS_INVALID_SCOPE = 0x0a , BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS = 0x0b , BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE = 0x0c , BT_AVRCP_STATUS_MEDIA_IN_USE = 0x0d , BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL = 0x0e , BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED = 0x0f , BT_AVRCP_STATUS_SEARCH_IN_PROGRESS = 0x10 , BT_AVRCP_STATUS_INVALID_PLAYER_ID = 0x11 , BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE = 0x12 , BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED = 0x13 , BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS = 0x14 , BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS = 0x15 , BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED = 0x16 , BT_AVRCP_STATUS_IN_TRANSITION = 0xfd , BT_AVRCP_STATUS_NOT_IMPLEMENTED = 0xfe , BT_AVRCP_STATUS_SUCCESS = BT_AVRCP_STATUS_OPERATION_COMPLETED }
```

相关声明：[bt_avrcp_status_t](#ga52368f4cc655bab75f96da80ddaaabe0)、[BT_AVRCP_STATUS_INVALID_COMMAND](#gga52368f4cc655bab75f96da80ddaaabe0a14e183c33a64cdac271ee7f320796bd6)、[BT_AVRCP_STATUS_INVALID_PARAMETER](#gga52368f4cc655bab75f96da80ddaaabe0a8a767466ac8069e20f6d9e0f30c33420)、[BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR](#gga52368f4cc655bab75f96da80ddaaabe0a7cba04973b3753b50f63e6b0bc205638)、[BT_AVRCP_STATUS_INTERNAL_ERROR](#gga52368f4cc655bab75f96da80ddaaabe0af48dcc2c65e4af461c1a6ece622a2f5a)、[BT_AVRCP_STATUS_OPERATION_COMPLETED](#gga52368f4cc655bab75f96da80ddaaabe0ad3a41ce04f27cc349c7466aae18bcee2)、[BT_AVRCP_STATUS_UID_CHANGED](#gga52368f4cc655bab75f96da80ddaaabe0a0e77e1782b5a0f88f4d45b6560df2b09)、[BT_AVRCP_STATUS_INVALID_DIRECTION](#gga52368f4cc655bab75f96da80ddaaabe0a448e1c0383e4e4b5fc3c0c80e2040af9)、[BT_AVRCP_STATUS_NOT_A_DIRECTORY](#gga52368f4cc655bab75f96da80ddaaabe0a6fee8c927f897fff59b7690c3e1732c2)、[BT_AVRCP_STATUS_DOES_NOT_EXIST](#gga52368f4cc655bab75f96da80ddaaabe0a9f552377c6bb93b3e52b29228a6feaa5)、[BT_AVRCP_STATUS_INVALID_SCOPE](#gga52368f4cc655bab75f96da80ddaaabe0aaddaf4f6439aa6a52e3a4fdbb3f0c071)、[BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS](#gga52368f4cc655bab75f96da80ddaaabe0a81094560261826c16be6ebba9d99081c)、[BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE](#gga52368f4cc655bab75f96da80ddaaabe0a2f8ca7c1fe4ba52a1a418612c094158a)、[BT_AVRCP_STATUS_MEDIA_IN_USE](#gga52368f4cc655bab75f96da80ddaaabe0ae63cf3ffada01f268498151d88c3a3ec)、[BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL](#gga52368f4cc655bab75f96da80ddaaabe0a359810fbbdf875adb89a192deaae6a6d)、[BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED](#gga52368f4cc655bab75f96da80ddaaabe0a4ee781cc845d8b1211217f8338b97023)、[BT_AVRCP_STATUS_SEARCH_IN_PROGRESS](#gga52368f4cc655bab75f96da80ddaaabe0a402038758703ee9f8543ad546681a3c5)、[BT_AVRCP_STATUS_INVALID_PLAYER_ID](#gga52368f4cc655bab75f96da80ddaaabe0a5cd415ba8d307dc5153a9a0b2f9958e3)、[BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE](#gga52368f4cc655bab75f96da80ddaaabe0a28925d094d4c3e55b259a55440a5c044)、[BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED](#gga52368f4cc655bab75f96da80ddaaabe0a3dfa01e069c517e7e466fa6edcc1c9cb)、[BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS](#gga52368f4cc655bab75f96da80ddaaabe0a033e10d03bf56df95ec1e888a07cedf9)、[BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS](#gga52368f4cc655bab75f96da80ddaaabe0a5544c22cad94dadb9eccf47669fabafb)、[BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED](#gga52368f4cc655bab75f96da80ddaaabe0a43e59407a44f87d85fa71cdb627524e3)、[BT_AVRCP_STATUS_IN_TRANSITION](#gga52368f4cc655bab75f96da80ddaaabe0af72a55b60fda9c157cdef8b1c6038780)、[BT_AVRCP_STATUS_NOT_IMPLEMENTED](#gga52368f4cc655bab75f96da80ddaaabe0a14868dd213f59e09dbdb066d5ca39c96)、[BT_AVRCP_STATUS_SUCCESS](#gga52368f4cc655bab75f96da80ddaaabe0afbff25149bb9c35756dfb7bb6f2516c3)。

AVRCP 状态码与错误码（Status and Error Codes）。

<a id="r_ga81330413af9eba049da6557b14ae082c"></a>

```c
enum bt_avrcp_charset_t { BT_AVRCP_CHARSET_UTF8 = 0x006a }
```

相关声明：[bt_avrcp_charset_t](#ga81330413af9eba049da6557b14ae082c)、[BT_AVRCP_CHARSET_UTF8](#gga81330413af9eba049da6557b14ae082ca29f70165632222ae40ac3e44554130b0)。

AVRCP 字符集标识符（Character Set IDs）。

<a id="r_gaabab9a4f37b3f9653ca95dd4b5944707"></a>

```c
enum bt_avrcp_scope_t { BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST = 0x00 , BT_AVRCP_SCOPE_VFS = 0x01 , BT_AVRCP_SCOPE_SEARCH = 0x02 , BT_AVRCP_SCOPE_NOW_PLAYING = 0x03 }
```

相关声明：[bt_avrcp_scope_t](#gaabab9a4f37b3f9653ca95dd4b5944707)、[BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST](#ggaabab9a4f37b3f9653ca95dd4b5944707a7a388bb84fbe14f8931ab9bf41b9823d)、[BT_AVRCP_SCOPE_VFS](#ggaabab9a4f37b3f9653ca95dd4b5944707a37002574948081d7b42001a62755636b)、[BT_AVRCP_SCOPE_SEARCH](#ggaabab9a4f37b3f9653ca95dd4b5944707a4db7699a5f22c8d5986f6f1ba7219dac)、[BT_AVRCP_SCOPE_NOW_PLAYING](#ggaabab9a4f37b3f9653ca95dd4b5944707a7baa6442aafc4d00635df52f44d0d608)。

AVRCP 范围值（Scope Values）。

<a id="r_ga02d67e84b4a48ebecf3b307cbd4bb61c"></a>

```c
enum bt_avrcp_change_path_t { BT_AVRCP_CHANGE_PATH_PARENT = 0x00 , BT_AVRCP_CHANGE_PATH_CHILD = 0x01 }
```

相关声明：[bt_avrcp_change_path_t](#ga02d67e84b4a48ebecf3b307cbd4bb61c)、[BT_AVRCP_CHANGE_PATH_PARENT](#gga02d67e84b4a48ebecf3b307cbd4bb61ca8914559b14b7529fc5f1df764036748d)、[BT_AVRCP_CHANGE_PATH_CHILD](#gga02d67e84b4a48ebecf3b307cbd4bb61ca5cbd84478163171359044825050dd172)。

AVRCP 更改路径方向（ChangePath Direction）。

<a id="r_ga09d191c490efcfb9f8139975090be0d5"></a>

```c
enum bt_avrcp_folder_type_t { BT_AVRCP_FOLDER_TYPE_MIXED = 0x00 , BT_AVRCP_FOLDER_TYPE_TITLES = 0x01 , BT_AVRCP_FOLDER_TYPE_ALBUMS = 0x02 , BT_AVRCP_FOLDER_TYPE_ARTISTS = 0x03 , BT_AVRCP_FOLDER_TYPE_GENRES = 0x04 , BT_AVRCP_FOLDER_TYPE_PLAYLISTS = 0x05 , BT_AVRCP_FOLDER_TYPE_YEARS = 0x06 }
```

相关声明：[bt_avrcp_folder_type_t](#ga09d191c490efcfb9f8139975090be0d5)、[BT_AVRCP_FOLDER_TYPE_MIXED](#gga09d191c490efcfb9f8139975090be0d5a06308eb3786579cf5aeb0f19f0ab37ac)、[BT_AVRCP_FOLDER_TYPE_TITLES](#gga09d191c490efcfb9f8139975090be0d5a702f9974cf5d51a77757fd7e1ef4ab0f)、[BT_AVRCP_FOLDER_TYPE_ALBUMS](#gga09d191c490efcfb9f8139975090be0d5ab33fca5f57f5b80785df367ab788a8fc)、[BT_AVRCP_FOLDER_TYPE_ARTISTS](#gga09d191c490efcfb9f8139975090be0d5a89aaeb11e807c44479ff47164d99c4f7)、[BT_AVRCP_FOLDER_TYPE_GENRES](#gga09d191c490efcfb9f8139975090be0d5a0ab0ffb986db900ece2146a347dae06d)、[BT_AVRCP_FOLDER_TYPE_PLAYLISTS](#gga09d191c490efcfb9f8139975090be0d5a708dfb5de11ae783b413d2d99202f9b5)、[BT_AVRCP_FOLDER_TYPE_YEARS](#gga09d191c490efcfb9f8139975090be0d5a0a60cb99cd19d203618b1264e2a3cca6)。

AVRCP 文件夹类型（Folder Types），用于文件夹条目。

<a id="r_gac927c7e7c59f6f0e6243ca0887945d5a"></a>

```c
enum bt_avrcp_media_type_t { BT_AVRCP_MEDIA_TYPE_AUDIO = 0x00 , BT_AVRCP_MEDIA_TYPE_VIDEO = 0x01 }
```

相关声明：[bt_avrcp_media_type_t](#gac927c7e7c59f6f0e6243ca0887945d5a)、[BT_AVRCP_MEDIA_TYPE_AUDIO](#ggac927c7e7c59f6f0e6243ca0887945d5aa9847baed2a6d09d4ac81039c7302832b)、[BT_AVRCP_MEDIA_TYPE_VIDEO](#ggac927c7e7c59f6f0e6243ca0887945d5aa76bd7c8c80d6ad9985430148cfd44e82)。

AVRCP 媒体类型（Media Types），用于媒体元素条目。

<a id="r_ga0ebc5d2657688b70119e11ac20d24592"></a>

```c
enum bt_avrcp_media_attr_id_t { BT_AVRCP_MEDIA_ATTR_ID_TITLE = 0x01 , BT_AVRCP_MEDIA_ATTR_ID_ARTIST = 0x02 , BT_AVRCP_MEDIA_ATTR_ID_ALBUM = 0x03 , BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER = 0x04 , BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS = 0x05 , BT_AVRCP_MEDIA_ATTR_ID_GENRE = 0x06 , BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME = 0x07 , BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART = 0x08 }
```

相关声明：[bt_avrcp_media_attr_id_t](#ga0ebc5d2657688b70119e11ac20d24592)、[BT_AVRCP_MEDIA_ATTR_ID_TITLE](#gga0ebc5d2657688b70119e11ac20d24592acce73266473e0a14580fa337d2fe53b3)、[BT_AVRCP_MEDIA_ATTR_ID_ARTIST](#gga0ebc5d2657688b70119e11ac20d24592a436c4847edcad7121f7d2ed97169fe61)、[BT_AVRCP_MEDIA_ATTR_ID_ALBUM](#gga0ebc5d2657688b70119e11ac20d24592a2b7e8439c8050cdeda97c43d07774001)、[BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER](#gga0ebc5d2657688b70119e11ac20d24592ac66e18f0843901209f9004a62ab55624)、[BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS](#gga0ebc5d2657688b70119e11ac20d24592a3dcfd47034d7890e80a05fd4f600f6bf)、[BT_AVRCP_MEDIA_ATTR_ID_GENRE](#gga0ebc5d2657688b70119e11ac20d24592a8fd312d2869f38b6d7446716a30392b1)、[BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME](#gga0ebc5d2657688b70119e11ac20d24592a0ba1f760a733cd00923970d01bb85293)、[BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART](#gga0ebc5d2657688b70119e11ac20d24592a958ef736372f39d8e180f8fdeb025121)。

AVRCP 媒体属性标识符（Media Attribute IDs）。

<a id="r_gac02fed37e267996d4de50b06292d0668"></a>

```c
enum bt_avrcp_item_type_t { BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER = 0x01 , BT_AVRCP_ITEM_TYPE_FOLDER = 0x02 , BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT = 0x03 }
```

相关声明：[bt_avrcp_item_type_t](#gac02fed37e267996d4de50b06292d0668)、[BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER](#ggac02fed37e267996d4de50b06292d0668ad8dd8a59776d9d29655cbd083fae6535)、[BT_AVRCP_ITEM_TYPE_FOLDER](#ggac02fed37e267996d4de50b06292d0668aeb7289d0102af72c607d42a8f1c6dfa5)、[BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT](#ggac02fed37e267996d4de50b06292d0668aca944e6647d353290b4e5c25fde28bd8)。

AVRCP 条目类型（Item Types），用于浏览操作 GetFolderItems 等。

<a id="r_ga433775fa2758df43ee1d26c78e9122d1"></a>

```c
enum bt_avrcp_playback_status_t { BT_AVRCP_PLAYBACK_STATUS_STOPPED = 0x00 , BT_AVRCP_PLAYBACK_STATUS_PLAYING = 0x01 , BT_AVRCP_PLAYBACK_STATUS_PAUSED = 0x02 , BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK = 0x03 , BT_AVRCP_PLAYBACK_STATUS_REV_SEEK = 0x04 , BT_AVRCP_PLAYBACK_STATUS_ERROR = 0xff }
```

相关声明：[bt_avrcp_playback_status_t](#ga433775fa2758df43ee1d26c78e9122d1)、[BT_AVRCP_PLAYBACK_STATUS_STOPPED](#gga433775fa2758df43ee1d26c78e9122d1a71ddb79b742f9acbd5d14a7639a09fe8)、[BT_AVRCP_PLAYBACK_STATUS_PLAYING](#gga433775fa2758df43ee1d26c78e9122d1ae620f45ad0ecb63be8a8a0b446b5817a)、[BT_AVRCP_PLAYBACK_STATUS_PAUSED](#gga433775fa2758df43ee1d26c78e9122d1a2509a9b77091db4ff185448d17d44244)、[BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK](#gga433775fa2758df43ee1d26c78e9122d1ab97050ae05ba6cdff052ac6181eed119)、[BT_AVRCP_PLAYBACK_STATUS_REV_SEEK](#gga433775fa2758df43ee1d26c78e9122d1a5dedf3d49340e3371b118215414aa8d8)、[BT_AVRCP_PLAYBACK_STATUS_ERROR](#gga433775fa2758df43ee1d26c78e9122d1a05cd93eef7ee39f8e7111d23131de6de)。

AVRCP 播放状态（Playback Status）。

<a id="r_ga128458626d5fe6ffbac7cf97867621aa"></a>

```c
enum bt_avrcp_system_status_t { BT_AVRCP_SYSTEM_STATUS_POWER_ON = 0x00 , BT_AVRCP_SYSTEM_STATUS_POWER_OFF = 0x01 , BT_AVRCP_SYSTEM_STATUS_UNPLUGGED = 0x02 }
```

相关声明：[bt_avrcp_system_status_t](#ga128458626d5fe6ffbac7cf97867621aa)、[BT_AVRCP_SYSTEM_STATUS_POWER_ON](#gga128458626d5fe6ffbac7cf97867621aaaea875986bd59d1da9650c5d5f2de20a2)、[BT_AVRCP_SYSTEM_STATUS_POWER_OFF](#gga128458626d5fe6ffbac7cf97867621aaa4d4a454f0b8a0a84b557a4075eff1215)、[BT_AVRCP_SYSTEM_STATUS_UNPLUGGED](#gga128458626d5fe6ffbac7cf97867621aaa1e1ed998f24038e6095f802144e240c2)。

AVRCP 系统状态码（System Status Code）。

<a id="r_ga33825b183b12a2b29d5148a7366c0e77"></a>

```c
enum bt_avrcp_battery_status_t { BT_AVRCP_BATTERY_STATUS_NORMAL = 0x00 , BT_AVRCP_BATTERY_STATUS_WARNING = 0x01 , BT_AVRCP_BATTERY_STATUS_CRITICAL = 0x02 , BT_AVRCP_BATTERY_STATUS_EXTERNAL = 0x03 , BT_AVRCP_BATTERY_STATUS_FULL = 0x04 }
```

相关声明：[bt_avrcp_battery_status_t](#ga33825b183b12a2b29d5148a7366c0e77)、[BT_AVRCP_BATTERY_STATUS_NORMAL](#gga33825b183b12a2b29d5148a7366c0e77aeaba1597c6c1854d46df1eaaff8862a2)、[BT_AVRCP_BATTERY_STATUS_WARNING](#gga33825b183b12a2b29d5148a7366c0e77a4f7cb6c1917180ca96b10d2c73df9fad)、[BT_AVRCP_BATTERY_STATUS_CRITICAL](#gga33825b183b12a2b29d5148a7366c0e77adafb0292944a3d4236608ca13d900c98)、[BT_AVRCP_BATTERY_STATUS_EXTERNAL](#gga33825b183b12a2b29d5148a7366c0e77a2883875f5d5441e7eb7976a38573c178)、[BT_AVRCP_BATTERY_STATUS_FULL](#gga33825b183b12a2b29d5148a7366c0e77a72880bd811f5cf87fedfa0ff006412b4)。

AVRCP 电池状态码（Battery Status Code）。

<a id="r_ga8047dddc873566ee372e77c6eecd008f"></a>

```c
enum bt_avrcp_player_attr_id_t { BT_AVRCP_PLAYER_ATTR_EQUALIZER = 0x01 , BT_AVRCP_PLAYER_ATTR_REPEAT_MODE = 0x02 , BT_AVRCP_PLAYER_ATTR_SHUFFLE = 0x03 , BT_AVRCP_PLAYER_ATTR_SCAN = 0x04 }
```

相关声明：[bt_avrcp_player_attr_id_t](#ga8047dddc873566ee372e77c6eecd008f)、[BT_AVRCP_PLAYER_ATTR_EQUALIZER](#gga8047dddc873566ee372e77c6eecd008fa226313d1f90779c47142ba4966ee968f)、[BT_AVRCP_PLAYER_ATTR_REPEAT_MODE](#gga8047dddc873566ee372e77c6eecd008fa4cfad017fc5870b099a8d4521e422dca)、[BT_AVRCP_PLAYER_ATTR_SHUFFLE](#gga8047dddc873566ee372e77c6eecd008fa278d43d52aa33cb54705e7d75ddd98b7)、[BT_AVRCP_PLAYER_ATTR_SCAN](#gga8047dddc873566ee372e77c6eecd008fa4157b63056caa15282fab2712a855cec)。

AVRCP 播放器应用设置属性标识符（Player Application Setting Attribute IDs）。

<a id="r_gae76f2666d10e6f46a1e5d68327fc7607"></a>

```c
enum bt_avrcp_equalizer_value_t { BT_AVRCP_EQUALIZER_OFF = 0x01 , BT_AVRCP_EQUALIZER_ON = 0x02 }
```

相关声明：[bt_avrcp_equalizer_value_t](#gae76f2666d10e6f46a1e5d68327fc7607)、[BT_AVRCP_EQUALIZER_OFF](#ggae76f2666d10e6f46a1e5d68327fc7607a31587fdac3ae979f111287a924115d4a)、[BT_AVRCP_EQUALIZER_ON](#ggae76f2666d10e6f46a1e5d68327fc7607aed029088c6bb73d0928ec19b9029e95e)。

AVRCP 播放器应用的均衡器设置值（Player Application Setting Values for Equalizer）。

<a id="r_ga22bf1b16b383ef473624769ae6ae893a"></a>

```c
enum bt_avrcp_repeat_mode_value_t { BT_AVRCP_REPEAT_MODE_OFF = 0x01 , BT_AVRCP_REPEAT_MODE_SINGLE_TRACK = 0x02 , BT_AVRCP_REPEAT_MODE_ALL_TRACKS = 0x03 , BT_AVRCP_REPEAT_MODE_GROUP = 0x04 }
```

相关声明：[bt_avrcp_repeat_mode_value_t](#ga22bf1b16b383ef473624769ae6ae893a)、[BT_AVRCP_REPEAT_MODE_OFF](#gga22bf1b16b383ef473624769ae6ae893aa4192bdec6c45e76769ca55ee6a3ab190)、[BT_AVRCP_REPEAT_MODE_SINGLE_TRACK](#gga22bf1b16b383ef473624769ae6ae893aa24914c843056b7fc58f534aec1693948)、[BT_AVRCP_REPEAT_MODE_ALL_TRACKS](#gga22bf1b16b383ef473624769ae6ae893aabf4b962a513c908baa7fac9454511aaa)、[BT_AVRCP_REPEAT_MODE_GROUP](#gga22bf1b16b383ef473624769ae6ae893aa926fe6e1fc4fee9bb108c9b0c2e46c9a)。

AVRCP 播放器应用的重复模式设置值（Player Application Setting Values for Repeat Mode）。

<a id="r_ga8e6ce46ba46268c2c80f4ec7570859c8"></a>

```c
enum bt_avrcp_shuffle_value_t { BT_AVRCP_SHUFFLE_OFF = 0x01 , BT_AVRCP_SHUFFLE_ALL_TRACKS = 0x02 , BT_AVRCP_SHUFFLE_GROUP = 0x03 }
```

相关声明：[bt_avrcp_shuffle_value_t](#ga8e6ce46ba46268c2c80f4ec7570859c8)、[BT_AVRCP_SHUFFLE_OFF](#gga8e6ce46ba46268c2c80f4ec7570859c8aac7dce4d43e84c3d80f9eb0791db7a8d)、[BT_AVRCP_SHUFFLE_ALL_TRACKS](#gga8e6ce46ba46268c2c80f4ec7570859c8ab36d34793768772409794570f740964a)、[BT_AVRCP_SHUFFLE_GROUP](#gga8e6ce46ba46268c2c80f4ec7570859c8a11a1b2613018ad24861a72313af4189a)。

AVRCP 播放器应用的随机播放设置值（Player Application Setting Values for Shuffle）。

<a id="r_ga4426612c49f8456f2543f373db72d3f2"></a>

```c
enum bt_avrcp_scan_value_t { BT_AVRCP_SCAN_OFF = 0x01 , BT_AVRCP_SCAN_ALL_TRACKS = 0x02 , BT_AVRCP_SCAN_GROUP = 0x03 }
```

相关声明：[bt_avrcp_scan_value_t](#ga4426612c49f8456f2543f373db72d3f2)、[BT_AVRCP_SCAN_OFF](#gga4426612c49f8456f2543f373db72d3f2ae12700ce9b55f758572b0fbfab18ea90)、[BT_AVRCP_SCAN_ALL_TRACKS](#gga4426612c49f8456f2543f373db72d3f2a0819f5ffd937f0d4a379ae5e7b9a2ebf)、[BT_AVRCP_SCAN_GROUP](#gga4426612c49f8456f2543f373db72d3f2abde23c31bbb6ab1c7daf85e3cd977cf9)。

AVRCP 播放器应用的扫描设置值（Player Application Setting Values for Scan）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.6\_函数（Functions）

<a id="r_ga6a212dd4765adc82eda6e35cd9742f0c"></a>

```c
int bt_avrcp_connect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_connect](#ga6a212dd4765adc82eda6e35cd9742f0c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

建立 AVRCP 连接（Connect）。

<a id="r_ga7ec468b9a50413ba478186c88728e13b"></a>

```c
int bt_avrcp_disconnect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_disconnect](#ga7ec468b9a50413ba478186c88728e13b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

断开 AVRCP 连接（Disconnect）。

<a id="r_gac3ccb5386c756bc2688ee5d4499aa29b"></a>

```c
struct net_buf * bt_avrcp_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_avrcp_create_pdu](#gac3ccb5386c756bc2688ee5d4499aa29b)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 AVRCP 协议数据单元（PDU）发送分配 `net_buf`，并为 AVRCP、AVRCTP（原文写作 AVRCTP）、L2CAP 和 ACL 头部预留空间（Headroom）。

<a id="r_gad0207b2d16d616b628e7bd2dd7fe4e41"></a>

```c
struct net_buf * bt_avrcp_create_vendor_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_avrcp_create_vendor_pdu](#gad0207b2d16d616b628e7bd2dd7fe4e41)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 AVRCP 厂商相关协议数据单元（Vendor-Dependent PDU）发送分配 `net_buf`；除 AVRCP、AVCTP、L2CAP 和 ACL 头部外，还为厂商 PDU 头部预留空间（Headroom）。

<a id="r_gac66d9b3fc6352e66716da3e10b25ccdb"></a>

```c
int bt_avrcp_browsing_connect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_browsing_connect](#gac66d9b3fc6352e66716da3e10b25ccdb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

连接 AVRCP 浏览通道（Browsing Channel）。

<a id="r_gaa00ea2046f2fe87676fe990e0d34de8b"></a>

```c
int bt_avrcp_browsing_disconnect (struct bt_conn *conn)
```

相关声明：[bt_avrcp_browsing_disconnect](#gaa00ea2046f2fe87676fe990e0d34de8b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

断开 AVRCP 浏览通道（Browsing Channel）。

<a id="r_ga7129d3dc93ea77140ae192099f4a4f92"></a>

```c
int bt_avrcp_ct_register_cb (const struct bt_avrcp_ct_cb *cb)
```

相关声明：[bt_avrcp_ct_register_cb](#ga7129d3dc93ea77140ae192099f4a4f92)、[bt_avrcp_ct_cb](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md)。

注册回调（Callback）。

<a id="r_ga311233e84ef1c0fc8c28baacbb77b831"></a>

```c
int bt_avrcp_ct_get_caps (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t cap_id)
```

相关声明：[bt_avrcp_ct_get_caps](#ga311233e84ef1c0fc8c28baacbb77b831)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 AVRCP 能力（Capabilities）。

<a id="r_ga0d59de3bbcfd036f267354fa4ee290dd"></a>

```c
int bt_avrcp_ct_get_unit_info (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_get_unit_info](#ga0d59de3bbcfd036f267354fa4ee290dd)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 AVRCP 单元信息（Unit Info）。

<a id="r_ga4ddceec722d768a0f0c86b3701e0e693"></a>

```c
int bt_avrcp_ct_get_subunit_info (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_get_subunit_info](#ga4ddceec722d768a0f0c86b3701e0e693)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 AVRCP 子单元信息（Subunit Info）。

<a id="r_ga16f8e224bc80ed0bca5ce04a93670320"></a>

```c
int bt_avrcp_ct_passthrough (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t opid, uint8_t state, const uint8_t *payload, uint8_t len)
```

相关声明：[bt_avrcp_ct_passthrough](#ga16f8e224bc80ed0bca5ce04a93670320)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 AVRCP 透传命令（Pass Through Command）。

<a id="r_gab0886ea325dddc67167bed86ec6c31e9"></a>

```c
int bt_avrcp_ct_set_browsed_player (struct bt_avrcp_ct *ct, uint8_t tid, uint16_t player_id)
```

相关声明：[bt_avrcp_ct_set_browsed_player](#gab0886ea325dddc67167bed86ec6c31e9)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置要浏览的播放器（Browsed Player）。

<a id="r_gab2e6565627deefd8dc5c79a08d02aa85"></a>

```c
int bt_avrcp_ct_register_notification (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t event_id, uint32_t interval, bt_avrcp_notify_changed_cb_t cb)
```

相关声明：[bt_avrcp_ct_register_notification](#gab2e6565627deefd8dc5c79a08d02aa85)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_avrcp_notify_changed_cb_t](#gab9bd888ef5443bd0a3d34a34b972f409)。

通过回调注册 AVRCP 变化通知（Changed Notifications）。

<a id="r_gadfafc60888e73a92c1d16fe9696565df"></a>

```c
int bt_avrcp_ct_list_player_app_setting_attrs (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_list_player_app_setting_attrs](#gadfafc60888e73a92c1d16fe9696565df)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `LIST_PLAYER_APP_SETTING_ATTRS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga11f34256317663cec599d7cb1b250243"></a>

```c
int bt_avrcp_ct_list_player_app_setting_vals (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t attr_id)
```

相关声明：[bt_avrcp_ct_list_player_app_setting_vals](#ga11f34256317663cec599d7cb1b250243)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `LIST_PLAYER_APP_SETTING_VALS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga232182eaa8d04921d85a68e35268212e"></a>

```c
int bt_avrcp_ct_get_curr_player_app_setting_val (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_curr_player_app_setting_val](#ga232182eaa8d04921d85a68e35268212e)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_CURR_PLAYER_APP_SETTING_VAL` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga962f7727f10ca2827c60d4d9a5dd2bde"></a>

```c
int bt_avrcp_ct_set_player_app_setting_val (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_set_player_app_setting_val](#ga962f7727f10ca2827c60d4d9a5dd2bde)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `SET_PLAYER_APP_SETTING_VAL` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga197fc46b498c5d4f52e4868bb85480b9"></a>

```c
int bt_avrcp_ct_get_player_app_setting_attr_text (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_player_app_setting_attr_text](#ga197fc46b498c5d4f52e4868bb85480b9)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gaccbb023e5051601e27ab1ca193152f7b"></a>

```c
int bt_avrcp_ct_get_player_app_setting_val_text (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_player_app_setting_val_text](#gaccbb023e5051601e27ab1ca193152f7b)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_PLAYER_APP_SETTING_VAL_TEXT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gab268d545750bd22b0625779d735d344a"></a>

```c
int bt_avrcp_ct_inform_displayable_char_set (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_inform_displayable_char_set](#gab268d545750bd22b0625779d735d344a)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `INFORM_DISPLAYABLE_CHAR_SET` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gae8cb7f3d8dbb8ae91167916e5c99ec39"></a>

```c
int bt_avrcp_ct_inform_batt_status_of_ct (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t battery_status)
```

相关声明：[bt_avrcp_ct_inform_batt_status_of_ct](#gae8cb7f3d8dbb8ae91167916e5c99ec39)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `INFORM_BATT_STATUS_OF_CT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga27b0a9e2d86fcc91d2e7b19f1bc5df2d"></a>

```c
int bt_avrcp_ct_set_absolute_volume (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t absolute_volume)
```

相关声明：[bt_avrcp_ct_set_absolute_volume](#ga27b0a9e2d86fcc91d2e7b19f1bc5df2d)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送设置绝对音量命令（Set Absolute Volume），用于控制方（CT）。

<a id="r_gaf5b49460a1037b0f146e7b16d89215e1"></a>

```c
int bt_avrcp_ct_get_element_attrs (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_element_attrs](#gaf5b49460a1037b0f146e7b16d89215e1)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_ELEMENT_ATTRS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga014c353ff7f2fc54eefad6a6e20112ec"></a>

```c
int bt_avrcp_ct_get_play_status (struct bt_avrcp_ct *ct, uint8_t tid)
```

相关声明：[bt_avrcp_ct_get_play_status](#ga014c353ff7f2fc54eefad6a6e20112ec)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 `GET_PLAY_STATUS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga69561453ade3e8ba07b2122efcddcfad"></a>

```c
int bt_avrcp_ct_set_addressed_player (struct bt_avrcp_ct *ct, uint8_t tid, uint16_t player_id)
```

相关声明：[bt_avrcp_ct_set_addressed_player](#ga69561453ade3e8ba07b2122efcddcfad)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送 `SET_ADDRESSED_PLAYER` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gab8d46ac46d35b711209f9a8572c1f8bd"></a>

```c
int bt_avrcp_ct_play_item (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_play_item](#gab8d46ac46d35b711209f9a8572c1f8bd)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `PLAY_ITEM` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_ga7e997ce46f322887227623b43e84ff28"></a>

```c
int bt_avrcp_ct_add_to_now_playing (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_add_to_now_playing](#ga7e997ce46f322887227623b43e84ff28)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `ADD_TO_NOW_PLAYING` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

<a id="r_gad77454a6d56942ffe57d5b716f7aa39d"></a>

```c
int bt_avrcp_ct_get_folder_items (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_folder_items](#gad77454a6d56942ffe57d5b716f7aa39d)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取文件夹条目（Get Folder Items）。

<a id="r_gab8730a40ab9bc208a53a035243b8cb1b"></a>

```c
int bt_avrcp_ct_change_path (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_change_path](#gab8730a40ab9bc208a53a035243b8cb1b)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

更改路径（Change Path）。

<a id="r_ga4ae38864d35a66a306ced13544e442d4"></a>

```c
int bt_avrcp_ct_get_item_attrs (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_get_item_attrs](#ga4ae38864d35a66a306ced13544e442d4)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取条目属性（Get Item Attributes）。

<a id="r_gadef2624ec50c0bb138d7eae8525784c5"></a>

```c
int bt_avrcp_ct_get_total_number_of_items (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t scope)
```

相关声明：[bt_avrcp_ct_get_total_number_of_items](#gadef2624ec50c0bb138d7eae8525784c5)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取条目总数（Get Total Number Of Items）。

<a id="r_gab8b765fab76ba2585730f328c0abc167"></a>

```c
int bt_avrcp_ct_search (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_ct_search](#gab8b765fab76ba2585730f328c0abc167)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

搜索（Search）。

<a id="r_ga7ba6030ff079e3c47bf6e5838b61ebdb"></a>

```c
int bt_avrcp_tg_register_cb (const struct bt_avrcp_tg_cb *cb)
```

相关声明：[bt_avrcp_tg_register_cb](#ga7ba6030ff079e3c47bf6e5838b61ebdb)、[bt_avrcp_tg_cb](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md)。

注册回调（Callback）。

<a id="r_gaecb26512e8b1d267bca0d3ea01438c9b"></a>

```c
int bt_avrcp_tg_send_unit_info_rsp (struct bt_avrcp_tg *tg, uint8_t tid, struct bt_avrcp_unit_info_rsp *rsp)
```

相关声明：[bt_avrcp_tg_send_unit_info_rsp](#gaecb26512e8b1d267bca0d3ea01438c9b)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_unit_info_rsp](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md)。

发送单元信息响应（Unit Info Response）。

<a id="r_gabc170c5c0aa39827b4efc43880dbf258"></a>

```c
int bt_avrcp_tg_send_subunit_info_rsp (struct bt_avrcp_tg *tg, uint8_t tid)
```

相关声明：[bt_avrcp_tg_send_subunit_info_rsp](#gabc170c5c0aa39827b4efc43880dbf258)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送子单元信息响应（Subunit Info Response）。

<a id="r_gad160c86f1647509e10d741284b9bbb03"></a>

```c
int bt_avrcp_tg_get_caps (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_caps](#gad160c86f1647509e10d741284b9bbb03)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 `GET_CAPABILITIES` 响应（Response）。

<a id="r_ga1ef0065fd9fa73bcd03491fe700fac65"></a>

```c
int bt_avrcp_tg_notification (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint8_t event_id, struct bt_avrcp_event_data *data)
```

相关声明：[bt_avrcp_tg_notification](#ga1ef0065fd9fa73bcd03491fe700fac65)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)。

发送通知响应（Notification Response）。

<a id="r_ga15bf2602f37ef83b3bcefd85920658eb"></a>

```c
int bt_avrcp_tg_set_browsed_player (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_set_browsed_player](#ga15bf2602f37ef83b3bcefd85920658eb)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置浏览播放器响应（Set Browsed Player Response）。

<a id="r_gac92854e7f567f6088a5cf3ad3c209343"></a>

```c
int bt_avrcp_tg_send_passthrough_rsp (struct bt_avrcp_tg *tg, uint8_t tid, bt_avrcp_rsp_t result, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_send_passthrough_rsp](#gac92854e7f567f6088a5cf3ad3c209343)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_rsp_t](#gaba2d8faec2c3baf7403199ea8a509326)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 AVRCP 透传响应（Pass Through Response）。

<a id="r_gab442ef3962bebd8dbe0d5681498f8453"></a>

```c
int bt_avrcp_tg_list_player_app_setting_attrs (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_list_player_app_setting_attrs](#gab442ef3962bebd8dbe0d5681498f8453)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_ATTRS` 对应的响应。

<a id="r_gae8b42aada8be4c9fac13fbd90e751a7b"></a>

```c
int bt_avrcp_tg_list_player_app_setting_vals (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_list_player_app_setting_vals](#gae8b42aada8be4c9fac13fbd90e751a7b)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_VALS` 对应的响应。

<a id="r_gab18ce4d9348698272eedff52ddb3052e"></a>

```c
int bt_avrcp_tg_get_curr_player_app_setting_val (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_curr_player_app_setting_val](#gab18ce4d9348698272eedff52ddb3052e)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_CURR_PLAYER_APP_SETTING_VAL` 对应的响应。

<a id="r_ga9d471d9a932dfd43b71e894ddec013b4"></a>

```c
int bt_avrcp_tg_set_player_app_setting_val (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_set_player_app_setting_val](#ga9d471d9a932dfd43b71e894ddec013b4)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_SET_PLAYER_APP_SETTING_VAL` 对应的响应。

<a id="r_ga123f5528b62f48faaf020f19dcc321c1"></a>

```c
int bt_avrcp_tg_get_player_app_setting_attr_text (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_player_app_setting_attr_text](#ga123f5528b62f48faaf020f19dcc321c1)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_ATTR_TEXT` 对应的响应。

<a id="r_ga8cc324a60a3480524336bc399d62c1ed"></a>

```c
int bt_avrcp_tg_get_player_app_setting_val_text (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_player_app_setting_val_text](#ga8cc324a60a3480524336bc399d62c1ed)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_VAL_TEXT` 对应的响应。

<a id="r_gadda57eb5c28f6b77bda5efe9286bc5f4"></a>

```c
int bt_avrcp_tg_inform_displayable_char_set (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_inform_displayable_char_set](#gadda57eb5c28f6b77bda5efe9286bc5f4)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_INFORM_DISPLAYABLE_CHAR_SET` 对应的响应。

<a id="r_gaa2aca5a011a99a20a3bd3fd7154a864a"></a>

```c
int bt_avrcp_tg_inform_batt_status_of_ct (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_inform_batt_status_of_ct](#gaa2aca5a011a99a20a3bd3fd7154a864a)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_INFORM_BATT_STATUS_OF_CT` 对应的响应。

<a id="r_gad0d937d50eccfbedc81cc575a3e238f2"></a>

```c
int bt_avrcp_tg_absolute_volume (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint8_t absolute_volume)
```

相关声明：[bt_avrcp_tg_absolute_volume](#gad0d937d50eccfbedc81cc575a3e238f2)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送设置绝对音量响应（Set Absolute Volume），用于目标方（TG）。

<a id="r_ga81333eaee7ca1838424ce9b513e6e2c5"></a>

```c
int bt_avrcp_tg_get_element_attrs (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_element_attrs](#ga81333eaee7ca1838424ce9b513e6e2c5)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_ELEMENT_ATTRS` 对应的响应。

<a id="r_ga4f37f0c696ea98f44bd5e8ce2905d9f4"></a>

```c
int bt_avrcp_tg_get_play_status (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_play_status](#ga4f37f0c696ea98f44bd5e8ce2905d9f4)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAY_STATUS` 对应的响应。

<a id="r_gadcf3f892a1d492a2743cdb4f8d205505"></a>

```c
int bt_avrcp_tg_set_addressed_player (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_set_addressed_player](#gadcf3f892a1d492a2743cdb4f8d205505)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_SET_ADDRESSED_PLAYER` 对应的响应。

<a id="r_ga5f72112c0887ed3efc3455ead567126d"></a>

```c
int bt_avrcp_tg_play_item (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_play_item](#ga5f72112c0887ed3efc3455ead567126d)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_PLAY_ITEM` 对应的响应。

<a id="r_gafc84238ea566bef4d2789e7cdba193dd"></a>

```c
int bt_avrcp_tg_add_to_now_playing (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_add_to_now_playing](#gafc84238ea566bef4d2789e7cdba193dd)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_ADD_TO_NOW_PLAYING` 对应的响应。

<a id="r_ga6261635bf3925766bb7af10696df6fd5"></a>

```c
int bt_avrcp_tg_get_folder_items (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_folder_items](#ga6261635bf3925766bb7af10696df6fd5)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取文件夹条目响应（Get Folder Items Response）。

<a id="r_ga851b0c30ac0b382658b5ce040d7755eb"></a>

```c
int bt_avrcp_tg_change_path (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint32_t num_items)
```

相关声明：[bt_avrcp_tg_change_path](#ga851b0c30ac0b382658b5ce040d7755eb)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送更改路径响应（Change Path Response）。

<a id="r_ga509746020e487d769f94174a4071b673"></a>

```c
int bt_avrcp_tg_get_item_attrs (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_item_attrs](#ga509746020e487d769f94174a4071b673)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取条目属性响应（Get Item Attributes Response）。

<a id="r_gaf521ea00d597fced528d86befd9b5bbb"></a>

```c
int bt_avrcp_tg_get_total_number_of_items (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_get_total_number_of_items](#gaf521ea00d597fced528d86befd9b5bbb)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取条目总数响应（Get Total Number Of Items Response）。

<a id="r_ga136fda008bf5d5f7e9cad3855a4173f9"></a>

```c
int bt_avrcp_tg_search (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[bt_avrcp_tg_search](#ga136fda008bf5d5f7e9cad3855a4173f9)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送搜索响应（Search Response）。

<a id="r_gaad6d011fe84aaa6cec8665aa87d4cc41"></a>

```c
int bt_avrcp_tg_browsing_general_reject (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status)
```

相关声明：[bt_avrcp_tg_browsing_general_reject](#gaad6d011fe84aaa6cec8665aa87d4cc41)、[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在 AVRCP 浏览通道（Browsing Channel）上发送通用拒绝响应（General Reject Response），用于目标方（TG）。

## 2.7\_详细说明（Detailed Documentation）

<a id="gae7a97b11a8954a2a25cc401ced566fd2"></a>

### `BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG`

```c
#define BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG (0x001958)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="gae4e7573280179717124104858629122a"></a>

### `BT_AVRCP_COMPANY_ID_SIZE`

```c
#define BT_AVRCP_COMPANY_ID_SIZE (3)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="ga5ecfdd180bc51dc0867e859d1b3a7fbe"></a>

### `BT_AVRCP_MAX_ABSOLUTE_VOLUME`

```c
#define BT_AVRCP_MAX_ABSOLUTE_VOLUME 0x7F
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

音视频遥控配置文件（Audio/Video Remote Control Profile，AVRCP）的最大绝对音量（Maximum Absolute Volume）。

<a id="ga8c8e1596f92e32781690c0a76196c4c8"></a>

### `BT_AVRCP_PASSTHROUGH_GET_OPID`

```c
#define BT_AVRCP_PASSTHROUGH_GET_OPID ( payload)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

展开值（Value）：

```c
((bt_avrcp_opid_t)(FIELD_GET(GENMASK(6, 0), ((payload)->opid_state))))
```

<a id="ga7eee1ffa11a5152a0dd014ac15979605"></a>

### `BT_AVRCP_PASSTHROUGH_GET_STATE`

```c
#define BT_AVRCP_PASSTHROUGH_GET_STATE ( payload)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

展开值（Value）：

```c
((bt_avrcp_button_state_t)(FIELD_GET(BIT(7), ((payload)->opid_state))))
```

<a id="ga4f8014317db642c98d3db9be6db7adea"></a>

### `BT_AVRCP_PASSTHROUGH_SET_STATE_OPID`

```c
#define BT_AVRCP_PASSTHROUGH_SET_STATE_OPID ( payload, state, opid )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

展开值（Value）：

```c
(payload)->opid_state = FIELD_PREP(BIT(7), state) | FIELD_PREP(GENMASK(6, 0), opid)
```

<a id="gab9bd888ef5443bd0a3d34a34b972f409"></a>

### `bt_avrcp_notify_changed_cb_t`

```c
typedef void(* bt_avrcp_notify_changed_cb_t) (struct bt_avrcp_ct *ct, uint8_t event_id, struct bt_avrcp_event_data *data)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 事件通知回调（Event Notification Callback），仅用于 CHANGED 通知。

当已注册事件发生、需要向控制器（Controller，CT）发送“已变化”（Changed）通知时，AVRCP 目标端（Target，TG）调用此回调。

对于临时响应（Interim）和拒绝错误（Rejected Error），该回调会触发控制器（Controller）注册的通知函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `event_id` | AVRCP 事件标识符。参见 `bt_avrcp_event_data`。它对应某个 AVRCP 事件类型，例如 `EVENT_PLAYBACK_STATUS_CHANGED`、`EVENT_TRACK_CHANGED` 等。 |
| `data` | 指向包含事件专用数据的 `bt_avrcp_event_data` 结构体的指针。联合体（Union）的内容取决于 `event_id`。 |

**说明（Note）**：注意：回调实现不应阻塞或执行耗时操作。必要时，将处理工作推迟到其他线程（Thread）或任务（Task）中执行。

<a id="ga33825b183b12a2b29d5148a7366c0e77"></a>

### `bt_avrcp_battery_status_t`

```c
enum bt_avrcp_battery_status_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 电池状态码（Battery Status Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_BATTERY_STATUS_NORMAL` |  |
| `BT_AVRCP_BATTERY_STATUS_WARNING` |  |
| `BT_AVRCP_BATTERY_STATUS_CRITICAL` |  |
| `BT_AVRCP_BATTERY_STATUS_EXTERNAL` |  |
| `BT_AVRCP_BATTERY_STATUS_FULL` |  |

<a id="ga15f9f868b056f17ea12d96530b7da881"></a>

### `bt_avrcp_button_state_t`

```c
enum bt_avrcp_button_state_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 按钮状态标志（Button State Flag）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_BUTTON_PRESSED` |  |
| `BT_AVRCP_BUTTON_RELEASED` |  |

<a id="gac311dc7b5f99162b954271529eeb84ea"></a>

### `bt_avrcp_cap_t`

```c
enum bt_avrcp_cap_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 能力标识符（Capability ID）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_CAP_COMPANY_ID` |  |
| `BT_AVRCP_CAP_EVENTS_SUPPORTED` |  |

<a id="ga02d67e84b4a48ebecf3b307cbd4bb61c"></a>

### `bt_avrcp_change_path_t`

```c
enum bt_avrcp_change_path_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 更改路径方向（ChangePath Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_CHANGE_PATH_PARENT` | 导航到父文件夹（Parent Folder）。 |
| `BT_AVRCP_CHANGE_PATH_CHILD` | 导航到子文件夹（Child Folder）。 |

<a id="ga81330413af9eba049da6557b14ae082c"></a>

### `bt_avrcp_charset_t`

```c
enum bt_avrcp_charset_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 字符集标识符（Character Set IDs）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_CHARSET_UTF8` |  |

<a id="ga2a4c610e00ba9832f954f30bd6b6618e"></a>

### `bt_avrcp_ctype_t`

```c
enum bt_avrcp_ctype_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

音视频控制（AV/C）命令类型（Command Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_CTYPE_CONTROL` |  |
| `BT_AVRCP_CTYPE_STATUS` |  |
| `BT_AVRCP_CTYPE_SPECIFIC_INQUIRY` |  |
| `BT_AVRCP_CTYPE_NOTIFY` |  |
| `BT_AVRCP_CTYPE_GENERAL_INQUIRY` |  |

<a id="gae76f2666d10e6f46a1e5d68327fc7607"></a>

### `bt_avrcp_equalizer_value_t`

```c
enum bt_avrcp_equalizer_value_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 播放器应用的均衡器设置值（Player Application Setting Values for Equalizer）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_EQUALIZER_OFF` |  |
| `BT_AVRCP_EQUALIZER_ON` |  |

<a id="gaf55aae17f67a1361279ae208b17e4a75"></a>

### `bt_avrcp_evt_t`

```c
enum bt_avrcp_evt_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 通知事件（Notification Events）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED` |  |
| `BT_AVRCP_EVT_TRACK_CHANGED` |  |
| `BT_AVRCP_EVT_TRACK_REACHED_END` |  |
| `BT_AVRCP_EVT_TRACK_REACHED_START` |  |
| `BT_AVRCP_EVT_PLAYBACK_POS_CHANGED` |  |
| `BT_AVRCP_EVT_BATT_STATUS_CHANGED` |  |
| `BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED` |  |
| `BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED` |  |
| `BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED` |  |
| `BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED` |  |
| `BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED` |  |
| `BT_AVRCP_EVT_UIDS_CHANGED` |  |
| `BT_AVRCP_EVT_VOLUME_CHANGED` |  |

<a id="ga09d191c490efcfb9f8139975090be0d5"></a>

### `bt_avrcp_folder_type_t`

```c
enum bt_avrcp_folder_type_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 文件夹类型（Folder Types），用于文件夹条目。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_FOLDER_TYPE_MIXED` | 混合文件夹类型（Mixed Folder Type）。 |
| `BT_AVRCP_FOLDER_TYPE_TITLES` | 标题文件夹（Titles Folder）。 |
| `BT_AVRCP_FOLDER_TYPE_ALBUMS` | 专辑文件夹（Albums Folder）。 |
| `BT_AVRCP_FOLDER_TYPE_ARTISTS` | 艺术家文件夹（Artists Folder）。 |
| `BT_AVRCP_FOLDER_TYPE_GENRES` | 流派文件夹（Genres Folder）。 |
| `BT_AVRCP_FOLDER_TYPE_PLAYLISTS` | 播放列表文件夹（Playlists Folder）。 |
| `BT_AVRCP_FOLDER_TYPE_YEARS` | 年份文件夹（Years Folder）。 |

<a id="gac02fed37e267996d4de50b06292d0668"></a>

### `bt_avrcp_item_type_t`

```c
enum bt_avrcp_item_type_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 条目类型（Item Types），用于浏览操作 GetFolderItems 等。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER` | 媒体播放器项目（Media Player Item）。 |
| `BT_AVRCP_ITEM_TYPE_FOLDER` | 文件夹项目（Folder Item）。 |
| `BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT` | 媒体元素项目（Media Element Item）。 |

<a id="ga0ebc5d2657688b70119e11ac20d24592"></a>

### `bt_avrcp_media_attr_id_t`

```c
enum bt_avrcp_media_attr_id_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 媒体属性标识符（Media Attribute IDs）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_MEDIA_ATTR_ID_TITLE` | 媒体标题（Title）。 |
| `BT_AVRCP_MEDIA_ATTR_ID_ARTIST` | 艺术家名称（Artist Name）。 |
| `BT_AVRCP_MEDIA_ATTR_ID_ALBUM` | 专辑名称（Album Name）。 |
| `BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER` | 曲目编号（Track Number）。 |
| `BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS` | 曲目总数（Total Number of Tracks）。 |
| `BT_AVRCP_MEDIA_ATTR_ID_GENRE` | 流派（Genre）。 |
| `BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME` | 播放时长（Playing Time），单位为毫秒。 |
| `BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART` | 默认封面图（Default Cover Art）。 |

<a id="gac927c7e7c59f6f0e6243ca0887945d5a"></a>

### `bt_avrcp_media_type_t`

```c
enum bt_avrcp_media_type_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 媒体类型（Media Types），用于媒体元素条目。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_MEDIA_TYPE_AUDIO` | 音频媒体（Audio Media）。 |
| `BT_AVRCP_MEDIA_TYPE_VIDEO` | 视频媒体（Video Media）。 |

<a id="ga3c997d96028343a0a5a4948dabe19b84"></a>

### `bt_avrcp_opid_t`

```c
enum bt_avrcp_opid_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 透传命令（Passthrough Commands）使用的 AV/C 操作标识符（Operation IDs）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_OPID_SELECT` |  |
| `BT_AVRCP_OPID_UP` |  |
| `BT_AVRCP_OPID_DOWN` |  |
| `BT_AVRCP_OPID_LEFT` |  |
| `BT_AVRCP_OPID_RIGHT` |  |
| `BT_AVRCP_OPID_RIGHT_UP` |  |
| `BT_AVRCP_OPID_RIGHT_DOWN` |  |
| `BT_AVRCP_OPID_LEFT_UP` |  |
| `BT_AVRCP_OPID_LEFT_DOWN` |  |
| `BT_AVRCP_OPID_ROOT_MENU` |  |
| `BT_AVRCP_OPID_SETUP_MENU` |  |
| `BT_AVRCP_OPID_CONTENTS_MENU` |  |
| `BT_AVRCP_OPID_FAVORITE_MENU` |  |
| `BT_AVRCP_OPID_EXIT` |  |
| `BT_AVRCP_OPID_0` |  |
| `BT_AVRCP_OPID_1` |  |
| `BT_AVRCP_OPID_2` |  |
| `BT_AVRCP_OPID_3` |  |
| `BT_AVRCP_OPID_4` |  |
| `BT_AVRCP_OPID_5` |  |
| `BT_AVRCP_OPID_6` |  |
| `BT_AVRCP_OPID_7` |  |
| `BT_AVRCP_OPID_8` |  |
| `BT_AVRCP_OPID_9` |  |
| `BT_AVRCP_OPID_DOT` |  |
| `BT_AVRCP_OPID_ENTER` |  |
| `BT_AVRCP_OPID_CLEAR` |  |
| `BT_AVRCP_OPID_CHANNEL_UP` |  |
| `BT_AVRCP_OPID_CHANNEL_DOWN` |  |
| `BT_AVRCP_OPID_PREVIOUS_CHANNEL` |  |
| `BT_AVRCP_OPID_SOUND_SELECT` |  |
| `BT_AVRCP_OPID_INPUT_SELECT` |  |
| `BT_AVRCP_OPID_DISPLAY_INFORMATION` |  |
| `BT_AVRCP_OPID_HELP` |  |
| `BT_AVRCP_OPID_PAGE_UP` |  |
| `BT_AVRCP_OPID_PAGE_DOWN` |  |
| `BT_AVRCP_OPID_POWER` |  |
| `BT_AVRCP_OPID_VOLUME_UP` |  |
| `BT_AVRCP_OPID_VOLUME_DOWN` |  |
| `BT_AVRCP_OPID_MUTE` |  |
| `BT_AVRCP_OPID_PLAY` |  |
| `BT_AVRCP_OPID_STOP` |  |
| `BT_AVRCP_OPID_PAUSE` |  |
| `BT_AVRCP_OPID_RECORD` |  |
| `BT_AVRCP_OPID_REWIND` |  |
| `BT_AVRCP_OPID_FAST_FORWARD` |  |
| `BT_AVRCP_OPID_EJECT` |  |
| `BT_AVRCP_OPID_FORWARD` |  |
| `BT_AVRCP_OPID_BACKWARD` |  |
| `BT_AVRCP_OPID_ANGLE` |  |
| `BT_AVRCP_OPID_SUBPICTURE` |  |
| `BT_AVRCP_OPID_F1` |  |
| `BT_AVRCP_OPID_F2` |  |
| `BT_AVRCP_OPID_F3` |  |
| `BT_AVRCP_OPID_F4` |  |
| `BT_AVRCP_OPID_F5` |  |
| `BT_AVRCP_OPID_VENDOR_UNIQUE` |  |

<a id="ga433775fa2758df43ee1d26c78e9122d1"></a>

### `bt_avrcp_playback_status_t`

```c
enum bt_avrcp_playback_status_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 播放状态（Playback Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_PLAYBACK_STATUS_STOPPED` |  |
| `BT_AVRCP_PLAYBACK_STATUS_PLAYING` |  |
| `BT_AVRCP_PLAYBACK_STATUS_PAUSED` |  |
| `BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK` |  |
| `BT_AVRCP_PLAYBACK_STATUS_REV_SEEK` |  |
| `BT_AVRCP_PLAYBACK_STATUS_ERROR` |  |

<a id="ga8047dddc873566ee372e77c6eecd008f"></a>

### `bt_avrcp_player_attr_id_t`

```c
enum bt_avrcp_player_attr_id_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 播放器应用设置属性标识符（Player Application Setting Attribute IDs）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_PLAYER_ATTR_EQUALIZER` |  |
| `BT_AVRCP_PLAYER_ATTR_REPEAT_MODE` |  |
| `BT_AVRCP_PLAYER_ATTR_SHUFFLE` |  |
| `BT_AVRCP_PLAYER_ATTR_SCAN` |  |

<a id="ga22bf1b16b383ef473624769ae6ae893a"></a>

### `bt_avrcp_repeat_mode_value_t`

```c
enum bt_avrcp_repeat_mode_value_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 播放器应用的重复模式设置值（Player Application Setting Values for Repeat Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_REPEAT_MODE_OFF` |  |
| `BT_AVRCP_REPEAT_MODE_SINGLE_TRACK` |  |
| `BT_AVRCP_REPEAT_MODE_ALL_TRACKS` |  |
| `BT_AVRCP_REPEAT_MODE_GROUP` |  |

<a id="gaba2d8faec2c3baf7403199ea8a509326"></a>

### `bt_avrcp_rsp_t`

```c
enum bt_avrcp_rsp_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

音视频控制（AV/C）响应码（Response Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_RSP_NOT_IMPLEMENTED` |  |
| `BT_AVRCP_RSP_ACCEPTED` |  |
| `BT_AVRCP_RSP_REJECTED` |  |
| `BT_AVRCP_RSP_IN_TRANSITION` |  |
| `BT_AVRCP_RSP_IMPLEMENTED` | 用于 `SPECIFIC_INQUIRY` 和 `GENERAL_INQUIRY` 命令。 |
| `BT_AVRCP_RSP_STABLE` | 用于 `STATUS` 命令。 |
| `BT_AVRCP_RSP_CHANGED` |  |
| `BT_AVRCP_RSP_INTERIM` |  |

<a id="ga4426612c49f8456f2543f373db72d3f2"></a>

### `bt_avrcp_scan_value_t`

```c
enum bt_avrcp_scan_value_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 播放器应用的扫描设置值（Player Application Setting Values for Scan）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_SCAN_OFF` |  |
| `BT_AVRCP_SCAN_ALL_TRACKS` |  |
| `BT_AVRCP_SCAN_GROUP` |  |

<a id="gaabab9a4f37b3f9653ca95dd4b5944707"></a>

### `bt_avrcp_scope_t`

```c
enum bt_avrcp_scope_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 范围值（Scope Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST` | 媒体播放器列表（Media Player List）。 |
| `BT_AVRCP_SCOPE_VFS` | 虚拟文件系统（Virtual File System）。 |
| `BT_AVRCP_SCOPE_SEARCH` | 搜索（Search）。 |
| `BT_AVRCP_SCOPE_NOW_PLAYING` | 正在播放（Now Playing）。 |

<a id="ga8e6ce46ba46268c2c80f4ec7570859c8"></a>

### `bt_avrcp_shuffle_value_t`

```c
enum bt_avrcp_shuffle_value_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 播放器应用的随机播放设置值（Player Application Setting Values for Shuffle）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_SHUFFLE_OFF` |  |
| `BT_AVRCP_SHUFFLE_ALL_TRACKS` |  |
| `BT_AVRCP_SHUFFLE_GROUP` |  |

<a id="ga52368f4cc655bab75f96da80ddaaabe0"></a>

### `bt_avrcp_status_t`

```c
enum bt_avrcp_status_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 状态码与错误码（Status and Error Codes）。

这些状态码（Status Codes）用于 AVRCP 响应，表示命令的执行结果。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_STATUS_INVALID_COMMAND` | 无效命令（Invalid Command）。 适用于所有命令（All）。 |
| `BT_AVRCP_STATUS_INVALID_PARAMETER` | 参数无效（Invalid Parameter）。 适用于所有命令（All）。 |
| `BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR` | 参数内容错误（Parameter Content Error）。 适用于所有命令（All）。 |
| `BT_AVRCP_STATUS_INTERNAL_ERROR` | 内部错误（Internal Error）。 适用于所有命令（All）。 |
| `BT_AVRCP_STATUS_OPERATION_COMPLETED` | 操作完成，无错误。 适用于所有命令，但响应 `CType` 为 `AV/C REJECTED` 的情况除外。 |
| `BT_AVRCP_STATUS_UID_CHANGED` | 设备上的唯一标识符（UID）已变化。 适用于所有命令（All）。 |
| `BT_AVRCP_STATUS_INVALID_DIRECTION` | 方向（Direction）参数无效。 适用于命令：`ChangePath`。 |
| `BT_AVRCP_STATUS_NOT_A_DIRECTORY` | 提供的唯一标识符（UID）并未指向文件夹项目（Folder Item）。 适用于命令：`ChangePath`。 |
| `BT_AVRCP_STATUS_DOES_NOT_EXIST` | 提供的唯一标识符（UID）并未指向任何当前有效的项目。 适用于命令：`ChangePath`、`PlayItem`、`AddToNowPlaying`、`GetItemAttributes`。 |
| `BT_AVRCP_STATUS_INVALID_SCOPE` | 范围（Scope）无效。 适用于命令：`GetFolderItems`、`PlayItem`、`AddToNowPlayer`、`GetItemAttributes`、`GetTotalNumberOfItems`。 |
| `BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS` | 范围越界（Range out of Bounds）。 适用于命令：`GetFolderItems`。 |
| `BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE` | 文件夹项目（Folder Item）不可播放。 适用于命令：`Play Item`、`AddToNowPlaying`。 |
| `BT_AVRCP_STATUS_MEDIA_IN_USE` | 媒体正在使用中（Media in Use）。 适用于命令：`PlayItem`、`AddToNowPlaying`。 |
| `BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL` | 正在播放列表（Now Playing List）已满。 适用于命令：`AddToNowPlaying`。 |
| `BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED` | 不支持搜索（Search）。 适用于命令：`Search`。 |
| `BT_AVRCP_STATUS_SEARCH_IN_PROGRESS` | 搜索正在进行中（Search in Progress）。 适用于命令：`Search`。 |
| `BT_AVRCP_STATUS_INVALID_PLAYER_ID` | 指定的播放器 ID（Player Id）并未指向有效播放器。 适用于命令：`SetAddressedPlayer`、`SetBrowsedPlayer`。 |
| `BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE` | 播放器不可浏览（Player Not Browsable）。 适用于命令：`SetBrowsedPlayer`。 |
| `BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED` | 播放器未被设为当前控制目标（Player Not Addressed）。 适用于命令：`Search`、`SetBrowsedPlayer`。 |
| `BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS` | 没有有效搜索结果（Search Results）。 适用于命令：`GetFolderItems`。 |
| `BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS` | 没有可用播放器（Available Players）。 适用于所有命令（ALL）。 |
| `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` | 当前控制的播放器（Addressed Player）已变化。 适用于所有注册通知（Register Notification）命令。 |
| `BT_AVRCP_STATUS_IN_TRANSITION` | 转换中响应（In Transition Response）。 目标端（Target）正在改变状态，例如在播放和暂停之间切换。注意：此状态不用于浏览命令（Browsing Commands）。 |
| `BT_AVRCP_STATUS_NOT_IMPLEMENTED` | 未实现响应（Not Implemented Response）。 目标设备（Target Device）不支持此命令或协议数据单元（PDU）。注意：此状态不用于浏览命令（Browsing Commands）。 |
| `BT_AVRCP_STATUS_SUCCESS` | 成功响应（Successful Response）。 目标设备（Target Device）已成功处理所请求的命令或协议数据单元（PDU）。 对于控制命令（Control Commands），表示请求已接受；对于状态命令（Status Commands），表示状态稳定并已成功报告。 |

<a id="ga78ba828636b731b2c43e088a581bfee9"></a>

### `bt_avrcp_subunit_type_t`

```c
enum bt_avrcp_subunit_type_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

音视频控制（AV/C）子单元类型（Subunit Type），也用于单元类型（Unit Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_SUBUNIT_TYPE_PANEL` |  |
| `BT_AVRCP_SUBUNIT_TYPE_UNIT` |  |

<a id="ga128458626d5fe6ffbac7cf97867621aa"></a>

### `bt_avrcp_system_status_t`

```c
enum bt_avrcp_system_status_t
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

AVRCP 系统状态码（System Status Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AVRCP_SYSTEM_STATUS_POWER_ON` |  |
| `BT_AVRCP_SYSTEM_STATUS_POWER_OFF` |  |
| `BT_AVRCP_SYSTEM_STATUS_UNPLUGGED` |  |

<a id="gac66d9b3fc6352e66716da3e10b25ccdb"></a>

### `bt_avrcp_browsing_connect()`

```c
int bt_avrcp_browsing_connect ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

连接 AVRCP 浏览通道（Browsing Channel）。

应在 AVRCP 控制通道（Control Channel）建立后调用此函数。此 API 用于在设备之间建立 AVRCP 浏览连接（Browsing Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向 `bt_conn` 结构体的指针。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gaa00ea2046f2fe87676fe990e0d34de8b"></a>

### `bt_avrcp_browsing_disconnect()`

```c
int bt_avrcp_browsing_disconnect ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

断开 AVRCP 浏览通道（Browsing Channel）。

此函数关闭 AVCTP 浏览通道（Browsing Channel）的 L2CAP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向 `bt_conn` 结构体的指针。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga6a212dd4765adc82eda6e35cd9742f0c"></a>

### `bt_avrcp_connect()`

```c
int bt_avrcp_connect ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

建立 AVRCP 连接（Connect）。

应在执行 GAP 过程（Procedure）取得 `conn` 参数后调用此函数。此 API 用于在设备之间建立 AVRCP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向 `bt_conn` 结构体的指针。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gac3ccb5386c756bc2688ee5d4499aa29b"></a>

### `bt_avrcp_create_pdu()`

```c
struct net_buf * bt_avrcp_create_pdu ( struct net_buf_pool * pool)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

为 AVRCP 协议数据单元（PDU）发送分配 `net_buf`，并为 AVRCP、AVRCTP（原文写作 AVRCTP）、L2CAP 和 ACL 头部预留空间（Headroom）。

此函数从指定缓冲池（Pool）分配缓冲区（Buffer），并为蓝牙 AVRCP 所需的协议头预留足够头部空间（Headroom）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 用于分配的缓冲池（Buffer Pool）。 |

**返回（Returns）**：返回值：新分配的 `net_buf`，其中已预留头部空间（Headroom）。

<a id="gad0207b2d16d616b628e7bd2dd7fe4e41"></a>

### `bt_avrcp_create_vendor_pdu()`

```c
struct net_buf * bt_avrcp_create_vendor_pdu ( struct net_buf_pool * pool)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

为 AVRCP 厂商相关协议数据单元（Vendor-Dependent PDU）发送分配 `net_buf`；除 AVRCP、AVCTP、L2CAP 和 ACL 头部外，还为厂商 PDU 头部预留空间（Headroom）。

此函数从指定缓冲池（Pool）分配缓冲区（Buffer），并为蓝牙 AVRCP 厂商相关协议数据单元（Vendor-Dependent PDUs）所需的协议头预留足够头部空间（Headroom）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 用于分配的缓冲池（Buffer Pool）。 |

**返回（Returns）**：返回值：新分配的 `net_buf`，其中已预留头部空间（Headroom）。

<a id="ga7e997ce46f322887227623b43e84ff28"></a>

### `bt_avrcp_ct_add_to_now_playing()`

```c
int bt_avrcp_ct_add_to_now_playing ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `ADD_TO_NOW_PLAYING` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `ADD_TO_NOW_PLAYING` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_add_to_now_playing_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gab8730a40ab9bc208a53a035243b8cb1b"></a>

### `bt_avrcp_ct_change_path()`

```c
int bt_avrcp_ct_change_path ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

更改路径（Change Path）。

此函数向远端设备发送 AVRCP 协议数据单元（PDU）`CHANGE_PATH`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Change Path command` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_change_path_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga311233e84ef1c0fc8c28baacbb77b831"></a>

### `bt_avrcp_ct_get_caps()`

```c
int bt_avrcp_ct_get_caps ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t cap_id )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

获取 AVRCP 能力（Capabilities）。

此函数获取远端设备支持的能力（Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `cap_id` | 请求的具体能力（Capability），参见 `bt_avrcp_cap_t`。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga232182eaa8d04921d85a68e35268212e"></a>

### `bt_avrcp_ct_get_curr_player_app_setting_val()`

```c
int bt_avrcp_ct_get_curr_player_app_setting_val ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `GET_CURR_PLAYER_APP_SETTING_VAL` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `GET_CURR_PLAYER_APP_SETTING_VAL` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_get_curr_player_app_setting_val_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gaf5b49460a1037b0f146e7b16d89215e1"></a>

### `bt_avrcp_ct_get_element_attrs()`

```c
int bt_avrcp_ct_get_element_attrs ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `GET_ELEMENT_ATTRS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `GET_ELEMENT_ATTRS` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_get_element_attrs_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gad77454a6d56942ffe57d5b716f7aa39d"></a>

### `bt_avrcp_ct_get_folder_items()`

```c
int bt_avrcp_ct_get_folder_items ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

获取文件夹条目（Get Folder Items）。

此函数向远端设备发送 AVRCP 协议数据单元（PDU）`GET_FOLDER_ITEMS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Get Folder Items command` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_get_folder_items_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga4ae38864d35a66a306ced13544e442d4"></a>

### `bt_avrcp_ct_get_item_attrs()`

```c
int bt_avrcp_ct_get_item_attrs ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

获取条目属性（Get Item Attributes）。

此函数向远端设备发送 AVRCP 协议数据单元（PDU）`GET_ITEM_ATTRIBUTES`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Get Item Attributes command` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_get_item_attrs_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga014c353ff7f2fc54eefad6a6e20112ec"></a>

### `bt_avrcp_ct_get_play_status()`

```c
int bt_avrcp_ct_get_play_status ( struct bt_avrcp_ct * ct, uint8_t tid )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `GET_PLAY_STATUS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga197fc46b498c5d4f52e4868bb85480b9"></a>

### `bt_avrcp_ct_get_player_app_setting_attr_text()`

```c
int bt_avrcp_ct_get_player_app_setting_attr_text ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_get_player_app_setting_attr_text_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gaccbb023e5051601e27ab1ca193152f7b"></a>

### `bt_avrcp_ct_get_player_app_setting_val_text()`

```c
int bt_avrcp_ct_get_player_app_setting_val_text ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `GET_PLAYER_APP_SETTING_VAL_TEXT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `GET_PLAYER_APP_SETTING_VAL_TEXT` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_get_player_app_setting_val_text_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga4ddceec722d768a0f0c86b3701e0e693"></a>

### `bt_avrcp_ct_get_subunit_info()`

```c
int bt_avrcp_ct_get_subunit_info ( struct bt_avrcp_ct * ct, uint8_t tid )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

获取 AVRCP 子单元信息（Subunit Info）。

此函数获取 AV/C 单元（Unit）的子单元（Subunit）信息。如果设备同时支持其他配置文件（Profiles），支持 AVRCP 的设备还可能支持面板子单元（Panel Subunit）以外的子单元。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gadef2624ec50c0bb138d7eae8525784c5"></a>

### `bt_avrcp_ct_get_total_number_of_items()`

```c
int bt_avrcp_ct_get_total_number_of_items ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t scope )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

获取条目总数（Get Total Number Of Items）。

此函数向远端设备发送 AVRCP 协议数据单元（PDU）`GET_TOTAL_NUMBER_OF_ITEMS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `scope` | 范围（Scope），参见 `bt_avrcp_scope_t`。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga0d59de3bbcfd036f267354fa4ee290dd"></a>

### `bt_avrcp_ct_get_unit_info()`

```c
int bt_avrcp_ct_get_unit_info ( struct bt_avrcp_ct * ct, uint8_t tid )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

获取 AVRCP 单元信息（Unit Info）。

此函数获取整个 AV/C 单元（Unit）的相关信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gae8cb7f3d8dbb8ae91167916e5c99ec39"></a>

### `bt_avrcp_ct_inform_batt_status_of_ct()`

```c
int bt_avrcp_ct_inform_batt_status_of_ct ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t battery_status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `INFORM_BATT_STATUS_OF_CT` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `battery_status` | 电池状态值，类型为 `bt_avrcp_battery_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gab268d545750bd22b0625779d735d344a"></a>

### `bt_avrcp_ct_inform_displayable_char_set()`

```c
int bt_avrcp_ct_inform_displayable_char_set ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `INFORM_DISPLAYABLE_CHAR_SET` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `INFORM_DISPLAYABLE_CHAR_SET` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_inform_displayable_char_set_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gadfafc60888e73a92c1d16fe9696565df"></a>

### `bt_avrcp_ct_list_player_app_setting_attrs()`

```c
int bt_avrcp_ct_list_player_app_setting_attrs ( struct bt_avrcp_ct * ct, uint8_t tid )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `LIST_PLAYER_APP_SETTING_ATTRS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga11f34256317663cec599d7cb1b250243"></a>

### `bt_avrcp_ct_list_player_app_setting_vals()`

```c
int bt_avrcp_ct_list_player_app_setting_vals ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t attr_id )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `LIST_PLAYER_APP_SETTING_VALS` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `attr_id` | 要列出其可能取值的播放器应用设置属性 ID，例如均衡器（Equalizer）、重复模式（Repeat Mode）、随机播放（Shuffle）和扫描（Scan）。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga16f8e224bc80ed0bca5ce04a93670320"></a>

### `bt_avrcp_ct_passthrough()`

```c
int bt_avrcp_ct_passthrough ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t opid, uint8_t state, const uint8_t * payload, uint8_t len )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 AVRCP 透传命令（Pass Through Command）。

此函数向远端设备发送直通命令（Pass Through Command）。直通命令用于将用户操作信息从控制器（CT）传递到目标端（TG）的面板子单元（Panel Subunit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `opid` | 用户操作 ID（Operation ID），参见 `bt_avrcp_opid_t`。 |
| `state` | 按钮状态（Button State），参见 `bt_avrcp_button_state_t`。 |
| `payload` | 直通命令（Pass Through Command）的载荷（Payload）。如果 `len` 非零，则不得为 `NULL`。 |
| `len` | 载荷（Payload）的长度。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gab8d46ac46d35b711209f9a8572c1f8bd"></a>

### `bt_avrcp_ct_play_item()`

```c
int bt_avrcp_ct_play_item ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `PLAY_ITEM` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `PLAY_ITEM` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_play_item_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga7129d3dc93ea77140ae192099f4a4f92"></a>

### `bt_avrcp_ct_register_cb()`

```c
int bt_avrcp_ct_register_cb ( const struct bt_avrcp_ct_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

注册回调（Callback）。

注册 AVRCP 回调（Callbacks），用于监控状态并与远端设备交互。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | AVRCP 控制器（CT）回调函数。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gab2e6565627deefd8dc5c79a08d02aa85"></a>

### `bt_avrcp_ct_register_notification()`

```c
int bt_avrcp_ct_register_notification ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t event_id, uint32_t interval, bt_avrcp_notify_changed_cb_t cb )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

通过回调注册 AVRCP 变化通知（Changed Notifications）。

此函数向目标设备（Target Device）注册通知（Notifications）。通知响应将通过提供的回调函数接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `event_id` | 要注册的事件 ID（Event ID），参见 `bt_avrcp_evt_t`。 |
| `interval` | 位置变化事件（Position Changed Events）的播放间隔（Playback Interval）。对于其他事件，此值设为 0 以忽略它。 |
| `cb` | 用于处理已变化通知响应（Changed Notification Response）的回调函数。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gab8b765fab76ba2585730f328c0abc167"></a>

### `bt_avrcp_ct_search()`

```c
int bt_avrcp_ct_search ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

搜索（Search）。

此函数向远端设备发送 AVRCP 协议数据单元（PDU）`SEARCH`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Search command` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_search_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga27b0a9e2d86fcc91d2e7b19f1bc5df2d"></a>

### `bt_avrcp_ct_set_absolute_volume()`

```c
int bt_avrcp_ct_set_absolute_volume ( struct bt_avrcp_ct * ct, uint8_t tid, uint8_t absolute_volume )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送设置绝对音量命令（Set Absolute Volume），用于控制方（CT）。

此函数向目标端（TG）发送设置绝对音量（Set Absolute Volume）命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 命令的事务标签（Transaction Label），有效范围为 0～15。 |
| `absolute_volume` | 绝对音量值，范围为 `0x00–0x7F`。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga69561453ade3e8ba07b2122efcddcfad"></a>

### `bt_avrcp_ct_set_addressed_player()`

```c
int bt_avrcp_ct_set_addressed_player ( struct bt_avrcp_ct * ct, uint8_t tid, uint16_t player_id )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `SET_ADDRESSED_PLAYER` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `player_id` | 要设为受控播放器（Addressed Player）的播放器 ID。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gab0886ea325dddc67167bed86ec6c31e9"></a>

### `bt_avrcp_ct_set_browsed_player()`

```c
int bt_avrcp_ct_set_browsed_player ( struct bt_avrcp_ct * ct, uint8_t tid, uint16_t player_id )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

设置要浏览的播放器（Browsed Player）。

此函数在远端设备上设置被浏览播放器（Browsed Player）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制器（CT）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `player_id` | 要设为浏览播放器（Browsed Player）的播放器 ID。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga962f7727f10ca2827c60d4d9a5dd2bde"></a>

### `bt_avrcp_ct_set_player_app_setting_val()`

```c
int bt_avrcp_ct_set_player_app_setting_val ( struct bt_avrcp_ct * ct, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `SET_PLAYER_APP_SETTING_VAL` 对应的音视频遥控配置文件（AVRCP）厂商相关命令（Vendor Dependent Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `SET_PLAYER_APP_SETTING_VAL` 请求载荷（Request Payload）的命令缓冲区，格式为 `bt_avrcp_set_player_app_setting_val_cmd`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga7ec468b9a50413ba478186c88728e13b"></a>

### `bt_avrcp_disconnect()`

```c
int bt_avrcp_disconnect ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

断开 AVRCP 连接（Disconnect）。

此函数关闭 AVCTP 的 L2CAP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向 `bt_conn` 结构体的指针。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gad0d937d50eccfbedc81cc575a3e238f2"></a>

### `bt_avrcp_tg_absolute_volume()`

```c
int bt_avrcp_tg_absolute_volume ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, uint8_t absolute_volume )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送设置绝对音量响应（Set Absolute Volume），用于目标方（TG）。

此函数向控制器（CT）发送设置绝对音量（Set Absolute Volume）响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `absolute_volume` | 绝对音量值，范围为 `0x00–0x7F`。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gafc84238ea566bef4d2789e7cdba193dd"></a>

### `bt_avrcp_tg_add_to_now_playing()`

```c
int bt_avrcp_tg_add_to_now_playing ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_ADD_TO_NOW_PLAYING` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gaad6d011fe84aaa6cec8665aa87d4cc41"></a>

### `bt_avrcp_tg_browsing_general_reject()`

```c
int bt_avrcp_tg_browsing_general_reject ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

在 AVRCP 浏览通道（Browsing Channel）上发送通用拒绝响应（General Reject Response），用于目标方（TG）。

当请求协议数据单元（PDU）无法理解、参数无效或无法按常规方式处理时，此 API 针对具体浏览命令（Browsing Command）发送 `GENERAL_REJECT` 响应，其 PDU ID 为 `BT_AVRCP_PDU_ID_GENERAL_REJECT`。浏览载荷（Browsing Payload）的格式为：`PDU_ID (0xA0) + ParameterLength (0x0001) + status (1B)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（Target）实例。 |
| `tid` | 请求的事务标签（Transaction Label），范围为 0～15。 |
| `status` | 状态码（Status Code，`bt_avrcp_status_t`），例如 `BT_AVRCP_STATUS_INVALID_COMMAND`（0x00）、`BT_AVRCP_STATUS_INVALID_PARAMETER`（0x01）等。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga851b0c30ac0b382658b5ce040d7755eb"></a>

### `bt_avrcp_tg_change_path()`

```c
int bt_avrcp_tg_change_path ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, uint32_t num_items )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送更改路径响应（Change Path Response）。

应用程序调用此函数发送 `CHANGE_PATH` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `status` | 操作状态，参见 `bt_avrcp_status_t`。 |
| `num_items` | 新文件夹中的条目数量，仅在 `status` 为 `BT_AVRCP_STATUS_OPERATION_COMPLETED` 时有效。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gad160c86f1647509e10d741284b9bbb03"></a>

### `bt_avrcp_tg_get_caps()`

```c
int bt_avrcp_tg_get_caps ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 `GET_CAPABILITIES` 响应（Response）。

应用程序调用此函数发送 `GET_CAPABILITIES` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `GET_CAPS` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_get_caps_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gab18ce4d9348698272eedff52ddb3052e"></a>

### `bt_avrcp_tg_get_curr_player_app_setting_val()`

```c
int bt_avrcp_tg_get_curr_player_app_setting_val ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_CURR_PLAYER_APP_SETTING_VAL` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `GET_CURR_PLAYER_APP_SETTING_VAL` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_get_curr_player_app_setting_val_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga81333eaee7ca1838424ce9b513e6e2c5"></a>

### `bt_avrcp_tg_get_element_attrs()`

```c
int bt_avrcp_tg_get_element_attrs ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_ELEMENT_ATTRS` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `GET_ELEMENT_ATTRS` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_get_element_attrs_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga6261635bf3925766bb7af10696df6fd5"></a>

### `bt_avrcp_tg_get_folder_items()`

```c
int bt_avrcp_tg_get_folder_items ( struct bt_avrcp_tg * tg, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送获取文件夹条目响应（Get Folder Items Response）。

应用程序调用此函数发送 `GET_FOLDER_ITEMS` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Get Folder Items` 响应参数的响应缓冲区（Response Buffer）。操作成功时，应用程序应按 `bt_avrcp_get_folder_items_rsp` 定义的格式组织此载荷。如果 `status` 表示拒绝错误或操作未完成，`buf` 只包含一个状态字节。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga509746020e487d769f94174a4071b673"></a>

### `bt_avrcp_tg_get_item_attrs()`

```c
int bt_avrcp_tg_get_item_attrs ( struct bt_avrcp_tg * tg, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送获取条目属性响应（Get Item Attributes Response）。

应用程序调用此函数发送 `GET_ITEM_ATTRIBUTES` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Get Item Attributes` 响应参数的响应缓冲区（Response Buffer）。操作成功时，应用程序应按 `bt_avrcp_get_item_attrs_rsp` 定义的格式组织此载荷。如果 `status` 表示拒绝错误或操作未完成，`buf` 只包含一个状态字节。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga4f37f0c696ea98f44bd5e8ce2905d9f4"></a>

### `bt_avrcp_tg_get_play_status()`

```c
int bt_avrcp_tg_get_play_status ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAY_STATUS` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `GET_PLAY_STATUS` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_get_play_status_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga123f5528b62f48faaf020f19dcc321c1"></a>

### `bt_avrcp_tg_get_player_app_setting_attr_text()`

```c
int bt_avrcp_tg_get_player_app_setting_attr_text ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_ATTR_TEXT` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_get_player_app_setting_attr_text_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga8cc324a60a3480524336bc399d62c1ed"></a>

### `bt_avrcp_tg_get_player_app_setting_val_text()`

```c
int bt_avrcp_tg_get_player_app_setting_val_text ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_VAL_TEXT` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `GET_PLAYER_APP_SETTING_VAL_TEXT` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_get_player_app_setting_val_text_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gaf521ea00d597fced528d86befd9b5bbb"></a>

### `bt_avrcp_tg_get_total_number_of_items()`

```c
int bt_avrcp_tg_get_total_number_of_items ( struct bt_avrcp_tg * tg, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送获取条目总数响应（Get Total Number Of Items Response）。

应用程序调用此函数发送 `GET_TOTAL_NUMBER_OF_ITEMS` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Get Total Number Of Items` 响应参数的响应缓冲区（Response Buffer）。操作成功时，应用程序应按 `bt_avrcp_get_total_number_of_items_rsp` 定义的格式组织此载荷。如果 `status` 表示拒绝错误或操作未完成，`buf` 只包含一个状态字节。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gaa2aca5a011a99a20a3bd3fd7154a864a"></a>

### `bt_avrcp_tg_inform_batt_status_of_ct()`

```c
int bt_avrcp_tg_inform_batt_status_of_ct ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_INFORM_BATT_STATUS_OF_CT` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gadda57eb5c28f6b77bda5efe9286bc5f4"></a>

### `bt_avrcp_tg_inform_displayable_char_set()`

```c
int bt_avrcp_tg_inform_displayable_char_set ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_INFORM_DISPLAYABLE_CHAR_SET` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gab442ef3962bebd8dbe0d5681498f8453"></a>

### `bt_avrcp_tg_list_player_app_setting_attrs()`

```c
int bt_avrcp_tg_list_player_app_setting_attrs ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_ATTRS` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `LIST_PLAYER_APP_SETTING_ATTRS` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_list_player_app_setting_attrs_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="gae8b42aada8be4c9fac13fbd90e751a7b"></a>

### `bt_avrcp_tg_list_player_app_setting_vals()`

```c
int bt_avrcp_tg_list_player_app_setting_vals ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_VALS` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `buf` | 包含 `LIST_PLAYER_APP_SETTING_VALS` 载荷（Payload）的响应缓冲区，格式为 `bt_avrcp_list_player_app_setting_vals_rsp`。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga1ef0065fd9fa73bcd03491fe700fac65"></a>

### `bt_avrcp_tg_notification()`

```c
int bt_avrcp_tg_notification ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status, uint8_t event_id, struct bt_avrcp_event_data * data )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送通知响应（Notification Response）。

此函数由 AVRCP 目标端（TG）向控制器（CT）发送之前已注册事件的通知响应（Notification Response）。响应可能为：

- `INTERIM`（临时）：对给定 `event_id` 首次调用时发送，表示正在监视该事件。
- `CHANGED`（已变化）：同一 `event_id` 的事件状态发生变化后，在下一次调用时发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |
| `event_id` | 本次发送通知的 AVRCP 事件 ID（Event ID），参见 `bt_avrcp_evt_t`。 |
| `data` | 指向包含事件特定数据的 `bt_avrcp_event_data` 结构。联合体（Union）的内容取决于 `event_id`。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

**说明（Note）**：注意：对于给定的 `event_id`，第一次成功调用发送 `INTERIM`（临时）响应；对同一 `event_id` 的下一次成功调用发送 `CHANGED`（已变化）响应。如果 `status` 为 `BT_AVRCP_STATUS_NOT_IMPLEMENTED`，则发送 `NOT_IMPLEMENTED`（未实现）响应；如果 `status` 为其他非 `SUCCESS` 值，则发送 `REJECTED`（拒绝）响应。

<a id="ga5f72112c0887ed3efc3455ead567126d"></a>

### `bt_avrcp_tg_play_item()`

```c
int bt_avrcp_tg_play_item ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_PLAY_ITEM` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga7ba6030ff079e3c47bf6e5838b61ebdb"></a>

### `bt_avrcp_tg_register_cb()`

```c
int bt_avrcp_tg_register_cb ( const struct bt_avrcp_tg_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

注册回调（Callback）。

注册 AVRCP 回调（Callbacks），用于监控状态并与远端设备交互。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | AVRCP 目标端（TG）回调函数。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga136fda008bf5d5f7e9cad3855a4173f9"></a>

### `bt_avrcp_tg_search()`

```c
int bt_avrcp_tg_search ( struct bt_avrcp_tg * tg, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送搜索响应（Search Response）。

应用程序调用此函数发送 `SEARCH` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含 `Search` 响应参数的响应缓冲区（Response Buffer）。操作成功时，应用程序应按 `bt_avrcp_search_rsp` 定义的格式组织此载荷。如果 `status` 表示拒绝错误或操作未完成，`buf` 只包含一个状态字节。注意：所有多八位字节字段均采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gac92854e7f567f6088a5cf3ad3c209343"></a>

### `bt_avrcp_tg_send_passthrough_rsp()`

```c
int bt_avrcp_tg_send_passthrough_rsp ( struct bt_avrcp_tg * tg, uint8_t tid, bt_avrcp_rsp_t result, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送 AVRCP 透传响应（Pass Through Response）。

应用程序调用此函数发送 `Pass Through` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `result` | 响应码（Response Code），参见 `bt_avrcp_rsp_t`；支持 `0x8`（`NOT_IMPLEMENTED`）、`0x9`（`ACCEPTED`）、`0xA`（`REJECTED`）。 |
| `buf` | 包含 `PASS THROUGH` 命令载荷（Payload）的缓冲区。应用程序可按 `bt_avrcp_passthrough_rsp` 定义的格式构造此载荷。注意：数据采用大端格式（Big-endian）编码。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gabc170c5c0aa39827b4efc43880dbf258"></a>

### `bt_avrcp_tg_send_subunit_info_rsp()`

```c
int bt_avrcp_tg_send_subunit_info_rsp ( struct bt_avrcp_tg * tg, uint8_t tid )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送子单元信息响应（Subunit Info Response）。

应用程序调用此函数发送 `subunit info` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gaecb26512e8b1d267bca0d3ea01438c9b"></a>

### `bt_avrcp_tg_send_unit_info_rsp()`

```c
int bt_avrcp_tg_send_unit_info_rsp ( struct bt_avrcp_tg * tg, uint8_t tid, struct bt_avrcp_unit_info_rsp * rsp )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送单元信息响应（Unit Info Response）。

应用程序调用此函数发送 `unit info` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `rsp` | 单元信息（UNIT INFO）命令的响应。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="gadcf3f892a1d492a2743cdb4f8d205505"></a>

### `bt_avrcp_tg_set_addressed_player()`

```c
int bt_avrcp_tg_set_addressed_player ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_SET_ADDRESSED_PLAYER` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。

<a id="ga15bf2602f37ef83b3bcefd85920658eb"></a>

### `bt_avrcp_tg_set_browsed_player()`

```c
int bt_avrcp_tg_set_browsed_player ( struct bt_avrcp_tg * tg, uint8_t tid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送设置浏览播放器响应（Set Browsed Player Response）。

应用程序调用此函数发送 `set browsed player` 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）实例。 |
| `tid` | 响应的事务标签（Transaction Label），有效范围为 0～15。 |
| `buf` | 包含设置被浏览播放器（Set Browsed Player）响应数据的响应缓冲区（Response Buffer）。 |

**返回（Returns）**：返回值：成功时为 0，出错时为错误码（Error Code）。

<a id="ga9d471d9a932dfd43b71e894ddec013b4"></a>

### `bt_avrcp_tg_set_player_app_setting_val()`

```c
int bt_avrcp_tg_set_player_app_setting_val ( struct bt_avrcp_tg * tg, uint8_t tid, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

发送协议数据单元标识符（PDU ID）`BT_AVRCP_PDU_ID_SET_PLAYER_APP_SETTING_VAL` 对应的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 操作状态码（Status Code），参见 `bt_avrcp_status_t`。 |

返回（Returns）：成功时为0，否则为错误码。


## 2.8\_原页交叉引用（Cross References）

- [音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）](../api_hid_pipeline_topic_reference/P001_音频_视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）.md)
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
- [bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)
- [bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/bluetooth/classic/avrcp.h](../api_file_coap_phy_reference/P001_zephyr__bluetooth__classic__avrcp.h_文件参考.md)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__avrcp_html_ga3c997d96028343a0a5a4948dabe19b84"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="agroup__bt__avrcp_html_ga15f9f868b056f17ea12d96530b7da881"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga33825b183b12a2b29d5148a7366c0e77aeaba1597c6c1854d46df1eaaff8862a2"></a>
<a id="gga33825b183b12a2b29d5148a7366c0e77a4f7cb6c1917180ca96b10d2c73df9fad"></a>
<a id="gga33825b183b12a2b29d5148a7366c0e77adafb0292944a3d4236608ca13d900c98"></a>
<a id="gga33825b183b12a2b29d5148a7366c0e77a2883875f5d5441e7eb7976a38573c178"></a>
<a id="gga33825b183b12a2b29d5148a7366c0e77a72880bd811f5cf87fedfa0ff006412b4"></a>
<a id="gga15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3"></a>
<a id="gga15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706"></a>
<a id="ggac311dc7b5f99162b954271529eeb84eaa89fecce56afb09791a2253a7ad840430"></a>
<a id="ggac311dc7b5f99162b954271529eeb84eaa2a7b326aded772c09cf01387145d2802"></a>
<a id="gga02d67e84b4a48ebecf3b307cbd4bb61ca8914559b14b7529fc5f1df764036748d"></a>
<a id="gga02d67e84b4a48ebecf3b307cbd4bb61ca5cbd84478163171359044825050dd172"></a>
<a id="gga81330413af9eba049da6557b14ae082ca29f70165632222ae40ac3e44554130b0"></a>
<a id="gga2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04"></a>
<a id="gga2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce"></a>
<a id="gga2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb"></a>
<a id="gga2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290"></a>
<a id="gga2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7"></a>
<a id="ggae76f2666d10e6f46a1e5d68327fc7607a31587fdac3ae979f111287a924115d4a"></a>
<a id="ggae76f2666d10e6f46a1e5d68327fc7607aed029088c6bb73d0928ec19b9029e95e"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75a892f2928d634b675426f2fe597a45f6d"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75a25f8e3e08b5988e833eb0d47452d12a9"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75a412a9b7cbb891bc50fb77c1e6de9faaf"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75af4f9e221522cd57461920d22e7a290b9"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75afc4ef6f8a80a9067ad9dfd30bf2a6958"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75a9ff1d99bc0c83399961ef23d4a75f9b6"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75ae6237555b0051b2395e0bf2287e954c1"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75ab2b2287a0db9be97af8c20298bebba2d"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75ac0b720defdd8716d757e0c8a7e57db83"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75abd82dd6ba6d5d76cf22a8c703c76c6e0"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75ab6fdeacb536067660f754b3c586e073a"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75a8ac593400cda085fbdff36e403bd2a91"></a>
<a id="ggaf55aae17f67a1361279ae208b17e4a75a8d526498fdcb1380e8e3944da2a5ef85"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5a06308eb3786579cf5aeb0f19f0ab37ac"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5a702f9974cf5d51a77757fd7e1ef4ab0f"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5ab33fca5f57f5b80785df367ab788a8fc"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5a89aaeb11e807c44479ff47164d99c4f7"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5a0ab0ffb986db900ece2146a347dae06d"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5a708dfb5de11ae783b413d2d99202f9b5"></a>
<a id="gga09d191c490efcfb9f8139975090be0d5a0a60cb99cd19d203618b1264e2a3cca6"></a>
<a id="ggac02fed37e267996d4de50b06292d0668ad8dd8a59776d9d29655cbd083fae6535"></a>
<a id="ggac02fed37e267996d4de50b06292d0668aeb7289d0102af72c607d42a8f1c6dfa5"></a>
<a id="ggac02fed37e267996d4de50b06292d0668aca944e6647d353290b4e5c25fde28bd8"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592acce73266473e0a14580fa337d2fe53b3"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592a436c4847edcad7121f7d2ed97169fe61"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592a2b7e8439c8050cdeda97c43d07774001"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592ac66e18f0843901209f9004a62ab55624"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592a3dcfd47034d7890e80a05fd4f600f6bf"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592a8fd312d2869f38b6d7446716a30392b1"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592a0ba1f760a733cd00923970d01bb85293"></a>
<a id="gga0ebc5d2657688b70119e11ac20d24592a958ef736372f39d8e180f8fdeb025121"></a>
<a id="ggac927c7e7c59f6f0e6243ca0887945d5aa9847baed2a6d09d4ac81039c7302832b"></a>
<a id="ggac927c7e7c59f6f0e6243ca0887945d5aa76bd7c8c80d6ad9985430148cfd44e82"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d"></a>
<a id="gga3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d"></a>
<a id="gga433775fa2758df43ee1d26c78e9122d1a71ddb79b742f9acbd5d14a7639a09fe8"></a>
<a id="gga433775fa2758df43ee1d26c78e9122d1ae620f45ad0ecb63be8a8a0b446b5817a"></a>
<a id="gga433775fa2758df43ee1d26c78e9122d1a2509a9b77091db4ff185448d17d44244"></a>
<a id="gga433775fa2758df43ee1d26c78e9122d1ab97050ae05ba6cdff052ac6181eed119"></a>
<a id="gga433775fa2758df43ee1d26c78e9122d1a5dedf3d49340e3371b118215414aa8d8"></a>
<a id="gga433775fa2758df43ee1d26c78e9122d1a05cd93eef7ee39f8e7111d23131de6de"></a>
<a id="gga8047dddc873566ee372e77c6eecd008fa226313d1f90779c47142ba4966ee968f"></a>
<a id="gga8047dddc873566ee372e77c6eecd008fa4cfad017fc5870b099a8d4521e422dca"></a>
<a id="gga8047dddc873566ee372e77c6eecd008fa278d43d52aa33cb54705e7d75ddd98b7"></a>
<a id="gga8047dddc873566ee372e77c6eecd008fa4157b63056caa15282fab2712a855cec"></a>
<a id="gga22bf1b16b383ef473624769ae6ae893aa4192bdec6c45e76769ca55ee6a3ab190"></a>
<a id="gga22bf1b16b383ef473624769ae6ae893aa24914c843056b7fc58f534aec1693948"></a>
<a id="gga22bf1b16b383ef473624769ae6ae893aabf4b962a513c908baa7fac9454511aaa"></a>
<a id="gga22bf1b16b383ef473624769ae6ae893aa926fe6e1fc4fee9bb108c9b0c2e46c9a"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988"></a>
<a id="ggaba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88"></a>
<a id="gga4426612c49f8456f2543f373db72d3f2ae12700ce9b55f758572b0fbfab18ea90"></a>
<a id="gga4426612c49f8456f2543f373db72d3f2a0819f5ffd937f0d4a379ae5e7b9a2ebf"></a>
<a id="gga4426612c49f8456f2543f373db72d3f2abde23c31bbb6ab1c7daf85e3cd977cf9"></a>
<a id="ggaabab9a4f37b3f9653ca95dd4b5944707a7a388bb84fbe14f8931ab9bf41b9823d"></a>
<a id="ggaabab9a4f37b3f9653ca95dd4b5944707a37002574948081d7b42001a62755636b"></a>
<a id="ggaabab9a4f37b3f9653ca95dd4b5944707a4db7699a5f22c8d5986f6f1ba7219dac"></a>
<a id="ggaabab9a4f37b3f9653ca95dd4b5944707a7baa6442aafc4d00635df52f44d0d608"></a>
<a id="gga8e6ce46ba46268c2c80f4ec7570859c8aac7dce4d43e84c3d80f9eb0791db7a8d"></a>
<a id="gga8e6ce46ba46268c2c80f4ec7570859c8ab36d34793768772409794570f740964a"></a>
<a id="gga8e6ce46ba46268c2c80f4ec7570859c8a11a1b2613018ad24861a72313af4189a"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a14e183c33a64cdac271ee7f320796bd6"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a8a767466ac8069e20f6d9e0f30c33420"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a7cba04973b3753b50f63e6b0bc205638"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0af48dcc2c65e4af461c1a6ece622a2f5a"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0ad3a41ce04f27cc349c7466aae18bcee2"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a0e77e1782b5a0f88f4d45b6560df2b09"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a448e1c0383e4e4b5fc3c0c80e2040af9"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a6fee8c927f897fff59b7690c3e1732c2"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a9f552377c6bb93b3e52b29228a6feaa5"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0aaddaf4f6439aa6a52e3a4fdbb3f0c071"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a81094560261826c16be6ebba9d99081c"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a2f8ca7c1fe4ba52a1a418612c094158a"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0ae63cf3ffada01f268498151d88c3a3ec"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a359810fbbdf875adb89a192deaae6a6d"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a4ee781cc845d8b1211217f8338b97023"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a402038758703ee9f8543ad546681a3c5"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a5cd415ba8d307dc5153a9a0b2f9958e3"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a28925d094d4c3e55b259a55440a5c044"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a3dfa01e069c517e7e466fa6edcc1c9cb"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a033e10d03bf56df95ec1e888a07cedf9"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a5544c22cad94dadb9eccf47669fabafb"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a43e59407a44f87d85fa71cdb627524e3"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0af72a55b60fda9c157cdef8b1c6038780"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0a14868dd213f59e09dbdb066d5ca39c96"></a>
<a id="gga52368f4cc655bab75f96da80ddaaabe0afbff25149bb9c35756dfb7bb6f2516c3"></a>
<a id="gga78ba828636b731b2c43e088a581bfee9a6db3104fa9727594b842b4ae9b64a605"></a>
<a id="gga78ba828636b731b2c43e088a581bfee9a8be8c211cd26a849c1c89e482aa10030"></a>
<a id="gga128458626d5fe6ffbac7cf97867621aaaea875986bd59d1da9650c5d5f2de20a2"></a>
<a id="gga128458626d5fe6ffbac7cf97867621aaa4d4a454f0b8a0a84b557a4075eff1215"></a>
<a id="gga128458626d5fe6ffbac7cf97867621aaa1e1ed998f24038e6095f802144e240c2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_通用音频分配编号（Generic Audio Assigned Numbers）.md) · [返回大纲](大纲.md) · [下一章](P003_GATT 服务器 API.md)
