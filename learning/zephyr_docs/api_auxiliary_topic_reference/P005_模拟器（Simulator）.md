---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-5
title: 模拟器（Simulator）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_模拟器（Simulator）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__simulator.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

EC 主机命令模拟器接口。

<a id="details"></a>

EC 主机命令模拟器接口。

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_simulator_2Eh"></a>

```c
file simulator.h
```

相关声明：[simulator.h](../api_file_configuration_reference/P069_zephyr__mgmt__ec_host_cmd__simulator.h_文件参考.md)。

用于通过常规设备接口之外的方式与模拟器（Simulator）交互的命令头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga4ed1a006639d068f95732a1d30ba001b"></a>

```c
void ec_host_cmd_backend_sim_install_send_cb (ec_host_cmd_backend_api_send cb, struct ec_host_cmd_tx_buf **tx_buf)
```

相关声明：[ec_host_cmd_backend_sim_install_send_cb](#ga4ed1a006639d068f95732a1d30ba001b)、[ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)、[ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)。

安装回调（Callback），在此设备向主机（Host）发送数据时调用。

<a id="r_gaecf09d7134542c3bec94c131136c1f40"></a>

```c
int ec_host_cmd_backend_sim_data_received (const uint8_t *buffer, size_t len)
```

相关声明：[ec_host_cmd_backend_sim_data_received](#gaecf09d7134542c3bec94c131136c1f40)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

模拟接收来自主机（Host）的数据；数据由调用者传入本函数。

## 5.3\_详细说明（Detailed Documentation）

<a id="gaecf09d7134542c3bec94c131136c1f40"></a>

### `ec_host_cmd_backend_sim_data_received()`

```c
int ec_host_cmd_backend_sim_data_received ( const uint8_t * buffer, size_t len )
```

```c
#include <zephyr/mgmt/ec_host_cmd/simulator.h>
```

模拟接收来自主机（Host）的数据；数据由调用者传入本函数。

调用此函数可模拟主机向被测设备（DUT）发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buffer` | 包含待接收数据的缓冲区。 |
| `len` | 从上述缓冲区接收的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOMEM` | `len` 大于接收（RX）缓冲区大小时。 |
| `-EBUSY` | 主机命令框架（host command framework）正忙于处理其他请求时。 |

<a id="ga4ed1a006639d068f95732a1d30ba001b"></a>

### `ec_host_cmd_backend_sim_install_send_cb()`

```c
void ec_host_cmd_backend_sim_install_send_cb ( ec_host_cmd_backend_api_send cb, struct ec_host_cmd_tx_buf ** tx_buf )
```

```c
#include <zephyr/mgmt/ec_host_cmd/simulator.h>
```

安装回调（Callback），在此设备向主机（Host）发送数据时调用。

当此主机命令模拟器设备（host command simulator device）应向主机发送数据时，它会调用本函数提供的 `callback` 参数。注意，同一时刻只能安装一个回调；第二次调用会覆盖第一次安装的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 设备将向主机发送数据时调用的回调。 |
| `tx_buf` | 二级指针，指向用于发送数据的发送缓冲区（TX buf）结构体指针。 |


## 5.4\_原页交叉引用（Cross References）

- [simulator.h](../api_file_configuration_reference/P069_zephyr__mgmt__ec_host_cmd__simulator.h_文件参考.md)
- [ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_Microchip XEC ECIA中断控制器（Interrupt Controller）.md) · [返回大纲](大纲.md) · [下一章](P006_FCX-MLDX5 API主题.md)
