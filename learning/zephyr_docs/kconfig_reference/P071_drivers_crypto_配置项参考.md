---
id: learning.zephyr-docs.kconfig-reference.page-71
title: "`drivers/crypto`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第71章\_`drivers/crypto`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/crypto` 的 60 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CRYPTO"></a>

## 71.1 `CONFIG_CRYPTO`

**提示（Prompt）**：密码学驱动（Crypto Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_OSDP_SC_ENABLED
CONFIG_NETMIDI2_HOST_AUTH
```

**定义位置（Location）**：[`drivers/crypto/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_SC_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP_SC_ENABLED)、[`CONFIG_NETMIDI2_HOST_AUTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETMIDI2_HOST_AUTH)。

<a id="CONFIG_CRYPTO_ASYNC"></a>

## 71.2 `CONFIG_CRYPTO_ASYNC`

**提示（Prompt）**：支持异步密码学操作（ASYNC Crypto Operations）

**说明（Help）**

启用异步密码学操作（ASYNC Crypto Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_SMARTBOND && CONFIG_CRYPTO
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.smartbond:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.smartbond#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → SmartBond 密码学加速器驱动（Cryptographic Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_SMARTBOND`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SMARTBOND)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_ATAES132A"></a>

## 71.3 `CONFIG_CRYPTO_ATAES132A`

**提示（Prompt）**：Atmel ATAES132A 32k AES 串行 EEPROM 支持（AES Serial EEPROM Support）

**说明（Help）**

启用 Atmel ATAES132A 32k AES 串行电可擦可编程只读存储器（Serial EEPROM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_ATAES132A_ENABLED && CONFIG_I2C && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.ataes132a:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.ataes132a#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_ATAES132A_I2C_SPEED_FAST"></a>

## 71.4 `CONFIG_CRYPTO_ATAES132A_I2C_SPEED_FAST`

**提示（Prompt）**：快速模式（Fast）

**说明（Help）**

最高 400 kHz 的快速总线速率（Fast Bus Speed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.ataes132a:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.ataes132a#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → Atmel ATAES132A 32k AES 串行 EEPROM 支持（AES Serial EEPROM Support） → ATAES132A I2C 总线速率（Bus Speed）

<a id="CONFIG_CRYPTO_ATAES132A_I2C_SPEED_STANDARD"></a>

## 71.5 `CONFIG_CRYPTO_ATAES132A_I2C_SPEED_STANDARD`

**提示（Prompt）**：标准模式（Standard）

**说明（Help）**

最高 100 kHz 的标准总线速率（Standard Bus Speed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.ataes132a:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.ataes132a#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → Atmel ATAES132A 32k AES 串行 EEPROM 支持（AES Serial EEPROM Support） → ATAES132A I2C 总线速率（Bus Speed）

<a id="CONFIG_CRYPTO_BEE_AES"></a>

## 71.6 `CONFIG_CRYPTO_BEE_AES`

**提示（Prompt）**：瑞昱 Bee AES 硬件加速器（Realtek AES Hardware Accelerator）

**说明（Help）**

启用瑞昱（Realtek）Bee 系列片上系统（SoC），即 RTL8752H、RTL87x2G，的 AES 硬件加速器（Hardware Accelerator）驱动。支持 AES-128 和 AES-256 的电子密码本（ECB）、密码分组链接（CBC）及计数器（CTR）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_AES_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_BEE_AES_SESSIONS_MAX"></a>

## 71.7 `CONFIG_CRYPTO_BEE_AES_SESSIONS_MAX`

**提示（Prompt）**：最大并发 AES 会话数量（Concurrent AES Sessions）

**说明（Help）**

最大并发 AES 密码运算会话（Cipher Session）数量。每个会话约使用 64 字节 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_BEE_AES && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bee:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bee#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 瑞昱 Bee AES 硬件加速器（Realtek AES Hardware Accelerator）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_BEE_AES`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_BEE_AES)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_BEE_AES_SWAP_BUF"></a>

## 71.8 `CONFIG_CRYPTO_BEE_AES_SWAP_BUF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在调用 AES 硬件引擎之前和之后启用字节交换（Byte Swapping）。RTL8752H 需要这样做以匹配硬件引擎的字顺序（Word Order）；RTL87x2G 接受正常字节顺序的缓冲区，应保持关闭。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_BEE_AES && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_RTL8752H
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bee:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bee#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 瑞昱 Bee AES 硬件加速器（Realtek AES Hardware Accelerator）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_BEE_AES`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_BEE_AES)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)。

