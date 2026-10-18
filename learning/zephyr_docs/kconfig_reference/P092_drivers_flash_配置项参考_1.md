---
id: learning.zephyr-docs.kconfig-reference.page-92
title: "`drivers/flash`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第92章\_`drivers/flash`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `drivers/flash` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CAD_QSPI_MICRON_N25Q_SUPPORT"></a>

## 92.1 `CONFIG_CAD_QSPI_MICRON_N25Q_SUPPORT`

**提示（Prompt）**：Cadence Quad SPI 美光（Micron）N25Q 支持

**说明（Help）**

启用美光（Micron）N25Q 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CAD_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_qspi_nor:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_qspi_nor#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_CAD_QSPI_NOR_SUBSECTOR_SIZE"></a>

## 92.2 `CONFIG_CAD_QSPI_NOR_SUBSECTOR_SIZE`

**提示（Prompt）**：Cadence Quad SPI 子扇区大小（Subsector Size）

**说明（Help）**

设置 Cadence Quad SPI 子扇区大小（Subsector Size）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CAD_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_qspi_nor:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_qspi_nor#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_CDNS_NAND_CDMA_MODE"></a>

## 92.3 `CONFIG_CDNS_NAND_CDMA_MODE`

**提示（Prompt）**：Cadence NAND CDMA 工作模式（Operating Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence NAND 闪存驱动（Flash Driver） → 设置 NAND 工作模式（Operating Mode）。

<a id="CONFIG_CDNS_NAND_GENERIC_MODE"></a>

## 92.4 `CONFIG_CDNS_NAND_GENERIC_MODE`

**提示（Prompt）**：Cadence NAND 通用工作模式（Generic Operating Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence NAND 闪存驱动（Flash Driver） → 设置 NAND 工作模式（Operating Mode）。

<a id="CONFIG_CDNS_NAND_INTERRUPT_SUPPORT"></a>

## 92.5 `CONFIG_CDNS_NAND_INTERRUPT_SUPPORT`

**提示（Prompt）**：Cadence NAND 中断支持（Interrupt Support）

**说明（Help）**

启用 Cadence NAND 中断（Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CDNS_NAND && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence NAND 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CDNS_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CDNS_NAND)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_CDNS_NAND_PIO_MODE"></a>

## 92.6 `CONFIG_CDNS_NAND_PIO_MODE`

**提示（Prompt）**：Cadence NAND 程序控制 I/O 工作模式（PIO Operating Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence NAND 闪存驱动（Flash Driver） → 设置 NAND 工作模式（Operating Mode）。

<a id="CONFIG_CHECK_BEFORE_READING"></a>

## 92.7 `CONFIG_CHECK_BEFORE_READING`

**提示（Prompt）**：读取区域之前先验证（Verify Before Reading）

**说明（Help）**

读取一个区域之前，先执行裕量检查闪存命令（Margin Check Flash Command）。此功能可防止错误或禁止的读取。某些启用了纠错码（ECC）的器件，在读取已擦除区域或编程错误的区域时会崩溃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_MCUX && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_LPC55XXX
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MCUX 闪存适配层驱动（Flash Shim Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_MCUX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC55XXX`。

<a id="CONFIG_ESP_FLASH_ASYNC"></a>

## 92.8 `CONFIG_ESP_FLASH_ASYNC`

**提示（Prompt）**：使用异步工作线程（Asynchronous Work Thread）执行闪存访问操作

**说明（Help）**

启用后，闪存访问操作（Flash Access Operation）被推迟到工作线程（Work Thread）执行。这意味着每次闪存读写都会延后，并在可以执行时进行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && !CONFIG_MCUBOOT && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ASYNC_IPM"></a>

## 92.9 `CONFIG_ESP_FLASH_ASYNC_IPM`

**提示（Prompt）**：允许多个 CPU 访问系统闪存（System Flash）

**说明（Help）**

启用通过 `ipm0` 进行多处理器闪存访问（Multiprocessor Flash Access）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_ASYNC && CONFIG_IPM && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_IPM
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 使用异步工作线程（Asynchronous Work Thread）执行闪存访问操作

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_ASYNC`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_ASYNC)、[`CONFIG_IPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPM)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ASYNC_TIMEOUT"></a>

## 92.10 `CONFIG_ESP_FLASH_ASYNC_TIMEOUT`

**提示（Prompt）**：等待请求可用的超时时间（Request Availability Timeout），以秒为单位

**说明（Help）**

等待请求（Request）的超时时间，以秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_ASYNC && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 使用异步工作线程（Asynchronous Work Thread）执行闪存访问操作

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_ASYNC`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_ASYNC)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ASYNC_WORK"></a>

## 92.11 `CONFIG_ESP_FLASH_ASYNC_WORK`

**提示（Prompt）**：使用专用工作线程（Dedicated Work Thread）执行工作任务

**说明（Help）**

使用专用工作线程（Dedicated Work Thread），执行涉及闪存异步操作（Flash Asynchronous Operation）的工作队列任务。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_ASYNC && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 使用异步工作线程（Asynchronous Work Thread）执行闪存访问操作

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_ASYNC`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_ASYNC)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ASYNC_WORK_PRIORITY"></a>

## 92.12 `CONFIG_ESP_FLASH_ASYNC_WORK_PRIORITY`

**提示（Prompt）**：专用工作线程优先级（Dedicated Work Thread Priority）

**说明（Help）**

定义处理工作队列（Workqueue）的专用工作线程（Dedicated Work Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_ASYNC_WORK && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 使用异步工作线程（Asynchronous Work Thread）执行闪存访问操作 → 使用专用工作线程（Dedicated Work Thread）执行工作任务

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_ASYNC_WORK`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_ASYNC_WORK)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ASYNC_WORK_STACK_SIZE"></a>

## 92.13 `CONFIG_ESP_FLASH_ASYNC_WORK_STACK_SIZE`

**提示（Prompt）**：专用工作线程栈大小（Dedicated Work Thread Stack Size）

**说明（Help）**

定义处理工作队列（Workqueue）的专用工作线程（Dedicated Work Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_ASYNC_WORK && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 使用异步工作线程（Asynchronous Work Thread）执行闪存访问操作 → 使用专用工作线程（Dedicated Work Thread）执行工作任务

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_ASYNC_WORK`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_ASYNC_WORK)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ERASE_YIELD_DURATION_MS"></a>

## 92.14 `CONFIG_ESP_FLASH_ERASE_YIELD_DURATION_MS`

**提示（Prompt）**：让出执行前的缓存关闭时间（Cache-Off Time Before Yield），以毫秒为单位

**说明（Help）**

驱动让出执行（Yield）之前，在擦除和写入时间窗口（Erase and Write Window）内允许缓存保持禁用的累计时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_YIELD_DURING_ERASE && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 擦除和写入期间向其他线程让出执行（Yield）

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_YIELD_DURING_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_YIELD_DURING_ERASE)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_ERASE_YIELD_MS"></a>

## 92.15 `CONFIG_ESP_FLASH_ERASE_YIELD_MS`

**提示（Prompt）**：让出执行时长（Yield Duration），以毫秒为单位

**说明（Help）**

驱动每次让出执行（Yield）时，在保持缓存启用的情况下休眠的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_FLASH_YIELD_DURING_ERASE && CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver） → 擦除和写入期间向其他线程让出执行（Yield）

**配置项引用（Symbol References）**：[`CONFIG_ESP_FLASH_YIELD_DURING_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_YIELD_DURING_ERASE)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_HOST"></a>

## 92.16 `CONFIG_ESP_FLASH_HOST`

**提示（Prompt）**：提供主机功能的闪存驱动（Host Functionality Flash Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if !CONFIG_ESP_FLASH_REMOTE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_ESP_FLASH_REMOTE`](P092_drivers_flash_配置项参考_1.md#CONFIG_ESP_FLASH_REMOTE)。

<a id="CONFIG_ESP_FLASH_REMOTE"></a>

## 92.17 `CONFIG_ESP_FLASH_REMOTE`

**提示（Prompt）**：远程处理器间消息闪存驱动（Remote IPM Flash Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if (CONFIG_SOC_ESP32_APPCPU_TARGET || CONFIG_SOC_ESP32C6_LPCORE) && (CONFIG_IPM || CONFIG_MBOX)
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_ESP32_APPCPU_TARGET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_APPCPU_TARGET)、[`CONFIG_SOC_ESP32C6_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C6_LPCORE)、[`CONFIG_IPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPM)、[`CONFIG_MBOX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX)。

<a id="CONFIG_ESP_FLASH_WRITE_CHUNK_SIZE"></a>

## 92.18 `CONFIG_ESP_FLASH_WRITE_CHUNK_SIZE`

**提示（Prompt）**：写入窗口大小（Write Window Size），以字节为单位

**说明（Help）**

写入按不超过此大小的窗口（Window）执行。窗口之间重新启用缓存（Cache），并在每个窗口开始前进行让出执行（Yield）检查。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
8192
```

**取值范围（Ranges）**

```text
[256, 8192]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_ESP_FLASH_YIELD_DURING_ERASE"></a>

## 92.19 `CONFIG_ESP_FLASH_YIELD_DURING_ERASE`

**提示（Prompt）**：擦除和写入期间向其他线程让出执行（Yield）

**说明（Help）**

擦除和写入操作（Erase and Write Operation）运行时禁用闪存缓存（Flash Cache）；在多核 SoC 上，还会暂停另一个处理器核（Park the Other Core）。将较长的操作拆分为多个窗口（Window），并在缓存累计禁用达到 `ESP_FLASH_ERASE_YIELD_DURATION_MS` 后，重新启用缓存并休眠 `ESP_FLASH_ERASE_YIELD_MS`，使其他线程、中断处理程序和另一个处理器核有机会运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_ESP32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 乐鑫（Espressif）ESP32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH"></a>

## 92.20 `CONFIG_FLASH`

**提示（Prompt）**：闪存驱动（Flash Drivers）

**说明（Help）**

