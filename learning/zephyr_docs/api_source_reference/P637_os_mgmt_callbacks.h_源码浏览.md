---
id: learning.zephyr-docs.api-source-reference.page-637
title: os_mgmt_callbacks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第637章\_os\_mgmt\_callbacks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h.html)。

## 637.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00027"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_ga261346c700a2522542d8282ca76f88a5"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f"></a>
<a id="agroup__mcumgr__callback__api__os__mgmt_html_gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructos__mgmt__bootloader__info__data_html"></a>
<a id="astructos__mgmt__bootloader__info__data_html_a0509ede3b6d0b40c0b93700a738f54cf"></a>
<a id="astructos__mgmt__bootloader__info__data_html_a19db05235f5b818dfc7e479265beee71"></a>
<a id="astructos__mgmt__bootloader__info__data_html_a2629ccb5b8ecc9da25bed2d0ec695938"></a>
<a id="astructos__mgmt__bootloader__info__data_html_add73c66753d7b66713e9fdac8a1f951f"></a>
<a id="astructos__mgmt__reset__data_html"></a>
<a id="astructos__mgmt__reset__data_html_aa9defc41c1e9aff601b5c98cb307bc01"></a>
<a id="astructos__mgmt__reset__data_html_acefd2b805d33ea0127a5577148439ecc"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CALLBACKS_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CALLBACKS_H_

#ifdef __cplusplus
extern "C" {
#endif


enum os_mgmt_group_events {
        MGMT_EVT_OP_OS_MGMT_RESET               = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 0),

        MGMT_EVT_OP_OS_MGMT_INFO_CHECK          = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 1),

        MGMT_EVT_OP_OS_MGMT_INFO_APPEND         = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 2),

        MGMT_EVT_OP_OS_MGMT_DATETIME_GET        = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 3),

        MGMT_EVT_OP_OS_MGMT_DATETIME_SET        = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 4),

        MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO     = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 5),

        MGMT_EVT_OP_OS_MGMT_ALL                 = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_OS),
};

struct os_mgmt_reset_data {
        bool force;

#if defined(CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE) || defined(__DOXYGEN__)
        uint8_t boot_mode;
#endif
};

struct os_mgmt_bootloader_info_data {
        zcbor_state_t *zse;

        const size_t *decoded;

        struct zcbor_string *query;

        bool *has_output;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CALLBACKS_H_ */
```

## 637.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CALLBACKS_H_`。

## 637.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h.html)
- [os_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#ga261346c700a2522542d8282ca76f88a5)
- [MGMT_EVT_OP_OS_MGMT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52)
- [MGMT_EVT_GRP_OS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae)
- [MGMT_EVT_OP_OS_MGMT_INFO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)
- [MGMT_EVT_OP_OS_MGMT_INFO_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f)
- [MGMT_EVT_OP_OS_MGMT_DATETIME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d)
- [MGMT_EVT_OP_OS_MGMT_DATETIME_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b)
- [MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf)
- [MGMT_EVT_OP_OS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a)
- [os_mgmt_reset_data](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md)
- [force](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md#aa9defc41c1e9aff601b5c98cb307bc01)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [boot_mode](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md#acefd2b805d33ea0127a5577148439ecc)
- [os_mgmt_bootloader_info_data](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md)
- [zse](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#a0509ede3b6d0b40c0b93700a738f54cf)
- [decoded](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#a19db05235f5b818dfc7e479265beee71)
- [query](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#add73c66753d7b66713e9fdac8a1f951f)
- [has_output](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#a2629ccb5b8ecc9da25bed2d0ec695938)
- [os_mgmt_bootloader_info_data::zse](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#a0509ede3b6d0b40c0b93700a738f54cf)
- [os_mgmt_bootloader_info_data::decoded](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#a19db05235f5b818dfc7e479265beee71)
- [os_mgmt_bootloader_info_data::has_output](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#a2629ccb5b8ecc9da25bed2d0ec695938)
- [os_mgmt_bootloader_info_data::query](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md#add73c66753d7b66713e9fdac8a1f951f)
- [os_mgmt_reset_data::force](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md#aa9defc41c1e9aff601b5c98cb307bc01)
- [os_mgmt_reset_data::boot_mode](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md#acefd2b805d33ea0127a5577148439ecc)

---

[上一章](P636_os_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P638_os_mgmt_client.h_源码浏览.md)
