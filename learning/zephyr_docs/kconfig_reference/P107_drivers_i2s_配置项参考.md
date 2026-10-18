---
id: learning.zephyr-docs.kconfig-reference.page-107
title: "`drivers/i2s`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第107章\_`drivers/i2s`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/i2s` 的 68 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_I2S"></a>

## 107.1 `CONFIG_I2S`

**提示（Prompt）**：集成电路间音频（Inter-IC Sound，I²S）总线驱动

**说明（Help）**

启用 I²S（Inter-IC Sound）硬件总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_MPXXDTYY
```

**定义位置（Location）**：[`drivers/i2s/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_MPXXDTYY`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_MPXXDTYY)。

<a id="CONFIG_I2S_AMBIQ"></a>

## 107.2 `CONFIG_I2S_AMBIQ`

**提示（Prompt）**：Ambiq I²S 驱动

**说明（Help）**

启用 Apollo 5 MCU 的 Ambiq I²S 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_I2S
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_I2S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_I2S)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_AMBIQ_BUFFER_ALIGNMENT"></a>

## 107.3 `CONFIG_I2S_AMBIQ_BUFFER_ALIGNMENT`

**提示（Prompt）**：设置 I²S DMA TCB 缓冲区对齐（Buffer Alignment）

**说明（Help）**

I²S 缓冲区放在可缓存区域（Cacheable Region）时应按 32 字节对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_AMBIQ && CONFIG_I2S
```

**默认值（Defaults）**

```text
CONFIG_DCACHE_LINE_SIZE if CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.ambiq:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.ambiq#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Ambiq I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_AMBIQ`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_AMBIQ)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_DCACHE_LINE_SIZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_I2S_AMBIQ_HANDLE_CACHE"></a>

## 107.4 `CONFIG_I2S_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 I²S 驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_I2S_AMBIQ && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.ambiq:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.ambiq#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Ambiq I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_I2S_AMBIQ`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_AMBIQ)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_AMBIQ_RX_BLOCK_COUNT"></a>

## 107.5 `CONFIG_I2S_AMBIQ_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_AMBIQ && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.ambiq:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.ambiq#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Ambiq I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_AMBIQ`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_AMBIQ)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_AMBIQ_TX_BLOCK_COUNT"></a>

## 107.6 `CONFIG_I2S_AMBIQ_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_AMBIQ && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.ambiq:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.ambiq#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Ambiq I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_AMBIQ`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_AMBIQ)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_EDMA_BURST_SIZE"></a>

## 107.7 `CONFIG_I2S_EDMA_BURST_SIZE`

**提示（Prompt）**：I²S EDMA 突发传输大小（Burst Size）

**说明（Help）**

I²S EDMA 突发传输大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_SAI && CONFIG_I2S
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → NXP MCUX I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_SAI)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_ESP32"></a>

## 107.8 `CONFIG_I2S_ESP32`

**提示（Prompt）**：ESP32 I²S 驱动

**说明（Help）**

启用 ESP32 I²S 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA if DT_HAS_ESPRESSIF_ESP32_GDMA_ENABLED
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.esp32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.esp32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2S_ESP32_ALLOWED_EMPTY_TX_QUEUE_DEFERRAL_TIME_MS"></a>

## 107.9 `CONFIG_I2S_ESP32_ALLOWED_EMPTY_TX_QUEUE_DEFERRAL_TIME_MS`

**提示（Prompt）**：ESP32 I²S 空发送队列处理延迟时间（Deferral Time）

**说明（Help）**

允许延后处理空发送（TX）队列的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_ESP32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.esp32:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.esp32#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → ESP32 I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_ESP32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_ESP32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_ESP32_DMA_DESC_NUM_MAX"></a>

## 107.10 `CONFIG_I2S_ESP32_DMA_DESC_NUM_MAX`

**提示（Prompt）**：ESP32 I²S 链接描述符（Link Descriptor）数量

**说明（Help）**