启用闪存硬件（Flash Hardware）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_IT51XXX
CONFIG_SOC_IT8XXX2_PLL_FLASH_48M
CONFIG_DISK_DRIVER_FLASH
CONFIG_DISK_DRIVER_FTL
CONFIG_EEPROM_EMULATOR
CONFIG_ESPI_TAF_NXP
CONFIG_HAPTICS_CS40L26_FLASH
CONFIG_HAPTICS_CS40L5X_FLASH
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD
CONFIG_OPENTHREAD
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL808
```

**定义位置（Location）**：[`drivers/flash/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX)、[`CONFIG_SOC_IT8XXX2_PLL_FLASH_48M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_PLL_FLASH_48M)、[`CONFIG_DISK_DRIVER_FLASH`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FLASH)、[`CONFIG_DISK_DRIVER_FTL`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FTL)、[`CONFIG_EEPROM_EMULATOR`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_EMULATOR)、[`CONFIG_ESPI_TAF_NXP`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_NXP)、[`CONFIG_HAPTICS_CS40L26_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L26_FLASH)、[`CONFIG_HAPTICS_CS40L5X_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L5X_FLASH)、[`CONFIG_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT51XXX`、`CONFIG_HAPTICS_CS40L26_FLASH`、`CONFIG_HAPTICS_CS40L5X_FLASH`。

<a id="CONFIG_FLASH_ADI_MAX32_SPIXF"></a>

## 92.21 `CONFIG_FLASH_ADI_MAX32_SPIXF`

**提示（Prompt）**：ADI MAX32 SPIXF 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**说明（Help）**

为 MAX32 系列处理器启用 QSPI-NOR 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_SPIXF_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.adi_max32_spixf:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.adi_max32_spixf#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_ADI_MAX32_SPIXF_SFDP_RUNTIME"></a>

## 92.22 `CONFIG_FLASH_ADI_MAX32_SPIXF_SFDP_RUNTIME`

**提示（Prompt）**：运行时读取闪存参数（Read Flash Parameters at Runtime）

**说明（Help）**

运行时从设备读取闪存设备特征（Flash Device Characteristics）。此选项应能为所有受支持的 JESD216 兼容器件提供功能，但需注意：SFDP 表中必须存在四线使能要求位域（Quad Enable Requirements，DW15），才能配置四线模式（Quad Mode）；否则根据器件支持情况，默认使用双线（Dual）或单线（Single）模式。

未选择此项时，驱动使用固定配置，必须在设备树（Devicetree）节点中设置器件大小、页大小和 `jedec-id` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_ADI_MAX32_SPIXF && CONFIG_FLASH_ADI_MAX32_SPIXF && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.adi_max32_spixf:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.adi_max32_spixf#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → ADI MAX32 SPIXF 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ADI_MAX32_SPIXF`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ADI_MAX32_SPIXF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_AESC"></a>

## 92.23 `CONFIG_FLASH_AESC`

**提示（Prompt）**：Aesc Silicon SPI 原地执行闪存控制器驱动（XIP Flash Controller Driver）

**说明（Help）**

启用 Aesc Silicon SPI 闪存控制器（Flash Controller）驱动。它对以原地执行（Execute-in-Place，XIP）方式映射的 SPI NOR 闪存提供只读访问；目前尚不支持编程（写入/擦除）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AESC_SPI_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
```

**定义位置（Location）**：[`drivers/flash/Kconfig.aesc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.aesc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)。

<a id="CONFIG_FLASH_AMBIQ"></a>

## 92.24 `CONFIG_FLASH_AMBIQ`

**提示（Prompt）**：用于 MRAM 或闪存的 Ambiq 闪存驱动（Flash Driver）

**说明（Help）**

启用用于磁阻式随机存取存储器（MRAM，例如 Apollo4x）或闪存（Flash，例如 Apollo3x、Apollo2x）的 Ambiq 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE if CONFIG_SOC_SERIES_APOLLO4X || CONFIG_SOC_SERIES_APOLLO5X
CONFIG_FLASH_HAS_EXPLICIT_ERASE if CONFIG_SOC_SERIES_APOLLO2X || CONFIG_SOC_SERIES_APOLLO3X
```

**定义位置（Location）**：[`drivers/flash/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)。

<a id="CONFIG_FLASH_AMEBA_BUF_SIZE"></a>

## 92.25 `CONFIG_FLASH_AMEBA_BUF_SIZE`

**提示（Prompt）**：AMEBA 闪存 RAM 缓冲区大小（RAM Buffer Size）

**说明（Help）**

如果闪存写操作（Flash Write Operation）的源地址也是闪存地址，必须先将数据复制到 RAM，再写入闪存。此配置设置该 RAM 缓冲区（Buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_AMEBA && CONFIG_FLASH
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/flash/Kconfig.ameba:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.ameba#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → AMEBA 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_AMEBA`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_AMEBA)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_ANDES_QSPI"></a>

## 92.26 `CONFIG_FLASH_ANDES_QSPI`

**提示（Prompt）**：Andes 闪存驱动（Flash Driver）

**说明（Help）**

启用 Andes QSPI 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_QSPI_NOR_ENABLED && !CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_ANDES_QSPI_INIT_PRIORITY"></a>

## 92.27 `CONFIG_FLASH_ANDES_QSPI_INIT_PRIORITY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_ANDES_QSPI || CONFIG_FLASH_ANDES_QSPI_XIP) && CONFIG_FLASH
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_FLASH_ANDES_QSPI_XIP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_XIP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_ANDES_QSPI_LAYOUT_PAGE_SIZE"></a>

## 92.28 `CONFIG_FLASH_ANDES_QSPI_LAYOUT_PAGE_SIZE`

**提示（Prompt）**：`FLASH_LAYOUT` 功能使用的页大小（Page Size）

**说明（Help）**

使用 `CONFIG_FLASH_PAGE_LAYOUT` 时，此驱动支持对应 API。默认页大小（Page Size）等于块大小（Block Size）`65536`。其他选项包括 32 KB 擦除大小 `32768`、扇区大小（Sector Size）`4096`，或扇区大小的任意非零整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_ANDES_QSPI || CONFIG_FLASH_ANDES_QSPI_XIP) && CONFIG_FLASH
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_FLASH_ANDES_QSPI_XIP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_XIP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_ANDES_QSPI_SFDP"></a>

## 92.29 `CONFIG_FLASH_ANDES_QSPI_SFDP`

**提示（Prompt）**：串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_ANDES_QSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_FLASH_ANDES_QSPI_SFDP_RUNTIME
```

**可选项（Choices）**

```text
CONFIG_FLASH_ANDES_QSPI_SFDP_DEVICETREE
CONFIG_FLASH_ANDES_QSPI_SFDP_RUNTIME
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Andes 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_ANDES_QSPI_SFDP_RUNTIME`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_SFDP_RUNTIME)、[`CONFIG_FLASH_ANDES_QSPI_SFDP_DEVICETREE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_SFDP_DEVICETREE)。

<a id="CONFIG_FLASH_ANDES_QSPI_SFDP_DEVICETREE"></a>

## 92.30 `CONFIG_FLASH_ANDES_QSPI_SFDP_DEVICETREE`

**提示（Prompt）**：来自设备树节点的基本闪存参数（Basic Flash Parameters）

**说明（Help）**

必须通过设备树（Devicetree）的 `sfdp-bfp` 属性提供 JESD216 基本闪存参数表（Basic Flash Parameters Table）。还必须提供 `size` 和 `jedec-id` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_ANDES_QSPI_SFDP>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Andes 闪存驱动（Flash Driver） → 串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ANDES_QSPI_SFDP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_SFDP)。

<a id="CONFIG_FLASH_ANDES_QSPI_SFDP_RUNTIME"></a>

## 92.31 `CONFIG_FLASH_ANDES_QSPI_SFDP_RUNTIME`

**提示（Prompt）**：运行时读取闪存参数（Read Flash Parameters at Runtime）

**说明（Help）**

运行时从设备读取全部闪存设备特征（Flash Device Characteristics）。此选项最灵活，因为它应能为所有受支持的 JESD216 兼容器件提供功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_ANDES_QSPI_SFDP>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Andes 闪存驱动（Flash Driver） → 串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ANDES_QSPI_SFDP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_SFDP)。

<a id="CONFIG_FLASH_ANDES_QSPI_XIP"></a>

## 92.32 `CONFIG_FLASH_ANDES_QSPI_XIP`

**提示（Prompt）**：用于原地执行（XIP）芯片的 Andes 闪存驱动

**说明（Help）**

启用 Andes QSPI 的精简驱动（Minimalistic Driver），可用于承担原地执行（XIP）任务的闪存芯片。驱动将必要代码放入 RAM，因为执行擦除或写入操作时，无法从闪存取指（Fetch Code）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_ANDES_QSPI_XIP_COUNT_REGS"></a>

## 92.33 `CONFIG_FLASH_ANDES_QSPI_XIP_COUNT_REGS`

**提示（Prompt）**：使用独立的读写计数寄存器（Separate Write/Read Count Registers）

**说明（Help）**

Andes QSPI 模块具有相互独立的写计数寄存器和读计数寄存器（Write/Read Count Registers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_ANDES_QSPI_XIP && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.andes:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.andes#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ANDES_QSPI_XIP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI_XIP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_CAD_QSPI_NOR"></a>

## 92.34 `CONFIG_FLASH_CAD_QSPI_NOR`

**提示（Prompt）**：Cadence 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**说明（Help）**

启用 Cadence QSPI-NOR 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_QSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_qspi_nor:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_qspi_nor#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_CDNS_CDMA_BLOCK_COUNT"></a>

## 92.35 `CONFIG_FLASH_CDNS_CDMA_BLOCK_COUNT`

**提示（Prompt）**：设置 CDMA 模式中单次传输的块数量（Block Count）

**说明（Help）**

配置 CDMA 模式中单次传输（Single Transfer）的块数量（Block Count）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CDNS_NAND && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence NAND 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CDNS_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CDNS_NAND)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_CDNS_CDMA_PAGE_COUNT"></a>

## 92.36 `CONFIG_FLASH_CDNS_CDMA_PAGE_COUNT`

**提示（Prompt）**：设置 CDMA 模式中单次传输的页数量（Page Count）

