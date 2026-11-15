---
id: learning.zephyr-docs.api-file-runtime-reference.page-63
title: zephyr__mgmt__mcumgr__grp__stat_mgmt__stat_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_stat\_mgmt\_\_stat\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr统计管理组（Statistics Management Group）API的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr统计管理组（Statistics Management Group）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 63.1\_数据结构（Data Structures）

<a id="r_stat_5Fmgmt_5Fentry"></a>

```c
struct stat_mgmt_entry
```

相关声明：[stat_mgmt_entry](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md)。

表示统计组（Statistics Group）中的单个值。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 63.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 统计管理组的命令标识（Command IDs）

<a id="r_ga155235d2c21b5a698d833ca468d9473e"></a>

```c
#define STAT_MGMT_ID_SHOW 0
```

相关声明：[STAT_MGMT_ID_SHOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#ga155235d2c21b5a698d833ca468d9473e)。

组数据（Group Data）。

<a id="r_gaed49473584422e0270f2f06e0ee0c330"></a>

```c
#define STAT_MGMT_ID_LIST 1
```

相关声明：[STAT_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gaed49473584422e0270f2f06e0ee0c330)。

列出组（List Groups）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 63.3\_枚举（Enumerations）

<a id="r_ga9144a5e8c384093e47603a15b3d1ff69"></a>

```c
enum stat_mgmt_err_code_t { STAT_MGMT_ERR_OK = 0 , STAT_MGMT_ERR_UNKNOWN , STAT_MGMT_ERR_INVALID_GROUP , STAT_MGMT_ERR_INVALID_STAT_NAME , STAT_MGMT_ERR_INVALID_STAT_SIZE , STAT_MGMT_ERR_WALK_ABORTED }
```

相关声明：[stat_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#ga9144a5e8c384093e47603a15b3d1ff69)、[STAT_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577)、[STAT_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82)、[STAT_MGMT_ERR_INVALID_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710)、[STAT_MGMT_ERR_INVALID_STAT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e)、[STAT_MGMT_ERR_INVALID_STAT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58)、[STAT_MGMT_ERR_WALK_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833)。

统计管理组（Statistics Management Group）的命令结果码（Command Result Codes）。


## 63.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P815_stat_mgmt.h_源码浏览.md)
- [stat_mgmt_entry](../system_service_model_reference/P084_stat_mgmt_entry_结构体.md)
- [STAT_MGMT_ID_SHOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#ga155235d2c21b5a698d833ca468d9473e)
- [STAT_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gaed49473584422e0270f2f06e0ee0c330)
- [stat_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#ga9144a5e8c384093e47603a15b3d1ff69)
- [STAT_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577)
- [STAT_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82)
- [STAT_MGMT_ERR_INVALID_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710)
- [STAT_MGMT_ERR_INVALID_STAT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e)
- [STAT_MGMT_ERR_INVALID_STAT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58)
- [STAT_MGMT_ERR_WALK_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__stat__mgmt.html#gga9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833)

<a id="header-details"></a>

---

[上一章](P062_zephyr__drivers__spi_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P064_zephyr__dt-bindings__sensor__stcc4.h_文件参考.md)
