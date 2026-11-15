---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-9
title: LoRa API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_LoRa API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LoRa 收发器接口。

<a id="details"></a>

LoRa 收发器接口（Transceiver Interfaces）。起始版本（Since）：2.2。版本（Version）：0.9.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 9.1\_主题（Topics）

<a id="r_lora_5Ffake"></a>

相关声明：[模拟 LoRa（Fake LoRa）](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__fake.html)。

模拟 LoRa 驱动程序。

<a id="r_lora_5Finterface_5Fbackend"></a>

相关声明：[LoRa 驱动后端 API](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 9.2\_文件（Files）

<a id="r_lora_2Eh"></a>

```c
file lora.h
```

相关声明：[lora.h](../api_file_clock_network_reference/P017_zephyr__drivers__lora.h_文件参考.md)。

LoRa驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.4\_宏定义（Macros）

<a id="r_gaf0419dcdf8ec56d9e1bfaaa35c1533c4"></a>

```c
#define LORA_GFSK_SYNC_WORD_MAX 8
```

相关声明：[LORA_GFSK_SYNC_WORD_MAX](#gaf0419dcdf8ec56d9e1bfaaa35c1533c4)。

GFSK 调制解调器可匹配的最长同步字（Sync Word），单位为字节。

<a id="r_gad59648fafcde1b76d7eb4d7c70b3a6af"></a>

```c
#define LORA_GFSK_PREAMBLE_MAX (UINT16_MAX / BITS_PER_BYTE)
```

相关声明：[LORA_GFSK_PREAMBLE_MAX](#gad59648fafcde1b76d7eb4d7c70b3a6af)、[UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)、[BITS_PER_BYTE](../util_reference/P001_通用工具公共接口.md#ga369ecd38b3ab077fc235f892354bb46f)。

GFSK 调制解调器可发送的最长前导码（Preamble），单位为字节。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.5\_枚举（Enumerations）

<a id="r_gabb5feb9d1a2bb160d9b55939efb17136"></a>

```c
enum lora_signal_bandwidth { BW_7_KHZ = 7 , BW_10_KHZ = 10 , BW_15_KHZ = 15 , BW_20_KHZ = 20 , BW_31_KHZ = 31 , BW_41_KHZ = 41 , BW_62_KHZ = 62 , BW_125_KHZ = 125 , BW_200_KHZ = 200 , BW_250_KHZ = 250 , BW_400_KHZ = 400 , BW_500_KHZ = 500 , BW_800_KHZ = 800 , BW_1000_KHZ = 1000 , BW_1600_KHZ = 1600 }
```

相关声明：[lora_signal_bandwidth](#gabb5feb9d1a2bb160d9b55939efb17136)、[BW_7_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136abc146b2fff61f782b2cb22c54113e46d)、[BW_10_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a1857aa53428a54c025f7af8addd92bf5)、[BW_15_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136af3b5a702fd61a6c4b393a4b612064ad4)、[BW_20_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136af3d00abffcee270d17533c78b26490d4)、[BW_31_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a316c5c1a9b09dda806ab803753f3bd6f)、[BW_41_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a85ebe31f96c03865427027ba1b9fc1de)、[BW_62_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136ab8bc5b1003950a7129df125eaa5231dc)、[BW_125_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1)、[BW_200_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a0ba99c3fe74214f3b58ad36c0b27213f)、[BW_250_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411)、[BW_400_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a7db7146160c9d714c9ecb1b57671b43f)、[BW_500_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9)、[BW_800_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136a83d98f1ab54b76c438b411d8de561aef)、[BW_1000_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136afdf65a32c9d8eeee1345a455e057fcc6)、[BW_1600_KHZ](#ggabb5feb9d1a2bb160d9b55939efb17136ae1aaba3f8e379b7cbdd8fd44b63e5ca5)。

LoRa 信号带宽（Signal Bandwidth）。

<a id="r_ga30bfeb2e6f4e35869996b597b614becb"></a>

```c
enum lora_datarate { SF_5 = 5 , SF_6 = 6 , SF_7 = 7 , SF_8 = 8 , SF_9 = 9 , SF_10 = 10 , SF_11 = 11 , SF_12 = 12 }
```

相关声明：[lora_datarate](#ga30bfeb2e6f4e35869996b597b614becb)、[SF_5](#gga30bfeb2e6f4e35869996b597b614becba88305a6b5aedf285c153266b13f94a73)、[SF_6](#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d)、[SF_7](#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608)、[SF_8](#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e)、[SF_9](#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc)、[SF_10](#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6)、[SF_11](#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407)、[SF_12](#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)。

LoRa 数据率（Data-rate）。

<a id="r_ga5af378491814d0d3a059cd6cd39265c8"></a>

```c
enum lora_coding_rate { CR_4_5 = 1 , CR_4_6 = 2 , CR_4_7 = 3 , CR_4_8 = 4 }
```

相关声明：[lora_coding_rate](#ga5af378491814d0d3a059cd6cd39265c8)、[CR_4_5](#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18)、[CR_4_6](#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e)、[CR_4_7](#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943)、[CR_4_8](#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42)。

LoRa 编码率（Coding Rate）。

<a id="r_ga0b6af528164f65b590295882590e7c7f"></a>

```c
enum lora_cad_symbol_num { LORA_CAD_SYMB_1 = 1 , LORA_CAD_SYMB_2 = 2 , LORA_CAD_SYMB_4 = 4 , LORA_CAD_SYMB_8 = 8 , LORA_CAD_SYMB_16 = 16 }
```

相关声明：[lora_cad_symbol_num](#ga0b6af528164f65b590295882590e7c7f)、[LORA_CAD_SYMB_1](#gga0b6af528164f65b590295882590e7c7fa944e8a714e86128d6eddf190a7968337)、[LORA_CAD_SYMB_2](#gga0b6af528164f65b590295882590e7c7fa926ae987d41f1452b6b0d719b87d3a48)、[LORA_CAD_SYMB_4](#gga0b6af528164f65b590295882590e7c7fa926e49c1ff792223c18d7df2ebf540df)、[LORA_CAD_SYMB_8](#gga0b6af528164f65b590295882590e7c7fa22aea3f5c73603f35bd51cbbbafd6590)、[LORA_CAD_SYMB_16](#gga0b6af528164f65b590295882590e7c7fa603d0a74c25b399add7f77cdc58aaa36)。

信道活动检测（Channel Activity Detection）使用的符号数量。

<a id="r_ga22c381e69be5cc630e283e8f5dfa940a"></a>

```c
enum lora_cad_mode { LORA_CAD_MODE_NONE = 0 , LORA_CAD_MODE_RX , LORA_CAD_MODE_LBT }
```

相关声明：[lora_cad_mode](#ga22c381e69be5cc630e283e8f5dfa940a)、[LORA_CAD_MODE_NONE](#gga22c381e69be5cc630e283e8f5dfa940aaab23feb65836b44af2684a5ae920abbd)、[LORA_CAD_MODE_RX](#gga22c381e69be5cc630e283e8f5dfa940aa2351cc0d7d91be6c59ad8dfa24cdb834)、[LORA_CAD_MODE_LBT](#gga22c381e69be5cc630e283e8f5dfa940aabe60002b7a1a80111d380cd34a7afb80)。

信道活动检测模式（Channel Activity Detection Mode）。

<a id="r_ga6b74d80debd5a629af29aedc7b174118"></a>

```c
enum lora_gfsk_pulse_shape { LORA_GFSK_PULSE_SHAPE_NONE , LORA_GFSK_PULSE_SHAPE_BT_0_3 , LORA_GFSK_PULSE_SHAPE_BT_0_5 , LORA_GFSK_PULSE_SHAPE_BT_0_7 , LORA_GFSK_PULSE_SHAPE_BT_1_0 }
```

相关声明：[lora_gfsk_pulse_shape](#ga6b74d80debd5a629af29aedc7b174118)、[LORA_GFSK_PULSE_SHAPE_NONE](#gga6b74d80debd5a629af29aedc7b174118aefd2af106e02a78d3b1c6e6b410b91b8)、[LORA_GFSK_PULSE_SHAPE_BT_0_3](#gga6b74d80debd5a629af29aedc7b174118a3178ad418e312e33a7375407b3e6e834)、[LORA_GFSK_PULSE_SHAPE_BT_0_5](#gga6b74d80debd5a629af29aedc7b174118a150063c466edc7c5646608bdc0420bd6)、[LORA_GFSK_PULSE_SHAPE_BT_0_7](#gga6b74d80debd5a629af29aedc7b174118a39352f92f030e4eccffe6c772fe0b47f)、[LORA_GFSK_PULSE_SHAPE_BT_1_0](#gga6b74d80debd5a629af29aedc7b174118a777fcfa7786fded4d242c4bd85496586)。

应用于 GFSK 发射脉冲的高斯滤波器（Gaussian Filter）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.6\_函数（Functions）

<a id="r_gad99239be6aeda56b859ca571514806b9"></a>

```c
static int lora_config (const struct device *dev, const struct lora_modem_config *config)
```

相关声明：[lora_config](#gad99239be6aeda56b859ca571514806b9)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)。

配置 LoRa 调制解调器（Modem）。

<a id="r_gac5db659ac5d4ce04dc3d2e69c1ecea22"></a>

```c
static int lora_config_gfsk (const struct device *dev, const struct lora_modem_config_gfsk *config)
```

相关声明：[lora_config_gfsk](#gac5db659ac5d4ce04dc3d2e69c1ecea22)、[device](../device_reference/P002_设备对象结构.md)、[lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)。

配置 GFSK 调制解调器（Modem）。

<a id="r_gaedf7847838b1e2b83bde8fc7bf735cf6"></a>

```c
static uint32_t lora_airtime (const struct device *dev, uint32_t data_len)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[lora_airtime](#gaedf7847838b1e2b83bde8fc7bf735cf6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询给定长度数据包的空中时间（Airtime）。

<a id="r_gad893b49a74e350bb05f42f863af31446"></a>

```c
static int lora_send (const struct device *dev, uint8_t *data, uint32_t data_len)
```

相关声明：[lora_send](#gad893b49a74e350bb05f42f863af31446)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 LoRa 发送数据。

<a id="r_ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b"></a>

```c
static int lora_send_async (const struct device *dev, uint8_t *data, uint32_t data_len, struct k_poll_signal *async)
```

相关声明：[lora_send_async](#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过 LoRa 异步发送数据（Asynchronous Send）。

<a id="r_ga28005c24ab1c13eb311bc05c3454a8f6"></a>

```c
static int lora_recv (const struct device *dev, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_recv](#ga28005c24ab1c13eb311bc05c3454a8f6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

通过 LoRa 接收数据。

<a id="r_gafeae6fa9d81508023665705bf16b6435"></a>

```c
static int lora_recv_async (const struct device *dev, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_recv_async](#gafeae6fa9d81508023665705bf16b6435)、[device](../device_reference/P002_设备对象结构.md)、[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)。

通过 LoRa 异步接收数据（Asynchronous Receive）。

<a id="r_ga497bf93cfe42ce6a6d48a4b463b52c21"></a>

```c
static int lora_cad (const struct device *dev, k_timeout_t timeout)
```

相关声明：[lora_cad](#ga497bf93cfe42ce6a6d48a4b463b52c21)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

执行信道活动检测（Channel Activity Detection）。

<a id="r_ga35e79551b8cdb160e74d3759a76f2db4"></a>

```c
static int lora_cad_async (const struct device *dev, lora_cad_cb cb, void *user_data)
```

相关声明：[lora_cad_async](#ga35e79551b8cdb160e74d3759a76f2db4)、[device](../device_reference/P002_设备对象结构.md)、[lora_cad_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga73606f1fdbea0b408315b9cbb28a4e19)。

异步执行信道活动检测（Channel Activity Detection）。

<a id="r_ga75d2c701f482d35cfbdd94906b8799c9"></a>

```c
static int lora_rssi (const struct device *dev, int16_t *rssi)
```

相关声明：[lora_rssi](#ga75d2c701f482d35cfbdd94906b8799c9)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

读取当前信道的瞬时接收信号强度指示（Instantaneous RSSI）。

<a id="r_gacf4c29b613fc525cfdc0b961c39981b4"></a>

```c
int lora_energy_detect (const struct device *dev, int16_t rssi_threshold, k_timeout_t duration)
```

相关声明：[lora_energy_detect](#gacf4c29b613fc525cfdc0b961c39981b4)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

执行基于能量检测的载波侦听（Energy-detection Carrier Sense）。

<a id="r_ga5d1802eed6067734ca45c70e3114b272"></a>

```c
static int lora_recv_duty_cycle (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, uint8_t *data, uint8_t size, k_timeout_t timeout, int16_t *rssi, int8_t *snr)
```

相关声明：[lora_recv_duty_cycle](#ga5d1802eed6067734ca45c70e3114b272)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

使用占空比循环（Duty Cycling，即无线唤醒 Wake-on-radio）接收数据。

<a id="r_ga2192d812e6203f6361b8beaeb1d7361c"></a>

```c
static int lora_recv_duty_cycle_async (const struct device *dev, k_timeout_t rx_period, k_timeout_t sleep_period, lora_recv_cb cb, void *user_data)
```

相关声明：[lora_recv_duty_cycle_async](#ga2192d812e6203f6361b8beaeb1d7361c)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)。

启动占空比循环接收（Receive Duty Cycling，即无线唤醒 Wake-on-radio）。

<a id="r_ga27d78168c737d56f9f7f3bbdacb808fb"></a>

```c
static int lora_test_cw (const struct device *dev, uint32_t frequency, int8_t tx_power, uint16_t duration)
```

相关声明：[lora_test_cw](#ga27d78168c737d56f9f7f3bbdacb808fb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在给定频率发送未调制连续波（Unmodulated Continuous Wave）。

## 9.7\_详细说明（Detailed Documentation）

<a id="gad59648fafcde1b76d7eb4d7c70b3a6af"></a>

### `LORA_GFSK_PREAMBLE_MAX`

```c
#define LORA_GFSK_PREAMBLE_MAX (UINT16_MAX / BITS_PER_BYTE)
```

```c
#include <zephyr/drivers/lora.h>
```

GFSK 调制解调器可发送的最长前导码（Preamble），单位为字节。

无线电设备使用 16 位数值、以比特为单位计数前导码（Preamble），因此超过此值的字节数无法容纳。

<a id="gaf0419dcdf8ec56d9e1bfaaa35c1533c4"></a>

### `LORA_GFSK_SYNC_WORD_MAX`

```c
#define LORA_GFSK_SYNC_WORD_MAX 8
```

```c
#include <zephyr/drivers/lora.h>
```

GFSK 调制解调器可匹配的最长同步字（Sync Word），单位为字节。

<a id="ga22c381e69be5cc630e283e8f5dfa940a"></a>

### `lora_cad_mode`

```c
enum lora_cad_mode
```

```c
#include <zephyr/drivers/lora.h>
```

信道活动检测模式（Channel Activity Detection Mode）。

控制发送／接收操作是否在实际操作之前执行信道活动检测（CAD）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORA_CAD_MODE_NONE` | 不执行信道活动检测（CAD），默认值。 |
| `LORA_CAD_MODE_RX` | 接收前执行信道活动检测（CAD）：`lora_recv()` 先进行 CAD；如果未检测到活动，立即返回 `0`。若需要持续低功耗监听（Continuous Low-power Listening），优先使用 `lora_recv_duty_cycle_async`。 |
| `LORA_CAD_MODE_LBT` | 先听后说（Listen Before Talk）：`lora_send()` 在发送前执行信道活动检测（CAD）；如果信道忙，返回 `-EBUSY`。 |

<a id="ga0b6af528164f65b590295882590e7c7f"></a>

### `lora_cad_symbol_num`

```c
enum lora_cad_symbol_num
```

```c
#include <zephyr/drivers/lora.h>
```

信道活动检测（Channel Activity Detection）使用的符号数量。

更多符号（Symbols）能够提高检测可靠性，但会增加时延（Latency）和功耗（Power Consumption）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORA_CAD_SYMB_1` | 1 个符号（Symbol）。 |
| `LORA_CAD_SYMB_2` | 2 个符号（Symbols）。 |
| `LORA_CAD_SYMB_4` | 4 个符号（Symbols）。 |
| `LORA_CAD_SYMB_8` | 8 个符号（Symbols）。 |
| `LORA_CAD_SYMB_16` | 16 个符号（Symbols）。 |

<a id="ga5af378491814d0d3a059cd6cd39265c8"></a>

### `lora_coding_rate`

```c
enum lora_coding_rate
```

```c
#include <zephyr/drivers/lora.h>
```

LoRa 编码率（Coding Rate）。

此枚举定义用于前向纠错（Forward Error Correction，FEC）的 LoRa 编码率（Coding Rate）。

编码率（Coding Rate）表示为 `4/x`。较小的分母（例如 `4/5`）意味着冗余较少，数据率更高，但鲁棒性较低；更高的冗余（例如 `4/8`）可以提高容错能力，但会降低数据率。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CR_4_5` | 编码率（Coding Rate）4/5：4 个信息位、1 个纠错位。 |
| `CR_4_6` | 编码率（Coding Rate）4/6：4 个信息位、2 个纠错位。 |
| `CR_4_7` | 编码率（Coding Rate）4/7：4 个信息位、3 个纠错位。 |
| `CR_4_8` | 编码率（Coding Rate）4/8：4 个信息位、4 个纠错位。 |

<a id="ga30bfeb2e6f4e35869996b597b614becb"></a>

### `lora_datarate`

```c
enum lora_datarate
```

```c
#include <zephyr/drivers/lora.h>
```

LoRa 数据率（Data-rate）。

此枚举表示 LoRa 信号的数据率（Data Rate），以扩频因子（Spreading Factor，SF）表示。

扩频因子（Spreading Factor）决定编码每个符号（Symbol）使用多少啁啾（Chirps）；每个符号包含 `2^SF` 个码片（Chips）。较高的值会降低数据率，但可增大通信距离并提高鲁棒性。译注：原文同时使用 “chirps” 和 “chips”，此处保留二者以便对照。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SF_5` | 扩频因子（Spreading Factor）5：速度最快，通信距离最短。 |
| `SF_6` | 扩频因子（Spreading Factor）6。 |
| `SF_7` | 扩频因子（Spreading Factor）7。 |
| `SF_8` | 扩频因子（Spreading Factor）8。 |
| `SF_9` | 扩频因子（Spreading Factor）9。 |
| `SF_10` | 扩频因子（Spreading Factor）10。 |
| `SF_11` | 扩频因子（Spreading Factor）11。 |
| `SF_12` | 扩频因子（Spreading Factor）12：速度最慢，通信距离最长。 |

<a id="ga6b74d80debd5a629af29aedc7b174118"></a>

### `lora_gfsk_pulse_shape`

```c
enum lora_gfsk_pulse_shape
```

```c
#include <zephyr/drivers/lora.h>
```

应用于 GFSK 发射脉冲的高斯滤波器（Gaussian Filter）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORA_GFSK_PULSE_SHAPE_NONE` | 不进行过滤（No Filtering）。 |
| `LORA_GFSK_PULSE_SHAPE_BT_0_3` | 高斯（Gaussian），`BT = 0.3`。 |
| `LORA_GFSK_PULSE_SHAPE_BT_0_5` | 高斯（Gaussian），`BT = 0.5`。 |
| `LORA_GFSK_PULSE_SHAPE_BT_0_7` | 高斯（Gaussian），`BT = 0.7`。 |
| `LORA_GFSK_PULSE_SHAPE_BT_1_0` | 高斯（Gaussian），`BT = 1.0`。 |

<a id="gabb5feb9d1a2bb160d9b55939efb17136"></a>

### `lora_signal_bandwidth`

```c
enum lora_signal_bandwidth
```

```c
#include <zephyr/drivers/lora.h>
```

LoRa 信号带宽（Signal Bandwidth）。

此枚举定义 LoRa 信号的带宽（Bandwidth）。

带宽（Bandwidth）决定发送数据所使用的频谱宽度。更宽的带宽可以实现更高的数据率，但通常会降低灵敏度和通信距离。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BW_7_KHZ` | 带宽（Bandwidth）：7.81 kHz。 |
| `BW_10_KHZ` | 带宽（Bandwidth）：10.42 kHz。 |
| `BW_15_KHZ` | 带宽（Bandwidth）：15.63 kHz。 |
| `BW_20_KHZ` | 带宽（Bandwidth）：20.83 kHz。 |
| `BW_31_KHZ` | 带宽（Bandwidth）：31.25 kHz。 |
| `BW_41_KHZ` | 带宽（Bandwidth）：41.67 kHz。 |
| `BW_62_KHZ` | 带宽（Bandwidth）：62.5 kHz。 |
| `BW_125_KHZ` | 带宽（Bandwidth）：125 kHz。 |
| `BW_200_KHZ` | 带宽（Bandwidth）：203 kHz。 |
| `BW_250_KHZ` | 带宽（Bandwidth）：250 kHz。 |
| `BW_400_KHZ` | 带宽（Bandwidth）：406 kHz。 |
| `BW_500_KHZ` | 带宽（Bandwidth）：500 kHz。 |
| `BW_800_KHZ` | 带宽（Bandwidth）：812 kHz。 |
| `BW_1000_KHZ` | 带宽（Bandwidth）：1000 kHz。 |
| `BW_1600_KHZ` | 带宽（Bandwidth）：1625 kHz。 |

<a id="gaedf7847838b1e2b83bde8fc7bf735cf6"></a>

### `lora_airtime()`

```c
uint32_t lora_airtime ( const struct device * dev, uint32_t data_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

查询给定长度数据包的空中时间（Airtime）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `data_len` | 数据长度（Data Length）。 |

**说明（Note）**：注意（Note）：使用 `lora_config` 设置的当前无线电配置（Radio Configuration）。

**返回（Returns）**：返回值（Returns）：数据包的空中传输时间（Airtime），单位为毫秒。

<a id="ga497bf93cfe42ce6a6d48a4b463b52c21"></a>

### `lora_cad()`

```c
int lora_cad ( const struct device * dev, k_timeout_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

执行信道活动检测（Channel Activity Detection）。

使用先前由 `lora_config` 设置的调制解调器配置（Modem Configuration），包括信道活动检测（CAD）参数，检查信道中是否存在 LoRa 信号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `timeout` | 等待信道活动检测（CAD）完成的最长时间。 |

**说明（Note）**：注意（Note）：这是阻塞调用（Blocking Call）。

**返回（Returns）**：返回值（Returns）：未检测到活动、信道空闲时为 `0`；检测到活动、信道忙时为 `1`；调制解调器正在使用时为 `-EBUSY`；操作超时时为 `-ETIMEDOUT`；其他错误返回负值。

<a id="ga35e79551b8cdb160e74d3759a76f2db4"></a>

### `lora_cad_async()`

```c
int lora_cad_async ( const struct device * dev, lora_cad_cb cb, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

异步执行信道活动检测（Channel Activity Detection）。

使用 `lora_config` 中的信道活动检测（CAD）参数，启动一次 CAD 操作。完成时调用 `cb` 并传入结果。

再次调用此函数并设置 `cb = NULL`，可取消待处理操作（Pending Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `cb` | 完成时调用的回调（Callback）；传入 `NULL` 可取消。 |
| `user_data` | 传给回调的用户数据。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gad99239be6aeda56b859ca571514806b9"></a>

### `lora_config()`

```c
int lora_config ( const struct device * dev, const struct lora_modem_config * config )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

配置 LoRa 调制解调器（Modem）。

LoRa 配置（Configuration）会覆盖先前由 `lora_config_gfsk` 设置的任何 GFSK 配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `config` | 包含期望调制解调器配置（Modem Configuration）的数据结构。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="gac5db659ac5d4ce04dc3d2e69c1ecea22"></a>

### `lora_config_gfsk()`

```c
int lora_config_gfsk ( const struct device * dev, const struct lora_modem_config_gfsk * config )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

配置 GFSK 调制解调器（Modem）。

GFSK 配置（Configuration）会覆盖先前由 `lora_config` 设置的任何 LoRa 配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `config` | 包含期望调制解调器配置（Modem Configuration）的数据结构。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；驱动没有 GFSK 调制解调器时为 `-ENOSYS`；出错时为负值。

<a id="gacf4c29b613fc525cfdc0b961c39981b4"></a>

### `lora_energy_detect()`

```c
int lora_energy_detect ( const struct device * dev, int16_t rssi_threshold, k_timeout_t duration )
```

```c
#include <zephyr/drivers/lora.h>
```

执行基于能量检测的载波侦听（Energy-detection Carrier Sense）。

使无线电设备进入接收模式（Receive Mode），并在 `duration` 期间重复采样接收信号强度指示（RSSI）。一旦某个样本达到 `rssi_threshold`，立即报告信道忙；若整个时间窗口内均未达到阈值，则报告信道空闲。

与 `lora_cad` 不同，此操作会响应信道上的任何能量，而不仅限于 LoRa 前导码（Preamble）。检测采用调制解调器最近一次通过 `lora_config` 或 `lora_config_gfsk` 设置的带宽（Bandwidth）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `rssi_threshold` | 以 dBm 表示的电平（Level）；达到或超过此电平时，信道被视为忙。 |
| `duration` | 载波侦听窗口（Carrier Sense Window），不能为 `K_NO_WAIT` 或 `K_FOREVER`。 |

**说明（Note）**：注意（Note）：这是阻塞调用（Blocking Call）。

**返回（Returns）**：返回值（Returns）：信道空闲时为 `0`；信道忙时为 `1`；`duration` 为 `K_NO_WAIT` 或 `K_FOREVER` 时为 `-EINVAL`；调制解调器正在使用时为 `-EBUSY`；驱动既不支持 RSSI 也不支持异步接收时为 `-ENOSYS`；其他错误返回负值。

<a id="ga28005c24ab1c13eb311bc05c3454a8f6"></a>

### `lora_recv()`

```c
int lora_recv ( const struct device * dev, uint8_t * data, uint8_t size, k_timeout_t timeout, int16_t * rssi, int8_t * snr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 接收数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `data` | 保存接收数据的缓冲区。 |
| `size` | 存放接收数据的缓冲区（Buffer）大小，允许的最大值为 `255`。 |
| `timeout` | 等待数据包（Packet）的时长。 |
| `rssi` | 接收数据的接收信号强度指示（RSSI）。 |
| `snr` | 接收数据的信噪比（SNR）。 |

**说明（Note）**：注意（Note）：这是阻塞调用（Blocking Call）。当 `cad.mode` 为 `LORA_CAD_MODE_RX` 时，先执行信道活动检测（CAD）再接收；未检测到活动时立即返回 `0`。

**返回（Returns）**：返回值（Returns）：成功时为收到的数据长度，出错时为负值。

<a id="gafeae6fa9d81508023665705bf16b6435"></a>

### `lora_recv_async()`

```c
int lora_recv_async ( const struct device * dev, lora_recv_cb cb, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 异步接收数据（Asynchronous Receive）。

使用先前由 `lora_config` 设置的配置（Configuration），连续接收数据包（Packets）。

再次调用此函数并设置 `cb = NULL` 可取消接收（Reception）；可以在回调处理函数内部执行此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 用于接收数据的调制解调器（Modem）。 |
| `cb` | 收到数据时执行的回调（Callback）。如果为 `NULL`，则取消所有待处理的异步接收（Asynchronous Receptions）。 |
| `user_data` | 传给回调的用户数据。 |

**返回（Returns）**：返回值（Returns）：成功设置接收（Reception）时为 `0`，出错时为负值。

<a id="ga5d1802eed6067734ca45c70e3114b272"></a>

### `lora_recv_duty_cycle()`

```c
int lora_recv_duty_cycle ( const struct device * dev, k_timeout_t rx_period, k_timeout_t sleep_period, uint8_t * data, uint8_t size, k_timeout_t timeout, int16_t * rssi, int8_t * snr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

使用占空比循环（Duty Cycling，即无线唤醒 Wake-on-radio）接收数据。

无线电设备自主地在睡眠（Sleep）与监听 LoRa 前导码（Preamble）之间交替。此函数阻塞，直到收到有效数据包或操作超时，随后停止占空比接收（Duty Cycle）。

为保证能够检测到信号，发送端（Transmitter）使用的前导码（Preamble）时长必须大于 `sleep_period + rx_period`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `rx_period` | 监听窗口时长（Listen Window Duration）。 |
| `sleep_period` | 两个监听窗口之间的睡眠时长（Sleep Duration）。 |
| `data` | 保存接收数据的缓冲区。 |
| `size` | 缓冲区大小（Buffer Size），最大为 `255`。 |
| `timeout` | 等待数据包（Packet）的时长。 |
| `rssi` | 接收数据的接收信号强度指示（RSSI）。 |
| `snr` | 接收数据的信噪比（SNR）。 |

**说明（Note）**：注意（Note）：这是阻塞调用（Blocking Call）。

**返回（Returns）**：返回值（Returns）：成功时为收到的数据长度，出错时为负值。

<a id="ga2192d812e6203f6361b8beaeb1d7361c"></a>

### `lora_recv_duty_cycle_async()`

```c
int lora_recv_duty_cycle_async ( const struct device * dev, k_timeout_t rx_period, k_timeout_t sleep_period, lora_recv_cb cb, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

启动占空比循环接收（Receive Duty Cycling，即无线唤醒 Wake-on-radio）。

无线电设备自主地在睡眠（Sleep）与监听 LoRa 前导码（Preamble）之间交替。收到有效数据包时调用 `cb`。占空比接收（Duty Cycle）持续运行，直到调用此函数并设置 `cb = NULL` 将其取消。

为保证能够检测到信号，发送端（Transmitter）使用的前导码（Preamble）时长必须大于 `sleep_period + rx_period`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `rx_period` | 监听窗口时长（Listen Window Duration）。 |
| `sleep_period` | 两个监听窗口之间的睡眠时长（Sleep Duration）。 |
| `cb` | 接收到数据包时的回调（Callback）；传入 `NULL` 可取消。 |
| `user_data` | 传给回调的用户数据。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga75d2c701f482d35cfbdd94906b8799c9"></a>

### `lora_rssi()`

```c
int lora_rssi ( const struct device * dev, int16_t * rssi )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

读取当前信道的瞬时接收信号强度指示（Instantaneous RSSI）。

以 `lora_config` 配置的带宽（Bandwidth），对接收器的信号强度（Signal Strength）采样一次。

无线电设备必须已经通过 `lora_recv_async` 设置为接收状态。在接收模式（Receive Mode）以外读取的值未定义，驱动不会检测这种情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `rssi` | 采样电平（Sampled Level），单位为 dBm。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；调制解调器正在使用时为 `-EBUSY`；驱动不支持该操作时为 `-ENOSYS`；其他错误返回负值。

<a id="gad893b49a74e350bb05f42f863af31446"></a>

### `lora_send()`

```c
int lora_send ( const struct device * dev, uint8_t * data, uint32_t data_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `data` | 待发送的数据（Data）。 |
| `data_len` | 待发送数据的长度（Data Length）。 |

**说明（Note）**：注意（Note）：此函数阻塞，直到发送完成。当 `cad.mode` 为 `LORA_CAD_MODE_LBT` 时，在发送前执行信道活动检测（CAD）；信道忙时返回 `-EBUSY`。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b"></a>

### `lora_send_async()`

```c
int lora_send_async ( const struct device * dev, uint8_t * data, uint32_t data_len, struct k_poll_signal * async )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

通过 LoRa 异步发送数据（Asynchronous Send）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `data` | 待发送的数据（Data）。 |
| `data_len` | 待发送数据的长度（Data Length）。 |
| `async` | 指向有效且已准备好接收信号的 `struct k_poll_signal` 的指针。注意：如果为 `NULL`，此函数不会通知发送结束。 |

**说明（Note）**：注意（Note）：此函数启动发送后立即返回，并锁定 LoRa 调制解调器（Modem），直到发送完成。当 `cad.mode` 为 `LORA_CAD_MODE_LBT` 时，在发送前执行信道活动检测（CAD）；信道忙时，信号结果（Signal Result）携带 `-EBUSY`。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。

<a id="ga27d78168c737d56f9f7f3bbdacb808fb"></a>

### `lora_test_cw()`

```c
int lora_test_cw ( const struct device * dev, uint32_t frequency, int8_t tx_power, uint16_t duration )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lora.h>
```

在给定频率发送未调制连续波（Unmodulated Continuous Wave）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LoRa 设备（Device） |
| `frequency` | 输出频率（Output Frequency），单位为赫兹（Hertz）。 |
| `tx_power` | 发送功率（TX Power），单位为 dBm。 |
| `duration` | 发送时长（Transmission Duration），单位为秒。 |

**说明（Note）**：注意（Note）：仅在发送不会干扰其他设备的测试环境（Test Setup）中使用此功能。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时为负值。


## 9.8\_原页交叉引用（Cross References）

- [模拟 LoRa（Fake LoRa）](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__fake.html)
- [LoRa 驱动后端 API](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md)
- [lora.h](../api_file_clock_network_reference/P017_zephyr__drivers__lora.h_文件参考.md)
- [lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)
- [lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [BITS_PER_BYTE](../util_reference/P001_通用工具公共接口.md#ga369ecd38b3ab077fc235f892354bb46f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [lora_recv_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga7fd50273b9463b602a4f457129d5c17f)
- [lora_cad_cb](../api_radio_permission_topic_reference/P014_LoRa 驱动后端 API.md#ga73606f1fdbea0b408315b9cbb28a4e19)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga22c381e69be5cc630e283e8f5dfa940aaab23feb65836b44af2684a5ae920abbd"></a>
<a id="gga22c381e69be5cc630e283e8f5dfa940aa2351cc0d7d91be6c59ad8dfa24cdb834"></a>
<a id="gga22c381e69be5cc630e283e8f5dfa940aabe60002b7a1a80111d380cd34a7afb80"></a>
<a id="gga0b6af528164f65b590295882590e7c7fa944e8a714e86128d6eddf190a7968337"></a>
<a id="gga0b6af528164f65b590295882590e7c7fa926ae987d41f1452b6b0d719b87d3a48"></a>
<a id="gga0b6af528164f65b590295882590e7c7fa926e49c1ff792223c18d7df2ebf540df"></a>
<a id="gga0b6af528164f65b590295882590e7c7fa22aea3f5c73603f35bd51cbbbafd6590"></a>
<a id="gga0b6af528164f65b590295882590e7c7fa603d0a74c25b399add7f77cdc58aaa36"></a>
<a id="gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18"></a>
<a id="gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e"></a>
<a id="gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943"></a>
<a id="gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becba88305a6b5aedf285c153266b13f94a73"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407"></a>
<a id="gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958"></a>
<a id="gga6b74d80debd5a629af29aedc7b174118aefd2af106e02a78d3b1c6e6b410b91b8"></a>
<a id="gga6b74d80debd5a629af29aedc7b174118a3178ad418e312e33a7375407b3e6e834"></a>
<a id="gga6b74d80debd5a629af29aedc7b174118a150063c466edc7c5646608bdc0420bd6"></a>
<a id="gga6b74d80debd5a629af29aedc7b174118a39352f92f030e4eccffe6c772fe0b47f"></a>
<a id="gga6b74d80debd5a629af29aedc7b174118a777fcfa7786fded4d242c4bd85496586"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136abc146b2fff61f782b2cb22c54113e46d"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a1857aa53428a54c025f7af8addd92bf5"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136af3b5a702fd61a6c4b393a4b612064ad4"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136af3d00abffcee270d17533c78b26490d4"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a316c5c1a9b09dda806ab803753f3bd6f"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a85ebe31f96c03865427027ba1b9fc1de"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136ab8bc5b1003950a7129df125eaa5231dc"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a0ba99c3fe74214f3b58ad36c0b27213f"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a7db7146160c9d714c9ecb1b57671b43f"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136a83d98f1ab54b76c438b411d8de561aef"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136afdf65a32c9d8eeee1345a455e057fcc6"></a>
<a id="ggabb5feb9d1a2bb160d9b55939efb17136ae1aaba3f8e379b7cbdd8fd44b63e5ca5"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_FIDO2 API主题.md) · [返回大纲](大纲.md) · [下一章](P010_LoRaWAN API主题.md)