**说明（Help）**

配置 CDMA 模式中单次传输（Single Transfer）的页数量（Page Count）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CDNS_NAND && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence NAND 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CDNS_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CDNS_NAND)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_CDNS_NAND"></a>

## 92.37 `CONFIG_FLASH_CDNS_NAND`

**提示（Prompt）**：Cadence NAND 闪存驱动（Flash Driver）

**说明（Help）**

启用 Cadence NAND 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_NAND_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_nand:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_nand#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_EX_OP_ENABLED"></a>

## 92.38 `CONFIG_FLASH_EX_OP_ENABLED`

**提示（Prompt）**：闪存扩展操作 API（Extended Flash Operations API）

**说明（Help）**

启用闪存扩展操作 API（Extended Flash Operations API）。可用于执行非标准操作（Non-Standard Operation），例如调整闪存保护（Flash Protection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_HAS_EX_OP && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_DISK_DRIVER_FTL
CONFIG_ESPI_TAF_NPCX_RPMC_SUPPORT
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
```

**定义位置（Location）**：[`drivers/flash/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_DISK_DRIVER_FTL`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FTL)、[`CONFIG_ESPI_TAF_NPCX_RPMC_SUPPORT`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_NPCX_RPMC_SUPPORT)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G3)。

<a id="CONFIG_FLASH_FILL_BUFFER_SIZE"></a>

## 92.39 `CONFIG_FLASH_FILL_BUFFER_SIZE`

**提示（Prompt）**：`flash_fill` 函数的缓冲区大小（Buffer Size）

**说明（Help）**

`flash_fill` 函数将设备填充为指定值时使用的缓冲区大小，该缓冲区分配在栈（Stack）上。多数设备具有写块对齐（Write-Block Alignment）要求，会限制一次可写入数据的最小大小以及写偏移（Write Offset）的对齐方式，因此需要此缓冲区。即使设备没有这些要求，逐字节填充也效率较低。此处所选值应为系统中全部存储设备的最大 `write-block-size` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/flash/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_FILL_GENERIC_IMPLEMENTATION"></a>

## 92.40 `CONFIG_FLASH_FILL_GENERIC_IMPLEMENTATION`

**提示（Prompt）**：包含基于循环的通用 `flash_fill()` 回退实现（Loop-Based Fallback）

**说明（Help）**

将通用写循环回退实现（Write-Loop Fallback）编译进系统；当驱动未实现自身的 `api->fill` 回调时，`flash_fill()` 使用此实现。如果构建中启用的全部闪存驱动都提供 `api->fill`，即全部选择了 `FLASH_HAS_DRIVER_FILL`，则可禁用此项，节省 `CONFIG_FLASH_FILL_BUFFER_SIZE` 字节的栈空间，以及 `z_impl_flash_fill()` 中的循环分派代码（Loop Dispatch Code）。禁用后，对于未提供 `api->fill` 的设备，`flash_fill()` 返回 `-ENOTSUP`，因此关闭之前应核实构建配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_FLASH_HAS_DRIVER_ENABLED"></a>

## 92.41 `CONFIG_FLASH_HAS_DRIVER_ENABLED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

只要启用了任一闪存驱动（Flash Driver），就启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_ADI_MAX32_SPIXF
CONFIG_FLASH_AESC
CONFIG_FLASH_AMBIQ
CONFIG_SOC_FLASH_AMEBA
CONFIG_FLASH_ANDES_QSPI
CONFIG_SPI_FLASH_AT25XV021A
CONFIG_SPI_FLASH_AT45
CONFIG_SOC_FLASH_TELINK_B91
CONFIG_SOC_FLASH_BEE_NOR
CONFIG_SOC_FLASH_BFLB
CONFIG_FLASH_CDNS_NAND
CONFIG_FLASH_CAD_QSPI_NOR
CONFIG_SOC_FLASH_CC13XX_CC26XX
CONFIG_SOC_FLASH_CC23X0
CONFIG_SOC_FLASH_ESP32
CONFIG_SOC_FLASH_GD32
CONFIG_SOC_FLASH_GECKO
CONFIG_FLASH_INFINEON_CAT1
CONFIG_FLASH_INFINEON_RRAM
CONFIG_FLASH_INFINEON_PDL
CONFIG_INFINEON_CAT1_QSPI_FLASH
CONFIG_FLASH_INTEL_PFLASH_CFI01
CONFIG_SOC_FLASH_ITE_IT51XXX_M1K
CONFIG_SOC_FLASH_ITE_IT8XXX2
CONFIG_SOC_FLASH_LPC
CONFIG_FLASH_SOC_LPC84X_IAP
CONFIG_SOC_FLASH_MAX32
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
CONFIG_SOC_FLASH_MCUX
CONFIG_FLASH_MCUX_FLEXSPI_NOR
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G
CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH
CONFIG_FLASH_MCUX_FLEXSPI_NAND
CONFIG_FLASH_MCUX_XSPI
CONFIG_SOC_FLASH_MCUX_C40
CONFIG_FLASH_MSPI
CONFIG_SPI_NAND
CONFIG_SPI_NOR
CONFIG_NORDIC_QSPI_NOR
CONFIG_FLASH_NPCX_FIU_NOR
CONFIG_SOC_FLASH_NRF
CONFIG_SOC_FLASH_NRF_MRAM
CONFIG_SOC_FLASH_NRF_MRAMC
CONFIG_SOC_FLASH_NRF_RRAM
CONFIG_SOC_FLASH_NUMAKER
CONFIG_SOC_FLASH_NUMAKER_RMC
CONFIG_FLASH_NXP_S32_QSPI_NOR
CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH
CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM
CONFIG_SOC_FLASH_RENESAS_RA_HP
CONFIG_SOC_FLASH_RENESAS_RA_LP
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
CONFIG_FLASH_RENESAS_RA_OSPI_B
CONFIG_FLASH_RENESAS_RA_QSPI
CONFIG_SOC_FLASH_RENESAS_RX
CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI
CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC
CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC
CONFIG_FLASH_RPI_PICO
CONFIG_SOC_FLASH_RTS5912
CONFIG_SOC_FLASH_RV32M1
CONFIG_FLASH_S3AXX04
CONFIG_SOC_FLASH_SAM
CONFIG_SOC_FLASH_SAM0
CONFIG_FLASH_SEMIHOST
CONFIG_FLASH_SF32LB_MPI_QSPI_NOR
CONFIG_SOC_FLASH_SI32
CONFIG_SOC_FLASH_SILABS_S2
CONFIG_SOC_FLASH_SILABS_S3_EXTMEM
CONFIG_FLASH_SIMULATOR
CONFIG_SOC_FLASH_SILABS_SIWX91X
CONFIG_SOC_FLASH_SMARTBOND
CONFIG_SOC_FLASH_STM32
CONFIG_FLASH_STM32_OSPI
CONFIG_FLASH_STM32_QSPI
CONFIG_FLASH_STM32_XSPI
CONFIG_FLASH_SOC_CH32V
CONFIG_SOC_FLASH_XMC4XXX
CONFIG_TEST_FLASH_DRIVERS
```

**定义位置（Location）**：[`drivers/flash/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ADI_MAX32_SPIXF`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ADI_MAX32_SPIXF)、[`CONFIG_FLASH_AESC`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_AESC)、[`CONFIG_FLASH_AMBIQ`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_AMBIQ)、[`CONFIG_SOC_FLASH_AMEBA`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_AMEBA)、[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_SPI_FLASH_AT25XV021A`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT25XV021A)、[`CONFIG_SPI_FLASH_AT45`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT45)、[`CONFIG_SOC_FLASH_TELINK_B91`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_TELINK_B91)、[`CONFIG_SOC_FLASH_BEE_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BEE_NOR)、[`CONFIG_SOC_FLASH_BFLB`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BFLB)、[`CONFIG_FLASH_CDNS_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CDNS_NAND)、[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_SOC_FLASH_CC13XX_CC26XX`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_CC13XX_CC26XX)、[`CONFIG_SOC_FLASH_CC23X0`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_CC23X0)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_SOC_FLASH_GD32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GD32)、[`CONFIG_SOC_FLASH_GECKO`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GECKO)、[`CONFIG_FLASH_INFINEON_CAT1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_CAT1)、[`CONFIG_FLASH_INFINEON_RRAM`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_RRAM)、[`CONFIG_FLASH_INFINEON_PDL`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_PDL)、[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)、[`CONFIG_FLASH_INTEL_PFLASH_CFI01`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INTEL_PFLASH_CFI01)、[`CONFIG_SOC_FLASH_ITE_IT51XXX_M1K`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT51XXX_M1K)、[`CONFIG_SOC_FLASH_ITE_IT8XXX2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT8XXX2)、[`CONFIG_SOC_FLASH_LPC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_LPC)、[`CONFIG_FLASH_SOC_LPC84X_IAP`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SOC_LPC84X_IAP)、[`CONFIG_SOC_FLASH_MAX32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MAX32)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G3)、[`CONFIG_SOC_FLASH_MCUX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G)、[`CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH)、[`CONFIG_FLASH_MCUX_FLEXSPI_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NAND)、[`CONFIG_FLASH_MCUX_XSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI)、[`CONFIG_SOC_FLASH_MCUX_C40`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX_C40)、[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH_NPCX_FIU_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_NOR)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_SOC_FLASH_NRF_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAM)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAMC)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_SOC_FLASH_NUMAKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER)、[`CONFIG_SOC_FLASH_NUMAKER_RMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER_RMC)、[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM)、[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)、[`CONFIG_SOC_FLASH_RENESAS_RA_LP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_LP)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)、[`CONFIG_FLASH_RENESAS_RA_OSPI_B`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_OSPI_B)、[`CONFIG_FLASH_RENESAS_RA_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_QSPI)、[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC)、[`CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC)、[`CONFIG_FLASH_RPI_PICO`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RPI_PICO)、[`CONFIG_SOC_FLASH_RTS5912`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RTS5912)、[`CONFIG_SOC_FLASH_RV32M1`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RV32M1)、[`CONFIG_FLASH_S3AXX04`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_S3AXX04)、[`CONFIG_SOC_FLASH_SAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM)、[`CONFIG_SOC_FLASH_SAM0`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM0)、[`CONFIG_FLASH_SEMIHOST`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SEMIHOST)、[`CONFIG_FLASH_SF32LB_MPI_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SF32LB_MPI_QSPI_NOR)、[`CONFIG_SOC_FLASH_SI32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SI32)、[`CONFIG_SOC_FLASH_SILABS_S2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S2)、[`CONFIG_SOC_FLASH_SILABS_S3_EXTMEM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S3_EXTMEM)、[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_SOC_FLASH_SILABS_SIWX91X`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_SIWX91X)、[`CONFIG_SOC_FLASH_SMARTBOND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SMARTBOND)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_FLASH_SOC_CH32V`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SOC_CH32V)、[`CONFIG_SOC_FLASH_XMC4XXX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_XMC4XXX)、[`CONFIG_TEST_FLASH_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_FLASH_DRIVERS)。

<a id="CONFIG_FLASH_HAS_DRIVER_FILL"></a>

## 92.42 `CONFIG_FLASH_HAS_DRIVER_FILL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由提供优化的 `api->fill` 回调的闪存驱动选中此项；该回调在驱动层执行类似 `memset` 的填充，参见 `include/zephyr/drivers/flash.h` 中的 `flash_api_fill`。如果已启用的驱动均未选择此项，则 `flash_fill()` 中的 `api->fill` 分派逻辑以及 `struct flash_driver_api` 中的对应字段不会编译进去，仅保留通用写循环回退实现（Write-Loop Fallback），为每个驱动实例节省一个函数指针及相关分派代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_NRF_RRAM
```

**定义位置（Location）**：[`drivers/flash/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)。