<a id="CONFIG_CRYPTO_BEE_SHA256"></a>

## 71.9 `CONFIG_CRYPTO_BEE_SHA256`

**提示（Prompt）**：瑞昱 Bee SHA-256 硬件加速器（Realtek Hardware Accelerator）

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC），即 RTL8752H、RTL87x2G，的 SHA-256 硬件加速器（Hardware Accelerator）驱动，支持一次性 SHA-256 计算（One-Shot Calculation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_SHA256_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bee:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bee#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_BFLB_SEC_ENG_AES"></a>

## 71.10 `CONFIG_CRYPTO_BFLB_SEC_ENG_AES`

**提示（Prompt）**：博流 SEC 引擎 AES 密码学驱动（Bouffalo Lab Crypto Driver）

**说明（Help）**

启用博流（Bouffalo Lab）SEC 引擎密码学（Crypto）驱动，提供硬件加速的 AES 电子密码本（ECB）、密码分组链接（CBC）和计数器（CTR）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_SEC_ENG_AES_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_BFLB_SEC_ENG_AES_MAX_SESSION"></a>

## 71.11 `CONFIG_CRYPTO_BFLB_SEC_ENG_AES_MAX_SESSION`

**提示（Prompt）**：最大并发 AES 密码运算会话数量（AES Cipher Sessions）

**说明（Help）**

最大并发 AES 密码运算会话（Cipher Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_BFLB_SEC_ENG_AES && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bflb:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bflb#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 博流 SEC 引擎 AES 密码学驱动（Bouffalo Lab Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_BFLB_SEC_ENG_AES`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_BFLB_SEC_ENG_AES)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_BFLB_SEC_ENG_SHA"></a>

## 71.12 `CONFIG_CRYPTO_BFLB_SEC_ENG_SHA`

**提示（Prompt）**：博流 SEC 引擎 SHA 哈希驱动（Bouffalo Lab Hash Driver）

**说明（Help）**

启用博流（Bouffalo Lab）SEC 引擎 SHA 哈希（Hash）驱动，提供硬件加速的 SHA-224 和 SHA-256。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_SEC_ENG_SHA_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bflb:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bflb#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_BFLB_SEC_ENG_SHA_MAX_SESSION"></a>

## 71.13 `CONFIG_CRYPTO_BFLB_SEC_ENG_SHA_MAX_SESSION`

**提示（Prompt）**：最大并发 SHA 哈希会话数量（SHA Hash Sessions）

**说明（Help）**

最大并发 SHA 哈希会话（Hash Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_BFLB_SEC_ENG_SHA && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.bflb:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.bflb#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 博流 SEC 引擎 SHA 哈希驱动（Bouffalo Lab Hash Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_BFLB_SEC_ENG_SHA`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_BFLB_SEC_ENG_SHA)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_CC23X0"></a>

## 71.14 `CONFIG_CRYPTO_CC23X0`

**提示（Prompt）**：CC23X0 AES 加速器驱动（Accelerator Driver）

**说明（Help）**

启用 TI CC23X0 AES 加速器（Accelerator）驱动。支持以下模式：

- 电子密码本（Electronic Code Book，ECB）：仅支持加密，硬件不支持解密。
- 计数器模式（Counter，CTR）。
- 带 CBC-MAC 的计数器模式（CTR with CBC-MAC，CCM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_AES_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.cc23x0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.cc23x0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_CC23X0_DMA"></a>

## 71.15 `CONFIG_CRYPTO_CC23X0_DMA`

**提示（Prompt）**：TI CC23X0 AES 加速器设备的 DMA 支持（DMA Support）

**说明（Help）**

为 AES 外设使用直接内存访问（DMA）驱动的事务（Transaction）。DMA 模式将数据传输任务从 CPU 移交给 DMA，并减少处理 AES 操作所需的中断数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_CC23X0 && CONFIG_CRYPTO
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.cc23x0:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.cc23x0#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → CC23X0 AES 加速器驱动（Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_CC23X0`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_CC23X0)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_CRYPTO_ESP32"></a>

