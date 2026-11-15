---
id: learning.zephyr-docs.api-file-clock-network-reference.page-5
title: zephyr__dt-bindings__gpio__digilent-pmod.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/digilent-pmod_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_gpio\_\_digilent-pmod.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/digilent-pmod_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Pmod GPIO连接节点（Nexus）的信号索引定义。

查看此文件的源码。

<a id="details"></a>

Pmod GPIO 连接节点信号索引定义（Nexus Signal Index Definitions）。这些定义配合 digilent,pmod GPIO 连接映射（Nexus Mapping）使用。用法示例：

```dts
&spi1 {
        cs-gpios = <&pmod0 PMOD_SPI_CS GPIO_ACTIVE_LOW>;

        example_device: example-dev@0 {
                compatible = "vnd,spi-device";
                reg = <0>;
        };
};
```

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_acdb27a6e2e72f1092d49f49f356bd43d"></a>

```c
#define PMOD_IO(n)
```

相关声明：[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

参考 Pmod 接口规范（Interface Specification）：https://digilent.com/reference/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf 。

<a id="r_a48eb79c05dcea7840d652b7614fbe904"></a>

```c
#define PMOD_SPI_CS PMOD_IO(1)
```

相关声明：[PMOD_SPI_CS](#a48eb79c05dcea7840d652b7614fbe904)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS 信号索引（Signal Index）。

<a id="r_ac93de481c5b6daa4b356221afa388817"></a>

```c
#define PMOD_SPI_MOSI PMOD_IO(2)
```

相关声明：[PMOD_SPI_MOSI](#ac93de481c5b6daa4b356221afa388817)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI MOSI 信号索引（Signal Index）。

<a id="r_aa1f12f927187670390a5d4dec0ebba8d"></a>

```c
#define PMOD_SPI_MISO PMOD_IO(3)
```

相关声明：[PMOD_SPI_MISO](#aa1f12f927187670390a5d4dec0ebba8d)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI MISO 信号索引（Signal Index）。

<a id="r_a29c5bc49f3083a3d3f5ed1480f631d19"></a>

```c
#define PMOD_SPI_SCK PMOD_IO(4)
```

相关声明：[PMOD_SPI_SCK](#a29c5bc49f3083a3d3f5ed1480f631d19)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI SCK 信号索引（Signal Index）。

<a id="r_a370445d23f8953515b65605d7cc5e74a"></a>

```c
#define PMOD_EXP_SPI_CS PMOD_IO(1)
```

相关声明：[PMOD_EXP_SPI_CS](#a370445d23f8953515b65605d7cc5e74a)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS 信号索引（Signal Index）。

<a id="r_a20fd09b2126ed280842bb31aeb945c29"></a>

```c
#define PMOD_EXP_SPI_MOSI PMOD_IO(2)
```

相关声明：[PMOD_EXP_SPI_MOSI](#a20fd09b2126ed280842bb31aeb945c29)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI MOSI 信号索引（Signal Index）。

<a id="r_a211303529f74cb0989dc0d842cf055b5"></a>

```c
#define PMOD_EXP_SPI_MISO PMOD_IO(3)
```

相关声明：[PMOD_EXP_SPI_MISO](#a211303529f74cb0989dc0d842cf055b5)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI MISO 信号索引（Signal Index）。

<a id="r_a9f507e1078c0a0e47dfa1f3a8f38fa44"></a>

```c
#define PMOD_EXP_SPI_SCK PMOD_IO(4)
```

相关声明：[PMOD_EXP_SPI_SCK](#a9f507e1078c0a0e47dfa1f3a8f38fa44)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI SCK 信号索引（Signal Index）。

<a id="r_afa8baff3ecfab732f6dc20bf48e9b180"></a>

```c
#define PMOD_EXP_SPI_INT PMOD_IO(5)
```

相关声明：[PMOD_EXP_SPI_INT](#afa8baff3ecfab732f6dc20bf48e9b180)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 INT alternate 信号索引（Signal Index）。

<a id="r_a84399ae6d85fd84e74e5a2d0b6976118"></a>

```c
#define PMOD_EXP_SPI_RESET PMOD_IO(6)
```

相关声明：[PMOD_EXP_SPI_RESET](#a84399ae6d85fd84e74e5a2d0b6976118)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 RESET alternate 信号索引（Signal Index）。

<a id="r_a3985b248e927887d3a941dd0325e6f38"></a>

```c
#define PMOD_EXP_SPI_CS2 PMOD_IO(7)
```

相关声明：[PMOD_EXP_SPI_CS2](#a3985b248e927887d3a941dd0325e6f38)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS2 alternate 信号索引（Signal Index）。

<a id="r_abbcd91eacbb32ee1605aacf52a9410a6"></a>

```c
#define PMOD_EXP_SPI_CS3 PMOD_IO(8)
```

相关声明：[PMOD_EXP_SPI_CS3](#abbcd91eacbb32ee1605aacf52a9410a6)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS3 alternate 信号索引（Signal Index）。

<a id="r_a814bf19bb81bf9164029938ce6b4f17e"></a>

```c
#define PMOD_EXP_UART_INT PMOD_IO(5)
```

相关声明：[PMOD_EXP_UART_INT](#a814bf19bb81bf9164029938ce6b4f17e)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 INT alternate 信号索引（Signal Index）。

<a id="r_a723647609938e4c52ff6f582167afb6b"></a>

```c
#define PMOD_EXP_UART_RESET PMOD_IO(6)
```

相关声明：[PMOD_EXP_UART_RESET](#a723647609938e4c52ff6f582167afb6b)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 RESET alternate 信号索引（Signal Index）。

<a id="r_a09a158ba814da24543af82f2e4630888"></a>

```c
#define PMOD_HBRIDGE_DIR PMOD_IO(1)
```

相关声明：[PMOD_HBRIDGE_DIR](#a09a158ba814da24543af82f2e4630888)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 DIR 信号索引（Signal Index）。

<a id="r_afd050d415e10a29ae7125f28283b82a6"></a>

```c
#define PMOD_HBRIDGE_EN PMOD_IO(2)
```

相关声明：[PMOD_HBRIDGE_EN](#afd050d415e10a29ae7125f28283b82a6)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 EN 信号索引（Signal Index）。

<a id="r_a6b700242b6cc5e8f8e7af57c8da79757"></a>

```c
#define PMOD_DUAL_HBRIDGE_DIR1 PMOD_IO(1)
```

相关声明：[PMOD_DUAL_HBRIDGE_DIR1](#a6b700242b6cc5e8f8e7af57c8da79757)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 DIR1 信号索引（Signal Index）。

<a id="r_a126cc48a2c01b25d4ed384c07d499389"></a>

```c
#define PMOD_DUAL_HBRIDGE_EN1 PMOD_IO(2)
```

相关声明：[PMOD_DUAL_HBRIDGE_EN1](#a126cc48a2c01b25d4ed384c07d499389)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 EN1 信号索引（Signal Index）。

<a id="r_aef4dd3e547bb3f94258aa7d2746f5b6f"></a>

```c
#define PMOD_DUAL_HBRIDGE_DIR2 PMOD_IO(3)
```

相关声明：[PMOD_DUAL_HBRIDGE_DIR2](#aef4dd3e547bb3f94258aa7d2746f5b6f)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 DIR2 信号索引（Signal Index）。

<a id="r_a8449577798dcf19e5530c84ddf2adb47"></a>

```c
#define PMOD_DUAL_HBRIDGE_EN2 PMOD_IO(4)
```

相关声明：[PMOD_DUAL_HBRIDGE_EN2](#a8449577798dcf19e5530c84ddf2adb47)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 EN2 信号索引（Signal Index）。

<a id="r_a417bce3a6076a8a00ff3fdafeda0b66e"></a>

```c
#define PMOD_EXP_DUAL_HBRIDGE_DIR1 PMOD_IO(1)
```

相关声明：[PMOD_EXP_DUAL_HBRIDGE_DIR1](#a417bce3a6076a8a00ff3fdafeda0b66e)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 DIR1 信号索引（Signal Index）。

<a id="r_a7d9f088f338c345693d8a1cf8f312d32"></a>

```c
#define PMOD_EXP_DUAL_HBRIDGE_EN1 PMOD_IO(2)
```

相关声明：[PMOD_EXP_DUAL_HBRIDGE_EN1](#a7d9f088f338c345693d8a1cf8f312d32)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 EN1 信号索引（Signal Index）。

<a id="r_af4d271f3a3addfb5cbda89bff1fa6cf0"></a>

```c
#define PMOD_EXP_DUAL_HBRIDGE_DIR2 PMOD_IO(5)
```

相关声明：[PMOD_EXP_DUAL_HBRIDGE_DIR2](#af4d271f3a3addfb5cbda89bff1fa6cf0)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 DIR2 信号索引（Signal Index）。

<a id="r_a6b21aeb28f7c9abfb4af142d1ca62730"></a>

```c
#define PMOD_EXP_DUAL_HBRIDGE_EN2 PMOD_IO(6)
```

相关声明：[PMOD_EXP_DUAL_HBRIDGE_EN2](#a6b21aeb28f7c9abfb4af142d1ca62730)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 EN2 信号索引（Signal Index）。

<a id="r_a32dffa0e863e07a2c793432a222fea36"></a>

```c
#define PMOD_I2C_INT PMOD_IO(1)
```

相关声明：[PMOD_I2C_INT](#a32dffa0e863e07a2c793432a222fea36)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 INT 信号索引（Signal Index）。

<a id="r_a2878169dfb9ae1a31de0f4594fa59821"></a>

```c
#define PMOD_I2C_RESET PMOD_IO(2)
```

相关声明：[PMOD_I2C_RESET](#a2878169dfb9ae1a31de0f4594fa59821)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 RESET 信号索引（Signal Index）。

<a id="r_ae10bd211e7a7a0fa73f1b5ba250efd36"></a>

```c
#define PMOD_I2C_SCL PMOD_IO(3)
```

相关声明：[PMOD_I2C_SCL](#ae10bd211e7a7a0fa73f1b5ba250efd36)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SCL 信号索引（Signal Index）。

<a id="r_a4fc8f68216833805395af7dc344f0c77"></a>

```c
#define PMOD_I2C_SDA PMOD_IO(4)
```

相关声明：[PMOD_I2C_SDA](#a4fc8f68216833805395af7dc344f0c77)、[PMOD_IO](#acdb27a6e2e72f1092d49f49f356bd43d)。

Pmod GPIO 连接节点（Nexus Node）上的 SDA 信号索引（Signal Index）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a6b700242b6cc5e8f8e7af57c8da79757"></a>

### `PMOD_DUAL_HBRIDGE_DIR1`

```c
#define PMOD_DUAL_HBRIDGE_DIR1 PMOD_IO(1)
```

Pmod GPIO 连接节点（Nexus Node）上的 DIR1 信号索引（Signal Index）。

用于 Pmod 接口类型 5（Interface Type 5，双 H 桥）外设。

<a id="aef4dd3e547bb3f94258aa7d2746f5b6f"></a>

### `PMOD_DUAL_HBRIDGE_DIR2`

```c
#define PMOD_DUAL_HBRIDGE_DIR2 PMOD_IO(3)
```

Pmod GPIO 连接节点（Nexus Node）上的 DIR2 信号索引（Signal Index）。

用于 Pmod 接口类型 5（Interface Type 5，双 H 桥）外设。

<a id="a126cc48a2c01b25d4ed384c07d499389"></a>

### `PMOD_DUAL_HBRIDGE_EN1`

```c
#define PMOD_DUAL_HBRIDGE_EN1 PMOD_IO(2)
```

Pmod GPIO 连接节点（Nexus Node）上的 EN1 信号索引（Signal Index）。

用于 Pmod 接口类型 5（Interface Type 5，双 H 桥）外设。

<a id="a8449577798dcf19e5530c84ddf2adb47"></a>

### `PMOD_DUAL_HBRIDGE_EN2`

```c
#define PMOD_DUAL_HBRIDGE_EN2 PMOD_IO(4)
```

Pmod GPIO 连接节点（Nexus Node）上的 EN2 信号索引（Signal Index）。

用于 Pmod 接口类型 5（Interface Type 5，双 H 桥）外设。

<a id="a417bce3a6076a8a00ff3fdafeda0b66e"></a>

### `PMOD_EXP_DUAL_HBRIDGE_DIR1`

```c
#define PMOD_EXP_DUAL_HBRIDGE_DIR1 PMOD_IO(1)
```

Pmod GPIO 连接节点（Nexus Node）上的 DIR1 信号索引（Signal Index）。

用于 Pmod 接口类型 5A（Interface Type 5A，扩展双 H 桥）外设。

<a id="af4d271f3a3addfb5cbda89bff1fa6cf0"></a>

### `PMOD_EXP_DUAL_HBRIDGE_DIR2`

```c
#define PMOD_EXP_DUAL_HBRIDGE_DIR2 PMOD_IO(5)
```

Pmod GPIO 连接节点（Nexus Node）上的 DIR2 信号索引（Signal Index）。

用于 Pmod 接口类型 5A（Interface Type 5A，扩展双 H 桥）外设。

<a id="a7d9f088f338c345693d8a1cf8f312d32"></a>

### `PMOD_EXP_DUAL_HBRIDGE_EN1`

```c
#define PMOD_EXP_DUAL_HBRIDGE_EN1 PMOD_IO(2)
```

Pmod GPIO 连接节点（Nexus Node）上的 EN1 信号索引（Signal Index）。

用于 Pmod 接口类型 5A（Interface Type 5A，扩展双 H 桥）外设。

<a id="a6b21aeb28f7c9abfb4af142d1ca62730"></a>

### `PMOD_EXP_DUAL_HBRIDGE_EN2`

```c
#define PMOD_EXP_DUAL_HBRIDGE_EN2 PMOD_IO(6)
```

Pmod GPIO 连接节点（Nexus Node）上的 EN2 信号索引（Signal Index）。

用于 Pmod 接口类型 5A（Interface Type 5A，扩展双 H 桥）外设。

<a id="a370445d23f8953515b65605d7cc5e74a"></a>

### `PMOD_EXP_SPI_CS`

```c
#define PMOD_EXP_SPI_CS PMOD_IO(1)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="a3985b248e927887d3a941dd0325e6f38"></a>

### `PMOD_EXP_SPI_CS2`

```c
#define PMOD_EXP_SPI_CS2 PMOD_IO(7)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS2 alternate 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="abbcd91eacbb32ee1605aacf52a9410a6"></a>

### `PMOD_EXP_SPI_CS3`

```c
#define PMOD_EXP_SPI_CS3 PMOD_IO(8)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS3 alternate 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="afa8baff3ecfab732f6dc20bf48e9b180"></a>

### `PMOD_EXP_SPI_INT`

```c
#define PMOD_EXP_SPI_INT PMOD_IO(5)
```

Pmod GPIO 连接节点（Nexus Node）上的 INT alternate 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="a211303529f74cb0989dc0d842cf055b5"></a>

### `PMOD_EXP_SPI_MISO`

```c
#define PMOD_EXP_SPI_MISO PMOD_IO(3)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI MISO 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="a20fd09b2126ed280842bb31aeb945c29"></a>

### `PMOD_EXP_SPI_MOSI`

```c
#define PMOD_EXP_SPI_MOSI PMOD_IO(2)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI MOSI 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="a84399ae6d85fd84e74e5a2d0b6976118"></a>

### `PMOD_EXP_SPI_RESET`

```c
#define PMOD_EXP_SPI_RESET PMOD_IO(6)
```

Pmod GPIO 连接节点（Nexus Node）上的 RESET alternate 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="a9f507e1078c0a0e47dfa1f3a8f38fa44"></a>

### `PMOD_EXP_SPI_SCK`

```c
#define PMOD_EXP_SPI_SCK PMOD_IO(4)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI SCK 信号索引（Signal Index）。

用于 Pmod 接口类型 2A（Interface Type 2A，扩展 SPI）外设。

<a id="a814bf19bb81bf9164029938ce6b4f17e"></a>

### `PMOD_EXP_UART_INT`

```c
#define PMOD_EXP_UART_INT PMOD_IO(5)
```

Pmod GPIO 连接节点（Nexus Node）上的 INT alternate 信号索引（Signal Index）。

用于 Pmod 接口类型 3A（Interface Type 3A，扩展 UART）外设。

<a id="a723647609938e4c52ff6f582167afb6b"></a>

### `PMOD_EXP_UART_RESET`

```c
#define PMOD_EXP_UART_RESET PMOD_IO(6)
```

Pmod GPIO 连接节点（Nexus Node）上的 RESET alternate 信号索引（Signal Index）。

用于 Pmod 接口类型 3A（Interface Type 3A，扩展 UART）外设。

<a id="a09a158ba814da24543af82f2e4630888"></a>

### `PMOD_HBRIDGE_DIR`

```c
#define PMOD_HBRIDGE_DIR PMOD_IO(1)
```

Pmod GPIO 连接节点（Nexus Node）上的 DIR 信号索引（Signal Index）。

用于 Pmod 接口类型 4（Interface Type 4，H 桥）外设。

<a id="afd050d415e10a29ae7125f28283b82a6"></a>

### `PMOD_HBRIDGE_EN`

```c
#define PMOD_HBRIDGE_EN PMOD_IO(2)
```

Pmod GPIO 连接节点（Nexus Node）上的 EN 信号索引（Signal Index）。

用于 Pmod 接口类型 4（Interface Type 4，H 桥）外设。

<a id="a32dffa0e863e07a2c793432a222fea36"></a>

### `PMOD_I2C_INT`

```c
#define PMOD_I2C_INT PMOD_IO(1)
```

Pmod GPIO 连接节点（Nexus Node）上的 INT 信号索引（Signal Index）。

用于 Pmod 接口类型 6（Interface Type 6，I2C）外设。

<a id="a2878169dfb9ae1a31de0f4594fa59821"></a>

### `PMOD_I2C_RESET`

```c
#define PMOD_I2C_RESET PMOD_IO(2)
```

Pmod GPIO 连接节点（Nexus Node）上的 RESET 信号索引（Signal Index）。

用于 Pmod 接口类型 6（Interface Type 6，I2C）外设。

<a id="ae10bd211e7a7a0fa73f1b5ba250efd36"></a>

### `PMOD_I2C_SCL`

```c
#define PMOD_I2C_SCL PMOD_IO(3)
```

Pmod GPIO 连接节点（Nexus Node）上的 SCL 信号索引（Signal Index）。

用于 Pmod 接口类型 6（Interface Type 6，I2C）外设。

<a id="a4fc8f68216833805395af7dc344f0c77"></a>

### `PMOD_I2C_SDA`

```c
#define PMOD_I2C_SDA PMOD_IO(4)
```

Pmod GPIO 连接节点（Nexus Node）上的 SDA 信号索引（Signal Index）。

用于 Pmod 接口类型 6（Interface Type 6，I2C）外设。

<a id="acdb27a6e2e72f1092d49f49f356bd43d"></a>

### `PMOD_IO`

```c
#define PMOD_IO ( n)
```

展开值（Value）：

```c
((n) - 1)
```

参考 Pmod 接口规范（Interface Specification）：https://digilent.com/reference/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf 。

Pmod GPIO 连接节点（Nexus Node）上的 IO[n] 信号，遵循 Pmod 接口类型 1 或 1A（GPIO 或扩展 GPIO）。

Pmod GPIO 连接节点（Nexus）将引脚索引 0..7 映射到 IO1..IO8。

<a id="a48eb79c05dcea7840d652b7614fbe904"></a>

### `PMOD_SPI_CS`

```c
#define PMOD_SPI_CS PMOD_IO(1)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI CS 信号索引（Signal Index）。

用于 Pmod 接口类型 2（Interface Type 2，SPI）外设。

<a id="aa1f12f927187670390a5d4dec0ebba8d"></a>

### `PMOD_SPI_MISO`

```c
#define PMOD_SPI_MISO PMOD_IO(3)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI MISO 信号索引（Signal Index）。

用于 Pmod 接口类型 2（Interface Type 2，SPI）外设。

<a id="ac93de481c5b6daa4b356221afa388817"></a>

### `PMOD_SPI_MOSI`

```c
#define PMOD_SPI_MOSI PMOD_IO(2)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI MOSI 信号索引（Signal Index）。

用于 Pmod 接口类型 2（Interface Type 2，SPI）外设。

<a id="a29c5bc49f3083a3d3f5ed1480f631d19"></a>

### `PMOD_SPI_SCK`

```c
#define PMOD_SPI_SCK PMOD_IO(4)
```

Pmod GPIO 连接节点（Nexus Node）上的 SPI SCK 信号索引（Signal Index）。

用于 Pmod 接口类型 2（Interface Type 2，SPI）外设。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_system_reference/P008_digilent-pmod.h_源码浏览.md)
- [https://digilent.com/reference/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf](https://digilent.com/reference/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf)
- [DIR](../api_file_reference/P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__bluetooth__cs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__net__dns_resolve.h_文件参考.md)