<a id="CONFIG_FLASH_HAS_EXPLICIT_ERASE"></a>

## 92.43 `CONFIG_FLASH_HAS_EXPLICIT_ERASE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设备不执行写时擦除（Erase-on-Write，也称编程时擦除或写入时自动擦除）。如果某个位置已编程为一个值，要将它编程为任意其他值，就需要显式擦除（Explicit Erase），因为编程只能把位从擦除态（Erased Value）改变为相反状态。所有纯闪存（Flash）器件都是从 EEPROM 演变而来，并将擦除与写入分开；EEPROM 则具有写时擦除功能。原文随后提到较高写入速度与较大擦除块之间的权衡。

具备显式擦除能力，并不表示在满足上述位变化限制时禁止不经擦除就写入；它仅表示写入任意信息需要擦除。擦除通常按页（Page）进行，这是 Zephyr 对擦除单位采用的名称。器件规范可能将此单位称为页、扇区（Sector）或块（Block），其大小也可能随厂商命名而不同。

服务于此类器件的驱动应选择此项。用户可据此提供仅适用于此类器件的代码路径；系统中没有此类器件时，编译器可以将这些路径优化掉。

> 译注：关于写入速度与擦除块大小，原文使用 `giving it advantage of higher write speeds at a cost of larger erase block`，其中 `it` 的指代不够明确；这里保留所述权衡，不将其改写为对所有 Flash 或 EEPROM 器件的性能保证。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_ADI_MAX32_SPIXF
CONFIG_FLASH_AMBIQ
CONFIG_SOC_FLASH_AMEBA
CONFIG_FLASH_ANDES_QSPI
CONFIG_SPI_FLASH_AT25XV021A
CONFIG_SPI_FLASH_AT45
CONFIG_SOC_FLASH_TELINK_B91
CONFIG_SOC_FLASH_BEE_NOR
CONFIG_SOC_FLASH_BFLB
CONFIG_FLASH_CDNS_NAND
CONFIG_FLASH_CAD_QSPI_NOR
CONFIG_SOC_FLASH_CC13XX_CC26XX
CONFIG_SOC_FLASH_ESP32
CONFIG_SOC_FLASH_GD32
CONFIG_SOC_FLASH_GECKO
CONFIG_FLASH_INFINEON_CAT1
CONFIG_FLASH_INFINEON_PDL
CONFIG_INFINEON_CAT1_QSPI_FLASH
CONFIG_FLASH_MSPI_INFINEON_S28HX512T
CONFIG_FLASH_INTEL_PFLASH_CFI01
CONFIG_SOC_FLASH_ITE_IT8XXX2
CONFIG_SOC_FLASH_LPC
CONFIG_FLASH_SOC_LPC84X_IAP
CONFIG_SOC_FLASH_MAX32
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
CONFIG_SOC_FLASH_MCUX
CONFIG_FLASH_MCUX_FLEXSPI_NOR
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G
CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH
CONFIG_FLASH_MCUX_FLEXSPI_NAND
CONFIG_FLASH_MCUX_XSPI
CONFIG_SOC_FLASH_MCUX_C40
CONFIG_SPI_NAND
CONFIG_SPI_NOR
CONFIG_NORDIC_QSPI_NOR
CONFIG_FLASH_NPCX_FIU_NOR
CONFIG_SOC_FLASH_NRF
CONFIG_SOC_FLASH_NUMAKER
CONFIG_FLASH_NXP_S32_QSPI_NOR
CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH
CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM
CONFIG_SOC_FLASH_RENESAS_RA_HP
CONFIG_SOC_FLASH_RENESAS_RA_LP
CONFIG_FLASH_RENESAS_RA_OSPI_B
CONFIG_FLASH_RENESAS_RA_QSPI
CONFIG_SOC_FLASH_RENESAS_RX
CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI
CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC
CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC
CONFIG_FLASH_RPI_PICO
CONFIG_SOC_FLASH_RTS5912
CONFIG_SOC_FLASH_RV32M1
CONFIG_SOC_FLASH_SAM
CONFIG_SOC_FLASH_SAM0
CONFIG_FLASH_SEMIHOST
CONFIG_FLASH_SF32LB_MPI_QSPI_NOR
CONFIG_SOC_FLASH_SI32
CONFIG_SOC_FLASH_SILABS_S2
CONFIG_SOC_FLASH_SILABS_S3_EXTMEM
CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE
CONFIG_SOC_FLASH_SILABS_SIWX91X
CONFIG_SOC_FLASH_SMARTBOND
CONFIG_SOC_FLASH_STM32
CONFIG_FLASH_STM32_OSPI
CONFIG_FLASH_STM32_QSPI
CONFIG_FLASH_STM32_XSPI
CONFIG_FLASH_SOC_CH32V
CONFIG_SOC_FLASH_XMC4XXX
```

**定义位置（Location）**：[`drivers/flash/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ADI_MAX32_SPIXF`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ADI_MAX32_SPIXF)、[`CONFIG_FLASH_AMBIQ`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_AMBIQ)、[`CONFIG_SOC_FLASH_AMEBA`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_AMEBA)、[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_SPI_FLASH_AT25XV021A`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT25XV021A)、[`CONFIG_SPI_FLASH_AT45`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT45)、[`CONFIG_SOC_FLASH_TELINK_B91`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_TELINK_B91)、[`CONFIG_SOC_FLASH_BEE_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BEE_NOR)、[`CONFIG_SOC_FLASH_BFLB`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BFLB)、[`CONFIG_FLASH_CDNS_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CDNS_NAND)、[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_SOC_FLASH_CC13XX_CC26XX`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_CC13XX_CC26XX)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_SOC_FLASH_GD32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GD32)、[`CONFIG_SOC_FLASH_GECKO`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GECKO)、[`CONFIG_FLASH_INFINEON_CAT1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_CAT1)、[`CONFIG_FLASH_INFINEON_PDL`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_PDL)、[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)、[`CONFIG_FLASH_MSPI_INFINEON_S28HX512T`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_INFINEON_S28HX512T)、[`CONFIG_FLASH_INTEL_PFLASH_CFI01`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INTEL_PFLASH_CFI01)、[`CONFIG_SOC_FLASH_ITE_IT8XXX2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT8XXX2)、[`CONFIG_SOC_FLASH_LPC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_LPC)、[`CONFIG_FLASH_SOC_LPC84X_IAP`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SOC_LPC84X_IAP)、[`CONFIG_SOC_FLASH_MAX32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MAX32)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G3)、[`CONFIG_SOC_FLASH_MCUX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G)、[`CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH)、[`CONFIG_FLASH_MCUX_FLEXSPI_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NAND)、[`CONFIG_FLASH_MCUX_XSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI)、[`CONFIG_SOC_FLASH_MCUX_C40`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX_C40)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH_NPCX_FIU_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_NOR)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_SOC_FLASH_NUMAKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER)、[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM)、[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)、[`CONFIG_SOC_FLASH_RENESAS_RA_LP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_LP)、[`CONFIG_FLASH_RENESAS_RA_OSPI_B`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_OSPI_B)、[`CONFIG_FLASH_RENESAS_RA_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_QSPI)、[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC)、[`CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC)、[`CONFIG_FLASH_RPI_PICO`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RPI_PICO)、[`CONFIG_SOC_FLASH_RTS5912`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RTS5912)、[`CONFIG_SOC_FLASH_RV32M1`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RV32M1)、[`CONFIG_SOC_FLASH_SAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM)、[`CONFIG_SOC_FLASH_SAM0`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM0)、[`CONFIG_FLASH_SEMIHOST`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SEMIHOST)、[`CONFIG_FLASH_SF32LB_MPI_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SF32LB_MPI_QSPI_NOR)、[`CONFIG_SOC_FLASH_SI32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SI32)、[`CONFIG_SOC_FLASH_SILABS_S2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S2)、[`CONFIG_SOC_FLASH_SILABS_S3_EXTMEM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S3_EXTMEM)、[`CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE)、[`CONFIG_SOC_FLASH_SILABS_SIWX91X`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_SIWX91X)、[`CONFIG_SOC_FLASH_SMARTBOND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SMARTBOND)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_FLASH_SOC_CH32V`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SOC_CH32V)、[`CONFIG_SOC_FLASH_XMC4XXX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_XMC4XXX)。

<a id="CONFIG_FLASH_HAS_EX_OP"></a>

## 92.44 `CONFIG_FLASH_HAS_EX_OP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由支持闪存扩展操作（Flash Extended Operations）的驱动选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_ITE_IT51XXX_M1K
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
CONFIG_FLASH_MCUX_FLEXSPI_NAND
CONFIG_SPI_NAND
CONFIG_SPI_NOR
CONFIG_FLASH_NPCX_FIU_NOR
CONFIG_FLASH_RENESAS_RA_QSPI
CONFIG_SOC_FLASH_RTS5912
CONFIG_FLASH_SIMULATOR_EX_OP
CONFIG_FLASH_STM32_WRITE_PROTECT
CONFIG_FLASH_STM32_READOUT_PROTECTION
CONFIG_FLASH_STM32_BLOCK_REGISTERS
CONFIG_FLASH_STM32_OPTION_BYTES
CONFIG_FLASH_STM32_QSPI_GENERIC_READ
CONFIG_FLASH_STM32_QSPI_GENERIC_WRITE
```

**定义位置（Location）**：[`drivers/flash/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_ITE_IT51XXX_M1K`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT51XXX_M1K)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G3)、[`CONFIG_FLASH_MCUX_FLEXSPI_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NAND)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH_NPCX_FIU_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_NOR)、[`CONFIG_FLASH_RENESAS_RA_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_QSPI)、[`CONFIG_SOC_FLASH_RTS5912`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RTS5912)、[`CONFIG_FLASH_SIMULATOR_EX_OP`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_EX_OP)、[`CONFIG_FLASH_STM32_WRITE_PROTECT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_WRITE_PROTECT)、[`CONFIG_FLASH_STM32_READOUT_PROTECTION`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_READOUT_PROTECTION)、[`CONFIG_FLASH_STM32_BLOCK_REGISTERS`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_BLOCK_REGISTERS)、[`CONFIG_FLASH_STM32_OPTION_BYTES`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OPTION_BYTES)、[`CONFIG_FLASH_STM32_QSPI_GENERIC_READ`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI_GENERIC_READ)、[`CONFIG_FLASH_STM32_QSPI_GENERIC_WRITE`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI_GENERIC_WRITE)。

