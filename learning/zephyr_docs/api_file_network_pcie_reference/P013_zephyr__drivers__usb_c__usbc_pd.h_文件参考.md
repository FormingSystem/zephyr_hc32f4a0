---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-13
title: zephyr__drivers__usb_c__usbc_pd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_drivers\_\_usb\_c\_\_usbc\_pd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB-C驱动使用的USB-C电力传输（Power Delivery）API。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

用于 USB-C 驱动的 USB-C 电力传输 API（USB-C Power Delivery API）。本文件中的信息取自《USB PD 规范》（USB PD Specification）修订版 3.0、版本 2.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_pd_5Fheader"></a>

```c
union pd_header
```

相关声明：[pd_header](../device_power_control_model_reference/P114_pd_header_联合体.md)。

构造电力传输（PD）消息头部，见表6-1“消息头部”。

<a id="r_pd_5Fext_5Fheader"></a>

```c
union pd_ext_header
```

相关声明：[pd_ext_header](../device_power_control_model_reference/P111_pd_ext_header_联合体.md)。

构造扩展消息头部（Extended Message Header），见表6-3。

<a id="r_pd_5Ffixed_5Fsupply_5Fpdo_5Fsource"></a>

```c
union pd_fixed_supply_pdo_source
```

相关声明：[pd_fixed_supply_pdo_source](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md)。

创建固定供电PDO供电端（Source）的值，见表6-9“固定供电PDO—供电端”。

<a id="r_pd_5Ffixed_5Fsupply_5Fpdo_5Fsink"></a>

```c
union pd_fixed_supply_pdo_sink
```

相关声明：[pd_fixed_supply_pdo_sink](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md)。

创建固定供电PDO受电端（Sink）的值，见表6-14“固定供电PDO—受电端”。

<a id="r_pd_5Fvariable_5Fsupply_5Fpdo_5Fsource"></a>

```c
union pd_variable_supply_pdo_source
```

相关声明：[pd_variable_supply_pdo_source](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md)。

创建可变供电PDO供电端（Source）的值，见表6-11“可变供电（非电池）PDO—供电端”。

<a id="r_pd_5Fvariable_5Fsupply_5Fpdo_5Fsink"></a>

```c
union pd_variable_supply_pdo_sink
```

相关声明：[pd_variable_supply_pdo_sink](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md)。

创建可变供电PDO受电端（Sink）的值，见表6-15“可变供电（非电池）PDO—受电端”。

<a id="r_pd_5Fbattery_5Fsupply_5Fpdo_5Fsource"></a>

```c
union pd_battery_supply_pdo_source
```

相关声明：[pd_battery_supply_pdo_source](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md)。

创建电池供电PDO供电端（Source）的值，见表6-12“电池供电PDO—供电端”。

<a id="r_pd_5Fbattery_5Fsupply_5Fpdo_5Fsink"></a>

```c
union pd_battery_supply_pdo_sink
```

相关声明：[pd_battery_supply_pdo_sink](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md)。

创建电池供电PDO受电端（Sink）的值，见表6-16“电池供电PDO—受电端”。

<a id="r_pd_5Faugmented_5Fsupply_5Fpdo_5Fsource"></a>

```c
union pd_augmented_supply_pdo_source
```

相关声明：[pd_augmented_supply_pdo_source](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md)。

创建增广供电PDO供电端（Source）的值，见表6-13“可编程电源APDO—供电端”。

<a id="r_pd_5Faugmented_5Fsupply_5Fpdo_5Fsink"></a>

```c
union pd_augmented_supply_pdo_sink
```

相关声明：[pd_augmented_supply_pdo_sink](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md)。

创建增广供电PDO受电端（Sink）的值，见表6-17“可编程电源APDO—受电端”。

<a id="r_pd_5Frdo"></a>

```c
union pd_rdo
```

相关声明：[pd_rdo](../device_power_control_model_reference/P115_pd_rdo_联合体.md)。

请求数据对象（Request Data Object，RDO）应由提出供电请求的受电端（Sink）返回。

<a id="r_pd_5Fmsg"></a>

```c
struct pd_msg
```