## 71.16 `CONFIG_CRYPTO_ESP32`

**提示（Prompt）**：乐鑫密码学驱动（Espressif Crypto Driver）

**说明（Help）**

启用乐鑫（Espressif）AES 和 SHA 加速器的硬件密码学（Crypto）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ESPRESSIF_ESP32_AES_ENABLED || DT_HAS_ESPRESSIF_ESP32_SHA_ENABLED) && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_ESP32_AES"></a>

## 71.17 `CONFIG_CRYPTO_ESP32_AES`

**提示（Prompt）**：ESP32 AES 硬件加速器（Hardware Accelerator）

**说明（Help）**

启用乐鑫（Espressif）AES 硬件加速器支持。驱动通过硬件抽象层（HAL）使用 AES 硬件引擎，实现 AES-ECB、AES-CBC 和 AES-CTR 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_AES_ENABLED && CONFIG_CRYPTO_ESP32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.esp32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.esp32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 乐鑫密码学驱动（Espressif Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_ESP32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_ESP32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_ESP32_SHA"></a>

## 71.18 `CONFIG_CRYPTO_ESP32_SHA`

**提示（Prompt）**：ESP32 SHA 硬件加速器（Hardware Accelerator）

**说明（Help）**

启用乐鑫（Espressif）SHA 硬件加速器支持。驱动使用乐鑫硬件抽象层（HAL）的 SHA 引擎，实现 SHA-224、SHA-256、SHA-384 和 SHA-512。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_SHA_ENABLED && CONFIG_CRYPTO_ESP32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.esp32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.esp32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 乐鑫密码学驱动（Espressif Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_ESP32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_ESP32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_ESP32_SHA_SESSIONS_MAX"></a>

## 71.19 `CONFIG_CRYPTO_ESP32_SHA_SESSIONS_MAX`

**提示（Prompt）**：ESP32 SHA 最大会话数量（Max SHA Sessions）

**说明（Help）**

最大并发 SHA 哈希会话（Hash Session）数量。每个会话约使用 300–400 字节 RAM；SHA-384／512 因状态更大而需要更多空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_ESP32_SHA && CONFIG_CRYPTO_ESP32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.esp32:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.esp32#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 乐鑫密码学驱动（Espressif Crypto Driver） → ESP32 SHA 硬件加速器（Hardware Accelerator）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_ESP32_SHA`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_ESP32_SHA)、[`CONFIG_CRYPTO_ESP32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_ESP32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_INFINEON_MXCRYPTO"></a>

## 71.20 `CONFIG_CRYPTO_INFINEON_MXCRYPTO`

**提示（Prompt）**：英飞凌 MXCRYPTO 硬件密码学驱动（Infineon Hardware Crypto Driver）

**说明（Help）**

为支持的器件启用英飞凌（Infineon）MXCRYPTO 硬件加速密码学（Crypto）驱动。通过 Zephyr 密码学 API 提供 AES-128／192／256 的 ECB、CBC、CTR、CCM 和 GCM 密码运算，以及 SHA-224／256／384／512 运算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MXCRYPTO_CRYPTO_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_USE_INFINEON_MXCRYPTO_AES
CONFIG_USE_INFINEON_MXCRYPTO_SHA
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.infineon_mxcrypto:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.infineon_mxcrypto#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_USE_INFINEON_MXCRYPTO_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTO_AES)、[`CONFIG_USE_INFINEON_MXCRYPTO_SHA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTO_SHA)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE"></a>

## 71.21 `CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE`

**提示（Prompt）**：英飞凌 MXCRYPTOLITE 硬件密码学驱动（Infineon Hardware Crypto Driver）

**说明（Help）**

为支持的器件启用英飞凌（Infineon）MXCRYPTOLITE 硬件加速密码学（Crypto）驱动。通过 Zephyr 密码学 API 提供 AES-128 的 ECB、CBC、CTR 和 CCM 密码运算，以及 SHA-256 哈希（Hash）运算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MXCRYPTOLITE_CRYPTO_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_USE_INFINEON_MXCRYPTOLITE_AES
CONFIG_USE_INFINEON_MXCRYPTOLITE_SHA256
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.infineon_mxcryptolite:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.infineon_mxcryptolite#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_USE_INFINEON_MXCRYPTOLITE_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTOLITE_AES)、[`CONFIG_USE_INFINEON_MXCRYPTOLITE_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTOLITE_SHA256)。

