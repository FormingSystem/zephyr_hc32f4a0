---
id: learning.zephyr-docs.api-extension-topic-reference.page-18
title: Zephyr 基础管理（Zephyr Basic Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_Zephyr 基础管理（Zephyr Basic Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr Zephyr 基础管理 API

<a id="details"></a>

MCUmgr Zephyr 基础管理 API

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_zephyr_5Fbasic_2Eh"></a>

```c
file zephyr_basic.h
```

相关声明：[zephyr_basic.h](../api_file_configuration_reference/P082_zephyr__mgmt__mcumgr__grp__zephyr__zephyr_basic.h_文件参考.md)。

MCUmgr Zephyr基本管理组（Basic Management Group）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.2\_枚举（Enumerations）

<a id="r_gab466c726d85f3289b3a064d64169914c"></a>

```c
enum zephyr_basic_group_err_code_t { ZEPHYRBASIC_MGMT_ERR_OK = 0 , ZEPHYRBASIC_MGMT_ERR_UNKNOWN , ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED , ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL , ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED }
```

相关声明：[zephyr_basic_group_err_code_t](#gab466c726d85f3289b3a064d64169914c)、[ZEPHYRBASIC_MGMT_ERR_OK](#ggab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681)、[ZEPHYRBASIC_MGMT_ERR_UNKNOWN](#ggab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2)、[ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED](#ggab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362)、[ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](#ggab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f)、[ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED](#ggab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646)。

统计管理组（Statistics Management Group）的命令结果码（Command Result Codes）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.3\_Zephyr 基础管理组的命令标识（Command IDs）

<a id="r_ga335d87c4927506ef1e5a52e3ae2b23d2"></a>

```c
#define ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE 0
```

相关声明：[ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE](#ga335d87c4927506ef1e5a52e3ae2b23d2)。

擦除存储分区（Storage Partition）。

## 18.4\_详细说明（Detailed Documentation）

<a id="ga335d87c4927506ef1e5a52e3ae2b23d2"></a>

### `ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE`

```c
#define ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/zephyr/zephyr_basic.h>
```

擦除存储分区（Storage Partition）。

<a id="gab466c726d85f3289b3a064d64169914c"></a>

### `zephyr_basic_group_err_code_t`

```c
enum zephyr_basic_group_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/zephyr/zephyr_basic.h>
```

统计管理组（Statistics Management Group）的命令结果码（Command Result Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ZEPHYRBASIC_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `ZEPHYRBASIC_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED` | 打开闪存区域（Flash Area）失败。 |
| `ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL` | 查询闪存区域参数（Flash Area Parameters）失败。 |
| `ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED` | 擦除闪存区域（Flash Area）失败。 |


## 18.5\_原页交叉引用（Cross References）

- [zephyr_basic.h](../api_file_configuration_reference/P082_zephyr__mgmt__mcumgr__grp__zephyr__zephyr_basic.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681"></a>
<a id="ggab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2"></a>
<a id="ggab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362"></a>
<a id="ggab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f"></a>
<a id="ggab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646"></a>

---

[上一章](P017_UDP 传输.md) · [返回大纲](大纲.md) · [下一章](P019_MH-Z19B API主题.md)
