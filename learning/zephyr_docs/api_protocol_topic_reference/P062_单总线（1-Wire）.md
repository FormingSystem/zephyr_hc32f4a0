---
id: learning.zephyr-docs.api-protocol-topic-reference.page-62
title: 单总线（1-Wire）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_单总线（1-Wire）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

1-Wire 设备接口。

<a id="details"></a>

单总线设备接口（Interfaces for 1-Wire devices）。自 Zephyr 3.2 起提供；API 版本为 0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 62.1\_主题（Topics）

<a id="r_w1_5Finterface_5Fbackend"></a>

相关声明：[1-Wire 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html)。

<a id="r_w1_5Fsensor"></a>

相关声明：[1-Wire 传感器 API（Sensor API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html)。

1-Wire 传感器 API（Sensor API）

<a id="r_w1_5Fdata_5Flink"></a>

相关声明：[1-Wire 数据链路层（Data link layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html)。

1-Wire 数据链路层（Data link layer）

<a id="r_w1_5Fnetwork"></a>

相关声明：[1-Wire 网络层（Network layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html)。

1-Wire 网络层（Network layer）

<a id="header-files"></a>
<a id="files"></a>

## 62.2\_文件（Files）

<a id="r_w1_2Eh"></a>

```c
file w1.h
```

相关声明：[w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)。

单总线（1-Wire）驱动API的主头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 62.3\_枚举（Enumerations）

<a id="r_ga382989ef707709b5d26c40a394833612"></a>

```c
enum w1_settings_type { W1_SETTING_SPEED , W1_SETTING_STRONG_PULLUP , W1_SETINGS_TYPE_COUNT }
```

相关声明：[w1_settings_type](#ga382989ef707709b5d26c40a394833612)、[W1_SETTING_SPEED](#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5)、[W1_SETTING_STRONG_PULLUP](#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811)、[W1_SETINGS_TYPE_COUNT](#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22)。

定义可在运行时配置的 1-Wire 主机设置类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 62.4\_函数（Functions）

<a id="r_gab18b0f60a126d38c982730d3ad9756c1"></a>

```c
static int w1_lock_bus (const struct device *dev)
```

相关声明：[w1_lock_bus](#gab18b0f60a126d38c982730d3ad9756c1)、[device](../device_reference/P002_设备对象结构.md)。

锁定 1-Wire 总线，防止同时访问。

<a id="r_ga7230fad2428ab62fa963b50e67388c19"></a>

```c
static int w1_unlock_bus (const struct device *dev)
```

相关声明：[w1_unlock_bus](#ga7230fad2428ab62fa963b50e67388c19)、[device](../device_reference/P002_设备对象结构.md)。

解锁 1-Wire 总线。

## 62.5\_详细说明（Detailed Documentation）

<a id="ga382989ef707709b5d26c40a394833612"></a>

### `w1_settings_type`

```c
enum w1_settings_type
```

```c
#include <zephyr/drivers/w1.h>
```

定义可在运行时配置的 1-Wire 主机设置类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `W1_SETTING_SPEED` | 传入 1 时启用超速模式（Overdrive speed），传入 0 时禁用。 |
| `W1_SETTING_STRONG_PULLUP` | 传入 1 时，将在下一个数据块写入完成后立即启用强上拉电阻（strong pull-up resistor）；传入 0 时停用。 |
| `W1_SETINGS_TYPE_COUNT` | 不同设置类型（settings types）的数量。 |

<a id="gab18b0f60a126d38c982730d3ad9756c1"></a>

### `w1_lock_bus()`

```c
int w1_lock_bus ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

锁定 1-Wire 总线，防止同时访问。

此例程锁定总线，防止不同线程同时访问。调用线程会等待总线可用。允许线程再次锁定自己已经持有的互斥锁（mutex）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7230fad2428ab62fa963b50e67388c19"></a>

### `w1_unlock_bus()`

```c
int w1_unlock_bus ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

解锁 1-Wire 总线。

此例程解锁总线，允许访问总线线路。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 62.6\_原页交叉引用（Cross References）

- [1-Wire 驱动后端 API（Driver Backend API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html)
- [1-Wire 传感器 API（Sensor API）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html)
- [1-Wire 数据链路层（Data link layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html)
- [1-Wire 网络层（Network layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html)
- [w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5"></a>
<a id="gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811"></a>
<a id="gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P061_TLE9104 API主题.md) · [返回大纲](大纲.md) · [下一章](P063_Xen版本查询（Version Queries）。.md)
