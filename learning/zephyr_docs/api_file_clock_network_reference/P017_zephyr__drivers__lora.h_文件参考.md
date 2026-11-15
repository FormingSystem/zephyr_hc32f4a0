---
id: learning.zephyr-docs.api-file-clock-network-reference.page-17
title: zephyr__drivers__lora.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lora_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_drivers\_\_lora.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LoRa驱动API的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
```

查看此文件的源码。

LoRa驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

<a id="r_lora_5Fmodem_5Fconfig_5Fgfsk"></a>

```c
struct lora_modem_config_gfsk
```

相关声明：[lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)。

包含高斯频移键控（GFSK）调制解调器配置的结构。

<a id="r_lora_5Fmodem_5Fconfig"></a>

```c
struct lora_modem_config
```

相关声明：[lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)。

包含LoRa调制解调器（Modem）配置的结构。

<a id="r_lora_5Fdriver_5Fapi"></a>

```c
struct lora_driver_api
```

相关声明：[lora_driver_api](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md)。

驱动操作（Driver Operations）：LoRa驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_gaf0419dcdf8ec56d9e1bfaaa35c1533c4"></a>

```c
#define LORA_GFSK_SYNC_WORD_MAX 8
```

相关声明：[LORA_GFSK_SYNC_WORD_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaf0419dcdf8ec56d9e1bfaaa35c1533c4)。

GFSK 调制解调器可匹配的最长同步字（Sync Word），单位为字节。

<a id="r_gad59648fafcde1b76d7eb4d7c70b3a6af"></a>

```c
#define LORA_GFSK_PREAMBLE_MAX (UINT16_MAX / BITS_PER_BYTE)
```

相关声明：[LORA_GFSK_PREAMBLE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad59648fafcde1b76d7eb4d7c70b3a6af)、[UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)、[BITS_PER_BYTE](../util_reference/P001_通用工具公共接口.md#ga369ecd38b3ab077fc235f892354bb46f)。

GFSK 调制解调器可发送的最长前导码（Preamble），单位为字节。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_ga7fd50273b9463b602a4f457129d5c17f"></a>

```c
typedef void(* lora_recv_cb) (const struct device *dev, uint8_t *data, uint16_t size, int16_t rssi, int8_t snr, void *user_data)
```

相关声明：[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

异步接收数据（Receiving Data Asynchronously）的回调 API。

<a id="r_ga73606f1fdbea0b408315b9cbb28a4e19"></a>

```c
typedef void(* lora_cad_cb) (const struct device *dev, bool activity_detected, void *user_data)
```

相关声明：[lora_cad_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga73606f1fdbea0b408315b9cbb28a4e19)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

异步信道活动检测（Channel Activity Detection）的回调 API。

<a id="r_gabc8cba7c3f81961eac289adc40d3c8e1"></a>

```c
typedef int(* lora_api_config) (const struct device *dev, const struct lora_modem_config *config)
```

相关声明：[lora_api_config](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gabc8cba7c3f81961eac289adc40d3c8e1)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)。

配置 LoRa 模块（Module）的回调 API。

<a id="r_ga8993b902d31eac8870eb3a7f27a255cd"></a>

```c
typedef int(* lora_api_config_gfsk) (const struct device *dev, const struct lora_modem_config_gfsk *config)
```

相关声明：[lora_api_config_gfsk](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga8993b902d31eac8870eb3a7f27a255cd)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)。

配置高斯频移键控调制解调器（GFSK Modem）的回调 API。

<a id="r_ga02edec1bd6925622926b3fc8833c8bec"></a>

```c
typedef uint32_t(* lora_api_airtime) (const struct device *dev, uint32_t data_len)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[lora_api_airtime](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga02edec1bd6925622926b3fc8833c8bec)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询数据包空中时间（Packet Airtime）的回调 API。

<a id="r_gaddff151212a432c1dbf00c3665033eb0"></a>

```c
typedef int(* lora_api_send) (const struct device *dev, uint8_t *data, uint32_t data_len)
```

