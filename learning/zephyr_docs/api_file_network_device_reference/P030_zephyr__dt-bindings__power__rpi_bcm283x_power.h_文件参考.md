---
id: learning.zephyr-docs.api-file-network-device-reference.page-30
title: zephyr__dt-bindings__power__rpi_bcm283x_power.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi__bcm283x__power_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_dt-bindings\_\_power\_\_rpi\_bcm283x\_power.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpi__bcm283x__power_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Raspberry Pi BCM283x的电源域标识符（Power Domain Identifiers）。

查看此文件的源码。

<a id="details"></a>

树莓派（Raspberry Pi）BCM283x 电源域标识符（Power Domain Identifiers），对应树莓派固件邮箱属性接口（Firmware Mailbox Property Interface）的电源设备标识。**另请参见（See Also）：**[邮箱电源属性说明](https://github.com/raspberrypi/firmware/wiki/Mailbox-property-interface#power)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 30.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 电源域标识（Power Domain IDs）

<a id="r_a7d80ff98d309711e9d808dab366de639"></a>

```c
#define RPI_POWER_DOMAIN_SD_CARD 0x00000000U
```

相关声明：[RPI_POWER_DOMAIN_SD_CARD](#a7d80ff98d309711e9d808dab366de639)。

安全数字存储卡（SD Card）。

<a id="r_ab3aa6437f1e0747e6a9a7dbc734bc67b"></a>

```c
#define RPI_POWER_DOMAIN_UART0 0x00000001U
```

相关声明：[RPI_POWER_DOMAIN_UART0](#ab3aa6437f1e0747e6a9a7dbc734bc67b)。

通用异步收发器 UART0。

<a id="r_a3cb2bfafcf214fb4636f4528205c7b85"></a>

```c
#define RPI_POWER_DOMAIN_UART1 0x00000002U
```

相关声明：[RPI_POWER_DOMAIN_UART1](#a3cb2bfafcf214fb4636f4528205c7b85)。

通用异步收发器 UART1。

<a id="r_a1853b8eeb98c8f513c0cc89cb10363c2"></a>

```c
#define RPI_POWER_DOMAIN_USB_HCD 0x00000003U
```

相关声明：[RPI_POWER_DOMAIN_USB_HCD](#a1853b8eeb98c8f513c0cc89cb10363c2)。

USB 主机控制器（USB Host Controller）

<a id="r_a72d1f0b51cffcdd58dcc018557da1d39"></a>

```c
#define RPI_POWER_DOMAIN_I2C0 0x00000004U
```

相关声明：[RPI_POWER_DOMAIN_I2C0](#a72d1f0b51cffcdd58dcc018557da1d39)。

集成电路间总线 I2C0。

<a id="r_acf226a114aa3950983d45f351f3fe69f"></a>

```c
#define RPI_POWER_DOMAIN_I2C1 0x00000005U
```

相关声明：[RPI_POWER_DOMAIN_I2C1](#acf226a114aa3950983d45f351f3fe69f)。

集成电路间总线 I2C1。

<a id="r_a68ef643fa0de34666b230b94cc5994a3"></a>

```c
#define RPI_POWER_DOMAIN_I2C2 0x00000006U
```

相关声明：[RPI_POWER_DOMAIN_I2C2](#a68ef643fa0de34666b230b94cc5994a3)。

集成电路间总线 I2C2。

<a id="r_a6c5fde9d16eda407af64fe06efd267e8"></a>

```c
#define RPI_POWER_DOMAIN_SPI 0x00000007U
```

相关声明：[RPI_POWER_DOMAIN_SPI](#a6c5fde9d16eda407af64fe06efd267e8)。

串行外设接口（SPI）

<a id="r_aac31d067a16d62650f47fbd62a062c2b"></a>

```c
#define RPI_POWER_DOMAIN_CCP2TX 0x00000008U
```

相关声明：[RPI_POWER_DOMAIN_CCP2TX](#aac31d067a16d62650f47fbd62a062c2b)。

CCP2TX 模块。

<a id="r_a2f765e7143cf4f7738188e6861689901"></a>

```c
#define RPI_POWER_DOMAIN_UNKNOWN0 0x00000009U
```

相关声明：[RPI_POWER_DOMAIN_UNKNOWN0](#a2f765e7143cf4f7738188e6861689901)。

未知域 0（Unknown Domain 0），仅适用于 RPi4。

<a id="r_a7c014d072a9bf16f3d842b0400f7aa70"></a>

```c
#define RPI_POWER_DOMAIN_UNKNOWN1 0x0000000AU
```

相关声明：[RPI_POWER_DOMAIN_UNKNOWN1](#a7c014d072a9bf16f3d842b0400f7aa70)。

未知域 1（Unknown Domain 1），仅适用于 RPi4。

## 30.2\_详细说明（Detailed Documentation）

<a id="aac31d067a16d62650f47fbd62a062c2b"></a>

### `RPI_POWER_DOMAIN_CCP2TX`

```c
#define RPI_POWER_DOMAIN_CCP2TX 0x00000008U
```

CCP2TX 模块。

<a id="a72d1f0b51cffcdd58dcc018557da1d39"></a>

### `RPI_POWER_DOMAIN_I2C0`

```c
#define RPI_POWER_DOMAIN_I2C0 0x00000004U
```

集成电路间总线 I2C0。

<a id="acf226a114aa3950983d45f351f3fe69f"></a>

### `RPI_POWER_DOMAIN_I2C1`

```c
#define RPI_POWER_DOMAIN_I2C1 0x00000005U
```

集成电路间总线 I2C1。

<a id="a68ef643fa0de34666b230b94cc5994a3"></a>

### `RPI_POWER_DOMAIN_I2C2`

```c
#define RPI_POWER_DOMAIN_I2C2 0x00000006U
```

集成电路间总线 I2C2。

<a id="a7d80ff98d309711e9d808dab366de639"></a>

### `RPI_POWER_DOMAIN_SD_CARD`

```c
#define RPI_POWER_DOMAIN_SD_CARD 0x00000000U
```

安全数字存储卡（SD Card）。

<a id="a6c5fde9d16eda407af64fe06efd267e8"></a>

### `RPI_POWER_DOMAIN_SPI`

```c
#define RPI_POWER_DOMAIN_SPI 0x00000007U
```

串行外设接口（SPI）

<a id="ab3aa6437f1e0747e6a9a7dbc734bc67b"></a>

### `RPI_POWER_DOMAIN_UART0`

```c
#define RPI_POWER_DOMAIN_UART0 0x00000001U
```

通用异步收发器 UART0。

<a id="a3cb2bfafcf214fb4636f4528205c7b85"></a>

### `RPI_POWER_DOMAIN_UART1`

```c
#define RPI_POWER_DOMAIN_UART1 0x00000002U
```

通用异步收发器 UART1。

<a id="a2f765e7143cf4f7738188e6861689901"></a>

### `RPI_POWER_DOMAIN_UNKNOWN0`

```c
#define RPI_POWER_DOMAIN_UNKNOWN0 0x00000009U
```

未知域 0（Unknown Domain 0），仅适用于 RPi4。

<a id="a7c014d072a9bf16f3d842b0400f7aa70"></a>

### `RPI_POWER_DOMAIN_UNKNOWN1`

```c
#define RPI_POWER_DOMAIN_UNKNOWN1 0x0000000AU
```

未知域 1（Unknown Domain 1），仅适用于 RPi4。

<a id="a1853b8eeb98c8f513c0cc89cb10363c2"></a>

### `RPI_POWER_DOMAIN_USB_HCD`

```c
#define RPI_POWER_DOMAIN_USB_HCD 0x00000003U
```

USB 主机控制器（USB Host Controller）


## 30.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P727_rpi_bcm283x_power.h_源码浏览.md)
- [https://github.com/raspberrypi/firmware/wiki/Mailbox-property-interface#power](https://github.com/raspberrypi/firmware/wiki/Mailbox-property-interface#power)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P029_zephyr__dt-bindings__gpio__realtek-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__bluetooth__mesh__rpr_cli.h_文件参考.md)
