---
id: learning.zephyr-docs.api-source-system-reference.page-40
title: sip_svc_agilex_smc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__smc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_sip\_svc\_agilex\_smc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__smc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P395_zephyr__drivers__sip_svc__sip_svc_agilex_smc.h_文件参考.md)。

## 40.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>

```c
/*
 * Copyright (c) 2022-2023, Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SIP_SVC_AGILEX_SMC_H_
#define ZEPHYR_INCLUDE_SIP_SVC_AGILEX_SMC_H_


/* @brief SMC return status
 */

#define SMC_STATUS_INVALID     0xFFFFFFFF
#define SMC_STATUS_OKAY        0
#define SMC_STATUS_BUSY        1
#define SMC_STATUS_REJECT      2
#define SMC_STATUS_NO_RESPONSE 3
#define SMC_STATUS_ERROR       4

/* @brief SMC Intel Header at a1
 *
 * bit
 *  7: 0   Transaction ID
 * 59: 8   Reserved
 * 63:60   Version
 */
#define SMC_PLAT_PROTO_VER 0x0

#define SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET 0
#define SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK   0xFF

#define SMC_PLAT_PROTO_HEADER_VER_OFFSET 60
#define SMC_PLAT_PROTO_HEADER_VER_MASK   0xF

#define SMC_PLAT_PROTO_HEADER                                                                      \
        ((SMC_PLAT_PROTO_VER & SMC_PLAT_PROTO_HEADER_VER_MASK) << SMC_PLAT_PROTO_HEADER_VER_OFFSET)

#define SMC_PLAT_PROTO_HEADER_SET_TRANS_ID(header, trans_id)                                       \
        (header) &=                                                                                \
                ~(SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK << SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET);   \
        (header) |= (((trans_id)&SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK)                              \
                     << SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET);

/* @brief SYNC SMC Function IDs
 */

#define SMC_FUNC_ID_GET_SVC_VERSION 0xC2000400
#define SMC_FUNC_ID_REG_READ        0xC2000401
#define SMC_FUNC_ID_REG_WRITE       0xC2000402
#define SMC_FUNC_ID_REG_UPDATE      0xC2000403
#define SMC_FUNC_ID_SET_HPS_BRIDGES 0xC2000404
#define SMC_FUNC_ID_RSU_UPDATE_ADDR 0xC2000405

/* @brief ASYNC SMC Function IDs
 */

#define SMC_FUNC_ID_MAILBOX_SEND_COMMAND  0xC2000420
#define SMC_FUNC_ID_MAILBOX_POLL_RESPONSE 0xC2000421

/* @brief SDM mailbox CANCEL command
 */
#define MAILBOX_CANCEL_COMMAND 0x03

#endif /* ZEPHYR_INCLUDE_SIP_SVC_AGILEX_SMC_H_ */
```

## 40.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023, Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

安全监视器调用返回状态（SMC Return Status）。

### 注释 3：原第 26 行

位于 `a1` 的安全监视器调用 Intel 头部（SMC Intel Header）。

| 位范围 | 含义 |
| --- | --- |
| 7:0 | 事务标识（Transaction ID） |
| 59:8 | 保留（Reserved） |
| 63:60 | 版本（Version） |

### 注释 4：原第 50 行

同步安全监视器调用函数标识（SYNC SMC Function IDs）。

### 注释 5：原第 60 行

异步安全监视器调用函数标识（ASYNC SMC Function IDs）。

### 注释 6：原第 66 行

安全设备管理器邮箱取消命令（SDM Mailbox CANCEL Command）。

### 注释 7：原第 70 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SIP_SVC_AGILEX_SMC_H_`。

## 40.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P395_zephyr__drivers__sip_svc__sip_svc_agilex_smc.h_文件参考.md)

---

[上一章](P039_semihost.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P041_socketcan.h_源码浏览.md)