<a id="CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE"></a>

## 92.45 `CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设备可在先前已经编程为其他值的任意位置写入任意新值，而无需事先显式擦除（Explicit Erase）。设备可能具有写时擦除（Erase-on-Write，即自动擦除）功能，例如 EEPROM；也可能完全没有擦除操作。

设备驱动仍可提供擦除回调（Erase Callback），尤其是在执行擦除能加速后续写入，或者能比通过连续写入模拟擦除更快地将请求擦除的区域填充为单一值时。

服务于此类器件的驱动应选择此项。用户可据此提供仅适用于此类器件的代码路径；系统中没有此类器件时，编译器可以将这些路径优化掉。任何能够随时通过写入将存储位从任一值改为其相反值的器件，都应选择此项。驱动设置此项时，还必须在其 `flash_parameters` 中设置 `no_explicit_erase` 能力标志。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_AMBIQ
CONFIG_FLASH_INFINEON_RRAM
CONFIG_FLASH_INFINEON_PDL
CONFIG_SOC_FLASH_NRF_MRAM
CONFIG_SOC_FLASH_NRF_MRAMC
CONFIG_SOC_FLASH_NRF_RRAM
CONFIG_SOC_FLASH_NUMAKER_RMC
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
CONFIG_FLASH_S3AXX04
CONFIG_FLASH_SIMULATOR_RAMLIKE
```

**定义位置（Location）**：[`drivers/flash/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_AMBIQ`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_AMBIQ)、[`CONFIG_FLASH_INFINEON_RRAM`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_RRAM)、[`CONFIG_FLASH_INFINEON_PDL`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_PDL)、[`CONFIG_SOC_FLASH_NRF_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAM)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAMC)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_SOC_FLASH_NUMAKER_RMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER_RMC)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)、[`CONFIG_FLASH_S3AXX04`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_S3AXX04)、[`CONFIG_FLASH_SIMULATOR_RAMLIKE`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_RAMLIKE)。

<a id="CONFIG_FLASH_HAS_PAGE_LAYOUT"></a>

## 92.46 `CONFIG_FLASH_HAS_PAGE_LAYOUT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 SoC 闪存驱动支持获取闪存页布局（Flash Memory Page Layout）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_ADI_MAX32_SPIXF
CONFIG_FLASH_AMBIQ
CONFIG_SOC_FLASH_AMEBA
CONFIG_FLASH_ANDES_QSPI
CONFIG_SPI_FLASH_AT25XV021A
CONFIG_SPI_FLASH_AT45
CONFIG_SOC_FLASH_TELINK_B91
CONFIG_SOC_FLASH_BEE_NOR
CONFIG_SOC_FLASH_BFLB
CONFIG_FLASH_CDNS_NAND
CONFIG_FLASH_CAD_QSPI_NOR
CONFIG_SOC_FLASH_CC13XX_CC26XX
CONFIG_SOC_FLASH_CC23X0
CONFIG_SOC_FLASH_ESP32
CONFIG_SOC_FLASH_GD32
CONFIG_SOC_FLASH_GECKO
CONFIG_FLASH_INFINEON_CAT1
CONFIG_FLASH_INFINEON_RRAM
CONFIG_FLASH_INFINEON_PDL
CONFIG_INFINEON_CAT1_QSPI_FLASH
CONFIG_FLASH_MSPI_INFINEON_S28HX512T
CONFIG_FLASH_INTEL_PFLASH_CFI01
CONFIG_SOC_FLASH_ITE_IT51XXX_M1K
CONFIG_SOC_FLASH_ITE_IT8XXX2
CONFIG_SOC_FLASH_LPC
CONFIG_FLASH_SOC_LPC84X_IAP
CONFIG_SOC_FLASH_MAX32
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
CONFIG_SOC_FLASH_MCUX
CONFIG_FLASH_MCUX_FLEXSPI_NOR
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G
CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH
CONFIG_FLASH_MCUX_FLEXSPI_NAND
CONFIG_FLASH_MCUX_XSPI
CONFIG_SOC_FLASH_MCUX_C40
CONFIG_SPI_NAND
CONFIG_SPI_NOR
CONFIG_NORDIC_QSPI_NOR
CONFIG_FLASH_NPCX_FIU_NOR
CONFIG_SOC_FLASH_NRF
CONFIG_SOC_FLASH_NRF_MRAM
CONFIG_SOC_FLASH_NRF_MRAMC
CONFIG_SOC_FLASH_NRF_RRAM
CONFIG_SOC_FLASH_NUMAKER
CONFIG_SOC_FLASH_NUMAKER_RMC
CONFIG_FLASH_NXP_S32_QSPI_NOR
CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH
CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM
CONFIG_SOC_FLASH_RENESAS_RA_HP
CONFIG_SOC_FLASH_RENESAS_RA_LP
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
CONFIG_FLASH_RENESAS_RA_OSPI_B
CONFIG_FLASH_RENESAS_RA_QSPI
CONFIG_SOC_FLASH_RENESAS_RX
CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI
CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC
CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC
CONFIG_FLASH_RPI_PICO
CONFIG_SOC_FLASH_RTS5912
CONFIG_SOC_FLASH_RV32M1
CONFIG_FLASH_S3AXX04
CONFIG_SOC_FLASH_SAM
CONFIG_SOC_FLASH_SAM0
CONFIG_FLASH_SEMIHOST
CONFIG_FLASH_SF32LB_MPI_QSPI_NOR
CONFIG_SOC_FLASH_SI32
CONFIG_SOC_FLASH_SILABS_S2
CONFIG_SOC_FLASH_SILABS_S3_EXTMEM
CONFIG_FLASH_SIMULATOR
CONFIG_SOC_FLASH_SILABS_SIWX91X
CONFIG_SOC_FLASH_SMARTBOND
CONFIG_SOC_FLASH_STM32
CONFIG_FLASH_STM32_OSPI
CONFIG_FLASH_STM32_QSPI
CONFIG_FLASH_STM32_XSPI
CONFIG_FLASH_SOC_CH32V
CONFIG_SOC_FLASH_XMC4XXX
```

**定义位置（Location）**：[`drivers/flash/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ADI_MAX32_SPIXF`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ADI_MAX32_SPIXF)、[`CONFIG_FLASH_AMBIQ`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_AMBIQ)、[`CONFIG_SOC_FLASH_AMEBA`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_AMEBA)、[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_SPI_FLASH_AT25XV021A`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT25XV021A)、[`CONFIG_SPI_FLASH_AT45`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT45)、[`CONFIG_SOC_FLASH_TELINK_B91`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_TELINK_B91)、[`CONFIG_SOC_FLASH_BEE_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BEE_NOR)、[`CONFIG_SOC_FLASH_BFLB`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BFLB)、[`CONFIG_FLASH_CDNS_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CDNS_NAND)、[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_SOC_FLASH_CC13XX_CC26XX`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_CC13XX_CC26XX)、[`CONFIG_SOC_FLASH_CC23X0`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_CC23X0)、[`CONFIG_SOC_FLASH_ESP32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_SOC_FLASH_GD32`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GD32)、[`CONFIG_SOC_FLASH_GECKO`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_GECKO)、[`CONFIG_FLASH_INFINEON_CAT1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_CAT1)、[`CONFIG_FLASH_INFINEON_RRAM`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_RRAM)、[`CONFIG_FLASH_INFINEON_PDL`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INFINEON_PDL)、[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)、[`CONFIG_FLASH_MSPI_INFINEON_S28HX512T`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_INFINEON_S28HX512T)、[`CONFIG_FLASH_INTEL_PFLASH_CFI01`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INTEL_PFLASH_CFI01)、[`CONFIG_SOC_FLASH_ITE_IT51XXX_M1K`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT51XXX_M1K)、[`CONFIG_SOC_FLASH_ITE_IT8XXX2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT8XXX2)、[`CONFIG_SOC_FLASH_LPC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_LPC)、[`CONFIG_FLASH_SOC_LPC84X_IAP`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SOC_LPC84X_IAP)、[`CONFIG_SOC_FLASH_MAX32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MAX32)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G3)、[`CONFIG_SOC_FLASH_MCUX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G)、[`CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH)、[`CONFIG_FLASH_MCUX_FLEXSPI_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NAND)、[`CONFIG_FLASH_MCUX_XSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI)、[`CONFIG_SOC_FLASH_MCUX_C40`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX_C40)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH_NPCX_FIU_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_NOR)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_SOC_FLASH_NRF_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAM)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAMC)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_SOC_FLASH_NUMAKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER)、[`CONFIG_SOC_FLASH_NUMAKER_RMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER_RMC)、[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM)、[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)、[`CONFIG_SOC_FLASH_RENESAS_RA_LP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_LP)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)、[`CONFIG_FLASH_RENESAS_RA_OSPI_B`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_OSPI_B)、[`CONFIG_FLASH_RENESAS_RA_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_QSPI)、[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC)、[`CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC)、[`CONFIG_FLASH_RPI_PICO`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RPI_PICO)、[`CONFIG_SOC_FLASH_RTS5912`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RTS5912)、[`CONFIG_SOC_FLASH_RV32M1`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RV32M1)、[`CONFIG_FLASH_S3AXX04`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_S3AXX04)、[`CONFIG_SOC_FLASH_SAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM)、[`CONFIG_SOC_FLASH_SAM0`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM0)、[`CONFIG_FLASH_SEMIHOST`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SEMIHOST)、[`CONFIG_FLASH_SF32LB_MPI_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SF32LB_MPI_QSPI_NOR)、[`CONFIG_SOC_FLASH_SI32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SI32)、[`CONFIG_SOC_FLASH_SILABS_S2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S2)、[`CONFIG_SOC_FLASH_SILABS_S3_EXTMEM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_S3_EXTMEM)、[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_SOC_FLASH_SILABS_SIWX91X`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_SIWX91X)、[`CONFIG_SOC_FLASH_SMARTBOND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SMARTBOND)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_FLASH_SOC_CH32V`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SOC_CH32V)、[`CONFIG_SOC_FLASH_XMC4XXX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_XMC4XXX)。