<a id="CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE_MAX_SESSION"></a>

## 71.22 `CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE_MAX_SESSION`

**提示（Prompt）**：最大同时活动密码学会话数量（Simultaneous Crypto Sessions）

**说明（Help）**

驱动支持的并发密码运算（Cipher）或哈希（Hash）会话数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.infineon_mxcryptolite:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.infineon_mxcryptolite#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 英飞凌 MXCRYPTOLITE 硬件密码学驱动（Infineon Hardware Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_INFINEON_MXCRYPTO_MAX_SESSION"></a>

## 71.23 `CONFIG_CRYPTO_INFINEON_MXCRYPTO_MAX_SESSION`

**提示（Prompt）**：最大同时活动密码学会话数量（Simultaneous Crypto Sessions）

**说明（Help）**

驱动支持的并发密码运算（Cipher）或哈希（Hash）会话数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_INFINEON_MXCRYPTO && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.infineon_mxcrypto:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.infineon_mxcrypto#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 英飞凌 MXCRYPTO 硬件密码学驱动（Infineon Hardware Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_INFINEON_MXCRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTO)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_INIT_PRIORITY"></a>

## 71.24 `CONFIG_CRYPTO_INIT_PRIORITY`

**提示（Prompt）**：密码学设备初始化优先级（Crypto Devices Init Priority）

**说明（Help）**

密码学（Crypto）设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/crypto/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_INTEL_SHA"></a>

## 71.25 `CONFIG_CRYPTO_INTEL_SHA`

**提示（Prompt）**：Intel SHA 驱动（Driver）

**说明（Help）**

启用 Intel SHA 驱动，用于 ACE 和 CAVS 平台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_SHA_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.intel:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.intel#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_IT51XXX_SHA"></a>

## 71.26 `CONFIG_CRYPTO_IT51XXX_SHA`

**提示（Prompt）**：ITE IT51XXX SHA 驱动（Driver）

**说明（Help）**

IT51XXX 硬件支持 SHA-256 计算，比固件实现（Firmware Implementation）更快。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_SHA_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE)。

<a id="CONFIG_CRYPTO_IT8XXX2_SHA"></a>

## 71.27 `CONFIG_CRYPTO_IT8XXX2_SHA`

**提示（Prompt）**：ITE IT8XXX2 SHA 驱动（Driver）

**说明（Help）**

启用 ITE IT8XXX2 SHA 驱动，支持 IT8XXX2 系列的 SHA-256 硬件加速器（Hardware Accelerator）。计算 SHA-256 哈希时，需要在 RAM 前 4k 字节中提供 `256 + 256` 字节空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_SHA_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE)。

<a id="CONFIG_CRYPTO_IT8XXX2_SHA_V2"></a>

## 71.28 `CONFIG_CRYPTO_IT8XXX2_SHA_V2`

**提示（Prompt）**：ITE IT8XXX2 SHA V2 驱动（Driver）

**说明（Help）**

启用 ITE IT8XXX2 SHA V2 驱动，支持 IT82XX2 系列的 SHA-256 硬件加速器（Hardware Accelerator）。计算 SHA-256 哈希时，需要在 RAM 前 4k 字节中提供 `1024 + 256` 字节空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_SHA_V2_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.it8xxx2:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.it8xxx2#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE)。

<a id="CONFIG_CRYPTO_MBEDTLS_SHIM"></a>

## 71.29 `CONFIG_CRYPTO_MBEDTLS_SHIM`

**提示（Prompt）**：Mbed TLS 适配驱动（Shim Driver）［实验性，EXPERIMENTAL］

**说明（Help）**

