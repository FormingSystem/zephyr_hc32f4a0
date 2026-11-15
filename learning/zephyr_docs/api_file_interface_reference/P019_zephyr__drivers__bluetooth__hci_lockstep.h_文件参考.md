---
id: learning.zephyr-docs.api-file-interface-reference.page-19
title: zephyr__drivers__bluetooth__hci_lockstep.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_bluetooth\_\_hci\_lockstep.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙HCI锁步命令（Lockstep Command）的辅助接口。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/bluetooth/hci_pkt.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

蓝牙HCI锁步命令（Lockstep Command）的辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Flockstep"></a>

```c
struct bt_hci_lockstep
```

相关声明：[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)。

锁步辅助对象（Lockstep Helper）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 19.2\_类型定义（Typedefs）

<a id="r_ga3eeed334ea5d5f212e3b560bd5cd4def"></a>

```c
typedef int(* bt_hci_lockstep_send_t) (const struct device *dev, const uint8_t *pkt, size_t len)
```

相关声明：[bt_hci_lockstep_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga3eeed334ea5d5f212e3b560bd5cd4def)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

锁步辅助器（lockstep helper）的传输发送函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.3\_函数（Functions）

<a id="r_ga02ea7a0ad2bbb7d8ee9845122e34f8ab"></a>

```c
void bt_hci_lockstep_init (struct bt_hci_lockstep *ls, const struct device *dev, bt_hci_lockstep_send_t send)
```

相关声明：[bt_hci_lockstep_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga02ea7a0ad2bbb7d8ee9845122e34f8ab)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_lockstep_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga3eeed334ea5d5f212e3b560bd5cd4def)、[send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)。

初始化锁步辅助器。

<a id="r_ga1d2d42b2db398cf4449b337588897f56"></a>

```c
void bt_hci_lockstep_reset (struct bt_hci_lockstep *ls)
```

相关声明：[bt_hci_lockstep_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga1d2d42b2db398cf4449b337588897f56)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)。

恢复锁步辅助器的初始状态。

<a id="r_gacb84fdafc6376483e12a8b7ec391fa7c"></a>

```c
bool bt_hci_lockstep_feed (struct bt_hci_lockstep *ls, const uint8_t *pkt, size_t len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_hci_lockstep_feed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gacb84fdafc6376483e12a8b7ec391fa7c)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将收到的主机控制器接口（HCI）数据包交给锁步辅助器。

<a id="r_gaa53d7b9aa5a7d6c5f11ea442c37f75d8"></a>

```c
int bt_hci_lockstep_cmd_send_sync (struct bt_hci_lockstep *ls, uint16_t opcode, struct net_buf_simple *cmd, struct net_buf_simple *rsp)
```

相关声明：[bt_hci_lockstep_cmd_send_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

发送 HCI 命令并等待其响应。


## 19.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/hci_pkt.h](../api_source_reference/P311_hci_pkt.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P309_hci_lockstep.h_源码浏览.md)
- [bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)
- [bt_hci_lockstep_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga3eeed334ea5d5f212e3b560bd5cd4def)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_lockstep_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga02ea7a0ad2bbb7d8ee9845122e34f8ab)
- [send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [bt_hci_lockstep_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga1d2d42b2db398cf4449b337588897f56)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_hci_lockstep_feed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gacb84fdafc6376483e12a8b7ec391fa7c)
- [bt_hci_lockstep_cmd_send_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="header-details"></a>

---

[上一章](P018_zephyr__drivers__clock_control__esp32_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__bluetooth__mesh__health_srv.h_文件参考.md)