<a id="CONFIG_FLASH_HAS_UNALIGNED_WRITE"></a>

## 92.47 `CONFIG_FLASH_HAS_UNALIGNED_WRITE`

**提示（Prompt）**：提供非对齐写入支持（Unaligned Write Support）

**说明（Help）**

启用此选项，允许 Zephyr 闪存 API 在未对齐到设备写块大小（Write Block Size）的偏移处写入数据。驱动在内部处理非对齐写入（Unaligned Write），通常通过读－改－写（Read-Modify-Write）操作确保数据完整性。应用程序因此可从闪存空间中的任意偏移开始写入，而不局限于对齐地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCHP_NVMCTRL_G1 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mchp:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mchp#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_INFINEON_CAT1"></a>

## 92.48 `CONFIG_FLASH_INFINEON_CAT1`

**提示（Prompt）**：Infineon CAT1 闪存驱动（Flash Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的闪存（Flash）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_FLASH_CONTROLLER_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_USE_INFINEON_FLASH
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.infineon:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.infineon#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_USE_INFINEON_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_FLASH)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_INFINEON_PDL"></a>

## 92.49 `CONFIG_FLASH_INFINEON_PDL`

**提示（Prompt）**：Infineon PDL 闪存驱动（Flash Driver）

**说明（Help）**

启用英飞凌（Infineon）基于 PDL 的系列（PSoC4、PSC3）的闪存（Flash）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_FLASH_CONTROLLER_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
CONFIG_USE_INFINEON_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.infineon:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.infineon#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_USE_INFINEON_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_FLASH)。

<a id="CONFIG_FLASH_INFINEON_RRAM"></a>

## 92.50 `CONFIG_FLASH_INFINEON_RRAM`

**提示（Prompt）**：Infineon CAT1 FLASH RRAM 驱动

**说明（Help）**

启用英飞凌（Infineon）Edge 系列的 FLASH RRAM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_RRAM_CONTROLLER_ENABLED && CONFIG_SOC_FAMILY_INFINEON_EDGE && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_USE_INFINEON_FLASH_RRAM
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.infineon:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.infineon#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_USE_INFINEON_FLASH_RRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_FLASH_RRAM)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_EDGE`。

<a id="CONFIG_FLASH_INFINEON_SMIF_HW_INIT"></a>

## 92.51 `CONFIG_FLASH_INFINEON_SMIF_HW_INIT`

**提示（Prompt）**：在闪存驱动中初始化 SMIF 硬件（SMIF Hardware）

**说明（Help）**

在闪存驱动的初始化函数中启用完整的 SMIF 硬件初始化，包括引脚、时钟、外设组和 SMIF 外设。当第一个应用程序从内部 RRAM 启动，而 ROM 扩展启动流程（Extended Boot）尚未配置 SMIF 时，需要此功能。禁用后，驱动假定 SMIF 已初始化，例如从外部闪存启动时由 ROM 完成初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INFINEON_CAT1_QSPI_FLASH && CONFIG_SOC_SERIES_PSE84 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.infineon:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.infineon#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Infineon CAT1 QSPI 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_INFINEON_CAT1_QSPI_FLASH`](P093_drivers_flash_配置项参考_2.md#CONFIG_INFINEON_CAT1_QSPI_FLASH)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_PSE84`。

<a id="CONFIG_FLASH_INIT_PRIORITY"></a>

## 92.52 `CONFIG_FLASH_INIT_PRIORITY`

**提示（Prompt）**：闪存初始化优先级（Flash Init Priority）

**说明（Help）**

闪存驱动设备的初始化优先级（Initialization Priority）。除非具体驱动实现具有自己的初始化优先级，否则使用此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/flash/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_FLASH_INTEL_PFLASH_CFI01"></a>

## 92.53 `CONFIG_FLASH_INTEL_PFLASH_CFI01`

**提示（Prompt）**：Intel CFI01 并行闪存（Parallel Flash，QEMU pflash）

**说明（Help）**

为 QEMU pflash 设备启用 Intel CFI01 闪存驱动。此驱动支持具有统一扇区大小（Uniform Sector Size）的内存映射（Memory-Mapped）Intel CFI01 并行闪存设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_PFLASH_CFI01_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
```

**定义位置（Location）**：[`drivers/flash/Kconfig.intel_pflash_cfi01:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.intel_pflash_cfi01#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)。

<a id="CONFIG_FLASH_JESD216"></a>

## 92.54 `CONFIG_FLASH_JESD216`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由支持 JESD216 兼容闪存设备的驱动选中，用于启用通用支持模块（Common Support Module）的构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_ADI_MAX32_SPIXF
CONFIG_FLASH_ANDES_QSPI
CONFIG_FLASH_MCUX_FLEXSPI_NOR
CONFIG_SPI_NOR
CONFIG_NORDIC_QSPI_NOR
CONFIG_FLASH_NPCX_FIU_NOR
CONFIG_FLASH_NXP_S32_QSPI_NOR
CONFIG_FLASH_RENESAS_RA_OSPI_B
CONFIG_FLASH_RENESAS_RA_QSPI
CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI
CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC
CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC
CONFIG_FLASH_SF32LB_MPI_QSPI_NOR
CONFIG_FLASH_STM32_OSPI
CONFIG_FLASH_STM32_QSPI
CONFIG_FLASH_STM32_XSPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_ADI_MAX32_SPIXF`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ADI_MAX32_SPIXF)、[`CONFIG_FLASH_ANDES_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_ANDES_QSPI)、[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH_NPCX_FIU_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_RENESAS_RA_OSPI_B`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_OSPI_B)、[`CONFIG_FLASH_RENESAS_RA_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_QSPI)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC)、[`CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC)、[`CONFIG_FLASH_SF32LB_MPI_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SF32LB_MPI_QSPI_NOR)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)。

<a id="CONFIG_FLASH_JESD216_API"></a>

## 92.55 `CONFIG_FLASH_JESD216_API`

**提示（Prompt）**：提供读取 JESD216 闪存参数（Flash Parameters）的 API

**说明（Help）**

此选项扩展 Zephyr 闪存 API，使其能够访问串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域，从而让提供此能力的闪存驱动在运行时确定串行闪存参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_JESD216 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MCHP_NVMCTRL_G1"></a>

## 92.56 `CONFIG_FLASH_MCHP_NVMCTRL_G1`

**提示（Prompt）**：Microchip G1 NVMCTRL 闪存驱动（Flash Driver）

**说明（Help）**

为 Microchip 非易失性存储器控制器（Non-Volatile Memory Controller）启用 G1 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_NVMCTRL_G1_FLASH_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EX_OP
CONFIG_FLASH_EX_OP_ENABLED
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_FLASH_EX_OP_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_EX_OP_ENABLED)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_FLASH_MCHP_NVMCTRL_G2"></a>

## 92.57 `CONFIG_FLASH_MCHP_NVMCTRL_G2`

**提示（Prompt）**：Microchip G2 NVMCTRL 闪存驱动（Flash Driver）

**说明（Help）**

启用用于闪存（Flash）的 Microchip G2 非易失性存储器控制器（Non-Volatile Memory Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_NVMCTRL_G2_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EX_OP
CONFIG_FLASH_EX_OP_ENABLED
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mchp:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mchp#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_FLASH_EX_OP_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_EX_OP_ENABLED)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_FLASH_MCHP_NVMCTRL_G3"></a>

## 92.58 `CONFIG_FLASH_MCHP_NVMCTRL_G3`

**提示（Prompt）**：Microchip G3 NVMCTRL 闪存驱动（Flash Driver）

**说明（Help）**

启用 Microchip G3 非易失性存储器控制器（Non-Volatile Memory Controller），用于闪存操作（Flash Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_NVMCTRL_G3_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EX_OP
CONFIG_FLASH_EX_OP_ENABLED
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mchp:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mchp#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_FLASH_EX_OP_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_EX_OP_ENABLED)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH"></a>

## 92.59 `CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH`

**提示（Prompt）**：MCUX FlexSPI HYPERFLASH 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_HYPERFLASH_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MEMC
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH_WRITE_BUFFER"></a>

## 92.60 `CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH_WRITE_BUFFER`