相关声明：[lora_api_send](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gaddff151212a432c1dbf00c3665033eb0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 LoRa 发送数据的回调 API。

<a id="r_ga1dafc39726315c7921d7dd6b1e0caac4"></a>

```c
typedef int(* lora_api_send_async) (const struct device *dev, uint8_t *data, uint32_t data_len, struct k_poll_signal *async)
```

相关声明：[lora_api_send_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga1dafc39726315c7921d7dd6b1e0caac4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过 LoRa 异步发送数据（Sending Data Asynchronously）的回调 API。

<a id="r_ga166896d4f655cc2630e5951b1ad45c01"></a>

```c
typedef int(* lora_api_recv) (const struct device *dev, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_api_recv](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga166896d4f655cc2630e5951b1ad45c01)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

通过 LoRa 接收数据的回调 API。

<a id="r_gad3bac89281cbf6cc79f2f4df6f4b4329"></a>

```c
typedef int(* lora_api_recv_async) (const struct device *dev, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_api_recv_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gad3bac89281cbf6cc79f2f4df6f4b4329)、[device](../device_reference/P002_设备对象结构.md)、[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)。

通过 LoRa 异步接收数据（Receiving Data Asynchronously）的回调 API。

<a id="r_gaf308b8431762462eb172f4e0bdfce99f"></a>

```c
typedef int(* lora_api_cad) (const struct device *dev, k_timeout_t timeout)
```

相关声明：[lora_api_cad](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gaf308b8431762462eb172f4e0bdfce99f)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

信道活动检测（Channel Activity Detection）的回调 API。

<a id="r_ga604500a11fa03edae97862c29b233ed1"></a>

```c
typedef int(* lora_api_cad_async) (const struct device *dev, lora_cad_cb cb, void *user_data)
```

相关声明：[lora_api_cad_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga604500a11fa03edae97862c29b233ed1)、[device](../device_reference/P002_设备对象结构.md)、[lora_cad_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga73606f1fdbea0b408315b9cbb28a4e19)。

异步信道活动检测（Channel Activity Detection）的回调 API。

<a id="r_ga185dba9fc898f2c9407b9a9461695b8e"></a>

```c
typedef int(* lora_api_rssi) (const struct device *dev, int16_t *rssi)
```

相关声明：[lora_api_rssi](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga185dba9fc898f2c9407b9a9461695b8e)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

读取瞬时接收信号强度指示（Instantaneous RSSI）的回调 API。

<a id="r_ga8ad83577ede3ca3c7d4b037c95e039e3"></a>

```c
typedef int(* lora_api_recv_duty_cycle) (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_api_recv_duty_cycle](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga8ad83577ede3ca3c7d4b037c95e039e3)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

以占空比循环（Duty Cycling）方式阻塞接收的回调 API。

<a id="r_gafac86253dce5dbe9286683f565663971"></a>

```c
typedef int(* lora_api_recv_duty_cycle_async) (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_api_recv_duty_cycle_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gafac86253dce5dbe9286683f565663971)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)。

以占空比循环方式接收，即无线唤醒（Wake-on-radio）的回调 API。

<a id="r_ga796b75a4b27b9331d78f1916e36ea1d2"></a>

```c
typedef int(* lora_api_test_cw) (const struct device *dev, uint32_t frequency, int8_t tx_power, uint16_t duration)
```

相关声明：[lora_api_test_cw](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga796b75a4b27b9331d78f1916e36ea1d2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送连续波（Continuous Wave）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.4\_枚举（Enumerations）

<a id="r_gabb5feb9d1a2bb160d9b55939efb17136"></a>

```c
enum lora_signal_bandwidth { BW_7_KHZ = 7 , BW_10_KHZ = 10 , BW_15_KHZ = 15 , BW_20_KHZ = 20 , BW_31_KHZ = 31 , BW_41_KHZ = 41 , BW_62_KHZ = 62 , BW_125_KHZ = 125 , BW_200_KHZ = 200 , BW_250_KHZ = 250 , BW_400_KHZ = 400 , BW_500_KHZ = 500 , BW_800_KHZ = 800 , BW_1000_KHZ = 1000 , BW_1600_KHZ = 1600 }
```

相关声明：[lora_signal_bandwidth](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gabb5feb9d1a2bb160d9b55939efb17136)、[BW_7_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136abc146b2fff61f782b2cb22c54113e46d)、[BW_10_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a1857aa53428a54c025f7af8addd92bf5)、[BW_15_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136af3b5a702fd61a6c4b393a4b612064ad4)、[BW_20_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136af3d00abffcee270d17533c78b26490d4)、[BW_31_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a316c5c1a9b09dda806ab803753f3bd6f)、[BW_41_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a85ebe31f96c03865427027ba1b9fc1de)、[BW_62_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136ab8bc5b1003950a7129df125eaa5231dc)、[BW_125_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1)、[BW_200_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a0ba99c3fe74214f3b58ad36c0b27213f)、[BW_250_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411)、[BW_400_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a7db7146160c9d714c9ecb1b57671b43f)、[BW_500_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9)、[BW_800_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a83d98f1ab54b76c438b411d8de561aef)、[BW_1000_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136afdf65a32c9d8eeee1345a455e057fcc6)、[BW_1600_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136ae1aaba3f8e379b7cbdd8fd44b63e5ca5)。

LoRa 信号带宽（Signal Bandwidth）。

<a id="r_ga30bfeb2e6f4e35869996b597b614becb"></a>

```c
enum lora_datarate { SF_5 = 5 , SF_6 = 6 , SF_7 = 7 , SF_8 = 8 , SF_9 = 9 , SF_10 = 10 , SF_11 = 11 , SF_12 = 12 }
```

相关声明：[lora_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga30bfeb2e6f4e35869996b597b614becb)、[SF_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becba88305a6b5aedf285c153266b13f94a73)、[SF_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d)、[SF_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608)、[SF_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e)、[SF_9](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc)、[SF_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6)、[SF_11](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407)、[SF_12](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)。

LoRa 数据率（Data-rate）。

<a id="r_ga5af378491814d0d3a059cd6cd39265c8"></a>

```c
enum lora_coding_rate { CR_4_5 = 1 , CR_4_6 = 2 , CR_4_7 = 3 , CR_4_8 = 4 }
```

相关声明：[lora_coding_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5af378491814d0d3a059cd6cd39265c8)、[CR_4_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18)、[CR_4_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e)、[CR_4_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943)、[CR_4_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42)。

LoRa 编码率（Coding Rate）。

<a id="r_ga0b6af528164f65b590295882590e7c7f"></a>

```c
enum lora_cad_symbol_num { LORA_CAD_SYMB_1 = 1 , LORA_CAD_SYMB_2 = 2 , LORA_CAD_SYMB_4 = 4 , LORA_CAD_SYMB_8 = 8 , LORA_CAD_SYMB_16 = 16 }
```

相关声明：[lora_cad_symbol_num](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga0b6af528164f65b590295882590e7c7f)、[LORA_CAD_SYMB_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa944e8a714e86128d6eddf190a7968337)、[LORA_CAD_SYMB_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa926ae987d41f1452b6b0d719b87d3a48)、[LORA_CAD_SYMB_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa926e49c1ff792223c18d7df2ebf540df)、[LORA_CAD_SYMB_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa22aea3f5c73603f35bd51cbbbafd6590)、[LORA_CAD_SYMB_16](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa603d0a74c25b399add7f77cdc58aaa36)。

信道活动检测（Channel Activity Detection）使用的符号数量。

<a id="r_ga22c381e69be5cc630e283e8f5dfa940a"></a>

```c
enum lora_cad_mode { LORA_CAD_MODE_NONE = 0 , LORA_CAD_MODE_RX , LORA_CAD_MODE_LBT }
```

相关声明：[lora_cad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga22c381e69be5cc630e283e8f5dfa940a)、[LORA_CAD_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aaab23feb65836b44af2684a5ae920abbd)、[LORA_CAD_MODE_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aa2351cc0d7d91be6c59ad8dfa24cdb834)、[LORA_CAD_MODE_LBT](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aabe60002b7a1a80111d380cd34a7afb80)。

信道活动检测模式（Channel Activity Detection Mode）。

<a id="r_ga6b74d80debd5a629af29aedc7b174118"></a>

```c
enum lora_gfsk_pulse_shape { LORA_GFSK_PULSE_SHAPE_NONE , LORA_GFSK_PULSE_SHAPE_BT_0_3 , LORA_GFSK_PULSE_SHAPE_BT_0_5 , LORA_GFSK_PULSE_SHAPE_BT_0_7 , LORA_GFSK_PULSE_SHAPE_BT_1_0 }
```

相关声明：[lora_gfsk_pulse_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga6b74d80debd5a629af29aedc7b174118)、[LORA_GFSK_PULSE_SHAPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118aefd2af106e02a78d3b1c6e6b410b91b8)、[LORA_GFSK_PULSE_SHAPE_BT_0_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a3178ad418e312e33a7375407b3e6e834)、[LORA_GFSK_PULSE_SHAPE_BT_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a150063c466edc7c5646608bdc0420bd6)、[LORA_GFSK_PULSE_SHAPE_BT_0_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a39352f92f030e4eccffe6c772fe0b47f)、[LORA_GFSK_PULSE_SHAPE_BT_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a777fcfa7786fded4d242c4bd85496586)。

应用于 GFSK 发射脉冲的高斯滤波器（Gaussian Filter）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.5\_函数（Functions）

<a id="r_gad99239be6aeda56b859ca571514806b9"></a>

```c
static int lora_config (const struct device *dev, const struct lora_modem_config *config)
```

相关声明：[lora_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad99239be6aeda56b859ca571514806b9)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)。

配置 LoRa 调制解调器（Modem）。

<a id="r_gac5db659ac5d4ce04dc3d2e69c1ecea22"></a>

```c
static int lora_config_gfsk (const struct device *dev, const struct lora_modem_config_gfsk *config)
```

相关声明：[lora_config_gfsk](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gac5db659ac5d4ce04dc3d2e69c1ecea22)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)。

