---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-5
title: HTU31D API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_HTU31D API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TE Connectivity HTU31D 温湿度传感器（Temperature and humidity sensor）。

<a id="details"></a>

TE Connectivity HTU31D 温湿度传感器（Temperature and humidity sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_htu31d_2Eh"></a>

```c
file htu31d.h
```

相关声明：[htu31d.h](../api_file_protocol_service_reference/P019_zephyr__drivers__sensor__htu31d.h_文件参考.md)。

HTU31D传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga607e81aff14b1638989d6f85f0fb661f"></a>

```c
int htu31d_heater_set (const struct device *dev, bool enable)
```

相关声明：[htu31d_heater_set](#ga607e81aff14b1638989d6f85f0fb661f)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用片上加热器（On-chip Heater）。

<a id="r_gad20e48337c29bf96075c428f2c6f6549"></a>

```c
int htu31d_read_diagnostics (const struct device *dev, uint8_t *diag)
```

相关声明：[htu31d_read_diagnostics](#gad20e48337c29bf96075c428f2c6f6549)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取传感器诊断寄存器（Diagnostics Register）。

<a id="r_ga18d4854388d8f53cf94c38b81b29ef2f"></a>

```c
int htu31d_read_serial (const struct device *dev, uint32_t *serial)
```

相关声明：[htu31d_read_serial](#ga18d4854388d8f53cf94c38b81b29ef2f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取工厂写入的 24 位序列号（Factory-programmed Serial Number）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.3\_诊断寄存器位标志（Diagnostics Register Bit Flags）

`htu31d_read_diagnostics()` 返回的诊断字节（Diagnostics Byte）中的位位置。

<a id="r_ga67d7943b289a59c6150daef738e40ceb"></a>

```c
#define HTU31D_DIAG_HEATER_ON BIT(0)
```

相关声明：[HTU31D_DIAG_HEATER_ON](#ga67d7943b289a59c6150daef738e40ceb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

加热器（Heater）当前已启用。

<a id="r_ga75b6d870de1388b42511d34bcc65b286"></a>

```c
#define HTU31D_DIAG_TEMP_LOW_ERR BIT(1)
```

相关声明：[HTU31D_DIAG_TEMP_LOW_ERR](#ga75b6d870de1388b42511d34bcc65b286)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

温度（Temperature）低于最小值。

<a id="r_ga07ad22feb0fc89bcc1c16971bd74e1ff"></a>

```c
#define HTU31D_DIAG_TEMP_HIGH_ERR BIT(2)
```

相关声明：[HTU31D_DIAG_TEMP_HIGH_ERR](#ga07ad22feb0fc89bcc1c16971bd74e1ff)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

温度（Temperature）高于最大值。

<a id="r_ga97027a00d1c4ea06db6a2d22236ccf09"></a>

```c
#define HTU31D_DIAG_TEMP_OVER_ERR BIT(3)
```

相关声明：[HTU31D_DIAG_TEMP_OVER_ERR](#ga97027a00d1c4ea06db6a2d22236ccf09)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

温度下溢／上溢（Temperature Under/Over-run）。

<a id="r_gaa08ff4f3d320249213925f1fb220d29a"></a>

```c
#define HTU31D_DIAG_HUMI_LOW_ERR BIT(4)
```

相关声明：[HTU31D_DIAG_HUMI_LOW_ERR](#gaa08ff4f3d320249213925f1fb220d29a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

湿度（Humidity）低于最小值。

<a id="r_gaa5d049d701095c976fb7a7f27d6a4878"></a>

```c
#define HTU31D_DIAG_HUMI_HIGH_ERR BIT(5)
```

相关声明：[HTU31D_DIAG_HUMI_HIGH_ERR](#gaa5d049d701095c976fb7a7f27d6a4878)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

湿度（Humidity）高于最大值。

<a id="r_ga06035755bd7c270e481b2434022b1664"></a>

```c
#define HTU31D_DIAG_HUMI_OVER_ERR BIT(6)
```

相关声明：[HTU31D_DIAG_HUMI_OVER_ERR](#ga06035755bd7c270e481b2434022b1664)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

湿度下溢／上溢（Humidity Under/Over-run）。

<a id="r_gad72c35292b8838b23fc7df3a102c6ba9"></a>

```c
#define HTU31D_DIAG_NVM_ERR BIT(7)
```

相关声明：[HTU31D_DIAG_NVM_ERR](#gad72c35292b8838b23fc7df3a102c6ba9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

非易失性存储器（NVM）校验和错误（Checksum Error）。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga67d7943b289a59c6150daef738e40ceb"></a>

### `HTU31D_DIAG_HEATER_ON`

```c
#define HTU31D_DIAG_HEATER_ON BIT(0)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

加热器（Heater）当前已启用。

<a id="gaa5d049d701095c976fb7a7f27d6a4878"></a>

### `HTU31D_DIAG_HUMI_HIGH_ERR`

```c
#define HTU31D_DIAG_HUMI_HIGH_ERR BIT(5)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

湿度（Humidity）高于最大值。

<a id="gaa08ff4f3d320249213925f1fb220d29a"></a>

### `HTU31D_DIAG_HUMI_LOW_ERR`

```c
#define HTU31D_DIAG_HUMI_LOW_ERR BIT(4)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

湿度（Humidity）低于最小值。

<a id="ga06035755bd7c270e481b2434022b1664"></a>

### `HTU31D_DIAG_HUMI_OVER_ERR`

```c
#define HTU31D_DIAG_HUMI_OVER_ERR BIT(6)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

湿度下溢／上溢（Humidity Under/Over-run）。

<a id="gad72c35292b8838b23fc7df3a102c6ba9"></a>

### `HTU31D_DIAG_NVM_ERR`

```c
#define HTU31D_DIAG_NVM_ERR BIT(7)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

非易失性存储器（NVM）校验和错误（Checksum Error）。

<a id="ga07ad22feb0fc89bcc1c16971bd74e1ff"></a>

### `HTU31D_DIAG_TEMP_HIGH_ERR`

```c
#define HTU31D_DIAG_TEMP_HIGH_ERR BIT(2)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

温度（Temperature）高于最大值。

<a id="ga75b6d870de1388b42511d34bcc65b286"></a>

### `HTU31D_DIAG_TEMP_LOW_ERR`

```c
#define HTU31D_DIAG_TEMP_LOW_ERR BIT(1)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

温度（Temperature）低于最小值。

<a id="ga97027a00d1c4ea06db6a2d22236ccf09"></a>

### `HTU31D_DIAG_TEMP_OVER_ERR`

```c
#define HTU31D_DIAG_TEMP_OVER_ERR BIT(3)
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

温度下溢／上溢（Temperature Under/Over-run）。

<a id="ga607e81aff14b1638989d6f85f0fb661f"></a>

### `htu31d_heater_set()`

```c
int htu31d_heater_set ( const struct device * dev, bool enable )
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

启用或禁用片上加热器（On-chip Heater）。

加热器（Heater）可用于去除凝露或执行传感器自诊断。启用时会使测得的温度升高数度，不应持续保持开启。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `enable` | `true` 启用加热器（Heater），`false` 禁用。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，I2C 错误时返回负 `errno`。

<a id="gad20e48337c29bf96075c428f2c6f6549"></a>

### `htu31d_read_diagnostics()`

```c
int htu31d_read_diagnostics ( const struct device * dev, uint8_t * diag )
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

读取传感器诊断寄存器（Diagnostics Register）。

诊断字节（Diagnostics Byte）报告持续保留的故障标志（Persistent Fault Flags）；使用 `HTU31D_DIAG_*` 位宏解码返回值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `diag` | 输出参数（Output），填入 8 位诊断字（Diagnostics Word）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，CRC 校验失败返回 `-EIO`，或返回其他负 `errno`。

<a id="ga18d4854388d8f53cf94c38b81b29ef2f"></a>

### `htu31d_read_serial()`

```c
int htu31d_read_serial ( const struct device * dev, uint32_t * serial )
```

```c
#include <zephyr/drivers/sensor/htu31d.h>
```

读取工厂写入的 24 位序列号（Factory-programmed Serial Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `serial` | 输出参数（Output），将 24 位序列号填入低三个字节，高字节为 `0`。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，CRC 校验失败返回 `-EIO`，或返回其他负 `errno`。


## 5.5\_原页交叉引用（Cross References）

- [htu31d.h](../api_file_protocol_service_reference/P019_zephyr__drivers__sensor__htu31d.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_主机命令驱动后端 API（Host Command Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P006_IT51XXX API主题.md)
