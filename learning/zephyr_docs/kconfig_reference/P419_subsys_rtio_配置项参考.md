---
id: learning.zephyr-docs.kconfig-reference.page-419
title: "`subsys/rtio`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第419章\_`subsys/rtio`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/rtio` 的 20 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RTIO"></a>

## 419.1 `CONFIG_RTIO`

**提示（Prompt）**：实时输入输出（Real-Time I/O，RTIO）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ADC_STREAM
CONFIG_ADC_DEFAULT_RTIO
CONFIG_I2C_RTIO
CONFIG_I3C_RTIO
CONFIG_SENSOR_ASYNC_API
CONFIG_ADIS1647X
CONFIG_SPI_RTIO
CONFIG_SENSING
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_ADC_STREAM`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STREAM)、[`CONFIG_ADC_DEFAULT_RTIO`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_DEFAULT_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADIS1647X`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_RTIO_BLOCK_POOL_PLACEMENT"></a>

## 419.2 `CONFIG_RTIO_BLOCK_POOL_PLACEMENT`

**提示（Prompt）**：实时 I/O（RTIO）块池存放位置（Block pool placement）

**说明（Help）**

选择实时 I/O（RTIO）块池的存放位置：

- 默认（Default）：普通 data/BSS 区。
- 数据紧耦合内存（DTCM）：不经过缓存的 DTCM 段。
- 无缓存（No-cache）：显式标记为不可缓存的段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**默认值（Defaults）**

```text
CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM if n
CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE if CONFIG_NOCACHE_MEMORY
CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DEFAULT
CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM
CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM)、[`CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DEFAULT`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DEFAULT)。

<a id="CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DEFAULT"></a>

## 419.3 `CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DEFAULT`

**提示（Prompt）**：默认数据内存（Default data memory）

**说明（Help）**

将实时 I/O（RTIO）块池放在默认 data/BSS 内存区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_BLOCK_POOL_PLACEMENT>
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时 I/O（RTIO）块池存放位置（Block pool placement）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_BLOCK_POOL_PLACEMENT`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_BLOCK_POOL_PLACEMENT)。

<a id="CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM"></a>

## 419.4 `CONFIG_RTIO_BLOCK_POOL_PLACEMENT_DTCM`

**提示（Prompt）**：数据紧耦合内存（DTCM；无缓存，Uncached）

**说明（Help）**

将实时 I/O（RTIO）块池放在数据紧耦合内存（DTCM）中。在受支持架构中，DTCM 本身不经过缓存，通常不需要额外缓存维护（Cache maintenance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时 I/O（RTIO）块池存放位置（Block pool placement）

<a id="CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE"></a>

## 419.5 `CONFIG_RTIO_BLOCK_POOL_PLACEMENT_NOCACHE`

**提示（Prompt）**：不可缓存内存（Non-cacheable memory，NOCACHE）

**说明（Help）**

将实时 I/O（RTIO）块池放在不可缓存内存区域（Non-cacheable memory region）。假定开发板和链接器提供相应的无缓存 data/BSS 段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NOCACHE_MEMORY && <choice CONFIG_RTIO_BLOCK_POOL_PLACEMENT>
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时 I/O（RTIO）块池存放位置（Block pool placement）

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_RTIO_BLOCK_POOL_PLACEMENT`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_BLOCK_POOL_PLACEMENT)。

<a id="CONFIG_RTIO_CONSUME_SEM"></a>

## 419.6 `CONFIG_RTIO_CONSUME_SEM`

**提示（Prompt）**：`rtio_cqe_consume_block` 等待完成事件时使用信号量（Semaphore）

**说明（Help）**

调用 `rtio_cqe_consume_block` 时，使用信号量（Semaphore）让调用线程在等待完成队列事件时休眠，直到满足等待计数。此方式增加一个信号量的少量 RAM 开销。否则，调用会轮询完成队列（Completion queue），在迭代之间执行 `k_yield()`。除 `!MULTITHREADING`，即未启用多线程的情况外，此选项默认启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**默认值（Defaults）**

```text
n if !CONFIG_MULTITHREADING
y
```

**被选择（Selected by）**

```text
CONFIG_ADC_STREAM
CONFIG_ADC_DEFAULT_RTIO
CONFIG_SENSOR_ASYNC_API
CONFIG_RTIO_WORKQ
CONFIG_SENSING
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_ADC_STREAM`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STREAM)、[`CONFIG_ADC_DEFAULT_RTIO`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_DEFAULT_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_RTIO_WORKQ`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_RTIO_CQE_CALLBACK"></a>

## 419.7 `CONFIG_RTIO_CQE_CALLBACK`

**提示（Prompt）**：向 RTIO 上下文提交完成队列项（CQE）时通过回调通知

**说明（Help）**

完成队列项（Completion Queue Entry，CQE）回调在 CQE 提交到 RTIO 上下文时发出通知，通过 `rtio_set_cqe_callback()` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)。

<a id="CONFIG_RTIO_OP_DELAY"></a>

## 419.8 `CONFIG_RTIO_OP_DELAY`

**提示（Prompt）**：延迟操作（Delay Operation）