相关声明：[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

电力传输消息（Power Delivery Message）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_ga998b67d43674778e42f6c49ec6a99af4"></a>

```c
#define PD_MAX_EXTENDED_MSG_LEGACY_LEN 26
```

相关声明：[PD_MAX_EXTENDED_MSG_LEGACY_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga998b67d43674778e42f6c49ec6a99af4)。

非扩展消息（Non-Extended Message）的最大长度，以字节为单位。

<a id="r_gabdb041542baaf2277e054dd9e3928b16"></a>

```c
#define PD_MAX_EXTENDED_MSG_LEN 260
```

相关声明：[PD_MAX_EXTENDED_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabdb041542baaf2277e054dd9e3928b16)。

扩展消息（Extended Message）的最大长度，以字节为单位。

<a id="r_gac0588f94c1792b5b8fefa6a60c1b237b"></a>

```c
#define PD_MAX_EXTENDED_MSG_CHUNK_LEN 26
```

相关声明：[PD_MAX_EXTENDED_MSG_CHUNK_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac0588f94c1792b5b8fefa6a60c1b237b)。

分块消息（Chunked Message）的最大长度，以字节为单位。

<a id="r_ga266725d0496981ee92b0008afe43505e"></a>

```c
#define PD_T_TYPEC_SINK_WAIT_CAP_MIN_MS 310
```

相关声明：[PD_T_TYPEC_SINK_WAIT_CAP_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga266725d0496981ee92b0008afe43505e)。

受电端（Sink）发送硬复位（Hard Reset）之前，等待 `Source_Capabilities` 消息的最短时间。参见表 6-61“时间值”（Time Values）。参数名称：`tTypeCSinkWaitCap`。

<a id="r_gae32afec56f34841200188e64dc1ab9ca"></a>

```c
#define PD_T_TYPEC_SINK_WAIT_CAP_MAX_MS 620
```

相关声明：[PD_T_TYPEC_SINK_WAIT_CAP_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae32afec56f34841200188e64dc1ab9ca)。

受电端（Sink）发送硬复位（Hard Reset）之前，等待 `Source_Capabilities` 消息的最短时间。参见表 6-61“时间值”（Time Values）。参数名称：`tTypeCSinkWaitCap`。

<a id="r_gac3a939394dab5a5038801f9a6b2dcd30"></a>

```c
#define PD_V_SAFE_0V_MAX_MV 800
```

相关声明：[PD_V_SAFE_0V_MAX_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac3a939394dab5a5038801f9a6b2dcd30)。

“零伏”状态下 VBUS 的最大安全工作电压（Maximum Safe Operating Voltage）。

<a id="r_gad4f0e12b7f0e2ccd6aee73cf1525b27c"></a>

```c
#define PD_V_SAFE_5V_MIN_MV 4750
```

相关声明：[PD_V_SAFE_5V_MIN_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad4f0e12b7f0e2ccd6aee73cf1525b27c)。

5 V 状态下 VBUS 的最小安全工作电压（Minimum Safe Operating Voltage）。

<a id="r_gad5667f26343d4601c9fd5c5e9d046802"></a>

```c
#define PD_T_SAFE_0V_MAX_MS 650
```

相关声明：[PD_T_SAFE_0V_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad5667f26343d4601c9fd5c5e9d046802)。

达到 `PD_V_SAFE_0V_MV max` 的时间，以毫秒为单位。

<a id="r_ga123abee7651bca30a3e6ec2956eb0563"></a>

```c
#define PD_T_SAFE_5V_MAX_MS 275
```

相关声明：[PD_T_SAFE_5V_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga123abee7651bca30a3e6ec2956eb0563)。

达到 `PD_V_SAFE_5V_MV max` 的时间，以毫秒为单位。

<a id="r_gab6c168d490983a136c184bbe3ed9e7c5"></a>

```c
#define PD_T_TX_TIMEOUT_MS 100
```

相关声明：[PD_T_TX_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab6c168d490983a136c184bbe3ed9e7c5)。

等待 Type-C 端口控制器（TCPC）完成发送的时间。

<a id="r_ga64b8c095dba137d7fe460ffe38f00ce5"></a>

```c
#define PD_T_HARD_RESET_COMPLETE_MIN_MS 4
```

相关声明：[PD_T_HARD_RESET_COMPLETE_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga64b8c095dba137d7fe460ffe38f00ce5)。

硬复位（Hard Reset）必须完成的最短时间。

<a id="r_ga2748e0775b50552cc7d26cb2b2d3103d"></a>

```c
#define PD_T_HARD_RESET_COMPLETE_MAX_MS 5
```

相关声明：[PD_T_HARD_RESET_COMPLETE_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga2748e0775b50552cc7d26cb2b2d3103d)。

硬复位（Hard Reset）必须完成的最长时间。

<a id="r_ga9722df85c1a842ff1661e534e88d472e"></a>

```c
#define PD_T_SENDER_RESPONSE_MIN_MS 24
```

相关声明：[PD_T_SENDER_RESPONSE_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga9722df85c1a842ff1661e534e88d472e)。

端口伙伴（Port Partner）必须发送响应的最短时间。参见表 6-68“时间值”（Time Values）。

<a id="r_gac905bf64de8a9f5acef6f8731c11d041"></a>

```c
#define PD_T_SENDER_RESPONSE_NOM_MS 27
```

相关声明：[PD_T_SENDER_RESPONSE_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac905bf64de8a9f5acef6f8731c11d041)。

端口伙伴（Port Partner）必须发送响应的标称时间（Nominal Time）。参见表 6-68“时间值”（Time Values）。

<a id="r_ga4b7c238e12770841b1852a0517b12071"></a>

```c
#define PD_T_SENDER_RESPONSE_MAX_MS 30
```

相关声明：[PD_T_SENDER_RESPONSE_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4b7c238e12770841b1852a0517b12071)。

端口伙伴（Port Partner）必须发送响应的最长时间。参见表 6-68“时间值”（Time Values）。

<a id="r_ga4726113aa8c0100fa1a88435d3a6b1d1"></a>

```c
#define PD_T_SPR_PS_TRANSITION_MIN_MS 450
```

相关声明：[PD_T_SPR_PS_TRANSITION_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4726113aa8c0100fa1a88435d3a6b1d1)。

标准功率范围模式（SPR Mode）下，电源切换到新电平的最短时间。参见表 6-68“时间值”（Time Values）。

<a id="r_ga01a2a71da7fdbe18d07dacb687f7d295"></a>

```c
#define PD_T_SPR_PS_TRANSITION_NOM_MS 500
```

相关声明：[PD_T_SPR_PS_TRANSITION_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga01a2a71da7fdbe18d07dacb687f7d295)。

标准功率范围模式（SPR Mode）下，电源切换到新电平的标称时间（Nominal Time）。参见表 6-68“时间值”（Time Values）。

<a id="r_ga7dac8d411d8f4651b177a6495146acb0"></a>

```c
#define PD_T_SPR_PS_TRANSITION_MAX_MS 550
```

相关声明：[PD_T_SPR_PS_TRANSITION_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga7dac8d411d8f4651b177a6495146acb0)。

标准功率范围模式（SPR Mode）下，电源切换到新电平的最长时间。参见表 6-68“时间值”（Time Values）。

<a id="r_ga7f9a916a88c626b76963a4950878fa20"></a>

```c
#define PD_T_EPR_PS_TRANSITION_MIN_MS 830
```

相关声明：[PD_T_EPR_PS_TRANSITION_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga7f9a916a88c626b76963a4950878fa20)。

扩展功率范围模式（EPR Mode）下，电源切换到新电平的最短时间。参见表 6-68“时间值”（Time Values）。

<a id="r_gabcd0576899a6ce1a147bffbb0c1b517f"></a>

```c
#define PD_T_EPR_PS_TRANSITION_NOM_MS 925
```

相关声明：[PD_T_EPR_PS_TRANSITION_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabcd0576899a6ce1a147bffbb0c1b517f)。

扩展功率范围模式（EPR Mode）下，电源切换到新电平的标称时间（Nominal Time）。参见表 6-68“时间值”（Time Values）。

<a id="r_gaaea48ba7ea96b304b18293c202325b0e"></a>

```c
#define PD_T_EPR_PS_TRANSITION_MAX_MS 1020
```

相关声明：[PD_T_EPR_PS_TRANSITION_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaaea48ba7ea96b304b18293c202325b0e)。

扩展功率范围模式（EPR Mode）下，电源切换到新电平的最长时间。参见表 6-68“时间值”（Time Values）。

<a id="r_ga4416cfc999de1ee2ed49ce89f54074b1"></a>

```c
#define PD_T_SINK_REQUEST_MIN_MS 100
```

相关声明：[PD_T_SINK_REQUEST_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4416cfc999de1ee2ed49ce89f54074b1)。

收到 `Wait` 消息后，发送另一个请求前应等待的最短时间。参见表 6-68“时间值”（Time Values）。

<a id="r_ga890ce7af4632f8a17b399f0821aee3cf"></a>

```c
#define PD_T_CHUNKING_NOT_SUPPORTED_MIN_MS 40
```

相关声明：[PD_T_CHUNKING_NOT_SUPPORTED_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga890ce7af4632f8a17b399f0821aee3cf)。

收到分块消息（Chunked Message）后，发送 `Not_Supported` 消息前应等待的最短时间。参见表 6-68“时间值”（Time Values）。

<a id="r_gad13130dbd7f6ed4276b1781c5bf2fb20"></a>

```c
#define PD_T_CHUNKING_NOT_SUPPORTED_NOM_MS 45
```

相关声明：[PD_T_CHUNKING_NOT_SUPPORTED_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad13130dbd7f6ed4276b1781c5bf2fb20)。

收到分块消息（Chunked Message）后，发送 `Not_Supported` 消息前应等待的标称时间（Nominal Time）。参见表 6-68“时间值”（Time Values）。

<a id="r_gaf28df42c00394f9d11dfade2cae910d4"></a>

```c
#define PD_T_CHUNKING_NOT_SUPPORTED_MAX_MS 50
```

相关声明：[PD_T_CHUNKING_NOT_SUPPORTED_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaf28df42c00394f9d11dfade2cae910d4)。

收到分块消息（Chunked Message）后，发送 `Not_Supported` 消息前应等待的最长时间。参见表 6-68“时间值”（Time Values）。

<a id="r_ga953bdd1d4893bebcaeb6b4b95667fd94"></a>

```c
#define PD_CONVERT_BYTES_TO_PD_HEADER_COUNT(c)
```

相关声明：[PD_CONVERT_BYTES_TO_PD_HEADER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga953bdd1d4893bebcaeb6b4b95667fd94)。

将字节数转换为 PD 头部的数据对象数量（Data Object Count），每个数据对象占 4 字节。

<a id="r_gad5c5b108e4b255633a52d0de48adaf71"></a>

```c
#define PD_CONVERT_PD_HEADER_COUNT_TO_BYTES(c)
```

相关声明：[PD_CONVERT_PD_HEADER_COUNT_TO_BYTES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad5c5b108e4b255633a52d0de48adaf71)。

将 PD 头部的数据对象数量（Data Object Count）转换为字节数。

<a id="r_ga69f749b5c7ecf6368002aae12277ac9f"></a>

```c
#define SINK_TX_OK TC_RP_3A0
```

相关声明：[SINK_TX_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga69f749b5c7ecf6368002aae12277ac9f)、[TC_RP_3A0](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c)。

修订版 3.0 中受电端可发送状态（Sink Transmit “OK”）的冲突避免 Rp 值（Collision Avoidance Rp Values）。

<a id="r_gaa3ca6814e56859792dd5524fe8cef6b1"></a>

```c
#define SINK_TX_NG TC_RP_1A5
```

相关声明：[SINK_TX_NG](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaa3ca6814e56859792dd5524fe8cef6b1)、[TC_RP_1A5](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28)。

修订版 3.0 中受电端禁止发送状态（Sink Transmit “NO GO”）的冲突避免 Rp 值（Collision Avoidance Rp Values）。

<a id="r_gaf3acdb691327adef04e418d7ded3d883"></a>

```c
#define PD_GET_EXT_HEADER(c)
```

相关声明：[PD_GET_EXT_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaf3acdb691327adef04e418d7ded3d883)。

用于从消息的第一个 32 位字（32-bit Word）获取扩展头部（Extended Header）。

<a id="r_gab1716bb587e2b162415ea21e3c8d4e74"></a>

```c
#define PDO_MAX_DATA_OBJECTS 7
```

相关声明：[PDO_MAX_DATA_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab1716bb587e2b162415ea21e3c8d4e74)。

PDO：电源数据对象（Power Data Object）。RDO：请求数据对象（Request Data Object）。

<a id="r_ga65e9aa05457df787c5be6792ce725afd"></a>

```c
#define PD_CONVERT_MA_TO_FIXED_PDO_CURRENT(c)
```

相关声明：[PD_CONVERT_MA_TO_FIXED_PDO_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga65e9aa05457df787c5be6792ce725afd)。

将毫安（mA）转换为以 10 mA 为单位的固定 PDO 电流（Fixed PDO Current）。

<a id="r_gad79de03a60054be13c9757d933069fe2"></a>

```c
#define PD_CONVERT_MV_TO_FIXED_PDO_VOLTAGE(v)
```

相关声明：[PD_CONVERT_MV_TO_FIXED_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad79de03a60054be13c9757d933069fe2)。

将毫伏（mV）转换为以 50 mV 为单位的固定 PDO 电压（Fixed PDO Voltage）。

<a id="r_gaa0997fc5d7f26115c64f220d2ab91ef2"></a>

```c
#define PD_CONVERT_FIXED_PDO_CURRENT_TO_MA(c)
```

相关声明：[PD_CONVERT_FIXED_PDO_CURRENT_TO_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaa0997fc5d7f26115c64f220d2ab91ef2)。

将以 10 mA 为单位的固定 PDO 电流（Fixed PDO Current）转换为毫安（mA）。

<a id="r_gae9eaed8554f857d183e24b96cd69afe3"></a>

```c
#define PD_CONVERT_FIXED_PDO_VOLTAGE_TO_MV(v)
```

相关声明：[PD_CONVERT_FIXED_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae9eaed8554f857d183e24b96cd69afe3)。

将以 50 mV 为单位的固定 PDO 电压（Fixed PDO Voltage）转换为毫伏（mV）。

<a id="r_gab3ea3b392e8fc27b4f100a99988d0ca5"></a>

```c
#define PD_CONVERT_MA_TO_VARIABLE_PDO_CURRENT(c)
```

相关声明：[PD_CONVERT_MA_TO_VARIABLE_PDO_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab3ea3b392e8fc27b4f100a99988d0ca5)。

将毫安（mA）转换为以 10 mA 为单位的可变 PDO 电流（Variable PDO Current）。

<a id="r_gae729bb9b17bc0df4201ec27f1f506921"></a>

```c
#define PD_CONVERT_MV_TO_VARIABLE_PDO_VOLTAGE(v)
```

相关声明：[PD_CONVERT_MV_TO_VARIABLE_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae729bb9b17bc0df4201ec27f1f506921)。

将毫伏（mV）转换为以 50 mV 为单位的可变 PDO 电压（Variable PDO Voltage）。

<a id="r_ga9cd0c218385b400b3efe34474f546203"></a>

```c
#define PD_CONVERT_VARIABLE_PDO_CURRENT_TO_MA(c)
```

相关声明：[PD_CONVERT_VARIABLE_PDO_CURRENT_TO_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga9cd0c218385b400b3efe34474f546203)。

将以 10 mA 为单位的可变 PDO 电流（Variable PDO Current）转换为毫安（mA）。

<a id="r_ga4973b120261cde51c86c7b76422222fc"></a>

```c
#define PD_CONVERT_VARIABLE_PDO_VOLTAGE_TO_MV(v)
```

相关声明：[PD_CONVERT_VARIABLE_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4973b120261cde51c86c7b76422222fc)。

将以 50 mV 为单位的可变 PDO 电压（Variable PDO Voltage）转换为毫伏（mV）。

<a id="r_ga457907a516a2cf497569ce43561fe7dd"></a>

```c
#define PD_CONVERT_MW_TO_BATTERY_PDO_POWER(c)
```

相关声明：[PD_CONVERT_MW_TO_BATTERY_PDO_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga457907a516a2cf497569ce43561fe7dd)。

将毫瓦（mW）转换为以 250 mW 为单位的电池 PDO 功率（Battery PDO Power）。

<a id="r_ga4832aa2b18ff84bfcf3a252361628281"></a>

```c
#define PD_CONVERT_MV_TO_BATTERY_PDO_VOLTAGE(v)
```

相关声明：[PD_CONVERT_MV_TO_BATTERY_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4832aa2b18ff84bfcf3a252361628281)。

将输入值转换为以 50 mV 为单位的电池 PDO 电压（Battery PDO Voltage）；原文将输入单位写为毫瓦（Milliwatts）。

<a id="r_ga614dd17b2b98309a837be8e0578bb06b"></a>

```c
#define PD_CONVERT_BATTERY_PDO_POWER_TO_MW(c)
```

相关声明：[PD_CONVERT_BATTERY_PDO_POWER_TO_MW](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga614dd17b2b98309a837be8e0578bb06b)。

将以 250 mW 为单位的电池 PDO 功率（Battery PDO Power）转换为毫瓦（mW）。

<a id="r_ga74af9a3f10f1855d7322dc36fabdff1a"></a>

```c
#define PD_CONVERT_BATTERY_PDO_VOLTAGE_TO_MV(v)
```

相关声明：[PD_CONVERT_BATTERY_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga74af9a3f10f1855d7322dc36fabdff1a)。

将以 50 mV 为单位的电池 PDO 电压（Battery PDO Voltage）转换为毫伏（mV）。

<a id="r_ga1d73d5ffc7e6657dae81604ffb49b358"></a>

```c
#define PD_CONVERT_MA_TO_AUGMENTED_PDO_CURRENT(c)
```

相关声明：[PD_CONVERT_MA_TO_AUGMENTED_PDO_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga1d73d5ffc7e6657dae81604ffb49b358)。

将毫安（mA）转换为以 50 mA 为单位的增强 PDO 电流（Augmented PDO Current）。

<a id="r_ga1dd7da9850daae859d572d866c8c87e2"></a>

```c
#define PD_CONVERT_MV_TO_AUGMENTED_PDO_VOLTAGE(v)
```

相关声明：[PD_CONVERT_MV_TO_AUGMENTED_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga1dd7da9850daae859d572d866c8c87e2)。

将毫伏（mV）转换为以 100 mV 为单位的增强 PDO 电压（Augmented PDO Voltage）。

<a id="r_ga202d52036ee2fb6d6da3594c126cf82b"></a>

```c
#define PD_CONVERT_AUGMENTED_PDO_CURRENT_TO_MA(c)
```

相关声明：[PD_CONVERT_AUGMENTED_PDO_CURRENT_TO_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga202d52036ee2fb6d6da3594c126cf82b)。

将以 50 mA 为单位的增强 PDO 电流（Augmented PDO Current）转换为毫安（mA）。

<a id="r_ga8623c319b19e7444ba400c738848d9ae"></a>

```c
#define PD_CONVERT_AUGMENTED_PDO_VOLTAGE_TO_MV(v)
```

相关声明：[PD_CONVERT_AUGMENTED_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga8623c319b19e7444ba400c738848d9ae)。

将以 100 mV 为单位的增强 PDO 电压（Augmented PDO Voltage）转换为毫伏（mV）。

<a id="r_ga1bb5fd6bb6657399a75b095eb3442bde"></a>

```c
#define NUM_SOP_STAR_TYPES (PD_PACKET_DEBUG_PRIME_PRIME + 1)
```

相关声明：[NUM_SOP_STAR_TYPES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga1bb5fd6bb6657399a75b095eb3442bde)、[PD_PACKET_DEBUG_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1)。

有效发送类型数量（Number of Valid Transmit Types）。

<a id="define-members-0"></a>

### USB PD 3.1 修订版 1.6 表 6-70：计数器参数（USB PD 3.1 Rev 1.6, Table 6-70 Counter Parameters）

<a id="r_gac517b081df0572803efb374839846f1f"></a>

```c
#define PD_N_CAPS_COUNT 50
```

相关声明：[PD_N_CAPS_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac517b081df0572803efb374839846f1f)。

`CapsCounter` 用于统计供电端（Source）上电或硬复位（Hard Reset）之后已发送的 `Source_Capabilities` 消息数量。

<a id="r_gae4f479f2e77066a9b870263e3580f03f"></a>

```c
#define PD_N_HARD_RESET_COUNT 2
```

相关声明：[PD_N_HARD_RESET_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae4f479f2e77066a9b870263e3580f03f)。

远端设备没有响应时，使用 `HardResetCounter` 重试硬复位（Hard Reset），参见第 6.6.6 节。参数名称：`nHardResetCounter`。

<a id="define-members-1"></a>

### USB PD 3.1 修订版 1.6 表 6-68：时间值（USB PD 3.1 Rev 1.6, Table 6-68 Time Values）

<a id="r_ga9dfd6527539e996ccc110036545e61e7"></a>

```c
#define PD_T_NO_RESPONSE_MIN_MS 4500
```

相关声明：[PD_T_NO_RESPONSE_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga9dfd6527539e996ccc110036545e61e7)。

供电端（Source）的策略引擎（Policy Engine）使用 `NoResponseTimer` 判定端口伙伴（Port Partner）在硬复位（Hard Reset）后是否没有响应。

<a id="r_gaed69627505bdad8fb87c37084e2222e1"></a>

```c
#define PD_T_NO_RESPONSE_MAX_MS 5500
```

相关声明：[PD_T_NO_RESPONSE_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaed69627505bdad8fb87c37084e2222e1)。

供电端（Source）的策略引擎（Policy Engine）使用 `NoResponseTimer` 判定端口伙伴（Port Partner）在硬复位（Hard Reset）后是否没有响应。

<a id="r_ga87d0eb341d76c01b4b355c1d5a0354a1"></a>

```c
#define PD_T_PS_HARD_RESET_MIN_MS 25
```

相关声明：[PD_T_PS_HARD_RESET_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga87d0eb341d76c01b4b355c1d5a0354a1)。

供电端（Source）关闭向 VBUS 提供的电源之前，等待受电端（Sink）有足够时间处理硬复位信令（Hard Reset Signaling）的最短时间。参数名称：`tPSHardReset`。

<a id="r_ga2c4abfef3a581e19677d8f0d845a3582"></a>

```c
#define PD_T_PS_HARD_RESET_MAX_MS 35
```

相关声明：[PD_T_PS_HARD_RESET_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga2c4abfef3a581e19677d8f0d845a3582)。

供电端（Source）关闭向 VBUS 提供的电源之前，等待受电端（Sink）有足够时间处理硬复位信令（Hard Reset Signaling）的最长时间。参数名称：`tPSHardReset`。

<a id="r_gae7db10623f2ec064ef0351bb1bba51cd"></a>

```c
#define PD_T_SINK_TX_MIN_MS 16
```

相关声明：[PD_T_SINK_TX_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae7db10623f2ec064ef0351bb1bba51cd)。

供电端（Source）将 Rp 从 `SinkTxOk` 改为 `SinkTxNG` 后，通过发送消息启动原子消息序列（AMS）之前应等待的最短时间。

<a id="r_gadb55b3f260a17458bf479a7273fd946c"></a>

```c
#define PD_T_SINK_TX_MAX_MS 20
```

相关声明：[PD_T_SINK_TX_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gadb55b3f260a17458bf479a7273fd946c)。

供电端（Source）将 Rp 从 `SinkTxOk` 改为 `SinkTxNG` 后，通过发送消息启动原子消息序列（AMS）之前应等待的最长时间。

<a id="r_gabe6d36578671578eddf1381f58bcc80a"></a>

```c
#define PD_T_TYPEC_SEND_SOURCE_CAP_MIN_MS 100
```

相关声明：[PD_T_TYPEC_SEND_SOURCE_CAP_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabe6d36578671578eddf1381f58bcc80a)。

以下条件成立时，供电端（Source）发送 `Source_Capabilities` 消息前应等待的最短时间：1）端口已连接（Attached）。

<a id="r_ga105a9791e086ade590b6fd825fe5cded"></a>

```c
#define PD_T_TYPEC_SEND_SOURCE_CAP_MAX_MS 200
```

相关声明：[PD_T_TYPEC_SEND_SOURCE_CAP_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga105a9791e086ade590b6fd825fe5cded)。

以下条件成立时，供电端（Source）发送 `Source_Capabilities` 消息前应等待的最长时间：1）端口已连接（Attached）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_ga316dca7ed0b85f1aa224d7a767896328"></a>

```c
enum pdo_type { PDO_FIXED = 0 , PDO_BATTERY = 1 , PDO_VARIABLE = 2 , PDO_AUGMENTED = 3 }
```

相关声明：[pdo_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga316dca7ed0b85f1aa224d7a767896328)、[PDO_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328abbc517bb47b6bdc76e44b599523e0d93)、[PDO_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa)、[PDO_VARIABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624)、[PDO_AUGMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e)。

电源数据对象类型（Power Data Object Type）。参见表 6-7“电源数据对象”（Power Data Object）。

<a id="r_ga48b33240e19524ea003052103d310358"></a>

```c
enum pd_frs_type { FRS_NOT_SUPPORTED , FRS_DEFAULT_USB_POWER , FRS_1P5A_5V , FRS_3P0A_5V }
```

相关声明：[pd_frs_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga48b33240e19524ea003052103d310358)、[FRS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726)、[FRS_DEFAULT_USB_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed)、[FRS_1P5A_5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1)、[FRS_3P0A_5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba)。

USB Type-C 电流所需的快速角色交换（Fast Role Swap Required）。

<a id="r_gab68c6b6e33449c5ceadfc9217dd7a700"></a>

```c
enum pd_rev_type { PD_REV10 = 0 , PD_REV20 = 1 , PD_REV30 = 2 }
```

相关声明：[pd_rev_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab68c6b6e33449c5ceadfc9217dd7a700)、[PD_REV10](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9)、[PD_REV20](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae)、[PD_REV30](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a)。

协议修订版（Protocol Revision）。

<a id="r_gad2df13a24f0365198d37b10af608376b"></a>

```c
enum pd_packet_type { PD_PACKET_SOP = 0 , PD_PACKET_SOP_PRIME = 1 , PD_PACKET_PRIME_PRIME = 2 , PD_PACKET_DEBUG_PRIME = 3 , PD_PACKET_DEBUG_PRIME_PRIME = 4 , PD_PACKET_TX_HARD_RESET = 5 , PD_PACKET_CABLE_RESET = 6 , PD_PACKET_TX_BIST_MODE_2 = 7 , PD_PACKET_MSG_INVALID = 0xf }
```

相关声明：[pd_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad2df13a24f0365198d37b10af608376b)、[PD_PACKET_SOP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14)、[PD_PACKET_SOP_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8)、[PD_PACKET_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c)、[PD_PACKET_DEBUG_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d)、[PD_PACKET_DEBUG_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1)、[PD_PACKET_TX_HARD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73)、[PD_PACKET_CABLE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8)、[PD_PACKET_TX_BIST_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc)、[PD_PACKET_MSG_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437)。

电力传输数据包类型（Power Delivery Packet Type）。参见《USB Type-C 端口控制器接口规范》（USB Type-C Port Controller Interface Specification）修订版 2.0、版本 1.2，表 4-38“TRANSMIT 寄存器定义”（TRANSMIT Register Definition）。

<a id="r_ga4c7862a3e953fb22534123223c942f9a"></a>

```c
enum pd_ctrl_msg_type { PD_CTRL_GOOD_CRC = 1 , PD_CTRL_GOTO_MIN = 2 , PD_CTRL_ACCEPT = 3 , PD_CTRL_REJECT = 4 , PD_CTRL_PING = 5 , PD_CTRL_PS_RDY = 6 , PD_CTRL_GET_SOURCE_CAP = 7 , PD_CTRL_GET_SINK_CAP = 8 , PD_CTRL_DR_SWAP = 9 , PD_CTRL_PR_SWAP = 10 , PD_CTRL_VCONN_SWAP = 11 , PD_CTRL_WAIT = 12 , PD_CTRL_SOFT_RESET = 13 , PD_CTRL_DATA_RESET = 14 , PD_CTRL_DATA_RESET_COMPLETE = 15 , PD_CTRL_NOT_SUPPORTED = 16 , PD_CTRL_GET_SOURCE_CAP_EXT = 17 , PD_CTRL_GET_STATUS = 18 , PD_CTRL_FR_SWAP = 19 , PD_CTRL_GET_PPS_STATUS = 20 , PD_CTRL_GET_COUNTRY_CODES = 21 , PD_CTRL_GET_SINK_CAP_EXT = 22 , PD_CTRL_GET_SOURCE_INFO = 23 , PD_CTRL_GET_REVISION = 24 , PD_CTRL_MSG_COUNT }
```

相关声明：[pd_ctrl_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4c7862a3e953fb22534123223c942f9a)、[PD_CTRL_GOOD_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9)、[PD_CTRL_GOTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e)、[PD_CTRL_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d)、[PD_CTRL_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81)、[PD_CTRL_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed)、[PD_CTRL_PS_RDY](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad)、[PD_CTRL_GET_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929)、[PD_CTRL_GET_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495)、[PD_CTRL_DR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4)、[PD_CTRL_PR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9)、[PD_CTRL_VCONN_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b)、[PD_CTRL_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90)、[PD_CTRL_SOFT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11)、[PD_CTRL_DATA_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a)、[PD_CTRL_DATA_RESET_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792)、[PD_CTRL_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f)、[PD_CTRL_GET_SOURCE_CAP_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa)、[PD_CTRL_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef)、[PD_CTRL_FR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24)、[PD_CTRL_GET_PPS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a)、[PD_CTRL_GET_COUNTRY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e)、[PD_CTRL_GET_SINK_CAP_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318)、[PD_CTRL_GET_SOURCE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa28bd36a3d8c92ba6ea2943b0617fe6af)、[PD_CTRL_GET_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa189edfda108af04877adc2025cabb1eb)、[PD_CTRL_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa676239b098266cbec7c448dbaeebfa6c)。

控制消息类型（Control Message Type）。参见表 6-5“控制消息类型”（Control Message Types）。

<a id="r_ga8239651864b4cb0e1fc89ba2d7e59462"></a>

```c
enum pd_data_msg_type { PD_DATA_SOURCE_CAP = 1 , PD_DATA_REQUEST = 2 , PD_DATA_BIST = 3 , PD_DATA_SINK_CAP = 4 , PD_DATA_BATTERY_STATUS = 5 , PD_DATA_ALERT = 6 , PD_DATA_GET_COUNTRY_INFO = 7 , PD_DATA_ENTER_USB = 8 , PD_DATA_EPR_REQUEST = 9 , PD_DATA_EPR_MODE = 10 , PD_DATA_SOURCE_INFO = 11 , PD_DATA_REVISION = 12 , PD_DATA_VENDOR_DEF = 15 , PD_DATA_MSG_COUNT }
```

相关声明：[pd_data_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga8239651864b4cb0e1fc89ba2d7e59462)、[PD_DATA_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc)、[PD_DATA_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a)、[PD_DATA_BIST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f)、[PD_DATA_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a)、[PD_DATA_BATTERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0)、[PD_DATA_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6)、[PD_DATA_GET_COUNTRY_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069)、[PD_DATA_ENTER_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846)、[PD_DATA_EPR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a5352e00ba0ae91b14a8ecff9107e1bca)、[PD_DATA_EPR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad8b62eecdf3b574585d259bb6cb34564)、[PD_DATA_SOURCE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462abd9d5984a02b719e3d9599d0228aa99e)、[PD_DATA_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462aaea7d41eb22db0a06d676714d0598ee0)、[PD_DATA_VENDOR_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d)、[PD_DATA_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a648d1d50d51c5999e053ddcee92c30db)。

数据消息类型（Data Message Type）。参见表 6-6“数据消息类型”（Data Message Types）。

<a id="r_ga457308d50365e0a2440e94e41a316cbf"></a>

```c
enum pd_ext_msg_type { PD_EXT_SOURCE_CAP = 1 , PD_EXT_STATUS = 2 , PD_EXT_GET_BATTERY_CAP = 3 , PD_EXT_GET_BATTERY_STATUS = 4 , PD_EXT_BATTERY_CAP = 5 , PD_EXT_GET_MANUFACTURER_INFO = 6 , PD_EXT_MANUFACTURER_INFO = 7 , PD_EXT_SECURITY_REQUEST = 8 , PD_EXT_SECURITY_RESPONSE = 9 , PD_EXT_FIRMWARE_UPDATE_REQUEST = 10 , PD_EXT_FIRMWARE_UPDATE_RESPONSE = 11 , PD_EXT_PPS_STATUS = 12 , PD_EXT_COUNTRY_INFO = 13 , PD_EXT_COUNTRY_CODES = 14 , PD_EXT_SINK_CAP = 15 , PD_EXT_EXTENDED_CONTROL = 16 , PD_EXT_EPR_SOURCE_CAP = 17 , PD_EXT_EPR_SINK_CAP = 18 , PD_EXT_VENDOR_DEFINED = 30 , PD_EXT_MSG_COUNT }
```

相关声明：[pd_ext_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga457308d50365e0a2440e94e41a316cbf)、[PD_EXT_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199)、[PD_EXT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f)、[PD_EXT_GET_BATTERY_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40)、[PD_EXT_GET_BATTERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7)、[PD_EXT_BATTERY_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0)、[PD_EXT_GET_MANUFACTURER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033)、[PD_EXT_MANUFACTURER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6)、[PD_EXT_SECURITY_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f)、[PD_EXT_SECURITY_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7)、[PD_EXT_FIRMWARE_UPDATE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af)、[PD_EXT_FIRMWARE_UPDATE_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67)、[PD_EXT_PPS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083)、[PD_EXT_COUNTRY_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b)、[PD_EXT_COUNTRY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658)、[PD_EXT_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa84ef06f718993e00134040d427b93591)、[PD_EXT_EXTENDED_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfaf3cdbd6af73a63879a5985e8db1e0d7f)、[PD_EXT_EPR_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa0544591815d3b3666db44d5cff561f83)、[PD_EXT_EPR_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae569507687c904dc65827c6a737012a5)、[PD_EXT_VENDOR_DEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa20d43a6bdbd425d8f17c01d6e6cbcce3)、[PD_EXT_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfacb6e48382233e62151ab1a1fd845d429)。

修订版 3.0 的扩展消息类型（Extended Message Type）。参见表 6-48“扩展消息类型”（Extended Message Types）。

<a id="r_gaee2fe2128557939404c62e8104269bbf"></a>

```c
enum usbpd_cc_pin { USBPD_CC_PIN_1 = 0 , USBPD_CC_PIN_2 = 1 }
```

相关声明：[usbpd_cc_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaee2fe2128557939404c62e8104269bbf)、[USBPD_CC_PIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694)、[USBPD_CC_PIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e)。

活动的 PD CC 引脚（Active PD CC Pin）。


## 13.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P890_usbc_pd.h_源码浏览.md)
- [pd_header](../device_power_control_model_reference/P114_pd_header_联合体.md)
- [pd_ext_header](../device_power_control_model_reference/P111_pd_ext_header_联合体.md)
- [pd_fixed_supply_pdo_source](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md)
- [pd_fixed_supply_pdo_sink](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md)
- [pd_variable_supply_pdo_source](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md)
- [pd_variable_supply_pdo_sink](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md)
- [pd_battery_supply_pdo_source](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md)
- [pd_battery_supply_pdo_sink](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md)
- [pd_augmented_supply_pdo_source](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md)
- [pd_augmented_supply_pdo_sink](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md)
- [pd_rdo](../device_power_control_model_reference/P115_pd_rdo_联合体.md)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [PD_MAX_EXTENDED_MSG_LEGACY_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga998b67d43674778e42f6c49ec6a99af4)
- [PD_MAX_EXTENDED_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabdb041542baaf2277e054dd9e3928b16)
- [PD_MAX_EXTENDED_MSG_CHUNK_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac0588f94c1792b5b8fefa6a60c1b237b)
- [PD_T_TYPEC_SINK_WAIT_CAP_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga266725d0496981ee92b0008afe43505e)
- [PD_T_TYPEC_SINK_WAIT_CAP_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae32afec56f34841200188e64dc1ab9ca)
- [PD_V_SAFE_0V_MAX_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac3a939394dab5a5038801f9a6b2dcd30)
- [PD_V_SAFE_5V_MIN_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad4f0e12b7f0e2ccd6aee73cf1525b27c)
- [PD_T_SAFE_0V_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad5667f26343d4601c9fd5c5e9d046802)
- [PD_T_SAFE_5V_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga123abee7651bca30a3e6ec2956eb0563)
- [PD_T_TX_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab6c168d490983a136c184bbe3ed9e7c5)
- [PD_T_HARD_RESET_COMPLETE_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga64b8c095dba137d7fe460ffe38f00ce5)
- [PD_T_HARD_RESET_COMPLETE_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga2748e0775b50552cc7d26cb2b2d3103d)
- [PD_T_SENDER_RESPONSE_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga9722df85c1a842ff1661e534e88d472e)
- [PD_T_SENDER_RESPONSE_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac905bf64de8a9f5acef6f8731c11d041)
- [PD_T_SENDER_RESPONSE_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4b7c238e12770841b1852a0517b12071)
- [PD_T_SPR_PS_TRANSITION_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4726113aa8c0100fa1a88435d3a6b1d1)
- [PD_T_SPR_PS_TRANSITION_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga01a2a71da7fdbe18d07dacb687f7d295)
- [PD_T_SPR_PS_TRANSITION_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga7dac8d411d8f4651b177a6495146acb0)
- [PD_T_EPR_PS_TRANSITION_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga7f9a916a88c626b76963a4950878fa20)
- [PD_T_EPR_PS_TRANSITION_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabcd0576899a6ce1a147bffbb0c1b517f)
- [PD_T_EPR_PS_TRANSITION_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaaea48ba7ea96b304b18293c202325b0e)
- [PD_T_SINK_REQUEST_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4416cfc999de1ee2ed49ce89f54074b1)
- [PD_T_CHUNKING_NOT_SUPPORTED_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga890ce7af4632f8a17b399f0821aee3cf)
- [PD_T_CHUNKING_NOT_SUPPORTED_NOM_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad13130dbd7f6ed4276b1781c5bf2fb20)
- [PD_T_CHUNKING_NOT_SUPPORTED_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaf28df42c00394f9d11dfade2cae910d4)
- [PD_CONVERT_BYTES_TO_PD_HEADER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga953bdd1d4893bebcaeb6b4b95667fd94)
- [PD_CONVERT_PD_HEADER_COUNT_TO_BYTES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad5c5b108e4b255633a52d0de48adaf71)
- [SINK_TX_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga69f749b5c7ecf6368002aae12277ac9f)
- [TC_RP_3A0](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c)
- [SINK_TX_NG](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaa3ca6814e56859792dd5524fe8cef6b1)
- [TC_RP_1A5](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28)
- [PD_GET_EXT_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaf3acdb691327adef04e418d7ded3d883)
- [PDO_MAX_DATA_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab1716bb587e2b162415ea21e3c8d4e74)
- [PD_CONVERT_MA_TO_FIXED_PDO_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga65e9aa05457df787c5be6792ce725afd)
- [PD_CONVERT_MV_TO_FIXED_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad79de03a60054be13c9757d933069fe2)
- [PD_CONVERT_FIXED_PDO_CURRENT_TO_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaa0997fc5d7f26115c64f220d2ab91ef2)
- [PD_CONVERT_FIXED_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae9eaed8554f857d183e24b96cd69afe3)
- [PD_CONVERT_MA_TO_VARIABLE_PDO_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab3ea3b392e8fc27b4f100a99988d0ca5)
- [PD_CONVERT_MV_TO_VARIABLE_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae729bb9b17bc0df4201ec27f1f506921)
- [PD_CONVERT_VARIABLE_PDO_CURRENT_TO_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga9cd0c218385b400b3efe34474f546203)
- [PD_CONVERT_VARIABLE_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4973b120261cde51c86c7b76422222fc)
- [PD_CONVERT_MW_TO_BATTERY_PDO_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga457907a516a2cf497569ce43561fe7dd)
- [PD_CONVERT_MV_TO_BATTERY_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4832aa2b18ff84bfcf3a252361628281)
- [PD_CONVERT_BATTERY_PDO_POWER_TO_MW](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga614dd17b2b98309a837be8e0578bb06b)
- [PD_CONVERT_BATTERY_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga74af9a3f10f1855d7322dc36fabdff1a)
- [PD_CONVERT_MA_TO_AUGMENTED_PDO_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga1d73d5ffc7e6657dae81604ffb49b358)
- [PD_CONVERT_MV_TO_AUGMENTED_PDO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga1dd7da9850daae859d572d866c8c87e2)
- [PD_CONVERT_AUGMENTED_PDO_CURRENT_TO_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga202d52036ee2fb6d6da3594c126cf82b)
- [PD_CONVERT_AUGMENTED_PDO_VOLTAGE_TO_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga8623c319b19e7444ba400c738848d9ae)
- [NUM_SOP_STAR_TYPES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga1bb5fd6bb6657399a75b095eb3442bde)
- [PD_PACKET_DEBUG_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1)
- [PD_N_CAPS_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gac517b081df0572803efb374839846f1f)
- [PD_N_HARD_RESET_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae4f479f2e77066a9b870263e3580f03f)
- [PD_T_NO_RESPONSE_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga9dfd6527539e996ccc110036545e61e7)
- [PD_T_NO_RESPONSE_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaed69627505bdad8fb87c37084e2222e1)
- [PD_T_PS_HARD_RESET_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga87d0eb341d76c01b4b355c1d5a0354a1)
- [PD_T_PS_HARD_RESET_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga2c4abfef3a581e19677d8f0d845a3582)
- [PD_T_SINK_TX_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gae7db10623f2ec064ef0351bb1bba51cd)
- [PD_T_SINK_TX_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gadb55b3f260a17458bf479a7273fd946c)
- [PD_T_TYPEC_SEND_SOURCE_CAP_MIN_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabe6d36578671578eddf1381f58bcc80a)
- [PD_T_TYPEC_SEND_SOURCE_CAP_MAX_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga105a9791e086ade590b6fd825fe5cded)
- [pdo_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga316dca7ed0b85f1aa224d7a767896328)
- [PDO_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328abbc517bb47b6bdc76e44b599523e0d93)
- [PDO_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa)
- [PDO_VARIABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624)
- [PDO_AUGMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e)
- [pd_frs_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga48b33240e19524ea003052103d310358)
- [FRS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726)
- [FRS_DEFAULT_USB_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed)
- [FRS_1P5A_5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1)
- [FRS_3P0A_5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba)
- [pd_rev_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab68c6b6e33449c5ceadfc9217dd7a700)
- [PD_REV10](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9)
- [PD_REV20](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae)
- [PD_REV30](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a)
- [pd_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad2df13a24f0365198d37b10af608376b)
- [PD_PACKET_SOP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14)
- [PD_PACKET_SOP_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8)
- [PD_PACKET_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c)
- [PD_PACKET_DEBUG_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d)
- [PD_PACKET_TX_HARD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73)
- [PD_PACKET_CABLE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8)
- [PD_PACKET_TX_BIST_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc)
- [PD_PACKET_MSG_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437)
- [pd_ctrl_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4c7862a3e953fb22534123223c942f9a)
- [PD_CTRL_GOOD_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9)
- [PD_CTRL_GOTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e)
- [PD_CTRL_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d)
- [PD_CTRL_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81)
- [PD_CTRL_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed)
- [PD_CTRL_PS_RDY](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad)
- [PD_CTRL_GET_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929)
- [PD_CTRL_GET_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495)
- [PD_CTRL_DR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4)
- [PD_CTRL_PR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9)
- [PD_CTRL_VCONN_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b)
- [PD_CTRL_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90)
- [PD_CTRL_SOFT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11)
- [PD_CTRL_DATA_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a)
- [PD_CTRL_DATA_RESET_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792)
- [PD_CTRL_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f)
- [PD_CTRL_GET_SOURCE_CAP_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa)
- [PD_CTRL_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef)
- [PD_CTRL_FR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24)
- [PD_CTRL_GET_PPS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a)
- [PD_CTRL_GET_COUNTRY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e)
- [PD_CTRL_GET_SINK_CAP_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318)
- [PD_CTRL_GET_SOURCE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa28bd36a3d8c92ba6ea2943b0617fe6af)
- [PD_CTRL_GET_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa189edfda108af04877adc2025cabb1eb)
- [PD_CTRL_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa676239b098266cbec7c448dbaeebfa6c)
- [pd_data_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga8239651864b4cb0e1fc89ba2d7e59462)
- [PD_DATA_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc)
- [PD_DATA_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a)
- [PD_DATA_BIST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f)
- [PD_DATA_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a)
- [PD_DATA_BATTERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0)
- [PD_DATA_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6)
- [PD_DATA_GET_COUNTRY_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069)
- [PD_DATA_ENTER_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846)
- [PD_DATA_EPR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a5352e00ba0ae91b14a8ecff9107e1bca)
- [PD_DATA_EPR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad8b62eecdf3b574585d259bb6cb34564)
- [PD_DATA_SOURCE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462abd9d5984a02b719e3d9599d0228aa99e)
- [PD_DATA_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462aaea7d41eb22db0a06d676714d0598ee0)
- [PD_DATA_VENDOR_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d)
- [PD_DATA_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a648d1d50d51c5999e053ddcee92c30db)
- [pd_ext_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga457308d50365e0a2440e94e41a316cbf)
- [PD_EXT_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199)
- [PD_EXT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f)
- [PD_EXT_GET_BATTERY_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40)
- [PD_EXT_GET_BATTERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7)
- [PD_EXT_BATTERY_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0)
- [PD_EXT_GET_MANUFACTURER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033)
- [PD_EXT_MANUFACTURER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6)
- [PD_EXT_SECURITY_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f)
- [PD_EXT_SECURITY_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7)
- [PD_EXT_FIRMWARE_UPDATE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af)
- [PD_EXT_FIRMWARE_UPDATE_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67)
- [PD_EXT_PPS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083)
- [PD_EXT_COUNTRY_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b)
- [PD_EXT_COUNTRY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658)
- [PD_EXT_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa84ef06f718993e00134040d427b93591)
- [PD_EXT_EXTENDED_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfaf3cdbd6af73a63879a5985e8db1e0d7f)
- [PD_EXT_EPR_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa0544591815d3b3666db44d5cff561f83)
- [PD_EXT_EPR_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae569507687c904dc65827c6a737012a5)
- [PD_EXT_VENDOR_DEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa20d43a6bdbd425d8f17c01d6e6cbcce3)
- [PD_EXT_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfacb6e48382233e62151ab1a1fd845d429)
- [usbpd_cc_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaee2fe2128557939404c62e8104269bbf)
- [USBPD_CC_PIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694)
- [USBPD_CC_PIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e)

<a id="header-details"></a>

---

[上一章](P012_zephyr__usb__class__usb_hub.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__usb_c__usbc_tcpc.h_文件参考.md)
