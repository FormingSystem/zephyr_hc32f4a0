---
id: learning.zephyr-docs.api-file-configuration-reference.page-82
title: zephyr__mgmt__mcumgr__grp__zephyr__zephyr_basic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zephyr__basic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_zephyr\_\_zephyr\_basic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/zephyr__basic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr Zephyr基本管理组（Basic Management Group）API的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr Zephyr基本管理组（Basic Management Group）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 82.1\_宏定义（Macros）

<a id="define-members-0"></a>

### Zephyr 基础管理组的命令标识（Command IDs）

<a id="r_ga335d87c4927506ef1e5a52e3ae2b23d2"></a>

```c
#define ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE 0
```

相关声明：[ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ga335d87c4927506ef1e5a52e3ae2b23d2)。

擦除存储分区（Storage Partition）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 82.2\_枚举（Enumerations）

<a id="r_gab466c726d85f3289b3a064d64169914c"></a>

```c
enum zephyr_basic_group_err_code_t { ZEPHYRBASIC_MGMT_ERR_OK = 0 , ZEPHYRBASIC_MGMT_ERR_UNKNOWN , ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED , ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL , ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED }
```

相关声明：[zephyr_basic_group_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#gab466c726d85f3289b3a064d64169914c)、[ZEPHYRBASIC_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681)、[ZEPHYRBASIC_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2)、[ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362)、[ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f)、[ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646)。

统计管理组（Statistics Management Group）的命令结果码（Command Result Codes）。


## 82.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P941_zephyr_basic.h_源码浏览.md)
- [ZEPHYR_MGMT_GRP_BASIC_CMD_ERASE_STORAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ga335d87c4927506ef1e5a52e3ae2b23d2)
- [zephyr_basic_group_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#gab466c726d85f3289b3a064d64169914c)
- [ZEPHYRBASIC_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681)
- [ZEPHYRBASIC_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2)
- [ZEPHYRBASIC_MGMT_ERR_FLASH_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362)
- [ZEPHYRBASIC_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f)
- [ZEPHYRBASIC_MGMT_ERR_FLASH_ERASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__zephyr__basic__mgmt.html#ggab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646)

<a id="header-details"></a>

---

[上一章](P081_zephyr__drivers__sensor__xbr818.h_文件参考.md) · [返回大纲](大纲.md)