**提示（Prompt）**：MCUX FlexSPI HYPERFLASH 写入 RAM 缓冲区（Write RAM Buffer）

**说明（Help）**

在将数据写入闪存之前，先复制到 RAM 缓冲区（Buffer）。这样可防止待写入数据本身位于闪存上时发生故障。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G"></a>

## 92.61 `CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`

**提示（Prompt）**：MCUX FlexSPI MX25UM51345G 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_MX25UM51345G_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MEMC
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_DTR"></a>

## 92.62 `CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_DTR`

**提示（Prompt）**：双倍传输速率（Double Transfer Rate，DTR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI MX25UM51345G 八线外设接口模式（OPI Mode）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE"></a>

## 92.63 `CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE`

**提示（Prompt）**：FlexSPI MX25UM51345G 八线外设接口模式（OPI Mode）

**说明（Help）**

选择 MX25UM51345G 八线闪存工作模式（Octal Flash Operation Mode）：八线 I/O 单倍传输速率（STR）或八线 I/O 双倍传输速率（DTR）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_DTR
```

**可选项（Choices）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_STR
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_DTR
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_DTR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_DTR)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_STR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_STR)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_STR"></a>

## 92.64 `CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_STR`

**提示（Prompt）**：单倍传输速率（Single Transfer Rate，STR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI MX25UM51345G 八线外设接口模式（OPI Mode）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G_OPI_MODE)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NAND"></a>

## 92.65 `CONFIG_FLASH_MCUX_FLEXSPI_NAND`

**提示（Prompt）**：MCUX FlexSPI NAND，支持 ONFI 参数探测（Probe）

**说明（Help）**

通过 NXP FlexSPI 访问 NAND 闪存的驱动，支持 ONFI 参数探测（Parameter Probe），并通过四线 I/O（Quad I/O）读写数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_NAND_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_EX_OP
CONFIG_MEMC
CONFIG_MEMC_MCUX_FLEXSPI
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NAND_INIT_PRIORITY"></a>

## 92.66 `CONFIG_FLASH_MCUX_FLEXSPI_NAND_INIT_PRIORITY`

**提示（Prompt）**：MCUX FlexSPI NAND 闪存初始化优先级（Init Priority）

**说明（Help）**

FlexSPI NAND 闪存驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_FLASH_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_INIT_PRIORITY`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_INIT_PRIORITY)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NAND_TIMEOUT_US"></a>

## 92.67 `CONFIG_FLASH_MCUX_FLEXSPI_NAND_TIMEOUT_US`

**提示（Prompt）**：FlexSPI NAND 忙等待轮询超时（Busy-Wait Polling Timeout）

**说明（Help）**

操作完成后，等待 NAND 闪存就绪的最长时间，以微秒为单位。设为 `0` 可无限轮询（Poll Indefinitely）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NOR"></a>

## 92.68 `CONFIG_FLASH_MCUX_FLEXSPI_NOR`

**提示（Prompt）**：MCUX FlexSPI NOR 驱动

**说明（Help）**

用于 NXP FlexSPI 控制器所连接外部 NOR 闪存的驱动。启用 `PM_DEVICE` 且闪存节点绑定到电源域（Power Domain）时，`TURN_ON` 恢复流程会从电源管理唤醒路径（PM Wake Path，即空闲线程）重新执行闪存探测（Flash Probe）。探测本身约需 270 字节栈空间，可能使默认空闲栈（带 FPU 的 ARM 上为 320 字节）不足，因此可能需要增大 `CONFIG_IDLE_STACK_SIZE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_NOR_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_MEMC
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NOR_MUTEX"></a>

## 92.69 `CONFIG_FLASH_MCUX_FLEXSPI_NOR_MUTEX`

**提示（Prompt）**：MCUX FlexSPI NOR 互斥锁保护（Mutex Protection）

**说明（Help）**

使用互斥锁（Mutex）保护 MCUX FlexSPI NOR API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_NOR && CONFIG_MULTITHREADING && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NOR_PM_RESTORE"></a>

## 92.70 `CONFIG_FLASH_MCUX_FLEXSPI_NOR_PM_RESTORE`

**提示（Prompt）**：电源域唤醒时恢复 FlexSPI NOR 配置（Restore on Power-Domain Wake）

**说明（Help）**

在 `PM_DEVICE_ACTION_TURN_ON` 时重新执行闪存探测（Flash Probe），以便电源域断电（Power-Domain Power-Down）造成控制器状态丢失后，重建 FlexSPI 控制器配置。例如，RW6xx 上 PM3 类状态的唤醒就属于这种情况。探测在空闲线程的电源管理唤醒上下文（Idle-Thread PM Wake Context）中运行，约需 270 字节栈空间，因此可能需要增大 `CONFIG_IDLE_STACK_SIZE`，在 `frdm_rw612` 上为 `2048`。此选项默认禁用，以免影响其他平台；将此驱动绑定到电源域的开发板应启用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → FlexSPI 闪存驱动（Flash Driver）。

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_NOR_WRITE_BUFFER"></a>

## 92.71 `CONFIG_FLASH_MCUX_FLEXSPI_NOR_WRITE_BUFFER`

**提示（Prompt）**：MCUX FlexSPI NOR 写入 RAM 缓冲区（Write RAM Buffer）

**说明（Help）**

在将数据写入闪存之前，先复制到 RAM 缓冲区（Buffer）。这样可防止待写入数据本身位于闪存上时发生故障。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_MCUX_FLEXSPI_NOR || CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G) && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MCUX_XSPI"></a>

## 92.72 `CONFIG_FLASH_MCUX_XSPI`

**提示（Prompt）**：MCUX XSPI 闪存驱动（Flash Driver）

**说明（Help）**

启用 MCUX XSPI 闪存（Flash）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_XSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC
CONFIG_MEMC_MCUX_XSPI
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_XSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_XSPI)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_XSPI`。

<a id="CONFIG_FLASH_MCUX_XSPI_WRITE_BUFFER"></a>

## 92.73 `CONFIG_FLASH_MCUX_XSPI_WRITE_BUFFER`

**提示（Prompt）**：MCUX XSPI 使用 RAM 缓冲区写入（Write with RAM Buffer）

**说明（Help）**

在将数据写入闪存之前，先复制到 RAM 缓冲区（Buffer）。这样可防止待写入数据本身位于闪存上时发生故障，并将传输大小填充到 4 字节对齐（4-Byte Alignment），以满足 XSPI IP 的发送（TX）限制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_XSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MCUX XSPI 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_XSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI"></a>

## 92.74 `CONFIG_FLASH_MSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已启用 MSPI 闪存驱动（Flash Drivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_MSPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_MSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI)。

<a id="CONFIG_FLASH_MSPI_ATXP032"></a>

## 92.75 `CONFIG_FLASH_MSPI_ATXP032`

**提示（Prompt）**：MSPI ATXP032 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_MSPI
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_MSPI_AMBIQ_CONTROLLER
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_AMBIQ_CONTROLLER)。

<a id="CONFIG_FLASH_MSPI_EMUL_DEVICE"></a>

## 92.76 `CONFIG_FLASH_MSPI_EMUL_DEVICE`

**提示（Prompt）**：MSPI 闪存设备仿真器（Flash Device Emulator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_MSPI
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_MSPI_HANDLE_CACHE"></a>

## 92.77 `CONFIG_FLASH_MSPI_HANDLE_CACHE`

**提示（Prompt）**：在闪存外设驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_FLASH_MSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_INFINEON_S28HX512T"></a>

## 92.78 `CONFIG_FLASH_MSPI_INFINEON_S28HX512T`

**提示（Prompt）**：MSPI Infineon S28HX512T 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_S28HX512T_ENABLED && CONFIG_FLASH_MSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.infineon:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.infineon#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_FLASH_MSPI_IS25XX0XX"></a>

## 92.79 `CONFIG_FLASH_MSPI_IS25XX0XX`

**提示（Prompt）**：MSPI IS25L/WX064/032 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_MSPI
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_MSPI_AMBIQ_CONTROLLER
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_AMBIQ_CONTROLLER)。

<a id="CONFIG_FLASH_MSPI_MEMMAP_READ"></a>

## 92.80 `CONFIG_FLASH_MSPI_MEMMAP_READ`

**提示（Prompt）**：在 `flash_read` 中启用内存映射读取（Memory-Mapped Read）

**说明（Help）**

