---
id: learning.zephyr-docs.api-source-supplement-reference.page-85
title: hci.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_hci.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)。

## 85.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00039"></a>
<a id="l00040"></a>
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
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="aaddr_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="ahci_8h_html_a061c7eee0b02021da072d9859ef838a6"></a>
<a id="ahci_8h_html_a27f6cd853c079e4412adbe4a1b32f8e6"></a>
<a id="ahci_8h_html_a31f7876c1a3e5dc7f1e1b2949b08139f"></a>
<a id="ahci_8h_html_a425f0cee74f061bb7f11e73da3ac627d"></a>
<a id="ahci_8h_html_a50f4a8808c26a7b4e288e650b2325883"></a>
<a id="ahci_8h_html_a73ba00112117da9ce60c850fa4cb4722"></a>
<a id="ahci_8h_html_a73fa69c6e4faea073433f3f73d327c46"></a>
<a id="ahci_8h_html_a8bf5e3e8b55633350a4cb34c928bce4d"></a>
<a id="ahci_8h_html_a8d306b5b56afdece1cadbbf0eecfe5a7"></a>
<a id="ahci_8h_html_a974e6e9262601e73537cbdcba7a7c93c"></a>
<a id="ahci_8h_html_a9931a6d4e55140e741b78656cb43e88c"></a>
<a id="ahci_8h_html_ac223ac9cddf8696d853c0942f9f148e0"></a>
<a id="ahci_8h_html_ae41be6f3dd87016bbb92f004adeb6ece"></a>
<a id="ahci_8h_html_af2eed9d93da45185aad9c2edc0001a54"></a>
<a id="ahci__types_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructbt__le__per__adv__sync_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/* hci.h - Bluetooth Host Control Interface definitions */

/*
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_HCI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_HCI_H_

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci_types.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_BT_HCI_ERR_TO_STR)
const char *bt_hci_err_to_str(uint8_t hci_err);
#else
#include <zephyr/toolchain.h>

static inline const char *bt_hci_err_to_str(uint8_t hci_err)
{
        ARG_UNUSED(hci_err);

        return "";
}
#endif

struct net_buf *bt_hci_cmd_alloc(k_timeout_t timeout);

int bt_hci_cmd_send(uint16_t opcode, struct net_buf *buf);

int bt_hci_cmd_send_sync(uint16_t opcode, struct net_buf *buf,
                         struct net_buf **rsp);

int bt_hci_get_conn_handle(const struct bt_conn *conn, uint16_t *conn_handle);

struct bt_conn *bt_hci_conn_lookup_handle(uint16_t handle);

int bt_hci_get_adv_handle(const struct bt_le_ext_adv *adv, uint8_t *adv_handle);

struct bt_le_ext_adv *bt_hci_adv_lookup_handle(uint8_t handle);

int bt_hci_get_adv_sync_handle(const struct bt_le_per_adv_sync *sync, uint16_t *sync_handle);

struct bt_le_per_adv_sync *bt_hci_per_adv_sync_lookup_handle(uint16_t handle);

const char *bt_hci_get_ver_str(uint8_t core_version);

typedef bool bt_hci_vnd_evt_cb_t(struct net_buf_simple *buf);

int bt_hci_register_vnd_evt_cb(bt_hci_vnd_evt_cb_t cb);

int bt_hci_le_rand(void *buffer, size_t len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_HCI_H_ */
```

## 85.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`hci.h`：蓝牙主机控制接口（Host Control Interface）的定义。

### 注释 2：原第 3 行

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 225 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_HCI_H_`。

## 85.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [bt_hci_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a31f7876c1a3e5dc7f1e1b2949b08139f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hci_cmd_alloc](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_hci_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#af2eed9d93da45185aad9c2edc0001a54)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hci_cmd_send_sync](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a8d306b5b56afdece1cadbbf0eecfe5a7)
- [bt_hci_get_conn_handle](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#ac223ac9cddf8696d853c0942f9f148e0)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hci_conn_lookup_handle](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a73ba00112117da9ce60c850fa4cb4722)
- [bt_hci_get_adv_handle](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a27f6cd853c079e4412adbe4a1b32f8e6)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_hci_adv_lookup_handle](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a8bf5e3e8b55633350a4cb34c928bce4d)
- [bt_hci_get_adv_sync_handle](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a73fa69c6e4faea073433f3f73d327c46)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_hci_per_adv_sync_lookup_handle](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a425f0cee74f061bb7f11e73da3ac627d)
- [bt_hci_get_ver_str](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a9931a6d4e55140e741b78656cb43e88c)
- [bt_hci_vnd_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a061c7eee0b02021da072d9859ef838a6)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_hci_register_vnd_evt_cb](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#ae41be6f3dd87016bbb92f004adeb6ece)
- [bt_hci_le_rand](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a50f4a8808c26a7b4e288e650b2325883)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P084_handlers.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P086_hdlc_rcp_if.h_源码浏览.md)