启用符合密码学 API（Crypto APIs）的 Mbed TLS 适配层（Shim Layer）。如果应用嵌入了 Mbed TLS，即启用 `CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`，则需要为 `CONFIG_MBEDTLS_HEAP_SIZE` 设置合适的值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_MBEDTLS_ENABLE_HEAP if CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_OSDP_SC_ENABLED
CONFIG_NETMIDI2_HOST_AUTH
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ALG_SHA_224
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_ALG_SHA_512
CONFIG_PSA_WANT_ALG_SHA3_224
CONFIG_PSA_WANT_ALG_SHA3_256
CONFIG_PSA_WANT_ALG_SHA3_384
CONFIG_PSA_WANT_ALG_SHA3_512
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_ALG_CCM
CONFIG_PSA_WANT_ALG_GCM
```

**定义位置（Location）**：[`drivers/crypto/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_MBEDTLS_ENABLE_HEAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_ENABLE_HEAP)、[`CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_OSDP_SC_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP_SC_ENABLED)、[`CONFIG_NETMIDI2_HOST_AUTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETMIDI2_HOST_AUTH)、[`CONFIG_PSA_WANT_ALG_SHA_224`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_224)、[`CONFIG_PSA_WANT_ALG_SHA_256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_SHA_384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_ALG_SHA_512`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_512)、[`CONFIG_PSA_WANT_ALG_SHA3_224`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA3_224)、[`CONFIG_PSA_WANT_ALG_SHA3_256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA3_256)、[`CONFIG_PSA_WANT_ALG_SHA3_384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA3_384)、[`CONFIG_PSA_WANT_ALG_SHA3_512`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA3_512)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_CCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_ALG_GCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_GCM)。

<a id="CONFIG_CRYPTO_MBEDTLS_SHIM_DRV_NAME"></a>

## 71.30 `CONFIG_CRYPTO_MBEDTLS_SHIM_DRV_NAME`

**提示（Prompt）**：Mbed TLS 伪设备名称（Pseudo Device Name）

**说明（Help）**

Mbed TLS 伪设备（Pseudo Device）的设备名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
"CRYPTO_MTLS"
```

**定义位置（Location）**：[`drivers/crypto/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → Mbed TLS 适配驱动（Shim Driver）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_MBEDTLS_SHIM_MAX_SESSION"></a>

## 71.31 `CONFIG_CRYPTO_MBEDTLS_SHIM_MAX_SESSION`

**提示（Prompt）**：Mbed TLS 适配驱动可处理的最大会话数量（Maximum Sessions）

**说明（Help）**

可用于调整驱动能够并行处理的会话（Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/crypto/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → Mbed TLS 适配驱动（Shim Driver）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_MCHP_AES_G1"></a>

## 71.32 `CONFIG_CRYPTO_MCHP_AES_G1`

**提示（Prompt）**：Microchip SAM AES 驱动（Driver）

**说明（Help）**

启用 Microchip SAM 高级加密标准（Advanced Encryption Standard，AES）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_AES_G1_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_MCHP_SHA_G1"></a>

## 71.33 `CONFIG_CRYPTO_MCHP_SHA_G1`

**提示（Prompt）**：Microchip SAM SHA 驱动（Driver）

**说明（Help）**

启用 Microchip SAM 安全哈希算法（Secure Hash Algorithm，SHA）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SHA_G1_CRYPTO_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mchp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mchp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_MCHP_XEC_SYMCR"></a>

## 71.34 `CONFIG_CRYPTO_MCHP_XEC_SYMCR`

**提示（Prompt）**：Microchip XEC 对称密码学驱动，AES／Hash（Symmetric Crypto Driver）

**说明（Help）**

启用 Microchip XEC 对称密码学（Symmetric Crypto）驱动，支持 AES／哈希（Hash）。对称密码学模块为 AES 和哈希引擎提供统一的硬件接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_SYMCR_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mchp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mchp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_MCUX_DCP"></a>

## 71.35 `CONFIG_CRYPTO_MCUX_DCP`

**提示（Prompt）**：恩智浦数据协处理器驱动（NXP Data Co-Processor，DCP）

**说明（Help）**

启用恩智浦（NXP）数据协处理器（Data Co-Processor，DCP）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_CACHE && DT_HAS_NXP_MCUX_DCP_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mcux_dcp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mcux_dcp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_CACHE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX_CACHE)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_CRYPTO_MCUX_DCP_MAX_SESSION"></a>

## 71.36 `CONFIG_CRYPTO_MCUX_DCP_MAX_SESSION`

**提示（Prompt）**：NXP DCP 密码学驱动可处理的最大会话数量（Maximum Crypto Sessions）

**说明（Help）**

