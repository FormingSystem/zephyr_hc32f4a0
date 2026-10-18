---
id: learning.zephyr-docs.api-source-reference.page-815
title: stat_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第815章\_stat\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h.html)。

## 815.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="agroup__mcumgr__stat__mgmt_html_ga9144a5e8c384093e47603a15b3d1ff69"></a>
<a id="agroup__mcumgr__stat__mgmt_html_gga9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710"></a>
<a id="agroup__mcumgr__stat__mgmt_html_gga9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e"></a>
<a id="agroup__mcumgr__stat__mgmt_html_gga9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833"></a>
<a id="agroup__mcumgr__stat__mgmt_html_gga9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577"></a>
<a id="agroup__mcumgr__stat__mgmt_html_gga9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82"></a>
<a id="agroup__mcumgr__stat__mgmt_html_gga9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructstat__mgmt__entry_html"></a>
<a id="astructstat__mgmt__entry_html_a44621593259f6f298bb62eb2675c1efb"></a>
<a id="astructstat__mgmt__entry_html_aa8441c1d2a1ce5acaa660e2e9b9d260d"></a>

```c
/*
 * Copyright (c) 2018-2021 mcumgr authors
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_STAT_MGMT_STAT_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_STAT_MGMT_STAT_MGMT_H_


#ifdef __cplusplus
extern "C" {
#endif

#define STAT_MGMT_ID_SHOW 0
#define STAT_MGMT_ID_LIST 1

enum stat_mgmt_err_code_t {
        STAT_MGMT_ERR_OK = 0,

        STAT_MGMT_ERR_UNKNOWN,

        STAT_MGMT_ERR_INVALID_GROUP,

        STAT_MGMT_ERR_INVALID_STAT_NAME,

        STAT_MGMT_ERR_INVALID_STAT_SIZE,

        STAT_MGMT_ERR_WALK_ABORTED,
};

struct stat_mgmt_entry {
        const char *name;

        uint64_t value;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_STAT_MGMT_STAT_MGMT_H_ */
```

## 815.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2021 mcumgr authors。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 78 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_STAT_MGMT_STAT_MGMT_H_`。

## 815.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h.html)
- [stat_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#ga9144a5e8c384093e47603a15b3d1ff69)
- [STAT_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577)
- [STAT_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82)
- [STAT_MGMT_ERR_INVALID_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710)
- [STAT_MGMT_ERR_INVALID_STAT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e)
- [STAT_MGMT_ERR_INVALID_STAT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58)
- [STAT_MGMT_ERR_WALK_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833)
- [stat_mgmt_entry](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md)
- [name](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md#a44621593259f6f298bb62eb2675c1efb)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [value](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md#aa8441c1d2a1ce5acaa660e2e9b9d260d)
- [stat_mgmt_entry::name](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md#a44621593259f6f298bb62eb2675c1efb)
- [stat_mgmt_entry::value](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md#aa8441c1d2a1ce5acaa660e2e9b9d260d)

---

[上一章](P814_stack.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P816_state.h_源码浏览.md)