每个 I²S 通道可用于 DMA 传输的链接描述符最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!DT_HAS_ESPRESSIF_ESP32_GDMA_ENABLED && CONFIG_I2S_ESP32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.esp32:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.esp32#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → ESP32 I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_ESP32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_ESP32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_ESP32_RX_BLOCK_COUNT"></a>

## 107.11 `CONFIG_I2S_ESP32_RX_BLOCK_COUNT`

**提示（Prompt）**：ESP32 I²S 接收块（RX Block）数量

**说明（Help）**

等待从 I²S 接收（RX）通道读取的最大块数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_ESP32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.esp32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.esp32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → ESP32 I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_ESP32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_ESP32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_ESP32_TX_BLOCK_COUNT"></a>

## 107.12 `CONFIG_I2S_ESP32_TX_BLOCK_COUNT`

**提示（Prompt）**：ESP32 I²S 发送块（TX Block）数量

**说明（Help）**

等待由 I²S 发送（TX）通道传输的最大块数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_ESP32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.esp32:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.esp32#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → ESP32 I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_ESP32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_ESP32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_HAS_PLL_SETTING"></a>

## 107.13 `CONFIG_I2S_HAS_PLL_SETTING`

**提示（Prompt）**：I²S 将在驱动中设置锁相环（PLL）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_SAI && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → NXP MCUX I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_SAI)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_INFINEON"></a>

## 107.14 `CONFIG_I2S_INFINEON`

**提示（Prompt）**：Infineon I²S 驱动

**说明（Help）**

此选项启用 I²S 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_I2S
CONFIG_PINCTRL
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_USE_INFINEON_I2S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_I2S)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2S_INFINEON_RX_QUEUE_SIZE"></a>

## 107.15 `CONFIG_I2S_INFINEON_RX_QUEUE_SIZE`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**

此选项设置为接收（RX）软件队列分配的元素数量。它应与用于保存 I²S 接收数据的固定大小内存块池（Memory Slab）中的块数一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_INFINEON && CONFIG_I2S
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.infineon:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.infineon#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Infineon I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_INFINEON`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_INFINEON)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_INFINEON_TX_QUEUE_SIZE"></a>

## 107.16 `CONFIG_I2S_INFINEON_TX_QUEUE_SIZE`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**

此选项设置为发送（TX）软件队列分配的元素数量。它应与用于保存 I²S 发送数据的固定大小内存块池（Memory Slab）中的块数一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_INFINEON && CONFIG_I2S
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.infineon:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.infineon#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Infineon I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_INFINEON`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_INFINEON)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_INIT_PRIORITY"></a>

## 107.17 `CONFIG_I2S_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/i2s/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_I2S_LITEX"></a>

## 107.18 `CONFIG_I2S_LITEX`

**提示（Prompt）**：LiteX I²S 驱动

**说明（Help）**

启用 LiteX 集成电路间音频（I²S）总线驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.litex:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.litex#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_LITEX_CHANNELS_CONCATENATED"></a>

## 107.19 `CONFIG_I2S_LITEX_CHANNELS_CONCATENATED`

**提示（Prompt）**：通道数据在 FIFO 中不插入填充（Padding）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_LITEX && CONFIG_I2S
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.litex:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.litex#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → LiteX I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_LITEX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_LITEX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_LITEX_DATA_BIG_ENDIAN"></a>

## 107.20 `CONFIG_I2S_LITEX_DATA_BIG_ENDIAN`

**提示（Prompt）**：接收数据将以大端序（Big Endian）存储。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_LITEX && CONFIG_I2S
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.litex:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.litex#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → LiteX I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_LITEX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_LITEX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_LITEX_RX_BLOCK_COUNT"></a>

## 107.21 `CONFIG_I2S_LITEX_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_LITEX && CONFIG_I2S
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.litex:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.litex#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → LiteX I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_LITEX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_LITEX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_LITEX_TX_BLOCK_COUNT"></a>

