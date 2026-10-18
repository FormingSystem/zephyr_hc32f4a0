---
id: learning.zephyr-docs.api-service-topic-reference.page-14
title: 统计信息管理（Statistics Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_统计信息管理（Statistics Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 统计信息管理 API

<a id="details"></a>

MCUmgr 统计信息管理 API

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_stat_5Fmgmt_2Eh"></a>

```c
file stat_mgmt.h
```

相关声明：[stat_mgmt.h](../api_file_runtime_reference/P063_zephyr__mgmt__mcumgr__grp__stat_mgmt__stat_mgmt.h_文件参考.md)。

MCUmgr统计管理组（Statistics Management Group）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_stat_5Fmgmt_5Fentry"></a>

```c
struct stat_mgmt_entry
```

相关声明：[stat_mgmt_entry](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md)。

表示统计组（Statistics Group）中的单个值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga9144a5e8c384093e47603a15b3d1ff69"></a>

```c
enum stat_mgmt_err_code_t { STAT_MGMT_ERR_OK = 0 , STAT_MGMT_ERR_UNKNOWN , STAT_MGMT_ERR_INVALID_GROUP , STAT_MGMT_ERR_INVALID_STAT_NAME , STAT_MGMT_ERR_INVALID_STAT_SIZE , STAT_MGMT_ERR_WALK_ABORTED }
```

相关声明：[stat_mgmt_err_code_t](#ga9144a5e8c384093e47603a15b3d1ff69)、[STAT_MGMT_ERR_OK](#gga9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577)、[STAT_MGMT_ERR_UNKNOWN](#gga9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82)、[STAT_MGMT_ERR_INVALID_GROUP](#gga9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710)、[STAT_MGMT_ERR_INVALID_STAT_NAME](#gga9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e)、[STAT_MGMT_ERR_INVALID_STAT_SIZE](#gga9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58)、[STAT_MGMT_ERR_WALK_ABORTED](#gga9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833)。

统计管理组（Statistics Management Group）的命令结果码（Command Result Codes）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.4\_统计管理组的命令标识（Command IDs）

<a id="r_ga155235d2c21b5a698d833ca468d9473e"></a>

```c
#define STAT_MGMT_ID_SHOW 0
```

相关声明：[STAT_MGMT_ID_SHOW](#ga155235d2c21b5a698d833ca468d9473e)。

组数据（Group Data）。

<a id="r_gaed49473584422e0270f2f06e0ee0c330"></a>

```c
#define STAT_MGMT_ID_LIST 1
```

相关声明：[STAT_MGMT_ID_LIST](#gaed49473584422e0270f2f06e0ee0c330)。

列出组（List Groups）。

## 14.5\_详细说明（Detailed Documentation）

<a id="gaed49473584422e0270f2f06e0ee0c330"></a>

### `STAT_MGMT_ID_LIST`

```c
#define STAT_MGMT_ID_LIST 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/stat_mgmt/stat_mgmt.h>
```

列出组（List Groups）。

<a id="ga155235d2c21b5a698d833ca468d9473e"></a>

### `STAT_MGMT_ID_SHOW`

```c
#define STAT_MGMT_ID_SHOW 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/stat_mgmt/stat_mgmt.h>
```

组数据（Group Data）。

<a id="ga9144a5e8c384093e47603a15b3d1ff69"></a>

### `stat_mgmt_err_code_t`

```c
enum stat_mgmt_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/stat_mgmt/stat_mgmt.h>
```

统计管理组（Statistics Management Group）的命令结果码（Command Result Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `STAT_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `STAT_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `STAT_MGMT_ERR_INVALID_GROUP` | 未找到提供的统计组名称（Statistic Group Name）。 |
| `STAT_MGMT_ERR_INVALID_STAT_NAME` | 未找到提供的统计项名称（Statistic Name）。 |
| `STAT_MGMT_ERR_INVALID_STAT_SIZE` | 无法处理该统计项大小（Statistic Size）。 |
| `STAT_MGMT_ERR_WALK_ABORTED` | 统计项遍历（Statistics Walk）已中止。 |


## 14.6\_原页交叉引用（Cross References）

- [stat_mgmt.h](../api_file_runtime_reference/P063_zephyr__mgmt__mcumgr__grp__stat_mgmt__stat_mgmt.h_文件参考.md)
- [stat_mgmt_entry](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577"></a>
<a id="gga9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82"></a>
<a id="gga9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710"></a>
<a id="gga9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e"></a>
<a id="gga9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58"></a>
<a id="gga9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833"></a>

---

[上一章](P013_MAX31790 API主题.md) · [返回大纲](大纲.md) · [下一章](P015_能力过滤器（Caps Filters）.md)
