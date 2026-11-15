---
id: learning.zephyr-docs.api-source-reference.page-638
title: os_mgmt_client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第638章\_os\_mgmt\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h.html)。

## 638.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="agroup__mcumgr__os__mgmt__client_html_ga2dd2edb7c3952413c361b3d38dc2eaad"></a>
<a id="agroup__mcumgr__os__mgmt__client_html_ga5cb153bf30c40e82e8f55ac18a45fa09"></a>
<a id="agroup__mcumgr__os__mgmt__client_html_gafab4d3da30fa2bf855110d541b8fee08"></a>
<a id="ainttypes_8h_html"></a>
<a id="asmp__client_8h_html"></a>
<a id="astructos__mgmt__client_html"></a>
<a id="astructos__mgmt__client_html_ac177e863befa59a099efd3ee7de0acc3"></a>
<a id="astructos__mgmt__client_html_ada340aa0c6da9632410c36695adc0c33"></a>
<a id="astructsmp__client__object_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CLIENT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CLIENT_H_

#include <inttypes.h>
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>


#ifdef __cplusplus
extern "C" {
#endif

struct os_mgmt_client {
        struct smp_client_object *smp_client;
        int status;
};

void os_mgmt_client_init(struct os_mgmt_client *client, struct smp_client_object *smp_client);

int os_mgmt_client_echo(struct os_mgmt_client *client, const char *echo_string, size_t max_len);

int os_mgmt_client_reset(struct os_mgmt_client *client);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CLIENT_H_ */
```

## 638.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_OS_MGMT_OS_MGMT_CLIENT_H_`。

## 638.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [zephyr/mgmt/mcumgr/smp/smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)
- [os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [smp_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md#ada340aa0c6da9632410c36695adc0c33)
- [status](../system_service_model_reference/P071_os_mgmt_client_结构体.md#ac177e863befa59a099efd3ee7de0acc3)
- [os_mgmt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#gafab4d3da30fa2bf855110d541b8fee08)
- [os_mgmt_client_echo](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#ga2dd2edb7c3952413c361b3d38dc2eaad)
- [os_mgmt_client_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#ga5cb153bf30c40e82e8f55ac18a45fa09)
- [smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)
- [os_mgmt_client::status](../system_service_model_reference/P071_os_mgmt_client_结构体.md#ac177e863befa59a099efd3ee7de0acc3)
- [os_mgmt_client::smp_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md#ada340aa0c6da9632410c36695adc0c33)

---

[上一章](P637_os_mgmt_callbacks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P639_otp.h_源码浏览.md)