配置 GFSK 调制解调器（Modem）。

<a id="r_gaedf7847838b1e2b83bde8fc7bf735cf6"></a>

```c
static uint32_t lora_airtime (const struct device *dev, uint32_t data_len)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[lora_airtime](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaedf7847838b1e2b83bde8fc7bf735cf6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询给定长度数据包的空中时间（Airtime）。

<a id="r_gad893b49a74e350bb05f42f863af31446"></a>

```c
static int lora_send (const struct device *dev, uint8_t *data, uint32_t data_len)
```

相关声明：[lora_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad893b49a74e350bb05f42f863af31446)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 LoRa 发送数据。

<a id="r_ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b"></a>

```c
static int lora_send_async (const struct device *dev, uint8_t *data, uint32_t data_len, struct k_poll_signal *async)
```

相关声明：[lora_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过 LoRa 异步发送数据（Asynchronous Send）。

<a id="r_ga28005c24ab1c13eb311bc05c3454a8f6"></a>

```c
static int lora_recv (const struct device *dev, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga28005c24ab1c13eb311bc05c3454a8f6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

通过 LoRa 接收数据。

<a id="r_gafeae6fa9d81508023665705bf16b6435"></a>

```c
static int lora_recv_async (const struct device *dev, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_recv_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gafeae6fa9d81508023665705bf16b6435)、[device](../device_reference/P002_设备对象结构.md)、[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)。

通过 LoRa 异步接收数据（Asynchronous Receive）。

<a id="r_ga497bf93cfe42ce6a6d48a4b463b52c21"></a>

```c
static int lora_cad (const struct device *dev, k_timeout_t timeout)
```

相关声明：[lora_cad](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga497bf93cfe42ce6a6d48a4b463b52c21)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

执行信道活动检测（Channel Activity Detection）。

<a id="r_ga35e79551b8cdb160e74d3759a76f2db4"></a>

```c
static int lora_cad_async (const struct device *dev, lora_cad_cb cb, void *user_data)
```

相关声明：[lora_cad_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga35e79551b8cdb160e74d3759a76f2db4)、[device](../device_reference/P002_设备对象结构.md)、[lora_cad_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga73606f1fdbea0b408315b9cbb28a4e19)。

异步执行信道活动检测（Channel Activity Detection）。

<a id="r_ga75d2c701f482d35cfbdd94906b8799c9"></a>

```c
static int lora_rssi (const struct device *dev, int16_t *rssi)
```

相关声明：[lora_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga75d2c701f482d35cfbdd94906b8799c9)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

读取当前信道的瞬时接收信号强度指示（Instantaneous RSSI）。

<a id="r_gacf4c29b613fc525cfdc0b961c39981b4"></a>

```c
int lora_energy_detect (const struct device *dev, int16_t rssi_threshold, k_timeout_t duration)
```

相关声明：[lora_energy_detect](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gacf4c29b613fc525cfdc0b961c39981b4)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

执行基于能量检测的载波侦听（Energy-detection Carrier Sense）。

<a id="r_ga5d1802eed6067734ca45c70e3114b272"></a>

```c
static int lora_recv_duty_cycle (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_recv_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

使用占空比循环（Duty Cycling，即无线唤醒 Wake-on-radio）接收数据。

<a id="r_ga2192d812e6203f6361b8beaeb1d7361c"></a>

```c
static int lora_recv_duty_cycle_async (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_recv_duty_cycle_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga2192d812e6203f6361b8beaeb1d7361c)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)。

启动占空比循环接收（Receive Duty Cycling，即无线唤醒 Wake-on-radio）。

<a id="r_ga27d78168c737d56f9f7f3bbdacb808fb"></a>

```c
static int lora_test_cw (const struct device *dev, uint32_t frequency, int8_t tx_power, uint16_t duration)
```

相关声明：[lora_test_cw](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga27d78168c737d56f9f7f3bbdacb808fb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在给定频率发送未调制连续波（Unmodulated Continuous Wave）。


## 17.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P451_lora.h_源码浏览.md)
- [lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)
- [lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)
- [lora_driver_api](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md)
- [LORA_GFSK_SYNC_WORD_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaf0419dcdf8ec56d9e1bfaaa35c1533c4)
- [LORA_GFSK_PREAMBLE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad59648fafcde1b76d7eb4d7c70b3a6af)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [BITS_PER_BYTE](../util_reference/P001_通用工具公共接口.md#ga369ecd38b3ab077fc235f892354bb46f)
- [lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [lora_cad_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga73606f1fdbea0b408315b9cbb28a4e19)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [lora_api_config](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gabc8cba7c3f81961eac289adc40d3c8e1)
- [lora_api_config_gfsk](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga8993b902d31eac8870eb3a7f27a255cd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [lora_api_airtime](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga02edec1bd6925622926b3fc8833c8bec)
- [lora_api_send](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gaddff151212a432c1dbf00c3665033eb0)
- [lora_api_send_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga1dafc39726315c7921d7dd6b1e0caac4)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [lora_api_recv](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga166896d4f655cc2630e5951b1ad45c01)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [lora_api_recv_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gad3bac89281cbf6cc79f2f4df6f4b4329)
- [lora_api_cad](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gaf308b8431762462eb172f4e0bdfce99f)
- [lora_api_cad_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga604500a11fa03edae97862c29b233ed1)
- [lora_api_rssi](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga185dba9fc898f2c9407b9a9461695b8e)
- [lora_api_recv_duty_cycle](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga8ad83577ede3ca3c7d4b037c95e039e3)
- [lora_api_recv_duty_cycle_async](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#gafac86253dce5dbe9286683f565663971)
- [lora_api_test_cw](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga796b75a4b27b9331d78f1916e36ea1d2)
- [lora_signal_bandwidth](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gabb5feb9d1a2bb160d9b55939efb17136)
- [BW_7_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136abc146b2fff61f782b2cb22c54113e46d)
- [BW_10_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a1857aa53428a54c025f7af8addd92bf5)
- [BW_15_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136af3b5a702fd61a6c4b393a4b612064ad4)
- [BW_20_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136af3d00abffcee270d17533c78b26490d4)
- [BW_31_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a316c5c1a9b09dda806ab803753f3bd6f)
- [BW_41_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a85ebe31f96c03865427027ba1b9fc1de)
- [BW_62_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136ab8bc5b1003950a7129df125eaa5231dc)
- [BW_125_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1)
- [BW_200_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a0ba99c3fe74214f3b58ad36c0b27213f)
- [BW_250_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411)
- [BW_400_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a7db7146160c9d714c9ecb1b57671b43f)
- [BW_500_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9)
- [BW_800_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a83d98f1ab54b76c438b411d8de561aef)
- [BW_1000_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136afdf65a32c9d8eeee1345a455e057fcc6)
- [BW_1600_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136ae1aaba3f8e379b7cbdd8fd44b63e5ca5)
- [lora_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga30bfeb2e6f4e35869996b597b614becb)
- [SF_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becba88305a6b5aedf285c153266b13f94a73)
- [SF_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d)
- [SF_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608)
- [SF_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e)
- [SF_9](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc)
- [SF_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6)
- [SF_11](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407)
- [SF_12](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)
- [lora_coding_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5af378491814d0d3a059cd6cd39265c8)
- [CR_4_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18)
- [CR_4_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e)
- [CR_4_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943)
- [CR_4_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42)
- [lora_cad_symbol_num](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga0b6af528164f65b590295882590e7c7f)
- [LORA_CAD_SYMB_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa944e8a714e86128d6eddf190a7968337)
- [LORA_CAD_SYMB_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa926ae987d41f1452b6b0d719b87d3a48)
- [LORA_CAD_SYMB_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa926e49c1ff792223c18d7df2ebf540df)
- [LORA_CAD_SYMB_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa22aea3f5c73603f35bd51cbbbafd6590)
- [LORA_CAD_SYMB_16](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa603d0a74c25b399add7f77cdc58aaa36)
- [lora_cad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga22c381e69be5cc630e283e8f5dfa940a)
- [LORA_CAD_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aaab23feb65836b44af2684a5ae920abbd)
- [LORA_CAD_MODE_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aa2351cc0d7d91be6c59ad8dfa24cdb834)
- [LORA_CAD_MODE_LBT](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aabe60002b7a1a80111d380cd34a7afb80)
- [lora_gfsk_pulse_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga6b74d80debd5a629af29aedc7b174118)
- [LORA_GFSK_PULSE_SHAPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118aefd2af106e02a78d3b1c6e6b410b91b8)
- [LORA_GFSK_PULSE_SHAPE_BT_0_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a3178ad418e312e33a7375407b3e6e834)
- [LORA_GFSK_PULSE_SHAPE_BT_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a150063c466edc7c5646608bdc0420bd6)
- [LORA_GFSK_PULSE_SHAPE_BT_0_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a39352f92f030e4eccffe6c772fe0b47f)
- [LORA_GFSK_PULSE_SHAPE_BT_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a777fcfa7786fded4d242c4bd85496586)
- [lora_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad99239be6aeda56b859ca571514806b9)
- [lora_config_gfsk](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gac5db659ac5d4ce04dc3d2e69c1ecea22)
- [lora_airtime](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaedf7847838b1e2b83bde8fc7bf735cf6)
- [lora_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad893b49a74e350bb05f42f863af31446)
- [lora_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)
- [lora_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga28005c24ab1c13eb311bc05c3454a8f6)
- [lora_recv_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gafeae6fa9d81508023665705bf16b6435)
- [lora_cad](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga497bf93cfe42ce6a6d48a4b463b52c21)
- [lora_cad_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga35e79551b8cdb160e74d3759a76f2db4)
- [lora_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga75d2c701f482d35cfbdd94906b8799c9)
- [lora_energy_detect](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gacf4c29b613fc525cfdc0b961c39981b4)
- [lora_recv_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)
- [lora_recv_duty_cycle_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga2192d812e6203f6361b8beaeb1d7361c)
- [lora_test_cw](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga27d78168c737d56f9f7f3bbdacb808fb)

<a id="header-details"></a>

---

[上一章](P016_zephyr__bluetooth__l2cap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__net__mqtt.h_文件参考.md)
