---
id: learning.zephyr-docs.api-source-reference.page-941
title: zephyr_basic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zephyr__basic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第941章\_zephyr\_basic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/zephyr__basic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/zephyr__basic_8h.html)。

## 941.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="agroup__mcumgr__zephyr__basic__mgmt_html_gab466c726d85f3289b3a064d64169914c"></a>
<a id="agroup__mcumgr__zephyr__basic__mgmt_html_ggab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2"></a>
<a id="agroup__mcumgr__zephyr__basic__mgmt_html_ggab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681"></a>
<a id="agroup__mcumgr__zephyr__basic__mgmt_html_ggab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f"></a>
<a id="agroup__mcumgr__zephyr__basic__mgmt_html_ggab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646"></a>
<a id="agroup__mcumgr__zephyr__basic__mgmt_html_ggab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362"></a>

```c
/*
 * Copyright (c) 2021-2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ZEPHYR_ZEPHYR_BASIC_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ZEPHYR_ZEPHYR_BASIC_H_


#ifdef __cplusplus
extern "C" {
#endif

#define ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE 0

enum zephyr_basic_group_err_code_t {
        ZEPHYRBASIC_MGMT_ERR_OK = 0,

        ZEPHYRBASIC_MGMT_ERR_UNKNOWN,

        ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED,

        ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL,

        ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ZEPHYR_ZEPHYR_BASIC_H_ */
```

## 941.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ZEPHYR_ZEPHYR_BASIC_H_`。

## 941.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/zephyr__basic_8h.html)
- [zephyr_basic_group_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#gab466c726d85f3289b3a064d64169914c)
- [ZEPHYRBASIC_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681)
- [ZEPHYRBASIC_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2)
- [ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362)
- [ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f)
- [ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646)

---

[上一章](P940_xg29-dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P942_eventfd.h_源码浏览.md)