## 107.22 `CONFIG_I2S_LITEX_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_LITEX && CONFIG_I2S
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.litex:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.litex#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → LiteX I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_LITEX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_LITEX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_MAX32"></a>

## 107.23 `CONFIG_I2S_MAX32`

**提示（Prompt）**：Analog Devices MAX32 系列 I²S 驱动

**说明（Help）**

启用 Analog Devices MAX32 系列 I²S 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2S_MAX32_QUEUE_SIZE"></a>

## 107.24 `CONFIG_I2S_MAX32_QUEUE_SIZE`

**提示（Prompt）**：队列大小（Queue Size）

**说明（Help）**

发送／接收（Tx/Rx）待处理块队列的大小，即可以排队等待发送或接收的最大块数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MAX32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.max32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.max32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Analog Devices MAX32 系列 I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MAX32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MAX32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_MCUX_FLEXCOMM"></a>

## 107.25 `CONFIG_I2S_MCUX_FLEXCOMM`

**提示（Prompt）**：MCUX FLEXCOMM I²S 驱动

**说明（Help）**

启用 MCUX FLEXCOMM I²S 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux_flexcomm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux_flexcomm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_MCUX_FLEXCOMM_DMA_RX_BLOCKS"></a>

## 107.26 `CONFIG_I2S_MCUX_FLEXCOMM_DMA_RX_BLOCKS`

**提示（Prompt）**：接收（RX）使用的 DMA 块数

**说明（Help）**

I²S 接收传输使用的 DMA 块数。更大的值可提供更多缓冲，但也会消耗更多内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_FLEXCOMM && CONFIG_I2S
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux_flexcomm:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux_flexcomm#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → MCUX FLEXCOMM I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_FLEXCOMM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_FLEXCOMM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_MCUX_FLEXCOMM_DMA_TX_BLOCKS"></a>

## 107.27 `CONFIG_I2S_MCUX_FLEXCOMM_DMA_TX_BLOCKS`

**提示（Prompt）**：发送（TX）使用的 DMA 块数

**说明（Help）**

I²S 发送传输使用的 DMA 块数。更大的值可提供更多缓冲，但也会消耗更多内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_FLEXCOMM && CONFIG_I2S
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux_flexcomm:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux_flexcomm#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → MCUX FLEXCOMM I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_FLEXCOMM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_FLEXCOMM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_MCUX_FLEXCOMM_RX_BLOCK_COUNT"></a>

## 107.28 `CONFIG_I2S_MCUX_FLEXCOMM_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_FLEXCOMM && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux_flexcomm:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux_flexcomm#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → MCUX FLEXCOMM I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_FLEXCOMM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_FLEXCOMM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_MCUX_FLEXCOMM_TX_BLOCK_COUNT"></a>

## 107.29 `CONFIG_I2S_MCUX_FLEXCOMM_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_FLEXCOMM && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux_flexcomm:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux_flexcomm#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → MCUX FLEXCOMM I²S 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_FLEXCOMM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_FLEXCOMM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_MCUX_SAI"></a>

## 107.30 `CONFIG_I2S_MCUX_SAI`

**提示（Prompt）**：NXP MCUX I²S 控制器驱动

**说明（Help）**

启用 i.MX 系列处理器的 I²S 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_NATIVE_SIM"></a>

## 107.31 `CONFIG_I2S_NATIVE_SIM`

**提示（Prompt）**：native_sim I²S 文件后端（File Backend）

**说明（Help）**

启用 native_sim I²S 后端，从主机文件读取接收（RX）脉冲编码调制（PCM）采样，并将发送（TX）PCM 采样写入主机文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_SIM_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.native_sim:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.native_sim#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_I2S_NATIVE_SIM_QUEUE_SIZE"></a>

## 107.32 `CONFIG_I2S_NATIVE_SIM_QUEUE_SIZE`

**提示（Prompt）**：native_sim I²S 队列深度（Queue Depth）

**说明（Help）**

