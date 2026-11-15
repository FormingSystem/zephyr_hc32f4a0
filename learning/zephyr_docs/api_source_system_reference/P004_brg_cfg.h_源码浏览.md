---
id: learning.zephyr-docs.api-source-system-reference.page-4
title: brg_cfg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_brg\_cfg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P011_zephyr__bluetooth__mesh__brg_cfg.h_文件参考.md)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00028"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="agroup__bt__mesh__brg__cfg_html_ga7bddcbe2b1196df6a1c80d8c213866f9"></a>
<a id="agroup__bt__mesh__brg__cfg_html_gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4"></a>
<a id="agroup__bt__mesh__brg__cfg_html_gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__brg__cfg__filter__netkey_html"></a>
<a id="astructbt__mesh__brg__cfg__filter__netkey_html_a41778bb5014eda9ee6e6fc4c83e339cb"></a>
<a id="astructbt__mesh__brg__cfg__filter__netkey_html_ab224e4982b355cc99e246b2b7c398fee"></a>
<a id="astructbt__mesh__brg__cfg__filter__netkey_html_abe9462af4258301317fe95757982e46a"></a>
<a id="astructbt__mesh__brg__cfg__subnets__list_html"></a>
<a id="astructbt__mesh__brg__cfg__subnets__list_html_a00ebe6255aabcd1cab49f08e4dc7e21b"></a>
<a id="astructbt__mesh__brg__cfg__subnets__list_html_a9f4cb39c12130ebba6c9d275a4a6b310"></a>
<a id="astructbt__mesh__brg__cfg__subnets__list_html_aa0ccb8e8b74365dfc7a4e2f5f38c50c6"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html_a672407976b409e44d06875f22f6891d3"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html_a8ce83ebdec5f306382881ceba71918cf"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html_a9262e4a78ca69846d3ac7e4f38d17d0d"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html_aa1150034663bb584779e88a5bed3fc8c"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html_acd096d1ddcf598f533c5b2b2a64c22af"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html_a091f7458fb6fcd6423c944cc1ebfe0a0"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html_a44ce11d9a2cbda69b605fab6ed68cc56"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html_a68cfc1c6514f3b7f6eb0d7ad98a15e96"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html_a6ac8abf7a95eda792065171e71f699b2"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html_a7c8ebdfc898826d95ec94b34ec3c0945"></a>
<a id="astructbt__mesh__brg__cfg__table__status_html"></a>
<a id="astructbt__mesh__brg__cfg__table__status_html_a6f1ad52ec00ec819064edf503f74744a"></a>
<a id="astructbt__mesh__brg__cfg__table__status_html_ae469e4759604077773b45b8ee1f28c37"></a>
<a id="astructnet__buf__simple_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_H__

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif


enum bt_mesh_brg_cfg_state {
        BT_MESH_BRG_CFG_DISABLED,
        BT_MESH_BRG_CFG_ENABLED,
};

/* Bridging from Addr1 to Addr2. */
#define BT_MESH_BRG_CFG_DIR_ONEWAY 1
/* Bidirectional bridging between Addr1 and Addr2. */
#define BT_MESH_BRG_CFG_DIR_TWOWAY 2

struct bt_mesh_brg_cfg_table_entry {
        uint8_t directions;
        uint16_t net_idx1;
        uint16_t net_idx2;
        uint16_t addr1;
        uint16_t addr2;
};

struct bt_mesh_brg_cfg_table_status {
        uint8_t status;
        struct bt_mesh_brg_cfg_table_entry entry;
};

struct bt_mesh_brg_cfg_filter_netkey {
        uint16_t filter: 2,    /* Filter applied to the set of pairs of NetKey Indexes */
                prohibited: 2, /* Prohibited */
                net_idx: 12;   /* NetKey Index used for filtering or ignored */
};

struct bt_mesh_brg_cfg_subnets_list {
        struct bt_mesh_brg_cfg_filter_netkey net_idx_filter;
        uint8_t start_idx;
        struct net_buf_simple *list;
};

