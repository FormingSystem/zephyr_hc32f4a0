---
id: learning.zephyr-docs.api-file-service-interface-reference.page-34
title: zephyr__lorawan__emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_lorawan\_\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_2emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LoRaWAN仿真器后端（Emulator Backend）API的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/lorawan/lorawan.h>
```

查看此文件的源码。

LoRaWAN仿真器后端（Emulator Backend）API的头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 34.1\_类型定义（Typedefs）

<a id="r_ad3b92479562707f0819696a5de0baa41"></a>

```c
typedef void(* lorawan_uplink_cb_t) (uint8_t port, uint8_t len, const uint8_t *data)
```

相关声明：[lorawan_uplink_cb_t](#ad3b92479562707f0819696a5de0baa41)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

定义仿真器上行回调处理函数（Uplink Callback Handler）的签名。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.2\_函数（Functions）

<a id="r_abedb7884445ac1bb0eb0351a6c413761"></a>

```c
void lorawan_emul_send_downlink (uint8_t port, bool data_pending, int16_t rssi, int8_t snr, uint8_t len, const uint8_t *data)
```

相关声明：[lorawan_emul_send_downlink](#abedb7884445ac1bb0eb0351a6c413761)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

仿真 LoRaWAN 下行消息（Downlink Message）。

<a id="r_a665c46cfe16f6c894e44a3bfbbf235b7"></a>

```c
void lorawan_emul_register_uplink_callback (lorawan_uplink_cb_t cb)
```

相关声明：[lorawan_emul_register_uplink_callback](#a665c46cfe16f6c894e44a3bfbbf235b7)、[lorawan_uplink_cb_t](#ad3b92479562707f0819696a5de0baa41)。

注册仿真上行消息（Uplink Messages）的回调。

## 34.3\_详细说明（Detailed Documentation）

<a id="ad3b92479562707f0819696a5de0baa41"></a>

### `lorawan_uplink_cb_t`

```c
typedef void(* lorawan_uplink_cb_t) (uint8_t port, uint8_t len, const uint8_t *data)
```

定义仿真器上行回调处理函数（Uplink Callback Handler）的签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | LoRaWAN 端口（Port）。 |
| `len` | 载荷数据长度（Payload Data Length）。 |
| `data` | 指向载荷数据（Payload Data）的指针。 |

<a id="a665c46cfe16f6c894e44a3bfbbf235b7"></a>

### `lorawan_emul_register_uplink_callback()`

```c
void lorawan_emul_register_uplink_callback ( lorawan_uplink_cb_t cb)
```

注册仿真上行消息（Uplink Messages）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向上行回调处理函数（Uplink Callback Handler）的指针。 |

<a id="abedb7884445ac1bb0eb0351a6c413761"></a>

### `lorawan_emul_send_downlink()`

```c
void lorawan_emul_send_downlink ( uint8_t port, bool data_pending, int16_t rssi, int8_t snr, uint8_t len, const uint8_t * data )
```

仿真 LoRaWAN 下行消息（Downlink Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 消息发送所使用的端口。 |
| `data_pending` | 网络服务器还有更多等待发送的下行数据包（Pending Downlink Packets）。 |
| `rssi` | 接收信号强度，单位为 dBm。 |
| `snr` | 信噪比（Signal to Noise ratio），原文单位为 dBm。

译注：原页此处将信噪比单位写作 dBm；本译文保留该表述供对照。 |
| `len` | 接收数据的长度；对于确认消息（ACK）为 0。 |
| `data` | 接收的数据；对于确认消息（ACK）为 `NULL`。 |


## 34.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/lorawan/lorawan.h](../api_source_reference/P453_lorawan.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P452_emul.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P033_zephyr__net__lldp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__dt-bindings__sensor__lsm6dsv16x.h_文件参考.md)
