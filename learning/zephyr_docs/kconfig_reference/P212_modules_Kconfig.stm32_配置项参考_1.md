---
id: learning.zephyr-docs.kconfig-reference.page-212
title: "`modules/Kconfig.stm32`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第212章\_`modules/Kconfig.stm32`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.stm32` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_STM32CUBE_SOC_NAME_OVERRIDE"></a>

## 212.1 `CONFIG_STM32CUBE_SOC_NAME_OVERRIDE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项（hidden option），用于在 STM32Cube 硬件抽象层（HAL）级别覆盖 SoC 名称。STM32Cube HAL 要求提供一个匹配目标 SoC 名称的全局预处理器定义（global preprocessor definition），通常可以从 `CONFIG_SOC` 推导。但有例外：两个不同的 SoC，虽然 `CONFIG_SOC` 值不同，却应在 STM32Cube HAL 级别使用同一预处理器定义。

默认情况下，此选项没有值，因此处于未定义状态；STM32Cube HAL 模块应从 `CONFIG_SOC` 推导全局预处理器定义。如果在 SoC 级别使用 `configdefault` 显式设置此项，则 STM32Cube HAL 模块应改为根据此选项推导，而不是使用 `CONFIG_SOC`。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`modules/Kconfig.stm32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

<a id="CONFIG_USE_STM32_HAL_ADC"></a>

## 212.2 `CONFIG_USE_STM32_HAL_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 模数转换器（Analog-to-Digital Converter (ADC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_ADC_EX"></a>

## 212.3 `CONFIG_USE_STM32_HAL_ADC_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展模数转换器（Extended Analog-to-Digital Converter (ADC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_AES"></a>

## 212.4 `CONFIG_USE_STM32_HAL_AES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube AES 硬件加速器（AES hardware accelerator (AES)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES
CONFIG_CRYPTO_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES)、[`CONFIG_CRYPTO_STM32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_BSEC"></a>

## 212.5 `CONFIG_USE_STM32_HAL_BSEC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 启动与安全控制（Boot and Security Control (BSEC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_OTP_STM32_BSEC
```

**定义位置（Location）**：[`modules/Kconfig.stm32:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_OTP_STM32_BSEC`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_STM32_BSEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CACHEAXI"></a>

## 212.6 `CONFIG_USE_STM32_HAL_CACHEAXI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube AXI 缓存（AXI Cache (CACHEAXI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CAN"></a>

## 212.7 `CONFIG_USE_STM32_HAL_CAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 控制器局域网（Controller Area Network (CAN)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CCB"></a>

## 212.8 `CONFIG_USE_STM32_HAL_CCB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 耦合与链接桥（Coupling and Chaining Bridge (CCB)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CEC"></a>

## 212.9 `CONFIG_USE_STM32_HAL_CEC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube HDMI-CEC 控制器（HDMI-CEC controller (CEC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_COMP"></a>

## 212.10 `CONFIG_USE_STM32_HAL_COMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 超低功耗比较器通道（Ultra Low Power Comparator channels (COMP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CORDIC"></a>

## 212.11 `CONFIG_USE_STM32_HAL_CORDIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube CORDIC 协处理器功能（CORDIC co-processor (CORDIC) functions）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CORTEX"></a>

## 212.12 `CONFIG_USE_STM32_HAL_CORTEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube CORTEX（CORTEX）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_BT_STM32WB0
CONFIG_BT_STM32_IPM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_BT_STM32WB0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WB0)、[`CONFIG_BT_STM32_IPM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_USE_STM32_HAL_CRC"></a>

## 212.13 `CONFIG_USE_STM32_HAL_CRC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 循环冗余校验计算单元（Cyclic redundancy check calculation unit (CRC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CRC_EX"></a>

## 212.14 `CONFIG_USE_STM32_HAL_CRC_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展循环冗余校验计算单元（Extended Cyclic redundancy check calculation unit (CRC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CRS"></a>

## 212.15 `CONFIG_USE_STM32_HAL_CRS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 时钟恢复系统（Clock recovery system (CRS)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CRYP"></a>

## 212.16 `CONFIG_USE_STM32_HAL_CRYP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 密码处理器（Cryptographic processor (CRYP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP
CONFIG_CRYPTO_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP)、[`CONFIG_CRYPTO_STM32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_CRYP_EX"></a>

## 212.17 `CONFIG_USE_STM32_HAL_CRYP_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展密码处理器（Extended Cryptographic processor (CRYP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP
CONFIG_CRYPTO_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP)、[`CONFIG_CRYPTO_STM32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DAC"></a>

## 212.18 `CONFIG_USE_STM32_HAL_DAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 数模转换器（Digital-to-analog converter (DAC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DAC_EX"></a>

## 212.19 `CONFIG_USE_STM32_HAL_DAC_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展数模转换器（Extended Digital-to-analog converter (DAC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DBGMCU"></a>

## 212.20 `CONFIG_USE_STM32_HAL_DBGMCU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 调试支持（debug support (DBGMCU)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DCACHE"></a>

## 212.21 `CONFIG_USE_STM32_HAL_DCACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 数据缓存（data cache (DCACHE)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DCMI"></a>

## 212.22 `CONFIG_USE_STM32_HAL_DCMI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 数字摄像头接口（Digital camera interface (DCM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_STM32_DCMI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_VIDEO_STM32_DCMI`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DCMIPP"></a>

## 212.23 `CONFIG_USE_STM32_HAL_DCMIPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 数字摄像头接口像素流水线（Digital Camera Interface Pixel Pipeline (DCMIPP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_STM32_DCMIPP
```

**定义位置（Location）**：[`modules/Kconfig.stm32:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_VIDEO_STM32_DCMIPP`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMIPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DCMI_EX"></a>

## 212.24 `CONFIG_USE_STM32_HAL_DCMI_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展数字摄像头接口（Extended Digital camera interface (DCM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DDR"></a>

## 212.25 `CONFIG_USE_STM32_HAL_DDR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube DDR-SDRAM 存储器（DDR-SDRAM）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DFSDM"></a>

## 212.26 `CONFIG_USE_STM32_HAL_DFSDM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube sigma-delta 调制器数字滤波器（Digital filter for sigma delta modulators (DFSDM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_STM32_DFSDM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_AUDIO_DMIC_STM32_DFSDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_DFSDM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DFSDM_EX"></a>

## 212.27 `CONFIG_USE_STM32_HAL_DFSDM_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展 sigma-delta 调制器数字滤波器（Extended Digital filter for sigma delta modulators (DFSDM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DMA"></a>

## 212.28 `CONFIG_USE_STM32_HAL_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 直接内存访问控制器（Direct Memory Access controller (DMA)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SDMMC_STM32
CONFIG_I2S_STM32_SAI
CONFIG_MEMC_STM32_OSPI_PSRAM
CONFIG_MSPI_STM32_OSPI
CONFIG_MSPI_STM32_QSPI
CONFIG_MSPI_STM32_XSPI
CONFIG_VIDEO_STM32_JPEG
```

**定义位置（Location）**：[`modules/Kconfig.stm32:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_I2S_STM32_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32_SAI)、[`CONFIG_MEMC_STM32_OSPI_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_OSPI_PSRAM)、[`CONFIG_MSPI_STM32_OSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_OSPI)、[`CONFIG_MSPI_STM32_QSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_QSPI)、[`CONFIG_MSPI_STM32_XSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_XSPI)、[`CONFIG_VIDEO_STM32_JPEG`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_JPEG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DMA2D"></a>

## 212.29 `CONFIG_USE_STM32_HAL_DMA2D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube Chrom-Art 加速器控制器（Chrom-Art Accelerator™ controller (DMA2D)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DMA_EX"></a>

## 212.30 `CONFIG_USE_STM32_HAL_DMA_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展直接内存访问控制器（Extended Direct Memory Access controller (DMA)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_FLASH_STM32_OSPI
CONFIG_I2S_STM32_SAI
CONFIG_MEMC_STM32_OSPI_PSRAM
CONFIG_MSPI_STM32_OSPI
CONFIG_MSPI_STM32_QSPI
CONFIG_MSPI_STM32_XSPI
CONFIG_VIDEO_STM32_JPEG
```

**定义位置（Location）**：[`modules/Kconfig.stm32:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_I2S_STM32_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32_SAI)、[`CONFIG_MEMC_STM32_OSPI_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_OSPI_PSRAM)、[`CONFIG_MSPI_STM32_OSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_OSPI)、[`CONFIG_MSPI_STM32_QSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_QSPI)、[`CONFIG_MSPI_STM32_XSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_XSPI)、[`CONFIG_VIDEO_STM32_JPEG`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_JPEG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DSI"></a>

## 212.31 `CONFIG_USE_STM32_HAL_DSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 显示串行接口主机（Display Serial Interface Host (DSI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_MIPI_DSI_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_MIPI_DSI_STM32`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_DTS"></a>

## 212.32 `CONFIG_USE_STM32_HAL_DTS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 数字温度传感器（Digital temperature sensor (DTS)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_ETH"></a>

## 212.33 `CONFIG_USE_STM32_HAL_ETH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 以太网（Ethernet (ETH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_ETH_STM32_HAL
```

**定义位置（Location）**：[`modules/Kconfig.stm32:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_ETH_EX"></a>

## 212.34 `CONFIG_USE_STM32_HAL_ETH_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展以太网（Extended Ethernet (ETH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_ETH_STM32_HAL_API_V2
```

**定义位置（Location）**：[`modules/Kconfig.stm32:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_ETH_STM32_HAL_API_V2`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_EXTI"></a>

## 212.35 `CONFIG_USE_STM32_HAL_EXTI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展中断与事件控制器（Extended interrupt and event controller (EXTI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FDCAN"></a>

## 212.36 `CONFIG_USE_STM32_HAL_FDCAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 具有灵活数据速率的控制器局域网（Controller area network with flexible data rate (FDCAN)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FIREWALL"></a>

## 212.37 `CONFIG_USE_STM32_HAL_FIREWALL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 防火墙（Firewall）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FLASH"></a>

## 212.38 `CONFIG_USE_STM32_HAL_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 嵌入式闪存（Embedded Flash Memory (FLASH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_EEPROM_STM32
CONFIG_SOC_FLASH_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_EEPROM_STM32`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_STM32)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FLASH_EX"></a>

## 212.39 `CONFIG_USE_STM32_HAL_FLASH_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展嵌入式闪存（Extended Embedded Flash Memory (FLASH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_EEPROM_STM32
CONFIG_SOC_FLASH_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_EEPROM_STM32`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_STM32)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FLASH_ITF"></a>

## 212.40 `CONFIG_USE_STM32_HAL_FLASH_ITF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 嵌入式闪存选项字节（Embedded Flash Memory option bytes (FLASH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FLASH_RAMFUNC"></a>

## 212.41 `CONFIG_USE_STM32_HAL_FLASH_RAMFUNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 嵌入式闪存 RAM 函数（Embedded Flash Memory RAM functions (FLASH_RAMFUNC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FMAC"></a>

## 212.42 `CONFIG_USE_STM32_HAL_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 滤波数学加速器（Filter Math Accelerator (FMAC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FMPI2C"></a>

## 212.43 `CONFIG_USE_STM32_HAL_FMPI2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 增强型快速模式 I2C（Fast-mode Plus Inter-integrated circuit (FMPI2C)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_FMPI2C_EX"></a>

## 212.44 `CONFIG_USE_STM32_HAL_FMPI2C_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展增强型快速模式 I2C（Extended Fast-mode Plus Inter-integrated circuit (FMPI2C)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_GFXMMU"></a>

## 212.45 `CONFIG_USE_STM32_HAL_GFXMMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube Chrom-GRCTM 图形内存管理单元（Chrom-GRCTM (GFXMMU)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:276`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L276)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_GFXTIM"></a>

## 212.46 `CONFIG_USE_STM32_HAL_GFXTIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 图形定时器（Graphic Timer (GFXTIM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:281`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L281)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_GPIO"></a>

## 212.47 `CONFIG_USE_STM32_HAL_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 通用输入／输出（General-purpose I/Os (GPIO)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_BT_STM32WB0
```

**定义位置（Location）**：[`modules/Kconfig.stm32:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_BT_STM32WB0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WB0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_GPIO_EX"></a>

## 212.48 `CONFIG_USE_STM32_HAL_GPIO_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展通用输入／输出（Extended General-purpose I/Os (GPIO)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_GPU2D"></a>

## 212.49 `CONFIG_USE_STM32_HAL_GPU2D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube Neo-Chrom 图形处理器（Neo-Chrom graphic processor (GPU2D)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_STM32_NEOCHROM_GPU2D
```

**定义位置（Location）**：[`modules/Kconfig.stm32:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_STM32_NEOCHROM_GPU2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_NEOCHROM_GPU2D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_GTZC"></a>

## 212.50 `CONFIG_USE_STM32_HAL_GTZC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 全局 TrustZone 控制器（Global TrustZone controller (GTZC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_HASH"></a>

## 212.51 `CONFIG_USE_STM32_HAL_HASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 散列处理器（Hash processor (HASH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH
CONFIG_CRYPTO_STM32_HASH
```

**定义位置（Location）**：[`modules/Kconfig.stm32:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH)、[`CONFIG_CRYPTO_STM32_HASH`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32_HASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_HASH_EX"></a>

## 212.52 `CONFIG_USE_STM32_HAL_HASH_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展散列处理器（Extended Hash processor (HASH)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH
CONFIG_CRYPTO_STM32_HASH
```

**定义位置（Location）**：[`modules/Kconfig.stm32:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L314)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH)、[`CONFIG_CRYPTO_STM32_HASH`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32_HASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_HCD"></a>

## 212.53 `CONFIG_USE_STM32_HAL_HCD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 主机控制器设备（Host Controller device (HCD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_HRTIM"></a>

## 212.54 `CONFIG_USE_STM32_HAL_HRTIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 高分辨率定时器（High-Resolution Timer (HRTIM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_HSEM"></a>

## 212.55 `CONFIG_USE_STM32_HAL_HSEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 硬件信号量（Hardware Semaphore (HSEM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_I2C"></a>

## 212.56 `CONFIG_USE_STM32_HAL_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube I2C 接口（Inter-integrated circuit (I2C) interface）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_I2C_EX"></a>

## 212.57 `CONFIG_USE_STM32_HAL_I2C_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展 I2C 接口（Extended Inter-integrated circuit (I2C) interface）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:340`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L340)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_I2S"></a>

## 212.58 `CONFIG_USE_STM32_HAL_I2S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 芯片间音频接口（Inter-IC sound (I2S)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:346`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L346)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_I2S_EX"></a>

## 212.59 `CONFIG_USE_STM32_HAL_I2S_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展芯片间音频接口（Extended Inter-IC sound (I2S)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_I3C"></a>

## 212.60 `CONFIG_USE_STM32_HAL_I3C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 改进型芯片间总线（Improved inter-integrated circuit (I3C)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:356`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L356)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_ICACHE"></a>

## 212.61 `CONFIG_USE_STM32_HAL_ICACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 指令缓存（Instruction cache (ICACHE)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_IPCC"></a>

## 212.62 `CONFIG_USE_STM32_HAL_IPCC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 处理器间通信控制器（Inter-Processor communication controller (IPCC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_IRDA"></a>

## 212.63 `CONFIG_USE_STM32_HAL_IRDA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 红外数据协会接口（Infrared Data Association (IRDA)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:373`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L373)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_IWDG"></a>

## 212.64 `CONFIG_USE_STM32_HAL_IWDG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 独立看门狗（Independent watchdog (IWDG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L378)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_JPEG"></a>

## 212.65 `CONFIG_USE_STM32_HAL_JPEG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube JPEG 编解码器（Jpeg codec (JPEG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_STM32_JPEG
```

**定义位置（Location）**：[`modules/Kconfig.stm32:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L383)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_VIDEO_STM32_JPEG`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_JPEG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_LCD"></a>

## 212.66 `CONFIG_USE_STM32_HAL_LCD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 液晶显示控制器（LCD controller (LCD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:388`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L388)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_LPAWUR"></a>

## 212.67 `CONFIG_USE_STM32_HAL_LPAWUR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 低功耗唤醒无线电（Low power wakeup radio (LPAWUR)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:393`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L393)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_LPTIM"></a>

## 212.68 `CONFIG_USE_STM32_HAL_LPTIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 低功耗定时器（Low Power Timer (LPTIM)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L398)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_LTDC"></a>

## 212.69 `CONFIG_USE_STM32_HAL_LTDC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube LCD-TFT 控制器（LCD-TFT controller (LTDC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_STM32_LTDC
```

**定义位置（Location）**：[`modules/Kconfig.stm32:403`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L403)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_LTDC_EX"></a>

## 212.70 `CONFIG_USE_STM32_HAL_LTDC_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展 LCD-TFT 控制器（Extended LCD-TFT controller (LTDC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L408)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MCE"></a>

## 212.71 `CONFIG_USE_STM32_HAL_MCE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 内存密码引擎（Memory Cipher Engine (MCE)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:413`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L413)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MDF"></a>

## 212.72 `CONFIG_USE_STM32_HAL_MDF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 多功能数字滤波器（Multi-function digital filter (MDF)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_STM32_MDF
```

**定义位置（Location）**：[`modules/Kconfig.stm32:418`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L418)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_AUDIO_DMIC_STM32_MDF`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_MDF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MDIOS"></a>

## 212.73 `CONFIG_USE_STM32_HAL_MDIOS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 管理数据输入／输出（Management data input/output (MDIOS)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:423`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L423)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MDMA"></a>

## 212.74 `CONFIG_USE_STM32_HAL_MDMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 主直接内存访问控制器（Master Direct Memory Access controller (MDMA)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_FLASH_STM32_OSPI
CONFIG_FLASH_STM32_QSPI
CONFIG_MSPI_STM32_OSPI
CONFIG_MSPI_STM32_QSPI
CONFIG_VIDEO_STM32_DCMI
CONFIG_VIDEO_STM32_JPEG
```

**定义位置（Location）**：[`modules/Kconfig.stm32:429`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L429)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_MSPI_STM32_OSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_OSPI)、[`CONFIG_MSPI_STM32_QSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_QSPI)、[`CONFIG_VIDEO_STM32_DCMI`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMI)、[`CONFIG_VIDEO_STM32_JPEG`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_JPEG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MMC"></a>

## 212.75 `CONFIG_USE_STM32_HAL_MMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 多媒体卡接口（MultiMediaCard interface (SDMMC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SDMMC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:435`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L435)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MMC_EX"></a>

## 212.76 `CONFIG_USE_STM32_HAL_MMC_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展多媒体卡接口（Extended MultiMediaCard interface (SDMMC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SDMMC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MRSUBG"></a>

## 212.77 `CONFIG_USE_STM32_HAL_MRSUBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube Sub-GHz 无线电（Sub-GHz radio (MRSUBG)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:446`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L446)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MRSUBG_TIMER"></a>

## 212.78 `CONFIG_USE_STM32_HAL_MRSUBG_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube Sub-GHz 无线电定时器（Sub-GHz radio timer (MRSUBG_TIMER)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:451`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L451)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_MSP"></a>

## 212.79 `CONFIG_USE_STM32_HAL_MSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 微控制器支持包（MCU Support Package (MSP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:456`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L456)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_NAND"></a>

## 212.80 `CONFIG_USE_STM32_HAL_NAND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube NAND 控制器（NAND Controller (NAND)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:461`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L461)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_NOR"></a>

## 212.81 `CONFIG_USE_STM32_HAL_NOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube NOR 控制器（NOR Controller (NOR)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_MEMC_STM32_NOR_PSRAM
```

**定义位置（Location）**：[`modules/Kconfig.stm32:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L466)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_MEMC_STM32_NOR_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_NOR_PSRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_OPAMP"></a>

## 212.82 `CONFIG_USE_STM32_HAL_OPAMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 运算放大器（Operational amplifiers (OPAMP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:471`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L471)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_OPAMP_EX"></a>

## 212.83 `CONFIG_USE_STM32_HAL_OPAMP_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展运算放大器（Extended Operational amplifiers (OPAMP)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L476)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_OSPI"></a>

## 212.84 `CONFIG_USE_STM32_HAL_OSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 八线 SPI 接口（Octo-SPI interface (OSPI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_FLASH_STM32_OSPI
CONFIG_MEMC_STM32_OSPI_PSRAM
CONFIG_MSPI_STM32_OSPI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:482`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L482)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_MEMC_STM32_OSPI_PSRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32_OSPI_PSRAM)、[`CONFIG_MSPI_STM32_OSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_OSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_OTFDEC"></a>

## 212.85 `CONFIG_USE_STM32_HAL_OTFDEC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 即时解密引擎（On-the-fly decryption engine (OTFDEC)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:487`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L487)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PCCARD"></a>

## 212.86 `CONFIG_USE_STM32_HAL_PCCARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube PC 卡存储器（PCCard memories (PCCARD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:493`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L493)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PCD"></a>

## 212.87 `CONFIG_USE_STM32_HAL_PCD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube USB 外设控制器（USB Peripheral Controller (PCD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_UDC_STM32
CONFIG_USB_DC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:498`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L498)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_USB_DC_STM32`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PCD_EX"></a>

## 212.88 `CONFIG_USE_STM32_HAL_PCD_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展 USB 外设控制器（Extended USB Peripheral Controller (PCD)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_UDC_STM32
CONFIG_USB_DC_STM32
```

**定义位置（Location）**：[`modules/Kconfig.stm32:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_USB_DC_STM32`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PKA"></a>

## 212.89 `CONFIG_USE_STM32_HAL_PKA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 公钥加速器（Public key accelerator (PKA)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_BT_STM32WB0
```

**定义位置（Location）**：[`modules/Kconfig.stm32:509`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L509)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_BT_STM32WB0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WB0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS"></a>

## 212.90 `CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`

**提示（Prompt）**：STM32 PSA 密码驱动（crypto drivers）［实验性，EXPERIMENTAL］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_HAS_STM32CUBE
```

**主动选择（Selects）**

```text
CONFIG_HAS_STM32LIB
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/Kconfig.stm32:962`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L962)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_HAS_STM32LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32LIB)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`、`CONFIG_HAS_STM32LIB`。

<a id="CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES"></a>

## 212.91 `CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES`

**提示（Prompt）**：STM32 AES PSA 密码驱动（crypto driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS && CONFIG_HAS_STM32CUBE
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_AES if CONFIG_STM32_HAL2
CONFIG_USE_STM32_HAL_CRYP if !CONFIG_STM32_HAL2
CONFIG_USE_STM32_HAL_CRYP_EX if !CONFIG_STM32_HAL2
```

**被选择（Selected by）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_SAES
```

**定义位置（Location）**：[`modules/Kconfig.stm32:970`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L970)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → STM32 PSA 密码驱动（crypto drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)、[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_AES`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_AES)、[`CONFIG_STM32_HAL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_HAL2)、[`CONFIG_USE_STM32_HAL_CRYP`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_CRYP)、[`CONFIG_USE_STM32_HAL_CRYP_EX`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_CRYP_EX)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_SAES`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_SAES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP"></a>

## 212.92 `CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_CRYP`

**提示（Prompt）**：STM32 CRYP PSA 密码驱动（crypto driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS && CONFIG_HAS_STM32CUBE
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_CRYP
CONFIG_USE_STM32_HAL_CRYP_EX
```

**定义位置（Location）**：[`modules/Kconfig.stm32:977`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L977)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → STM32 PSA 密码驱动（crypto drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)、[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_CRYP`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_CRYP)、[`CONFIG_USE_STM32_HAL_CRYP_EX`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_CRYP_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH"></a>

## 212.93 `CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_HASH`

**提示（Prompt）**：STM32 HASH PSA 密码驱动（crypto driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS && CONFIG_HAS_STM32CUBE
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_HASH
CONFIG_USE_STM32_HAL_HASH_EX
```

**定义位置（Location）**：[`modules/Kconfig.stm32:988`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L988)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → STM32 PSA 密码驱动（crypto drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)、[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_HASH`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_HASH)、[`CONFIG_USE_STM32_HAL_HASH_EX`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_HASH_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG"></a>

## 212.94 `CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_RNG`

**提示（Prompt）**：STM32 RNG PSA 密码驱动（crypto driver）

**说明（Help）**

由于 Zephyr 集成的 PSA Crypto 依赖 Zephyr 熵驱动（entropy driver），通常不需要此配置。除非希望绕过 Zephyr 熵驱动，否则应保持禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS && CONFIG_HAS_STM32CUBE
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_RNG
CONFIG_USE_STM32_HAL_RNG_EX
```

**定义位置（Location）**：[`modules/Kconfig.stm32:994`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L994)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → STM32 PSA 密码驱动（crypto drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)、[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_RNG`](P213_modules_Kconfig.stm32_配置项参考_2.md#CONFIG_USE_STM32_HAL_RNG)、[`CONFIG_USE_STM32_HAL_RNG_EX`](P213_modules_Kconfig.stm32_配置项参考_2.md#CONFIG_USE_STM32_HAL_RNG_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_SAES"></a>

## 212.95 `CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_SAES`

**提示（Prompt）**：STM32 SAES PSA 密码驱动（crypto driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS && CONFIG_HAS_STM32CUBE
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES
```

**定义位置（Location）**：[`modules/Kconfig.stm32:983`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L983)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → STM32 PSA 密码驱动（crypto drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)、[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS_AES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PSSI"></a>

## 212.96 `CONFIG_USE_STM32_HAL_PSSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 并行同步从接口（Parallel Synchronous Slave Interface (PSSI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:514`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L514)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PWR"></a>

## 212.97 `CONFIG_USE_STM32_HAL_PWR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 电源控制（Power control (PWR)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**定义位置（Location）**：[`modules/Kconfig.stm32:520`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L520)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_PWR_EX"></a>

## 212.98 `CONFIG_USE_STM32_HAL_PWR_EX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 扩展电源控制（Extended Power control (PWR)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32WBAX
```

**定义位置（Location）**：[`modules/Kconfig.stm32:525`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L525)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`、`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_USE_STM32_HAL_QSPI"></a>

## 212.99 `CONFIG_USE_STM32_HAL_QSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 四线 SPI 接口（Quad-SPI interface (QSPI)）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_FLASH_STM32_QSPI
CONFIG_MSPI_STM32_QSPI
```

**定义位置（Location）**：[`modules/Kconfig.stm32:530`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L530)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_MSPI_STM32_QSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_QSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<a id="CONFIG_USE_STM32_HAL_RADIO"></a>

## 212.100 `CONFIG_USE_STM32_HAL_RADIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32Cube 无线电（Radio）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32CUBE
```

**被选择（Selected by）**

```text
CONFIG_BT_STM32WB0
```

**定义位置（Location）**：[`modules/Kconfig.stm32:541`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.stm32#L541)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32CUBE)、[`CONFIG_BT_STM32WB0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WB0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32CUBE`。

<!-- kconfig-navigation -->

[上一章](P211_modules_Kconfig.simplelink_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P213_modules_Kconfig.stm32_配置项参考_2.md)