可用于调整驱动能够并行处理的会话（Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_MCUX_DCP && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mcux_dcp:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mcux_dcp#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 恩智浦数据协处理器驱动（NXP Data Co-Processor，DCP）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_MCUX_DCP`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MCUX_DCP)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_MSPM0_AES"></a>

## 71.37 `CONFIG_CRYPTO_MSPM0_AES`

**提示（Prompt）**：TI MSPM0 AES 驱动支持（Driver Support）

**说明（Help）**

启用 TI MSPM0 AES 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_AES_ENABLED && CONFIG_CRYPTO && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_AES
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mspm0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mspm0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_USE_MSPM0_DL_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_AES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_AES`。

<a id="CONFIG_CRYPTO_MSPM0_MAX_SESSION"></a>

## 71.38 `CONFIG_CRYPTO_MSPM0_MAX_SESSION`

**提示（Prompt）**：MSPM0 AES 驱动可处理的最大会话数量（Maximum Sessions）

**说明（Help）**

可用于调整驱动能够并行处理的会话（Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_MSPM0_AES && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.mspm0:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.mspm0#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → TI MSPM0 AES 驱动支持（Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_MSPM0_AES`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MSPM0_AES)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_NPCX_SHA"></a>

## 71.39 `CONFIG_CRYPTO_NPCX_SHA`

**提示（Prompt）**：NPCX SHA 驱动（Driver）

**说明（Help）**

启用 NPCX SHA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_SHA_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_NRF_ECB"></a>

## 71.40 `CONFIG_CRYPTO_NRF_ECB`

**提示（Prompt）**：nRF AES 电子密码本模式加密（Electronic Codebook Mode Encryption）

**说明（Help）**

启用基于 nRF 硬件抽象层（HAL）的 AES 电子密码本（ECB）加密驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_ECB_ENABLED && !CONFIG_HAS_BT_CTLR && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.nrf_ecb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.nrf_ecb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_CRYPTO_NXP_S32_HSE"></a>

## 71.41 `CONFIG_CRYPTO_NXP_S32_HSE`

**提示（Prompt）**：恩智浦 S32 HSE 密码学驱动（NXP Crypto Driver）

**说明（Help）**

启用恩智浦（NXP）硬件安全引擎（HSE）的密码学（Crypto）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_CRYPTO_HSE_MU_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.nxp_s32_hse:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.nxp_s32_hse#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_NXP_S32_HSE_AES_KEY_GROUP_ID"></a>

## 71.42 `CONFIG_CRYPTO_NXP_S32_HSE_AES_KEY_GROUP_ID`

**提示（Prompt）**：RAM 密钥目录（Key Catalog）中的 AES 密钥组标识（Key Group ID）。

**说明（Help）**

RAM 密钥目录（Key Catalog）中的 AES 密钥组标识（Key Group ID）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_NXP_S32_HSE && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.nxp_s32_hse:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.nxp_s32_hse#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 恩智浦 S32 HSE 密码学驱动（NXP Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_NXP_S32_HSE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_NXP_S32_HSE)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_NXP_S32_HSE_AES_KEY_SIZE"></a>

## 71.43 `CONFIG_CRYPTO_NXP_S32_HSE_AES_KEY_SIZE`

**提示（Prompt）**：密钥长度，单位为位（Key Size）

**说明（Help）**

AES 密钥长度，单位为位（Bit）。仅支持 128 位或 256 位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_NXP_S32_HSE && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.nxp_s32_hse:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.nxp_s32_hse#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 恩智浦 S32 HSE 密码学驱动（NXP Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_NXP_S32_HSE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_NXP_S32_HSE)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_NXP_S32_HSE_OUTPUT_BUFFER_SIZE"></a>

## 71.44 `CONFIG_CRYPTO_NXP_S32_HSE_OUTPUT_BUFFER_SIZE`

**提示（Prompt）**：HSE 密码学服务输出缓冲区大小，单位为字节（Output Buffer Size）

**说明（Help）**

用于保存硬件安全引擎（HSE）密码学服务输出数据的缓冲区大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_NXP_S32_HSE && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.nxp_s32_hse:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.nxp_s32_hse#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 恩智浦 S32 HSE 密码学驱动（NXP Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_NXP_S32_HSE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_NXP_S32_HSE)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_RPI_PICO_SHA256"></a>

## 71.45 `CONFIG_CRYPTO_RPI_PICO_SHA256`

