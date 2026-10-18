---
id: learning.zephyr-docs.modem-wireless-model-reference.page-28
title: lora_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlora__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_lora\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlora__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：LoRa驱动操作。

```c
#include <zephyr/drivers/lora.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：LoRa 驱动操作。这是每个 LoRa 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_ae5fc4c8418225f44a220b6b4d223f114"></a>

```c
lora_api_config config
```

相关声明：[lora_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gabc8cba7c3f81961eac289adc40d3c8e1)、[config](#ae5fc4c8418225f44a220b6b4d223f114)。

必需（REQ）：配置 LoRa 调制解调器。

<a id="r_a83a2e31b05a17ddf82de6bb6e55c1381"></a>

```c
lora_api_config_gfsk config_gfsk
```

相关声明：[lora_api_config_gfsk](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga8993b902d31eac8870eb3a7f27a255cd)、[config_gfsk](#a83a2e31b05a17ddf82de6bb6e55c1381)。

可选（OPT）：配置高斯频移键控（GFSK）调制解调器。

<a id="r_aa8600981dbaa6eaf35da02fb586828ab"></a>

```c
lora_api_airtime airtime
```

相关声明：[lora_api_airtime](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga02edec1bd6925622926b3fc8833c8bec)、[airtime](#aa8600981dbaa6eaf35da02fb586828ab)。

必需（REQ）：查询给定长度数据包的空中传输时间（airtime）。

<a id="r_ad37a8cdd8801b9c0036259dde6bc1a93"></a>

```c
lora_api_send send
```

相关声明：[lora_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gaddff151212a432c1dbf00c3665033eb0)、[send](#ad37a8cdd8801b9c0036259dde6bc1a93)。

必需（REQ）：通过 LoRa 发送数据。

<a id="r_ab5ac6d906cc2429f065d720e3af1ceaf"></a>

```c
lora_api_send_async send_async
```

相关声明：[lora_api_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga1dafc39726315c7921d7dd6b1e0caac4)、[send_async](#ab5ac6d906cc2429f065d720e3af1ceaf)。

必需（REQ）：通过 LoRa 异步发送数据。

<a id="r_a30296d89ea10356fd1ded3dcbcae7618"></a>

```c
lora_api_recv recv
```

相关声明：[lora_api_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga166896d4f655cc2630e5951b1ad45c01)、[recv](#a30296d89ea10356fd1ded3dcbcae7618)。

必需（REQ）：通过 LoRa 接收数据。

<a id="r_aa2b7d4975ed91b4c0898842aa9e271fd"></a>

```c
lora_api_recv_async recv_async
```

相关声明：[lora_api_recv_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gad3bac89281cbf6cc79f2f4df6f4b4329)、[recv_async](#aa2b7d4975ed91b4c0898842aa9e271fd)。

必需（REQ）：通过 LoRa 异步接收数据。

<a id="r_a98fc632a4e30079bc08b94b9d5dbbb1c"></a>

```c
lora_api_cad cad
```

相关声明：[lora_api_cad](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gaf308b8431762462eb172f4e0bdfce99f)、[cad](#a98fc632a4e30079bc08b94b9d5dbbb1c)。

可选（OPT）：执行信道活动检测（Channel Activity Detection，CAD）。

<a id="r_a8c579d89e40f1b9374711d5d3bef148b"></a>

```c
lora_api_cad_async cad_async
```

相关声明：[lora_api_cad_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga604500a11fa03edae97862c29b233ed1)、[cad_async](#a8c579d89e40f1b9374711d5d3bef148b)。

可选（OPT）：异步执行信道活动检测（CAD）。

<a id="r_afc1eb7fabc1e59b224317ddd912f4d77"></a>

```c
lora_api_rssi rssi
```

相关声明：[lora_api_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga185dba9fc898f2c9407b9a9461695b8e)、[rssi](#afc1eb7fabc1e59b224317ddd912f4d77)。

可选（OPT）：读取当前信道的瞬时接收信号强度指示（RSSI）。

<a id="r_a255ba5321ad6423de1b613b2c3520334"></a>

```c
lora_api_recv_duty_cycle_async recv_duty_cycle_async
```

相关声明：[lora_api_recv_duty_cycle_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gafac86253dce5dbe9286683f565663971)、[recv_duty_cycle_async](#a255ba5321ad6423de1b613b2c3520334)。

可选（OPT）：启动周期性接收，即无线唤醒（wake-on-radio）。

<a id="r_a1e2d0208c52e6fe0ec6c51484537f033"></a>

```c
lora_api_recv_duty_cycle recv_duty_cycle
```

相关声明：[lora_api_recv_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga8ad83577ede3ca3c7d4b037c95e039e3)、[recv_duty_cycle](#a1e2d0208c52e6fe0ec6c51484537f033)。

可选（OPT）：使用周期性接收机制接收数据，即无线唤醒（wake-on-radio）。

<a id="r_ad582af08f38b4c2fc83588e7108bef6b"></a>

```c
lora_api_test_cw test_cw
```

相关声明：[lora_api_test_cw](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga796b75a4b27b9331d78f1916e36ea1d2)、[test_cw](#ad582af08f38b4c2fc83588e7108bef6b)。

可选（OPT）：在给定频率上发射未调制的连续波（continuous wave）。

## 28.2\_详细说明（Detailed Documentation）

<a id="aa8600981dbaa6eaf35da02fb586828ab"></a>

### `airtime`

```c
lora_api_airtime lora_driver_api::airtime
```

必需（REQ）：查询给定长度数据包的空中传输时间（airtime）。

<a id="a98fc632a4e30079bc08b94b9d5dbbb1c"></a>

### `cad`

```c
lora_api_cad lora_driver_api::cad
```

可选（OPT）：执行信道活动检测（Channel Activity Detection，CAD）。

<a id="a8c579d89e40f1b9374711d5d3bef148b"></a>

### `cad_async`

```c
lora_api_cad_async lora_driver_api::cad_async
```

可选（OPT）：异步执行信道活动检测（CAD）。

<a id="ae5fc4c8418225f44a220b6b4d223f114"></a>

### `config`

```c
lora_api_config lora_driver_api::config
```

必需（REQ）：配置 LoRa 调制解调器。

<a id="a83a2e31b05a17ddf82de6bb6e55c1381"></a>

### `config_gfsk`

```c
lora_api_config_gfsk lora_driver_api::config_gfsk
```

可选（OPT）：配置高斯频移键控（GFSK）调制解调器。

<a id="a30296d89ea10356fd1ded3dcbcae7618"></a>

### `recv`

```c
lora_api_recv lora_driver_api::recv
```

必需（REQ）：通过 LoRa 接收数据。

<a id="aa2b7d4975ed91b4c0898842aa9e271fd"></a>

### `recv_async`

```c
lora_api_recv_async lora_driver_api::recv_async
```

必需（REQ）：通过 LoRa 异步接收数据。

<a id="a1e2d0208c52e6fe0ec6c51484537f033"></a>

### `recv_duty_cycle`

```c
lora_api_recv_duty_cycle lora_driver_api::recv_duty_cycle
```

可选（OPT）：使用周期性接收机制接收数据，即无线唤醒（wake-on-radio）。

<a id="a255ba5321ad6423de1b613b2c3520334"></a>

### `recv_duty_cycle_async`

```c
lora_api_recv_duty_cycle_async lora_driver_api::recv_duty_cycle_async
```

可选（OPT）：启动周期性接收，即无线唤醒（wake-on-radio）。

<a id="afc1eb7fabc1e59b224317ddd912f4d77"></a>

### `rssi`

```c
lora_api_rssi lora_driver_api::rssi
```

可选（OPT）：读取当前信道的瞬时接收信号强度指示（RSSI）。

<a id="ad37a8cdd8801b9c0036259dde6bc1a93"></a>

### `send`

```c
lora_api_send lora_driver_api::send
```

必需（REQ）：通过 LoRa 发送数据。

<a id="ab5ac6d906cc2429f065d720e3af1ceaf"></a>

### `send_async`

```c
lora_api_send_async lora_driver_api::send_async
```

必需（REQ）：通过 LoRa 异步发送数据。

<a id="ad582af08f38b4c2fc83588e7108bef6b"></a>

### `test_cw`

```c
lora_api_test_cw lora_driver_api::test_cw
```

可选（OPT）：在给定频率上发射未调制的连续波（continuous wave）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lora.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lora.h](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h_source.html)
- [lora_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gabc8cba7c3f81961eac289adc40d3c8e1)
- [lora_api_config_gfsk](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga8993b902d31eac8870eb3a7f27a255cd)
- [lora_api_airtime](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga02edec1bd6925622926b3fc8833c8bec)
- [lora_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gaddff151212a432c1dbf00c3665033eb0)
- [lora_api_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga1dafc39726315c7921d7dd6b1e0caac4)
- [lora_api_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga166896d4f655cc2630e5951b1ad45c01)
- [lora_api_recv_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gad3bac89281cbf6cc79f2f4df6f4b4329)
- [lora_api_cad](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gaf308b8431762462eb172f4e0bdfce99f)
- [lora_api_cad_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga604500a11fa03edae97862c29b233ed1)
- [lora_api_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga185dba9fc898f2c9407b9a9461695b8e)
- [lora_api_recv_duty_cycle_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gafac86253dce5dbe9286683f565663971)
- [lora_api_recv_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga8ad83577ede3ca3c7d4b037c95e039e3)
- [lora_api_test_cw](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga796b75a4b27b9331d78f1916e36ea1d2)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_hl78xx_network_operator_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_lora_modem_config_结构体.md)