**说明（Help）**

启用 `OP_DELAY`，允许在操作链（Chain of operations）中使用内核超时进行延迟。延迟由共享的超时 I/O 设备（Timeout iodev）处理，因此启用后无需在每个提交队列项（Submission queue entry）中内嵌一个超时对象。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ENS210
CONFIG_BME680
CONFIG_MS5637
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_ENS210`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS210)、[`CONFIG_BME680`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BME680)、[`CONFIG_MS5637`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MS5637)。

<a id="CONFIG_RTIO_SQE_CACHELINE_CHECK"></a>

## 419.9 `CONFIG_RTIO_SQE_CACHELINE_CHECK`

**提示（Prompt）**：提交队列项（SQE）的缓存行大小检查（Cacheline size check）

**说明（Help）**

构建时检查 `struct rtio_sqe` 的大小，确保小于一个缓存行（Cache line），否则构建失败。这有助于在对数据缓存影响敏感的系统上保持高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)。

<a id="CONFIG_RTIO_SQE_PLACEMENT"></a>

## 419.10 `CONFIG_RTIO_SQE_PLACEMENT`

**提示（Prompt）**：实时 I/O（RTIO）提交队列项（SQE）的存放位置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**默认值（Defaults）**

```text
CONFIG_RTIO_SQE_PLACEMENT_DTCM if n
CONFIG_RTIO_SQE_PLACEMENT_NOCACHE if CONFIG_NOCACHE_MEMORY
CONFIG_RTIO_SQE_PLACEMENT_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RTIO_SQE_PLACEMENT_DEFAULT
CONFIG_RTIO_SQE_PLACEMENT_DTCM
CONFIG_RTIO_SQE_PLACEMENT_NOCACHE
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_RTIO_SQE_PLACEMENT_DTCM`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_SQE_PLACEMENT_DTCM)、[`CONFIG_RTIO_SQE_PLACEMENT_NOCACHE`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_SQE_PLACEMENT_NOCACHE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_RTIO_SQE_PLACEMENT_DEFAULT`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_SQE_PLACEMENT_DEFAULT)。

<a id="CONFIG_RTIO_SQE_PLACEMENT_DEFAULT"></a>

## 419.11 `CONFIG_RTIO_SQE_PLACEMENT_DEFAULT`

**提示（Prompt）**：默认数据内存（Default data memory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_SQE_PLACEMENT>
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时 I/O（RTIO）提交队列项（SQE）的存放位置

**配置项引用（Symbol References）**：[`CONFIG_RTIO_SQE_PLACEMENT`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_SQE_PLACEMENT)。

<a id="CONFIG_RTIO_SQE_PLACEMENT_DTCM"></a>

## 419.12 `CONFIG_RTIO_SQE_PLACEMENT_DTCM`

**提示（Prompt）**：数据紧耦合内存（DTCM；无缓存，Uncached）

**说明（Help）**

将提交队列项（SQE）环形队列放在链接器名为 DTCM 的内存区域，即无缓存、低延迟的数据紧耦合内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时 I/O（RTIO）提交队列项（SQE）的存放位置

<a id="CONFIG_RTIO_SQE_PLACEMENT_NOCACHE"></a>

## 419.13 `CONFIG_RTIO_SQE_PLACEMENT_NOCACHE`

**提示（Prompt）**：不可缓存内存（Non-cacheable memory，NOCACHE）

**说明（Help）**

将提交队列项（SQE）环形队列放在 Zephyr 的无缓存区域（No-cache region），避免微小传输受到数据缓存一致性（D-cache coherency）副作用影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NOCACHE_MEMORY && <choice CONFIG_RTIO_SQE_PLACEMENT>
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时 I/O（RTIO）提交队列项（SQE）的存放位置

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_RTIO_SQE_PLACEMENT`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_SQE_PLACEMENT)。

<a id="CONFIG_RTIO_SUBMIT_SEM"></a>

## 419.14 `CONFIG_RTIO_SUBMIT_SEM`

**提示（Prompt）**：`rtio_submit` 等待完成事件时使用信号量（Semaphore）

**说明（Help）**

调用 `rtio_submit` 时，使用信号量（Semaphore）让调用线程在等待完成队列事件时休眠，直到满足等待计数。此方式增加一个信号量的少量 RAM 开销。否则，`wait_for` 会轮询完成队列（Completion queue），在迭代之间执行 `k_yield()`。除 `!MULTITHREADING`，即未启用多线程的情况外，此选项默认启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**默认值（Defaults）**

```text
n if !CONFIG_MULTITHREADING
y
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)。

<a id="CONFIG_RTIO_SYS_MEM_BLOCKS"></a>

## 419.15 `CONFIG_RTIO_SYS_MEM_BLOCKS`

**提示（Prompt）**：将系统内存块（System memory blocks）作为可选的读取后备内存池

**说明（Help）**

