---
id: learning.zephyr-docs.api-source-reference.page-390
title: inst.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inst_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第390章\_inst.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html)。

## 390.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
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
<a id="agatt_8h_html"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="ainst_8h_html_a3bb5cd4e4367d402f377cee751f9b434"></a>
<a id="ainst_8h_html_a964bdf4d6c01f257533c0a5c337f562e"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__gatt__attr_html"></a>
<a id="astructbt__gatt__service__static_html"></a>
<a id="astructbt__nus__inst_html"></a>
<a id="astructbt__nus__inst_html_a3a3dd0e1f20e47a39124f10982a6be59"></a>
<a id="astructbt__nus__inst_html_a47c7d47a0cbad0e5696c64e3592de776"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Croxel, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_INST_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_INST_H_

#include <zephyr/bluetooth/gatt.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_nus_inst {
        const struct bt_gatt_service_static *svc;

        sys_slist_t *cbs;
};

#define BT_UUID_NUS_SERVICE BT_UUID_DECLARE_128(BT_UUID_NUS_SRV_VAL)
#define BT_UUID_NUS_TX_CHAR BT_UUID_DECLARE_128(BT_UUID_NUS_TX_CHAR_VAL)
#define BT_UUID_NUS_RX_CHAR BT_UUID_DECLARE_128(BT_UUID_NUS_RX_CHAR_VAL)

ssize_t nus_bt_chr_write(struct bt_conn *conn, const struct bt_gatt_attr *attr,
        const void *buf, uint16_t len, uint16_t offset, uint8_t flags);
void nus_ccc_cfg_changed(const struct bt_gatt_attr *attr, uint16_t value);

#define Z_INTERNAL_BT_NUS_INST_DEFINE(_name)                                                       \
                                                                                                   \
BT_GATT_SERVICE_DEFINE(_name##_svc,                                                                \
        BT_GATT_PRIMARY_SERVICE(BT_UUID_NUS_SERVICE),                                              \
        BT_GATT_CHARACTERISTIC(BT_UUID_NUS_TX_CHAR,                                                \
                BT_GATT_CHRC_NOTIFY,                                                               \
                BT_GATT_PERM_NONE,                                                                 \
                NULL, NULL, NULL),                                                                 \
        BT_GATT_CCC(nus_ccc_cfg_changed,                                                           \
                BT_GATT_PERM_READ | BT_GATT_PERM_WRITE),                                           \
        BT_GATT_CHARACTERISTIC(BT_UUID_NUS_RX_CHAR,                                                \
                BT_GATT_CHRC_WRITE |                                                               \
                BT_GATT_CHRC_WRITE_WITHOUT_RESP,                                                   \
                BT_GATT_PERM_WRITE,                                                                \
                NULL, nus_bt_chr_write, NULL),                                                     \
);                                                                                                 \
                                                                                                   \
sys_slist_t _name##_cbs = SYS_SLIST_STATIC_INIT(&_name##_cbs);                                     \
                                                                                                   \
STRUCT_SECTION_ITERABLE(bt_nus_inst, _name) = {                                                    \
        .svc = &_name##_svc,                                                                       \
        .cbs = &_name##_cbs,                                                                       \
}

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_INST_H_ */
```

## 390.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Croxel, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_INST_H_`。

## 390.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html)
- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)
- [bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)
- [svc](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md#a3a3dd0e1f20e47a39124f10982a6be59)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [cbs](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md#a47c7d47a0cbad0e5696c64e3592de776)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [nus_bt_chr_write](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html#a3bb5cd4e4367d402f377cee751f9b434)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [nus_ccc_cfg_changed](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html#a964bdf4d6c01f257533c0a5c337f562e)
- [gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_nus_inst::svc](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md#a3a3dd0e1f20e47a39124f10982a6be59)
- [bt_nus_inst::cbs](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md#a47c7d47a0cbad0e5696c64e3592de776)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P389_inputmux_trigger_ports.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P391_instr_mem.h_源码浏览.md)