对于支持将设备映射到内存，且希望 `flash_read` 通过该内存映射区域（Memory-Mapped Region）读取的控制器，启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_MEMMAP && CONFIG_FLASH_MSPI && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_MEMMAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_MEMMAP)、[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_NOR"></a>

## 92.81 `CONFIG_FLASH_MSPI_NOR`

**提示（Prompt）**：通用 MSPI NOR 闪存（Generic MSPI NOR Flash）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_MSPI
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EX_OP
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_FLASH_MSPI_NOR_ACTIVE_DWELL_MS"></a>

## 92.82 `CONFIG_FLASH_MSPI_NOR_ACTIVE_DWELL_MS`

**提示（Prompt）**：最后一次使用后保持活动模式的停留时间（Dwell Period），以毫秒为单位

**说明（Help）**

闪存访问通常成批发生。如果每次访问之间都进入并退出深度掉电模式（Deep Power-Down，DPD），总操作时间会显著增加。此选项控制每次 API 调用后保持活动模式（Active Mode）的时长；如果下一次事务在停留时间（Dwell Period）结束前发生，就可省去“活动→空闲→活动”的状态转换过程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_FLASH_MSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver） → 通用 MSPI NOR 闪存（Generic MSPI NOR Flash）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_FLASH_MSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_NOR_DMA_CONTROL_XFER"></a>

## 92.83 `CONFIG_FLASH_MSPI_NOR_DMA_CONTROL_XFER`

**提示（Prompt）**：对 MSPI NOR 闪存控制传输（Control Transfer）使用 DMA

**说明（Help）**

寄存器读写及命令类 MSPI 事务（Transaction）的传输模式（Transfer Mode）。由于这些传输较短，通常建议使用 `MSPI_PIO`，即程序控制 I/O（Programmed I/O），其开销小于建立 DMA 传输的开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_DMA && CONFIG_FLASH_MSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver） → 通用 MSPI NOR 闪存（Generic MSPI NOR Flash）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_DMA)、[`CONFIG_FLASH_MSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_NOR_DMA_DATA_XFER"></a>

## 92.84 `CONFIG_FLASH_MSPI_NOR_DMA_DATA_XFER`

**提示（Prompt）**：对 MSPI NOR 闪存数据传输（Data Transfer）使用 DMA

**说明（Help）**

MSPI 读写数据事务（Transaction）的传输模式（Transfer Mode）。读写通常涉及较大的数据传输，因此通常建议使用 `MSPI_DMA`，以降低 CPU 负载并提高吞吐量（Throughput）。启用 `CONFIG_MSPI_DMA` 时，默认为 `MSPI_DMA`；否则默认为 `MSPI_PIO`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_DMA && CONFIG_FLASH_MSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver） → 通用 MSPI NOR 闪存（Generic MSPI NOR Flash）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_DMA)、[`CONFIG_FLASH_MSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_NOR_LAYOUT_PAGE_SIZE"></a>

## 92.85 `CONFIG_FLASH_MSPI_NOR_LAYOUT_PAGE_SIZE`

**提示（Prompt）**：`FLASH_LAYOUT` 功能使用的页大小（Page Size）

**说明（Help）**

使用 `CONFIG_FLASH_PAGE_LAYOUT` 时，此驱动支持对应 API。默认页大小（Page Size）等于块大小（Block Size）`65536`。其他选项包括 32 KB 擦除大小 `32768`、扇区大小（Sector Size）`4096`，或扇区大小的任意非零整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_PAGE_LAYOUT && CONFIG_FLASH_MSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver） → 通用 MSPI NOR 闪存（Generic MSPI NOR Flash）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_FLASH_MSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_NOR_USE_SFDP"></a>

## 92.86 `CONFIG_FLASH_MSPI_NOR_USE_SFDP`

**提示（Prompt）**：使用串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）

**说明（Help）**

使用 SFDP 信息设置闪存命令传输（Flash Command Transfer）并配置闪存芯片。目前仅支持在构建时（Build Time）处理 SFDP 结构，数据来自闪存设备树节点属性所提供的数组，例如 `sfdp-bfp`、`sfdp-ff05` 和 `sfdp-ff84`。根据所用 I/O 模式，构建闪存驱动时需要其中一部分或全部属性。这些属性的数据可通过 `drivers/jesd216` 示例取得。

如果闪存芯片不提供某个 SFDP 表，可将相应属性定义为空数组（Empty Array），以避免相关构建断言（Build Assertion）失败；原本应从该 SFDP 表读取的参数将采用默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MSPI 闪存设备驱动（Flash Device Driver） → 通用 MSPI NOR 闪存（Generic MSPI NOR Flash）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_MSPI_RANGE_HANDLE_CACHE_SIZE"></a>

## 92.87 `CONFIG_FLASH_MSPI_RANGE_HANDLE_CACHE_SIZE`

**提示（Prompt）**：按范围或整体处理缓存的阈值（Cache Handling Threshold），以字节为单位

**说明（Help）**

如果大小超过此值，按范围处理缓存（Cache Handling by Range）就不划算。不过，此值来自经验，可能与具体平台有关。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mspi:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mspi#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NPCX_FIU_DRA_EX"></a>

## 92.88 `CONFIG_FLASH_NPCX_FIU_DRA_EX`

**提示（Prompt）**：扩展直接读取访问模式支持（Extended Direct Read Access Mode）

**说明（Help）**

此选项为 NPCKn 处理器变体（Variant）启用扩展直接读取访问（DRA）模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

<a id="CONFIG_FLASH_NPCX_FIU_DRA_V1"></a>

## 92.89 `CONFIG_FLASH_NPCX_FIU_DRA_V1`

**提示（Prompt）**：直接读取访问第 1 版支持（Direct Read Access Version 1）

**说明（Help）**

此选项启用直接读取访问（DRA）V1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

<a id="CONFIG_FLASH_NPCX_FIU_DRA_V2"></a>

## 92.90 `CONFIG_FLASH_NPCX_FIU_DRA_V2`

**提示（Prompt）**：直接读取访问第 2 版支持（Direct Read Access Version 2）

**说明（Help）**

此选项启用直接读取访问（DRA）V2 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

<a id="CONFIG_FLASH_NPCX_FIU_NOR"></a>

## 92.91 `CONFIG_FLASH_NPCX_FIU_NOR`

**提示（Prompt）**：新唐（Nuvoton）NPCX 嵌入式控制器（Embedded Controller，EC）QSPI NOR 闪存驱动

**说明（Help）**

此选项为 NPCX 系列处理器启用 QSPI NOR 闪存（Flash）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_FIU_NOR_ENABLED && CONFIG_FLASH_NPCX_FIU_QSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 新唐（Nuvoton）NPCX QSPI 总线闪存驱动（Bus Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NPCX_FIU_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_NPCX_FIU_NOR_INIT"></a>

## 92.92 `CONFIG_FLASH_NPCX_FIU_NOR_INIT`

**提示（Prompt）**：驱动初始化期间的 QSPI NOR 闪存功能（Flash Features）

**说明（Help）**

此选项在驱动初始化期间启用 QSPI NOR 闪存功能，例如四线使能（Quad Enable）、4 字节地址支持等。如果 QSPI NOR 设备在驱动初始化时尚未就绪，则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_NPCX_FIU_NOR && CONFIG_FLASH_NPCX_FIU_QSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NPCX_FIU_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_NOR)、[`CONFIG_FLASH_NPCX_FIU_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NPCX_FIU_QSPI"></a>

## 92.93 `CONFIG_FLASH_NPCX_FIU_QSPI`

**提示（Prompt）**：新唐（Nuvoton）NPCX QSPI 总线闪存驱动（Bus Flash Driver）

**说明（Help）**

此选项为 NPCX 系列处理器启用 QSPI 总线闪存驱动（Bus Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_FIU_QSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_NPCX_FIU_SUPP_DRA_2_DEV"></a>

## 92.94 `CONFIG_FLASH_NPCX_FIU_SUPP_DRA_2_DEV`

**提示（Prompt）**：直接读取访问模式（Direct Read Access Mode）下的 4 字节地址支持

**说明（Help）**

如果 NPCX 系列支持在 QSPI 总线上以直接读取访问（Direct Read Access，DRA）方式访问两个外部 SPI 设备，则选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_NPCX_FIU_QSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_FLASH_NPCX_FIU_DRA_V1 || CONFIG_FLASH_NPCX_FIU_DRA_V2
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NPCX_FIU_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_NPCX_FIU_DRA_V1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_DRA_V1)、[`CONFIG_FLASH_NPCX_FIU_DRA_V2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_DRA_V2)。

<a id="CONFIG_FLASH_NPCX_FIU_SUPP_DRA_4B_ADDR"></a>

## 92.95 `CONFIG_FLASH_NPCX_FIU_SUPP_DRA_4B_ADDR`

**提示（Prompt）**：直接读取访问模式（Direct Read Access Mode）下的 4 字节地址支持

**说明（Help）**

如果 NPCX 系列在直接读取访问模式（Direct Read Access Mode）下支持 4 字节地址模式（4-Byte Address Mode），则选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_NPCX_FIU_QSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_FLASH_NPCX_FIU_DRA_V1 || CONFIG_FLASH_NPCX_FIU_DRA_V2 || CONFIG_FLASH_NPCX_FIU_DRA_EX
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NPCX_FIU_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_NPCX_FIU_DRA_V1`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_DRA_V1)、[`CONFIG_FLASH_NPCX_FIU_DRA_V2`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_DRA_V2)、[`CONFIG_FLASH_NPCX_FIU_DRA_EX`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_DRA_EX)。

<a id="CONFIG_FLASH_NPCX_FIU_SUPP_LOW_DEV_SWAP"></a>

## 92.96 `CONFIG_FLASH_NPCX_FIU_SUPP_LOW_DEV_SWAP`

**提示（Prompt）**：交换两个外部闪存的访问（Swap External Flash Access）

**说明（Help）**

如果需要交换两个外部闪存的访问，则选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_NPCX_FIU_QSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NPCX4 && CONFIG_FLASH_NPCX_FIU_SUPP_DRA_2_DEV && n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NPCX_FIU_QSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_FLASH_NPCX_FIU_SUPP_DRA_2_DEV`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NPCX_FIU_SUPP_DRA_2_DEV)。

<a id="CONFIG_FLASH_NPCX_FIU_UMA_EX"></a>

## 92.97 `CONFIG_FLASH_NPCX_FIU_UMA_EX`

**提示（Prompt）**：扩展用户模式访问支持（Extended User Mode Access）

**说明（Help）**

此选项为 NPCKn 处理器变体（Variant）启用扩展用户模式访问（UMA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

<a id="CONFIG_FLASH_NPCX_FIU_USE_DMA"></a>

## 92.98 `CONFIG_FLASH_NPCX_FIU_USE_DMA`

**提示（Prompt）**：对闪存接口单元（FIU）事务使用通用 DMA（GDMA）

**说明（Help）**

启用通用 DMA（GDMA）事务（Transaction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_NPCX_GDMA && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.npcx_fiu:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.npcx_fiu#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DMA_NPCX_GDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_NPCX_GDMA)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NRF_FORCE_ALT"></a>

## 92.99 `CONFIG_FLASH_NRF_FORCE_ALT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可启用此选项，强制使用闪存驱动（Flash Driver）的另一种实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_FLASH
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_NRF_RRAM
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH"></a>

## 92.100 `CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`

**提示（Prompt）**：NXP S32 QSPI HYPERFLASH 驱动

**说明（Help）**

启用用于连接到 NXP S32 QSPI 总线的 HyperFlash 存储器设备（Memory Device）的闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_QSPI_HYPERFLASH_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_qspi:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_qspi#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<!-- kconfig-navigation -->

[上一章](P091_drivers_firmware_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P093_drivers_flash_配置项参考_2.md)