启用 `RTIO_DEFINE_WITH_MEMPOOL` 宏，使读取操作无需预先分配缓冲区即可入队。缓冲区改从关联 RTIO 上下文的已分配内存池（Memory pool）中取得。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
```

**被选择（Selected by）**

```text
CONFIG_ADC_STREAM
CONFIG_ADC_DEFAULT_RTIO
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`subsys/rtio/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_SYS_MEM_BLOCKS`](P199_lib_配置项参考_3.md#CONFIG_SYS_MEM_BLOCKS)、[`CONFIG_ADC_STREAM`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STREAM)、[`CONFIG_ADC_DEFAULT_RTIO`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_DEFAULT_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_RTIO_WORKQ"></a>

## 419.16 `CONFIG_RTIO_WORKQ`

**提示（Prompt）**：用于处理同步操作的 RTIO 工作队列服务（Work-queues service）

**说明（Help）**

启用 RTIO 工作队列（Work-queues），以异步、非阻塞（Asynchronous, non-blocking）的方式处理同步操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO
```

**主动选择（Selects）**

```text
CONFIG_RTIO_CONSUME_SEM
```

**被选择（Selected by）**

```text
CONFIG_ADC_DEFAULT_RTIO
CONFIG_I2C_RTIO
CONFIG_I3C_RTIO
CONFIG_SENSOR_ASYNC_API
CONFIG_ADXL345
CONFIG_ADXL355
CONFIG_ADXL362
CONFIG_ADXL372
CONFIG_MAX30009
CONFIG_AKM09918C
CONFIG_BMA4XX
CONFIG_BME280
CONFIG_AFBR_S50
CONFIG_SENSOR_DS3231
CONFIG_PAT9136
CONFIG_LIS2DUX12
CONFIG_LSM6DSV16X
CONFIG_VL53L5CX
CONFIG_ICM4268X
CONFIG_SPI_RTIO
```

**定义位置（Location）**：[`subsys/rtio/Kconfig.workq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig.workq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_RTIO_CONSUME_SEM`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_CONSUME_SEM)、[`CONFIG_ADC_DEFAULT_RTIO`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_DEFAULT_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADXL345`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345)、[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_MAX30009`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009)、[`CONFIG_AKM09918C`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AKM09918C)、[`CONFIG_BMA4XX`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA4XX)、[`CONFIG_BME280`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BME280)、[`CONFIG_AFBR_S50`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AFBR_S50)、[`CONFIG_SENSOR_DS3231`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_DS3231)、[`CONFIG_PAT9136`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAT9136)、[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_VL53L5CX`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VL53L5CX)、[`CONFIG_ICM4268X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)。

<a id="CONFIG_RTIO_WORKQ_POOL_ITEMS"></a>

## 419.17 `CONFIG_RTIO_WORKQ_POOL_ITEMS`

**提示（Prompt）**：供 RTIO 工作队列使用的工作项池（Work-item pool）

**说明（Help）**

根据应用需要配置工作项池（Work-item pool）；预期同时发出的请求越多，池就应越大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO_WORKQ && CONFIG_RTIO
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/rtio/Kconfig.workq:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig.workq#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 用于处理同步操作的 RTIO 工作队列服务（Work-queues service）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_WORKQ`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_WORKQ)、[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)。

<a id="CONFIG_RTIO_WORKQ_THREADS_POOL"></a>

## 419.18 `CONFIG_RTIO_WORKQ_THREADS_POOL`

**提示（Prompt）**：用于处理工作项（Work item）的线程数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO_WORKQ && CONFIG_RTIO
```

**默认值（Defaults）**

```text
2 if CONFIG_SPI_RTIO || CONFIG_I2C_RTIO || CONFIG_I3C_RTIO
1
```

**定义位置（Location）**：[`subsys/rtio/Kconfig.workq:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig.workq#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 用于处理同步操作的 RTIO 工作队列服务（Work-queues service）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_WORKQ`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_WORKQ)、[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)。

<a id="CONFIG_RTIO_WORKQ_THREADS_POOL_PRIO"></a>

## 419.19 `CONFIG_RTIO_WORKQ_THREADS_POOL_PRIO`

**提示（Prompt）**：RTIO 工作队列线程池（Workqueue thread pool）的优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO_WORKQ && CONFIG_RTIO
```

**默认值（Defaults）**

```text
CONFIG_MAIN_THREAD_PRIORITY
```

**定义位置（Location）**：[`subsys/rtio/Kconfig.workq:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig.workq#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 用于处理同步操作的 RTIO 工作队列服务（Work-queues service）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_WORKQ`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_WORKQ)、[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_MAIN_THREAD_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_MAIN_THREAD_PRIORITY)。

<a id="CONFIG_RTIO_WORKQ_THREADS_POOL_STACK_SIZE"></a>

## 419.20 `CONFIG_RTIO_WORKQ_THREADS_POOL_STACK_SIZE`

**提示（Prompt）**：RTIO 工作队列线程（Workqueue thread）的栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTIO_WORKQ && CONFIG_RTIO
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/rtio/Kconfig.workq:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/Kconfig.workq#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 用于处理同步操作的 RTIO 工作队列服务（Work-queues service）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_WORKQ`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_WORKQ)、[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)。

<!-- kconfig-navigation -->

[上一章](P418_subsys_retention_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P420_subsys_sd_配置项参考.md)
