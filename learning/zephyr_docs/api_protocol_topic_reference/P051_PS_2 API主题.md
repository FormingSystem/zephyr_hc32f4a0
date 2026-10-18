---
id: learning.zephyr-docs.api-protocol-topic-reference.page-51
title: PS_2 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_PS\_2 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PS/2 设备接口。

<a id="details"></a>

PS/2 设备接口（Interfaces for PS/2 devices）。自 Zephyr 2.1 起提供；API 版本为 0.8.0。此 API 的调用方负责设置按键自动重复速率（typematic rate），并使用所需的扫描码表（scan code tables）解码按键。

<a id="header-groups"></a>
<a id="groups"></a>

## 51.1\_主题（Topics）

<a id="r_ps2_5Finterface_5Fbackend"></a>

相关声明：[PS/2 驱动后端 API](P052_PS_2 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 51.2\_文件（Files）

<a id="r_ps2_2Eh"></a>

```c
file ps2.h
```

相关声明：[ps2.h](../peripheral_bus_storage_header_reference/P022_zephyr__drivers__ps2.h_头文件参考.md)。

个人系统/2（Personal System/2，PS/2）驱动API的主头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 51.3\_类型定义（Typedefs）

<a id="r_gad7cf29301681fac0d2a359d425a13b5f"></a>

```c
typedef void(* ps2_callback_t) (const struct device *dev, uint8_t data)
```

相关声明：[ps2_callback_t](#gad7cf29301681fac0d2a359d425a13b5f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用户键入或点击鼠标时调用的 PS/2 回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 51.4\_函数（Functions）

<a id="r_ga8d6da9b966432defb0cd482003c11f15"></a>

```c
int ps2_config (const struct device *dev, ps2_callback_t callback_isr)
```

相关声明：[ps2_config](#ga8d6da9b966432defb0cd482003c11f15)、[device](../device_reference/P002_设备对象结构.md)、[ps2_callback_t](#gad7cf29301681fac0d2a359d425a13b5f)。

配置 PS/2 设备实例。

<a id="r_gae291cb991ae9525552fdb52c2fa4ac5e"></a>

```c
int ps2_write (const struct device *dev, uint8_t value)
```

相关声明：[ps2_write](#gae291cb991ae9525552fdb52c2fa4ac5e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 PS/2 设备写入。

<a id="r_gab91b1efe1f07d409607922f4eb87b221"></a>

```c
int ps2_read (const struct device *dev, uint8_t *value)
```

相关声明：[ps2_read](#gab91b1efe1f07d409607922f4eb87b221)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 PS/2 设备读取从设备到主机方向的数据值。

<a id="r_ga9568487018f4ef972eb463ea2098e254"></a>

```c
int ps2_enable_callback (const struct device *dev)
```

相关声明：[ps2_enable_callback](#ga9568487018f4ef972eb463ea2098e254)、[device](../device_reference/P002_设备对象结构.md)。

启用回调。

<a id="r_gade1a470c3583e465d6a8f24a28611397"></a>

```c
int ps2_disable_callback (const struct device *dev)
```

相关声明：[ps2_disable_callback](#gade1a470c3583e465d6a8f24a28611397)、[device](../device_reference/P002_设备对象结构.md)。

禁用回调。

## 51.5\_详细说明（Detailed Documentation）

<a id="gad7cf29301681fac0d2a359d425a13b5f"></a>

### `ps2_callback_t`

```c
typedef void(* ps2_callback_t) (const struct device *dev, uint8_t data)
```

```c
#include <zephyr/drivers/ps2.h>
```

用户键入或点击鼠标时调用的 PS/2 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `data` | 传回用户的数据字节。 |

<a id="ga8d6da9b966432defb0cd482003c11f15"></a>

### `ps2_config()`

```c
int ps2_config ( const struct device * dev, ps2_callback_t callback_isr )
```

```c
#include <zephyr/drivers/ps2.h>
```

配置 PS/2 设备实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `callback_isr` | 当 PS/2 设备回复配置命令，或鼠标／键盘向客户端应用程序发送数据时调用。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gade1a470c3583e465d6a8f24a28611397"></a>

### `ps2_disable_callback()`

```c
int ps2_disable_callback ( const struct device * dev)
```

```c
#include <zephyr/drivers/ps2.h>
```

禁用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga9568487018f4ef972eb463ea2098e254"></a>

### `ps2_enable_callback()`

```c
int ps2_enable_callback ( const struct device * dev)
```

```c
#include <zephyr/drivers/ps2.h>
```

启用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gab91b1efe1f07d409607922f4eb87b221"></a>

### `ps2_read()`

```c
int ps2_read ( const struct device * dev, uint8_t * value )
```

```c
#include <zephyr/drivers/ps2.h>
```

从 PS/2 设备读取从设备到主机方向的数据值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `value` | 用于读取 PS/2 设备的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae291cb991ae9525552fdb52c2fa4ac5e"></a>

### `ps2_write()`

```c
int ps2_write ( const struct device * dev, uint8_t value )
```

```c
#include <zephyr/drivers/ps2.h>
```

向 PS/2 设备写入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `value` | 供 PS/2 设备使用的数据。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 51.6\_原页交叉引用（Cross References）

- [PS/2 驱动后端 API](P052_PS_2 驱动后端 API.md)
- [ps2.h](../peripheral_bus_storage_header_reference/P022_zephyr__drivers__ps2.h_头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P050_Renesas RZ_T 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P052_PS_2 驱动后端 API.md)