**提示（Prompt）**：树莓派 RP2 系列 SHA-256 加速器（Raspberry Pi Accelerator）

**说明（Help）**

启用 RP2 系列 SHA-256 加速器（Accelerator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_SHA256_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_SHA256
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_PICOSDK_USE_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_SHA256)。

<a id="CONFIG_CRYPTO_RTS5912_SHA"></a>

## 71.46 `CONFIG_CRYPTO_RTS5912_SHA`

**提示（Prompt）**：瑞昱嵌入式控制器 SHA2 驱动（Realtek EC Driver）

**说明（Help）**

启用 SHA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_SHA_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.rts5912:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.rts5912#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SF32LB"></a>

## 71.47 `CONFIG_CRYPTO_SF32LB`

**提示（Prompt）**：思澈 SF32LB 密码学加速器驱动（SiFli Crypto Accelerator Driver）

**说明（Help）**

启用思澈（SiFli）SF32LB 密码学加速器（Crypto Accelerator）驱动，支持 AES 加密／解密（Encryption / Decryption）和 SHA 哈希（Hash）运算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_CRYPTO_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.sf32lb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.sf32lb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SI32"></a>

## 71.48 `CONFIG_CRYPTO_SI32`

**提示（Prompt）**：Si32 AES 驱动（Driver）

**说明（Help）**

启用硬件加速的 AES 驱动（Hardware-Accelerated AES Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_AES_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.si32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.si32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_CRYPTO_SI32_MAX_SESSION"></a>

## 71.49 `CONFIG_CRYPTO_SI32_MAX_SESSION`

**提示（Prompt）**：Si32 驱动可处理的最大会话数量（Maximum Sessions）

**说明（Help）**

可用于调整驱动能够并行处理的会话（Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_SI32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.si32:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.si32#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → Si32 AES 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_SI32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SI32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SIFLI_AES"></a>

## 71.50 `CONFIG_CRYPTO_SIFLI_AES`

**提示（Prompt）**：思澈 AES 密码运算支持（SiFli AES Cipher Support）

**说明（Help）**

启用 AES-128／192／256 的电子密码本（ECB）、密码分组链接（CBC）和计数器（CTR）模式密码运算支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_SF32LB && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.sf32lb:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.sf32lb#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 思澈 SF32LB 密码学加速器驱动（SiFli Crypto Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_SF32LB`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SF32LB)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SIFLI_ASYNC"></a>

## 71.51 `CONFIG_CRYPTO_SIFLI_ASYNC`

**提示（Prompt）**：思澈异步密码学操作支持（SiFli Async Crypto Operations）

**说明（Help）**

通过中断（Interrupt）启用异步密码学操作（Async Crypto Operations）。禁用后，驱动使用轮询模式（Polling Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_SF32LB && CONFIG_CRYPTO
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.sf32lb:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.sf32lb#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 思澈 SF32LB 密码学加速器驱动（SiFli Crypto Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_SF32LB`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SF32LB)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SIFLI_HASH"></a>

## 71.52 `CONFIG_CRYPTO_SIFLI_HASH`

**提示（Prompt）**：思澈 SHA 哈希支持（SiFli SHA Hash Support）

**说明（Help）**

启用 SHA-224 和 SHA-256 哈希（Hash）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_SF32LB && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.sf32lb:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.sf32lb#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 思澈 SF32LB 密码学加速器驱动（SiFli Crypto Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_SF32LB`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SF32LB)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SIFLI_MAX_SESSION"></a>

## 71.53 `CONFIG_CRYPTO_SIFLI_MAX_SESSION`

**提示（Prompt）**：最大会话数量（Maximum Number of Sessions）

**说明（Help）**

最大并发密码学会话（Crypto Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_SF32LB && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.sf32lb:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.sf32lb#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 思澈 SF32LB 密码学加速器驱动（SiFli Crypto Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_SF32LB`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SF32LB)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_SMARTBOND"></a>

## 71.54 `CONFIG_CRYPTO_SMARTBOND`

**提示（Prompt）**：SmartBond 密码学加速器驱动（Cryptographic Accelerator Driver）

**说明（Help）**

启用 SmartBond 密码学加速器（Cryptographic Accelerator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_CRYPTO_ENABLED && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_STM32"></a>