struct bt_mesh_brg_cfg_table_list {
        uint8_t status;
        uint16_t net_idx1;
        uint16_t net_idx2;
        uint16_t start_idx;
        struct net_buf_simple *list;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_H__ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

从 `Addr1` 到 `Addr2` 的桥接（Bridging）。

### 注释 3：原第 39 行

`Addr1` 与 `Addr2` 之间的双向桥接（Bidirectional Bridging）。

### 注释 4：原第 66 行

应用于网络密钥索引对集合（Set of Pairs of NetKey Indexes）的过滤器（Filter）。

### 注释 5：原第 67 行

禁止（Prohibited）。

### 注释 6：原第 68 行

用于过滤（Filtering）或被忽略的网络密钥索引（NetKey Index）。

### 注释 7：原第 103 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_H__`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P011_zephyr__bluetooth__mesh__brg_cfg.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)
- [BT_MESH_BRG_CFG_DISABLED](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4)
- [BT_MESH_BRG_CFG_ENABLED](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2)
- [bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [directions](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#a8ce83ebdec5f306382881ceba71918cf)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_idx1](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#acd096d1ddcf598f533c5b2b2a64c22af)
- [net_idx2](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#a672407976b409e44d06875f22f6891d3)
- [addr1](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#aa1150034663bb584779e88a5bed3fc8c)
- [addr2](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#a9262e4a78ca69846d3ac7e4f38d17d0d)
- [bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md#a6f1ad52ec00ec819064edf503f74744a)
- [entry](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md#ae469e4759604077773b45b8ee1f28c37)
- [bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [filter](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md#ab224e4982b355cc99e246b2b7c398fee)
- [prohibited](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md#a41778bb5014eda9ee6e6fc4c83e339cb)
- [net_idx](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md#abe9462af4258301317fe95757982e46a)
- [bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [net_idx_filter](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#aa0ccb8e8b74365dfc7a4e2f5f38c50c6)
- [start_idx](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#a9f4cb39c12130ebba6c9d275a4a6b310)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#a00ebe6255aabcd1cab49f08e4dc7e21b)
- [bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)
- [status](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a6ac8abf7a95eda792065171e71f699b2)
- [net_idx1](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a68cfc1c6514f3b7f6eb0d7ad98a15e96)
- [net_idx2](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a091f7458fb6fcd6423c944cc1ebfe0a0)
- [start_idx](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a7c8ebdfc898826d95ec94b34ec3c0945)
- [list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a44ce11d9a2cbda69b605fab6ed68cc56)
- [bt_mesh_brg_cfg_filter_netkey::prohibited](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md#a41778bb5014eda9ee6e6fc4c83e339cb)
- [bt_mesh_brg_cfg_filter_netkey::filter](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md#ab224e4982b355cc99e246b2b7c398fee)
- [bt_mesh_brg_cfg_filter_netkey::net_idx](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md#abe9462af4258301317fe95757982e46a)
- [bt_mesh_brg_cfg_subnets_list::list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#a00ebe6255aabcd1cab49f08e4dc7e21b)
- [bt_mesh_brg_cfg_subnets_list::start_idx](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#a9f4cb39c12130ebba6c9d275a4a6b310)
- [bt_mesh_brg_cfg_subnets_list::net_idx_filter](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#aa0ccb8e8b74365dfc7a4e2f5f38c50c6)
- [bt_mesh_brg_cfg_table_entry::net_idx2](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#a672407976b409e44d06875f22f6891d3)
- [bt_mesh_brg_cfg_table_entry::directions](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#a8ce83ebdec5f306382881ceba71918cf)
- [bt_mesh_brg_cfg_table_entry::addr2](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#a9262e4a78ca69846d3ac7e4f38d17d0d)
- [bt_mesh_brg_cfg_table_entry::addr1](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#aa1150034663bb584779e88a5bed3fc8c)
- [bt_mesh_brg_cfg_table_entry::net_idx1](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md#acd096d1ddcf598f533c5b2b2a64c22af)
- [bt_mesh_brg_cfg_table_list::net_idx2](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a091f7458fb6fcd6423c944cc1ebfe0a0)
- [bt_mesh_brg_cfg_table_list::list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a44ce11d9a2cbda69b605fab6ed68cc56)
- [bt_mesh_brg_cfg_table_list::net_idx1](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a68cfc1c6514f3b7f6eb0d7ad98a15e96)
- [bt_mesh_brg_cfg_table_list::status](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a6ac8abf7a95eda792065171e71f699b2)
- [bt_mesh_brg_cfg_table_list::start_idx](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a7c8ebdfc898826d95ec94b34ec3c0945)
- [bt_mesh_brg_cfg_table_status::status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md#a6f1ad52ec00ec819064edf503f74744a)
- [bt_mesh_brg_cfg_table_status::entry](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md#ae469e4759604077773b45b8ee1f28c37)

---

[上一章](P003_bluetooth.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_buf.h_源码浏览.md)