每个 native_sim I²S 设备可排队的 I²S 块数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NATIVE_SIM && CONFIG_I2S
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[2, 64]
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.native_sim:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.native_sim#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → native_sim I²S 文件后端（File Backend）

**配置项引用（Symbol References）**：[`CONFIG_I2S_NATIVE_SIM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NATIVE_SIM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NATIVE_SIM_RX_FILE_PATH"></a>

## 107.33 `CONFIG_I2S_NATIVE_SIM_RX_FILE_PATH`

**提示（Prompt）**：native_sim I²S RX PCM 文件路径（File Path）

**说明（Help）**

native_sim I²S 接收设备读取的默认主机 PCM 文件路径。可通过命令行覆盖。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NATIVE_SIM && CONFIG_I2S
```

**默认值（Defaults）**

```text
"i2s_in.pcm"
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.native_sim:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.native_sim#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → native_sim I²S 文件后端（File Backend）

**配置项引用（Symbol References）**：[`CONFIG_I2S_NATIVE_SIM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NATIVE_SIM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NATIVE_SIM_THREAD_PRIORITY"></a>

## 107.34 `CONFIG_I2S_NATIVE_SIM_THREAD_PRIORITY`

**提示（Prompt）**：native_sim I²S 工作线程优先级（Worker Priority）

**说明（Help）**

native_sim I²S 工作线程（Worker Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NATIVE_SIM && CONFIG_I2S
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.native_sim:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.native_sim#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → native_sim I²S 文件后端（File Backend）

**配置项引用（Symbol References）**：[`CONFIG_I2S_NATIVE_SIM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NATIVE_SIM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NATIVE_SIM_TX_FILE_PATH"></a>

## 107.35 `CONFIG_I2S_NATIVE_SIM_TX_FILE_PATH`

**提示（Prompt）**：native_sim I²S TX PCM 文件路径（File Path）

**说明（Help）**

native_sim I²S 发送设备生成的默认主机 PCM 文件路径。可通过命令行覆盖。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NATIVE_SIM && CONFIG_I2S
```

**默认值（Defaults）**

```text
"i2s_out.pcm"
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.native_sim:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.native_sim#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → native_sim I²S 文件后端（File Backend）

**配置项引用（Symbol References）**：[`CONFIG_I2S_NATIVE_SIM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NATIVE_SIM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NRFX"></a>

## 107.36 `CONFIG_I2S_NRFX`

**提示（Prompt）**：nRF I²S nrfx 驱动

**说明（Help）**

启用 nRF MCU 系列的 nrfx I²S 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_I2S
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_NRFX_I2S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_I2S)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_NRFX_ALLOW_MCK_BYPASS"></a>

## 107.37 `CONFIG_I2S_NRFX_ALLOW_MCK_BYPASS`

**提示（Prompt）**：存在合适比率时允许 MCK 旁路（Bypass）

**说明（Help）**

直接根据 MCK 与 LRCK 查找受支持的比率（Ratio），若存在则启用旁路。否则回退到标准 MCK 选择机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF53 && CONFIG_I2S_NRFX && CONFIG_I2S
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → nRF I²S nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_I2S_NRFX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NRFX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NRFX_RX_BLOCK_COUNT"></a>

## 107.38 `CONFIG_I2S_NRFX_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NRFX && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → nRF I²S nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_NRFX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NRFX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NRFX_TX_BLOCK_COUNT"></a>

## 107.39 `CONFIG_I2S_NRFX_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NRFX && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → nRF I²S nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_NRFX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NRFX)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NRF_TDM"></a>

## 107.40 `CONFIG_I2S_NRF_TDM`

**提示（Prompt）**：nRF 时分复用（TDM）驱动

**说明（Help）**

启用 nRF MCU 系列的时分复用（TDM）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_TDM_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_NRF_TDM_RX_BLOCK_COUNT"></a>

## 107.41 `CONFIG_I2S_NRF_TDM_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NRF_TDM && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → nRF 时分复用（TDM）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_NRF_TDM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NRF_TDM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_NRF_TDM_TX_BLOCK_COUNT"></a>

## 107.42 `CONFIG_I2S_NRF_TDM_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_NRF_TDM && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.nrfx:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.nrfx#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → nRF 时分复用（TDM）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_NRF_TDM`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NRF_TDM)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_RENESAS_RA_SSIE"></a>

## 107.43 `CONFIG_I2S_RENESAS_RA_SSIE`

**提示（Prompt）**：Renesas RA I²S SSIE

**说明（Help）**

启用 Renesas RA I²S SSIE 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_I2S_SSIE_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SSI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_USE_RA_FSP_SSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SSI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_RENESAS_RA_SSIE_DTC"></a>

## 107.44 `CONFIG_I2S_RENESAS_RA_SSIE_DTC`

**提示（Prompt）**：发送和接收使用 DTC

**说明（Help）**

在发送（Transmission）和接收（Reception）时启用 DTC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_RENESAS_RA_SSIE && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.renesas_ra:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.renesas_ra#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Renesas RA I²S SSIE

**配置项引用（Symbol References）**：[`CONFIG_I2S_RENESAS_RA_SSIE`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_I2S_RENESAS_RA_SSIE_RX_BLOCK_COUNT"></a>

## 107.45 `CONFIG_I2S_RENESAS_RA_SSIE_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_RENESAS_RA_SSIE && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.renesas_ra:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.renesas_ra#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Renesas RA I²S SSIE

**配置项引用（Symbol References）**：[`CONFIG_I2S_RENESAS_RA_SSIE`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_RENESAS_RA_SSIE_RX_SECONDARY_BUFFER"></a>

## 107.46 `CONFIG_I2S_RENESAS_RA_SSIE_RX_SECONDARY_BUFFER`

**提示（Prompt）**：辅助接收缓冲区（Secondary RX Buffer）

**说明（Help）**

为接收启用辅助缓冲区分配，将其用作链式缓冲区（Chained Buffer），以改善数据接收的连续性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_RENESAS_RA_SSIE && CONFIG_I2S
```

**默认值（Defaults）**

```text
y if CONFIG_I2S_RENESAS_RA_SSIE_DTC
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.renesas_ra:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.renesas_ra#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Renesas RA I²S SSIE

**配置项引用（Symbol References）**：[`CONFIG_I2S_RENESAS_RA_SSIE`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_I2S_RENESAS_RA_SSIE_DTC`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE_DTC)。

<a id="CONFIG_I2S_RENESAS_RA_SSIE_TX_BLOCK_COUNT"></a>

## 107.47 `CONFIG_I2S_RENESAS_RA_SSIE_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_RENESAS_RA_SSIE && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.renesas_ra:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.renesas_ra#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Renesas RA I²S SSIE

**配置项引用（Symbol References）**：[`CONFIG_I2S_RENESAS_RA_SSIE`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_RX_BLOCK_COUNT"></a>

## 107.48 `CONFIG_I2S_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_SAI && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → NXP MCUX I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_SAI)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SAM_SSC"></a>

## 107.49 `CONFIG_I2S_SAM_SSC`

**提示（Prompt）**：Atmel SAM MCU 系列 I²S（SSC）总线驱动

**说明（Help）**

启用 Atmel SAM MCU 系列基于同步串行控制器（Synchronous Serial Controller，SSC）模块的 I²S 总线驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_SSC_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.sam_ssc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.sam_ssc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2S_SAM_SSC_0_PIN_RF_EN"></a>

## 107.50 `CONFIG_I2S_SAM_SSC_0_PIN_RF_EN`

**提示（Prompt）**：启用 RF 引脚

**说明（Help）**

启用时，RF 信号连接到 RF 引脚；根据接收器处于主模式（Master）还是从模式（Slave），将其配置为输出或输入。禁用时，RF 信号与 RF 引脚断开，在内部连接到 TF（发送器帧同步信号，Transmitter Frame Synchro Signal）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SAM_SSC && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.sam_ssc:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.sam_ssc#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Atmel SAM MCU 系列 I²S（SSC）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SAM_SSC`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SAM_SSC)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SAM_SSC_0_PIN_RK_EN"></a>

## 107.51 `CONFIG_I2S_SAM_SSC_0_PIN_RK_EN`

**提示（Prompt）**：启用 RK 引脚

**说明（Help）**

启用时，RK 信号连接到 RK 引脚；根据接收器处于主模式（Master）还是从模式（Slave），将其配置为输出或输入。禁用时，RK 信号与 RK 引脚断开，在内部连接到 TK（发送器时钟信号，Transmitter Clock Signal）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SAM_SSC && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.sam_ssc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.sam_ssc#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Atmel SAM MCU 系列 I²S（SSC）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SAM_SSC`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SAM_SSC)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SAM_SSC_RX_BLOCK_COUNT"></a>

## 107.52 `CONFIG_I2S_SAM_SSC_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SAM_SSC && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.sam_ssc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.sam_ssc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Atmel SAM MCU 系列 I²S（SSC）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SAM_SSC`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SAM_SSC)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SAM_SSC_TX_BLOCK_COUNT"></a>

## 107.53 `CONFIG_I2S_SAM_SSC_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SAM_SSC && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.sam_ssc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.sam_ssc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Atmel SAM MCU 系列 I²S（SSC）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SAM_SSC`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SAM_SSC)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SHELL"></a>

## 107.54 `CONFIG_I2S_SHELL`

**提示（Prompt）**：I²S 命令行（Shell）

**说明（Help）**

启用 `i2s` Shell：通过任意 I²S 控制器流式发送生成的测试音（`i2s tone` / `i2s stop` / `i2s info`）。它仅负责传输；需配合 `codec` Shell，通过音频编解码器（Codec）路由音频。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_I2S
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.shell:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.shell#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SHELL_BLOCK_COUNT"></a>

## 107.55 `CONFIG_I2S_SHELL_BLOCK_COUNT`

**提示（Prompt）**：I²S 发送块（TX Block）数量

**说明（Help）**

发送固定大小内存块池（TX Slab）中的块数。更多块意味着更多缓冲，代价是增加 RAM 占用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SHELL && CONFIG_I2S
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.shell:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.shell#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I²S 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_I2S_SHELL`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SHELL)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SHELL_BLOCK_FRAMES"></a>

## 107.56 `CONFIG_I2S_SHELL_BLOCK_FRAMES`

**提示（Prompt）**：每个 I²S 发送块的帧数（16 位）

**说明（Help）**

16 位音频每个发送块中的立体声帧（Stereo Frame）数量。对于 24/32 位音频，每个字（Word）占 4 字节，因此相同块大小下，每块的帧数减半。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SHELL && CONFIG_I2S
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.shell:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.shell#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I²S 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_I2S_SHELL`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SHELL)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SHELL_STACK_SIZE"></a>

## 107.57 `CONFIG_I2S_SHELL_STACK_SIZE`

**提示（Prompt）**：I²S Shell 流式传输线程栈大小（Stack Size）

**说明（Help）**

向 I²S 提供 PCM 块的后台线程（Background Thread）栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SHELL && CONFIG_I2S
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.shell:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.shell#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I²S 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_I2S_SHELL`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SHELL)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SHELL_THREAD_PRIO"></a>

## 107.58 `CONFIG_I2S_SHELL_THREAD_PRIO`

**提示（Prompt）**：I²S Shell 流式传输线程优先级（Thread Priority）

**说明（Help）**

I²S 数据供给线程（Feeder Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SHELL && CONFIG_I2S
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.shell:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.shell#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I²S 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_I2S_SHELL`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SHELL)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SILABS_SIWX91X"></a>

## 107.59 `CONFIG_I2S_SILABS_SIWX91X`

**提示（Prompt）**：Silabs Siwx91x MCU I²S 控制器驱动

**说明（Help）**

启用 Siwx91x 系列的 I²S 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_I2S_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_DMA
CONFIG_PINCTRL
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_I2S_SILABS_SIWX91X_DMA_MAX_BLOCKS"></a>

## 107.60 `CONFIG_I2S_SILABS_SIWX91X_DMA_MAX_BLOCKS`

**提示（Prompt）**：一次事务中每个通道的最大 DMA 传输块数。

**说明（Help）**

每 1024 字节需要一个块（Block）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SILABS_SIWX91X && CONFIG_I2S
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.siwx91x:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.siwx91x#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Silabs Siwx91x MCU I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SILABS_SIWX91X`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SILABS_SIWX91X)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SILABS_SIWX91X_RX_BLOCK_COUNT"></a>

## 107.61 `CONFIG_I2S_SILABS_SIWX91X_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SILABS_SIWX91X && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.siwx91x:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.siwx91x#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Silabs Siwx91x MCU I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SILABS_SIWX91X`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SILABS_SIWX91X)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_SILABS_SIWX91X_TX_BLOCK_COUNT"></a>

## 107.62 `CONFIG_I2S_SILABS_SIWX91X_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_SILABS_SIWX91X && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.siwx91x:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.siwx91x#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → Silabs Siwx91x MCU I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_SILABS_SIWX91X`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_SILABS_SIWX91X)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_STM32"></a>

## 107.63 `CONFIG_I2S_STM32`

**提示（Prompt）**：STM32 MCU I²S 控制器驱动

**说明（Help）**

启用 STM32 系列处理器的 I²S 支持。（原文说明已在 STM32F4 和 STM32H7 系列上测试。）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_I2S_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_DMA
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2S_STM32_RX_BLOCK_COUNT"></a>

## 107.64 `CONFIG_I2S_STM32_RX_BLOCK_COUNT`

**提示（Prompt）**：接收（RX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_STM32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.stm32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.stm32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → STM32 MCU I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_STM32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_STM32_SAI"></a>

## 107.65 `CONFIG_I2S_STM32_SAI`

**提示（Prompt）**：STM32 MCU 串行音频接口（SAI）控制器驱动

**说明（Help）**

启用 STM32 系列处理器的串行音频接口（SAI）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_SAI_ENABLED && CONFIG_I2S
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_DMA
CONFIG_USE_STM32_HAL_DMA
CONFIG_USE_STM32_HAL_DMA_EX
CONFIG_USE_STM32_HAL_SAI
CONFIG_USE_STM32_HAL_SAI_EX if CONFIG_SOC_SERIES_STM32F4X
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.stm32:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.stm32#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)、[`CONFIG_USE_STM32_HAL_SAI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SAI)、[`CONFIG_USE_STM32_HAL_SAI_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SAI_EX)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F4X`。

<a id="CONFIG_I2S_STM32_SAI_BLOCK_COUNT"></a>

## 107.66 `CONFIG_I2S_STM32_SAI_BLOCK_COUNT`

**提示（Prompt）**：SAI 队列长度（Queue Length）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_STM32_SAI && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.stm32:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.stm32#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → STM32 MCU 串行音频接口（SAI）控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_STM32_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32_SAI)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_STM32_TX_BLOCK_COUNT"></a>

## 107.67 `CONFIG_I2S_STM32_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_STM32 && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.stm32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.stm32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → STM32 MCU I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_STM32`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_STM32)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_I2S_TX_BLOCK_COUNT"></a>

## 107.68 `CONFIG_I2S_TX_BLOCK_COUNT`

**提示（Prompt）**：发送（TX）队列长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2S_MCUX_SAI && CONFIG_I2S
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2s/Kconfig.mcux:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2s/Kconfig.mcux#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → NXP MCUX I²S 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2S_MCUX_SAI`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_MCUX_SAI)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<!-- kconfig-navigation -->

[上一章](P106_drivers_i2c_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P108_drivers_i3c_配置项参考.md)
