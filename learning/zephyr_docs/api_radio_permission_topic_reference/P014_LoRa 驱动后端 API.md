---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-14
title: LoRa 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_LoRa 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现 LoRa 驱动所需的 API 类型定义、回调签名（Callback Signatures）和其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_lora_5Fdriver_5Fapi"></a>

```c
struct lora_driver_api
```

相关声明：[lora_driver_api](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md)。

驱动操作（Driver Operations）：LoRa驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.2\_类型定义（Typedefs）

<a id="r_ga7fd50273b9463b602a4f457129d5c17f"></a>

```c
typedef void(* lora_recv_cb) (const struct device *dev, uint8_t *data, uint16_t size, int16_t rssi, int8_t snr, void *user_data)
```

相关声明：[lora_recv_cb](#ga7fd50273b9463b602a4f457129d5c17f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

异步接收数据（Receiving Data Asynchronously）的回调 API。

<a id="r_ga73606f1fdbea0b408315b9cbb28a4e19"></a>

```c
typedef void(* lora_cad_cb) (const struct device *dev, bool activity_detected, void *user_data)
```

相关声明：[lora_cad_cb](#ga73606f1fdbea0b408315b9cbb28a4e19)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

异步信道活动检测（Channel Activity Detection）的回调 API。

<a id="r_gabc8cba7c3f81961eac289adc40d3c8e1"></a>

```c
typedef int(* lora_api_config) (const struct device *dev, const struct lora_modem_config *config)
```

相关声明：[lora_api_config](#gabc8cba7c3f81961eac289adc40d3c8e1)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)。

配置 LoRa 模块（Module）的回调 API。

<a id="r_ga8993b902d31eac8870eb3a7f27a255cd"></a>

```c
typedef int(* lora_api_config_gfsk) (const struct device *dev, const struct lora_modem_config_gfsk *config)
```

相关声明：[lora_api_config_gfsk](#ga8993b902d31eac8870eb3a7f27a255cd)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)。

配置高斯频移键控调制解调器（GFSK Modem）的回调 API。

<a id="r_ga02edec1bd6925622926b3fc8833c8bec"></a>

```c
typedef uint32_t(* lora_api_airtime) (const struct device *dev, uint32_t data_len)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[lora_api_airtime](#ga02edec1bd6925622926b3fc8833c8bec)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询数据包空中时间（Packet Airtime）的回调 API。

<a id="r_gaddff151212a432c1dbf00c3665033eb0"></a>

```c
typedef int(* lora_api_send) (const struct device *dev, uint8_t *data, uint32_t data_len)
```

相关声明：[lora_api_send](#gaddff151212a432c1dbf00c3665033eb0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 LoRa 发送数据的回调 API。

<a id="r_ga1dafc39726315c7921d7dd6b1e0caac4"></a>

```c
typedef int(* lora_api_send_async) (const struct device *dev, uint8_t *data, uint32_t data_len, struct k_poll_signal *async)
```

相关声明：[lora_api_send_async](#ga1dafc39726315c7921d7dd6b1e0caac4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过 LoRa 异步发送数据（Sending Data Asynchronously）的回调 API。

<a id="r_ga166896d4f655cc2630e5951b1ad45c01"></a>

```c
typedef int(* lora_api_recv) (const struct device *dev, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_api_recv](#ga166896d4f655cc2630e5951b1ad45c01)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

通过 LoRa 接收数据的回调 API。

<a id="r_gad3bac89281cbf6cc79f2f4df6f4b4329"></a>

```c
typedef int(* lora_api_recv_async) (const struct device *dev, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_api_recv_async](#gad3bac89281cbf6cc79f2f4df6f4b4329)、[device](../device_reference/P002_设备对象结构.md)、[lora_recv_cb](#ga7fd50273b9463b602a4f457129d5c17f)。

通过 LoRa 异步接收数据（Receiving Data Asynchronously）的回调 API。

<a id="r_gaf308b8431762462eb172f4e0bdfce99f"></a>

```c
typedef int(* lora_api_cad) (const struct device *dev, k_timeout_t timeout)
```

相关声明：[lora_api_cad](#gaf308b8431762462eb172f4e0bdfce99f)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

信道活动检测（Channel Activity Detection）的回调 API。

<a id="r_ga604500a11fa03edae97862c29b233ed1"></a>

```c
typedef int(* lora_api_cad_async) (const struct device *dev, lora_cad_cb cb, void *user_data)
```

相关声明：[lora_api_cad_async](#ga604500a11fa03edae97862c29b233ed1)、[device](../device_reference/P002_设备对象结构.md)、[lora_cad_cb](#ga73606f1fdbea0b408315b9cbb28a4e19)。

异步信道活动检测（Channel Activity Detection）的回调 API。

<a id="r_ga185dba9fc898f2c9407b9a9461695b8e"></a>

```c
typedef int(* lora_api_rssi) (const struct device *dev, int16_t *rssi)
```

相关声明：[lora_api_rssi](#ga185dba9fc898f2c9407b9a9461695b8e)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

读取瞬时接收信号强度指示（Instantaneous RSSI）的回调 API。

<a id="r_ga8ad83577ede3ca3c7d4b037c95e039e3"></a>

```c
typedef int(* lora_api_recv_duty_cycle) (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_api_recv_duty_cycle](#ga8ad83577ede3ca3c7d4b037c95e039e3)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

以占空比循环（Duty Cycling）方式阻塞接收的回调 API。

<a id="r_gafac86253dce5dbe9286683f565663971"></a>

```c
typedef int(* lora_api_recv_duty_cycle_async) (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_api_recv_duty_cycle_async](#gafac86253dce5dbe9286683f565663971)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[lora_recv_cb](#ga7fd50273b9463b602a4f457129d5c17f)。

以占空比循环方式接收，即无线唤醒（Wake-on-radio）的回调 API。

<a id="r_ga796b75a4b27b9331d78f1916e36ea1d2"></a>

```c
typedef int(* lora_api_test_cw) (const struct device *dev, uint32_t frequency, int8_t tx_power, uint16_t duration)
```

相关声明：[lora_api_test_cw](#ga796b75a4b27b9331d78f1916e36ea1d2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送连续波（Continuous Wave）的回调 API。

## 14.3\_详细说明（Detailed Documentation）

<a id="ga02edec1bd6925622926b3fc8833c8bec"></a>

### `lora_api_airtime`

```c
typedef uint32_t(* lora_api_airtime) (const struct device *dev, uint32_t data_len)
```

```c
#include <zephyr/drivers/lora.h>
```

查询数据包空中时间（Packet Airtime）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_airtime()。

<a id="gaf308b8431762462eb172f4e0bdfce99f"></a>

### `lora_api_cad`

```c
typedef int(* lora_api_cad) (const struct device *dev, k_timeout_t timeout)
```

```c
#include <zephyr/drivers/lora.h>
```

信道活动检测（Channel Activity Detection）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_cad()。

<a id="ga604500a11fa03edae97862c29b233ed1"></a>

### `lora_api_cad_async`

```c
typedef int(* lora_api_cad_async) (const struct device *dev, lora_cad_cb cb, void *user_data)
```

```c
#include <zephyr/drivers/lora.h>
```

异步信道活动检测（Channel Activity Detection）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_cad_async()。

<a id="gabc8cba7c3f81961eac289adc40d3c8e1"></a>

### `lora_api_config`

```c
typedef int(* lora_api_config) (const struct device *dev, const struct lora_modem_config *config)
```

```c
#include <zephyr/drivers/lora.h>
```

配置 LoRa 模块（Module）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_config()。

<a id="ga8993b902d31eac8870eb3a7f27a255cd"></a>

### `lora_api_config_gfsk`

```c
typedef int(* lora_api_config_gfsk) (const struct device *dev, const struct lora_modem_config_gfsk *config)
```

```c
#include <zephyr/drivers/lora.h>
```

配置高斯频移键控调制解调器（GFSK Modem）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_config_gfsk()。

<a id="ga166896d4f655cc2630e5951b1ad45c01"></a>

### `lora_api_recv`

```c
typedef int(* lora_api_recv) (const struct device *dev, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 接收数据的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_recv()。

<a id="gad3bac89281cbf6cc79f2f4df6f4b4329"></a>

### `lora_api_recv_async`

```c
typedef int(* lora_api_recv_async) (const struct device *dev, lora_recv_cb cb, void *user_data)
```

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 异步接收数据（Receiving Data Asynchronously）的回调 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 用于接收数据的调制解调器（Modem）。 |
| `cb` | 接收到数据时运行的回调（Callback）。 |
| `user_data` | 传给回调的用户数据。 |

<a id="ga8ad83577ede3ca3c7d4b037c95e039e3"></a>

### `lora_api_recv_duty_cycle`

```c
typedef int(* lora_api_recv_duty_cycle) (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

```c
#include <zephyr/drivers/lora.h>
```

以占空比循环（Duty Cycling）方式阻塞接收的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_recv_duty_cycle()。

<a id="gafac86253dce5dbe9286683f565663971"></a>

### `lora_api_recv_duty_cycle_async`

```c
typedef int(* lora_api_recv_duty_cycle_async) (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, lora_recv_cb cb, void *user_data)
```

```c
#include <zephyr/drivers/lora.h>
```

以占空比循环方式接收，即无线唤醒（Wake-on-radio）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_recv_duty_cycle_async()。

<a id="ga185dba9fc898f2c9407b9a9461695b8e"></a>

### `lora_api_rssi`

```c
typedef int(* lora_api_rssi) (const struct device *dev, int16_t *rssi)
```

```c
#include <zephyr/drivers/lora.h>
```

读取瞬时接收信号强度指示（Instantaneous RSSI）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_rssi()。

<a id="gaddff151212a432c1dbf00c3665033eb0"></a>

### `lora_api_send`

```c
typedef int(* lora_api_send) (const struct device *dev, uint8_t *data, uint32_t data_len)
```

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 发送数据的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_send()。

<a id="ga1dafc39726315c7921d7dd6b1e0caac4"></a>

### `lora_api_send_async`

```c
typedef int(* lora_api_send_async) (const struct device *dev, uint8_t *data, uint32_t data_len, struct k_poll_signal *async)
```

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 异步发送数据（Sending Data Asynchronously）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_send_async()。

<a id="ga796b75a4b27b9331d78f1916e36ea1d2"></a>

### `lora_api_test_cw`

```c
typedef int(* lora_api_test_cw) (const struct device *dev, uint32_t frequency, int8_t tx_power, uint16_t duration)
```

```c
#include <zephyr/drivers/lora.h>
```

发送连续波（Continuous Wave）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_test_cw()。

<a id="ga73606f1fdbea0b408315b9cbb28a4e19"></a>

### `lora_cad_cb`

```c
typedef void(* lora_cad_cb) (const struct device *dev, bool activity_detected, void *user_data)
```

```c
#include <zephyr/drivers/lora.h>
```

异步信道活动检测（Channel Activity Detection）的回调 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `activity_detected` | 信道中检测到 LoRa 活动时为 true。 |
| `user_data` | 传给 lora_cad_async 的用户数据（User Data） |

<a id="ga7fd50273b9463b602a4f457129d5c17f"></a>

### `lora_recv_cb`

```c
typedef void(* lora_recv_cb) (const struct device *dev, uint8_t *data, uint16_t size, int16_t rssi, int8_t snr, void *user_data)
```

```c
#include <zephyr/drivers/lora.h>
```

异步接收数据（Receiving Data Asynchronously）的回调 API。

**参阅（See Also）**：参数说明另请参阅（See Also）：lora_recv()。


## 14.4\_原页交叉引用（Cross References）

- [lora_driver_api](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)
- [lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zephyr/drivers/lora.h](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h.html)
- [lora_airtime()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaedf7847838b1e2b83bde8fc7bf735cf6)
- [lora_cad()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga497bf93cfe42ce6a6d48a4b463b52c21)
- [lora_cad_async()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga35e79551b8cdb160e74d3759a76f2db4)
- [lora_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad99239be6aeda56b859ca571514806b9)
- [lora_config_gfsk()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gac5db659ac5d4ce04dc3d2e69c1ecea22)
- [lora_recv()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga28005c24ab1c13eb311bc05c3454a8f6)
- [lora_recv_duty_cycle()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)
- [lora_recv_duty_cycle_async()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga2192d812e6203f6361b8beaeb1d7361c)
- [lora_rssi()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga75d2c701f482d35cfbdd94906b8799c9)
- [lora_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad893b49a74e350bb05f42f863af31446)
- [lora_send_async()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)
- [lora_test_cw()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga27d78168c737d56f9f7f3bbdacb808fb)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P013_线性范围（Linear Range）.md) · [返回大纲](大纲.md) · [下一章](P015_网络抓包（Network packet capture）.md)
