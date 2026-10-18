---
id: learning.zephyr-docs.api-source-reference.page-636
title: os_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第636章\_os\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h.html)。

## 636.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00045"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00123"></a>
<a id="l00127"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="agroup__mcumgr__os__mgmt_html_ga14dc9256e6585450ea34b13666aa8765"></a>
<a id="agroup__mcumgr__os__mgmt_html_ga54512f3d774835d1d277872835a3b26f"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a31f119f779c11a4c416a45940ce57abf"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765a947e3f94cbc9bc0b9c2062dde14fc01f"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d"></a>
<a id="agroup__mcumgr__os__mgmt_html_gga54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructos__mgmt__info__append_html"></a>
<a id="astructos__mgmt__info__append_html_a1fb38ad80f92519c649aab7ef258095b"></a>
<a id="astructos__mgmt__info__append_html_a6c43c79ab799b7b585453ead48f3c1a3"></a>
<a id="astructos__mgmt__info__append_html_abf016939fbc1d0aaba9712dfacf2d04f"></a>
<a id="astructos__mgmt__info__append_html_acc89541b668ff791a1927c549d36b1b2"></a>
<a id="astructos__mgmt__info__append_html_acd3e277aef6b3bc69346996c073f993b"></a>
<a id="astructos__mgmt__info__append_html_ae96963a00ef4b15099cf36399a159382"></a>
<a id="astructos__mgmt__info__check_html"></a>
<a id="astructos__mgmt__info__check_html_a068e3425bf3a12b043f26b0d6dd07267"></a>
<a id="astructos__mgmt__info__check_html_a09c4371a4bfa20192411fff922747a2c"></a>
<a id="astructos__mgmt__info__check_html_a7aae2f1feb1adfdc18f11a671c3bad26"></a>
<a id="astructos__mgmt__info__check_html_aa5da5de4bfd4f9f54319458c3c8a5fbb"></a>

```c
/*
 * Copyright (c) 2018-2021 mcumgr authors
 * Copyright (c) 2022 Laird Connectivity
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_H_


#ifdef __cplusplus
extern "C" {
#endif

#define OS_MGMT_ID_ECHO            0
#define OS_MGMT_ID_CONS_ECHO_CTRL  1
#define OS_MGMT_ID_TASKSTAT        2
#define OS_MGMT_ID_MPSTAT          3
#define OS_MGMT_ID_DATETIME_STR    4
#define OS_MGMT_ID_RESET           5
#define OS_MGMT_ID_MCUMGR_PARAMS   6
#define OS_MGMT_ID_INFO            7
#define OS_MGMT_ID_BOOTLOADER_INFO 8

enum os_mgmt_err_code_t {
        OS_MGMT_ERR_OK = 0,

        OS_MGMT_ERR_UNKNOWN,

        OS_MGMT_ERR_INVALID_FORMAT,

        OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER,

        OS_MGMT_ERR_RTC_NOT_SET,

        OS_MGMT_ERR_RTC_COMMAND_FAILED,

        OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID,

        OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED,
};

enum os_mgmt_info_formats {
        OS_MGMT_INFO_FORMAT_KERNEL_NAME = BIT(0),
        OS_MGMT_INFO_FORMAT_NODE_NAME = BIT(1),
        OS_MGMT_INFO_FORMAT_KERNEL_RELEASE = BIT(2),
        OS_MGMT_INFO_FORMAT_KERNEL_VERSION = BIT(3),
        OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME = BIT(4),
        OS_MGMT_INFO_FORMAT_MACHINE = BIT(5),
        OS_MGMT_INFO_FORMAT_PROCESSOR = BIT(6),
        OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM = BIT(7),
        OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM = BIT(8),

        OS_MGMT_INFO_FORMAT_USER_CUSTOM_START = BIT(9),
};

struct os_mgmt_info_check {
        struct zcbor_string *format;
        uint32_t *format_bitmask;
        uint16_t *valid_formats;
        bool *custom_os_name;
};

struct os_mgmt_info_append {
        uint32_t *format_bitmask;
        bool all_format_specified;
        uint8_t *output;
        uint16_t *output_length;
        uint16_t buffer_size;
        bool *prior_output;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_H_ */
```

## 636.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2021 mcumgr authors。

版权（Copyright）：© 2022 Laird Connectivity。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_H_`。

## 636.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h.html)
- [os_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga14dc9256e6585450ea34b13666aa8765)
- [OS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4)
- [OS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752)
- [OS_MGMT_ERR_INVALID_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd)
- [OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d)
- [OS_MGMT_ERR_RTC_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517)
- [OS_MGMT_ERR_RTC_COMMAND_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a)
- [OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a31f119f779c11a4c416a45940ce57abf)
- [OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a947e3f94cbc9bc0b9c2062dde14fc01f)
- [os_mgmt_info_formats](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga54512f3d774835d1d277872835a3b26f)
- [OS_MGMT_INFO_FORMAT_KERNEL_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [OS_MGMT_INFO_FORMAT_NODE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3)
- [OS_MGMT_INFO_FORMAT_KERNEL_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd)
- [OS_MGMT_INFO_FORMAT_KERNEL_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328)
- [OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d)
- [OS_MGMT_INFO_FORMAT_MACHINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848)
- [OS_MGMT_INFO_FORMAT_PROCESSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082)
- [OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5)
- [OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76)
- [OS_MGMT_INFO_FORMAT_USER_CUSTOM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2)
- [os_mgmt_info_check](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md)
- [format](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#aa5da5de4bfd4f9f54319458c3c8a5fbb)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [format_bitmask](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#a068e3425bf3a12b043f26b0d6dd07267)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [valid_formats](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#a7aae2f1feb1adfdc18f11a671c3bad26)
- [custom_os_name](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#a09c4371a4bfa20192411fff922747a2c)
- [os_mgmt_info_append](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md)
- [format_bitmask](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#a6c43c79ab799b7b585453ead48f3c1a3)
- [all_format_specified](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#abf016939fbc1d0aaba9712dfacf2d04f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [output](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#a1fb38ad80f92519c649aab7ef258095b)
- [output_length](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#acd3e277aef6b3bc69346996c073f993b)
- [buffer_size](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#ae96963a00ef4b15099cf36399a159382)
- [prior_output](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#acc89541b668ff791a1927c549d36b1b2)
- [os_mgmt_info_append::output](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#a1fb38ad80f92519c649aab7ef258095b)
- [os_mgmt_info_append::format_bitmask](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#a6c43c79ab799b7b585453ead48f3c1a3)
- [os_mgmt_info_append::all_format_specified](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#abf016939fbc1d0aaba9712dfacf2d04f)
- [os_mgmt_info_append::prior_output](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#acc89541b668ff791a1927c549d36b1b2)
- [os_mgmt_info_append::output_length](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#acd3e277aef6b3bc69346996c073f993b)
- [os_mgmt_info_append::buffer_size](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md#ae96963a00ef4b15099cf36399a159382)
- [os_mgmt_info_check::format_bitmask](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#a068e3425bf3a12b043f26b0d6dd07267)
- [os_mgmt_info_check::custom_os_name](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#a09c4371a4bfa20192411fff922747a2c)
- [os_mgmt_info_check::valid_formats](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#a7aae2f1feb1adfdc18f11a671c3bad26)
- [os_mgmt_info_check::format](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md#aa5da5de4bfd4f9f54319458c3c8a5fbb)

---

[上一章](P635_openisa-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P637_os_mgmt_callbacks.h_源码浏览.md)