## 71.55 `CONFIG_CRYPTO_STM32`

**提示（Prompt）**：STM32 密码学加速器驱动（Cryptographic Accelerator Driver）

**说明（Help）**

启用基于 STM32 硬件抽象层（HAL）的密码学加速器（Cryptographic Accelerator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_AES_ENABLED || DT_HAS_ST_STM32_CRYP_ENABLED) && !CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES && !CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_AES if CONFIG_STM32_HAL2
CONFIG_USE_STM32_HAL_CRYP if !CONFIG_STM32_HAL2
CONFIG_USE_STM32_HAL_CRYP_EX if !CONFIG_STM32_HAL2
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_USE_STM32_HAL_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_AES)、[`CONFIG_STM32_HAL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_HAL2)、[`CONFIG_USE_STM32_HAL_CRYP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_CRYP)、[`CONFIG_USE_STM32_HAL_CRYP_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_CRYP_EX)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

<a id="CONFIG_CRYPTO_STM32_HASH"></a>

## 71.56 `CONFIG_CRYPTO_STM32_HASH`

**提示（Prompt）**：STM32 哈希加速器驱动（Hash Accelerator Driver）

**说明（Help）**

通过 STM32 HAL HASH 驱动，启用 STM32 HASH 硬件加速器（Hardware Accelerator）支持，支持 SHA-224／SHA-256。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_HASH_ENABLED && !CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_HASH
CONFIG_USE_STM32_HAL_HASH_EX
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.stm32:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.stm32#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_USE_STM32_HAL_HASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_HASH)、[`CONFIG_USE_STM32_HAL_HASH_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_HASH_EX)。

<a id="CONFIG_CRYPTO_STM32_HASH_MAX_SESSIONS"></a>

## 71.57 `CONFIG_CRYPTO_STM32_HASH_MAX_SESSIONS`

**提示（Prompt）**：STM32 哈希驱动可处理的最大会话数量（Maximum Hash Sessions）

**说明（Help）**

可用于调整驱动能够并行处理的会话（Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_STM32_HASH && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.stm32:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.stm32#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → STM32 哈希加速器驱动（Hash Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_STM32_HASH`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32_HASH)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_STM32_MAX_SESSION"></a>

## 71.58 `CONFIG_CRYPTO_STM32_MAX_SESSION`

**提示（Prompt）**：STM32 密码学驱动可处理的最大会话数量（Maximum Crypto Sessions）

**说明（Help）**

可用于调整驱动能够并行处理的会话（Session）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_STM32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.stm32:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.stm32#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → STM32 密码学加速器驱动（Cryptographic Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_STM32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_CRYPTO_STM32_USE_MBEDTLS_CT_MEMCMP"></a>

## 71.59 `CONFIG_CRYPTO_STM32_USE_MBEDTLS_CT_MEMCMP`

**提示（Prompt）**：使用 mbedtls_ct_memcmp 进行恒定时间比较（Constant-Time Comparison）

**说明（Help）**

启用后，驱动使用 `mbedtls_ct_memcmp` 比较认证标签（Authentication Tag）。禁用后，使用较简单、未优化的恒定时间比较函数（Constant-Time Comparison Function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS && CONFIG_CRYPTO_STM32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.stm32:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.stm32#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → STM32 密码学加速器驱动（Cryptographic Accelerator Driver）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS)、[`CONFIG_CRYPTO_STM32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<a id="CONFIG_ESP32_CRYPTO_AES_SESSIONS_MAX"></a>

## 71.60 `CONFIG_ESP32_CRYPTO_AES_SESSIONS_MAX`

**提示（Prompt）**：ESP32 AES 最大会话数量（Max AES Sessions）

**说明（Help）**

最大并发 AES 会话（Session）数量。每个会话约使用 300–400 字节 RAM；AES-256 因状态更大而需要更多空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRYPTO_ESP32_AES && CONFIG_CRYPTO_ESP32 && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/crypto/Kconfig.esp32:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/Kconfig.esp32#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 乐鑫密码学驱动（Espressif Crypto Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_ESP32_AES`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_ESP32_AES)、[`CONFIG_CRYPTO_ESP32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_ESP32)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)。

<!-- kconfig-navigation -->

[上一章](P070_drivers_crc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P072_drivers_dac_配置项参考.md)
