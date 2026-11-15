---
id: learning.zephyr-docs.kconfig-reference.page-73
title: "`drivers/dai`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第73章\_`drivers/dai`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/dai` 的 27 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DAI"></a>

## 73.1 `CONFIG_DAI`

**提示（Prompt）**：数字音频接口（Digital Audio Interface，DAI）驱动

**说明（Help）**

启用数字音频接口（DAI）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/dai/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_DAI_ALH_HAS_OWNERSHIP"></a>

## 73.2 `CONFIG_DAI_ALH_HAS_OWNERSHIP`

**提示（Prompt）**：Intel ALH 驱动仅在 ACE 1.5 上具有所有权（Ownership）

**说明（Help）**

选择此项，启用对硬件所有权（HW Ownership）的编程设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ACE15_MTPM && CONFIG_DAI_INTEL_ALH && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dai/intel/alh/Kconfig.alh:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/alh/Kconfig.alh#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel ALH 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_ACE15_MTPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACE15_MTPM)、[`CONFIG_DAI_INTEL_ALH`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_ALH)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_AMD_SDW"></a>

## 73.3 `CONFIG_DAI_AMD_SDW`

**提示（Prompt）**：AMD SoundWire DAI 驱动

**说明（Help）**

选择此项，启用 AMD SoundWire DAI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI && DT_HAS_AMD_ACP_SDW_DAI_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dai/amd/sdw/Kconfig.acp_sdw_dai:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/amd/sdw/Kconfig.acp_sdw_dai#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_AMD_TDM"></a>

## 73.4 `CONFIG_DAI_AMD_TDM`

**提示（Prompt）**：AMD TDM DAI 驱动

**说明（Help）**

启用统一的时分复用（Time Division Multiplexing，TDM）DAI 驱动。该驱动处理全部三个 TDM 实例：TDM0（耳麦，Headset）、TDM1（SP）和 TDM2（蓝牙，Bluetooth）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMD_TDM_DAI_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dai/amd/tdm/Kconfig.acp_tdm_dai:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/amd/tdm/Kconfig.acp_tdm_dai#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_DMIC_HAS_MULTIPLE_LINE_SYNC"></a>

## 73.5 `CONFIG_DAI_DMIC_HAS_MULTIPLE_LINE_SYNC`

**提示（Prompt）**：对多条线路使用 DMIC 同步（Sync）

**说明（Help）**

这是 ACE1.5 硬件引入的一项功能；使用数字麦克风（DMIC）之前，必须设置 DMIC 同步寄存器（Sync Registers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_DMIC && CONFIG_DAI
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_DMIC`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_DMIC)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_DMIC_HAS_OWNERSHIP"></a>

## 73.6 `CONFIG_DAI_DMIC_HAS_OWNERSHIP`

**提示（Prompt）**：使用 DMIC 所有权申请与释放（Ownership Claim/Release）

**说明（Help）**

这是 ACE1.5 硬件引入的一项功能；使用数字麦克风（DMIC）之前，必须取得 DMIC 的所有权（Ownership）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_DMIC && CONFIG_DAI
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_DMIC`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_DMIC)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_DMIC_HW_CONTROLLERS"></a>

## 73.7 `CONFIG_DAI_DMIC_HW_CONTROLLERS`

**提示（Prompt）**：系统中的硬件控制器（Hardware Controller）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_DMIC && CONFIG_DAI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_DMIC`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_DMIC)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_DMIC_HW_FIFOS"></a>

## 73.8 `CONFIG_DAI_DMIC_HW_FIFOS`

**提示（Prompt）**：DMIC 控制器中的流 FIFO（Stream FIFO）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_DMIC && CONFIG_DAI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_DMIC`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_DMIC)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_DMIC_HW_IOCLK"></a>

## 73.9 `CONFIG_DAI_DMIC_HW_IOCLK`

**提示（Prompt）**：DMIC 的 I/O 时钟（IO Clock）数值

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_DMIC && CONFIG_DAI
```

**默认值（Defaults）**

```text
19200000
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_DMIC`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_DMIC)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_DMIC_PLATFORM_SYNC_PERIOD"></a>

## 73.10 `CONFIG_DAI_DMIC_PLATFORM_SYNC_PERIOD`

**提示（Prompt）**：各平台的同步周期（Sync Period）

**说明（Help）**

DMIC 同步周期（Sync Period）用于以下计算：

```text
CONFIG_DAI_DMIC_HW_IOCLK / CONFIG_DAI_DMIC_PLATFORM_SYNC_PERIOD
```

规范中的例子：对于 19.2 MHz 晶体振荡器（XTAL Oscillator）时钟和 4 kHz 同步周期，需要编程写入的值为 4799（12BFh）。

> 译注：原文将以 kHz 表示的量称为“sync period”，此处保留原用语及计算例，不自行改动其配置含义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_DMIC && CONFIG_DAI
```

**默认值（Defaults）**

```text
4000
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_DMIC`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_DMIC)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_INIT_PRIORITY"></a>

## 73.11 `CONFIG_DAI_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/dai/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_INTEL_ALH"></a>

## 73.12 `CONFIG_DAI_INTEL_ALH`

**提示（Prompt）**：用于 DAI 接口的 Intel ALH 驱动

**说明（Help）**

选择此项，启用 Intel ALH 驱动。ALH 是一种中间设备（Intermediary Device），充当集线器（Hub），为多种声音接口（例如 SoundWire）提供抽象支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ALH_DAI_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dai/intel/alh/Kconfig.alh:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/alh/Kconfig.alh#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_DAI_INTEL_DMIC"></a>

## 73.13 `CONFIG_DAI_INTEL_DMIC`

**提示（Prompt）**：用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持

**说明（Help）**

启用用于 DAI 接口的 Intel 数字脉冲密度调制（Pulse Density Modulation，PDM）麦克风驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_DAI_DMIC_ENABLED && CONFIG_PM_DEVICE_RUNTIME && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_INTEL_DMIC_NHLT"></a>

## 73.14 `CONFIG_DAI_INTEL_DMIC_NHLT`

**提示（Prompt）**：使用 NHLT DMIC 二进制配置块（Blob）

**说明（Help）**

所有寄存器配置均从二进制配置块（Blob）读取。通道数、采样率（Sample Rate）和脉冲编码调制（PCM）格式都在配置块中定义，运行时不作配置选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持 → 驱动工作模式（Operation Mode）

<a id="CONFIG_DAI_INTEL_DMIC_TPLG_PARAMS"></a>

## 73.15 `CONFIG_DAI_INTEL_DMIC_TPLG_PARAMS`

**提示（Prompt）**：使用拓扑（Topology）中的参数——开发中（WIP）

**说明（Help）**

根据使用场景、麦克风数据手册参数以及拓扑（Topology）定义的 PCM 格式，动态计算全部寄存器配置。这些参数便于在拓扑中定制。此功能仍在开发中（Work in Progress），尚未在驱动中启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dai/intel/dmic/Kconfig.dmic:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/dmic/Kconfig.dmic#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel 数字 PDM 麦克风驱动支持 → 驱动工作模式（Operation Mode）

<a id="CONFIG_DAI_INTEL_HDA"></a>

## 73.16 `CONFIG_DAI_INTEL_HDA`

**提示（Prompt）**：用于 DAI 接口的 Intel HDA 驱动

**说明（Help）**

选择此项，启用 Intel HDA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_HDA_DAI_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dai/intel/hda/Kconfig.hda:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/hda/Kconfig.hda#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_DAI_INTEL_SSP"></a>

## 73.17 `CONFIG_DAI_INTEL_SSP`

**提示（Prompt）**：用于 DAI 接口的 Intel I2S（SSP）总线驱动

**说明（Help）**

启用基于同步串行端口（Synchronous Serial Port，SSP）模块的 I2S 总线驱动；原文将 I2S 展开为 Inter Sound。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SSP_DAI_ENABLED && CONFIG_PM_DEVICE_RUNTIME && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dai/intel/ssp/Kconfig.ssp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/ssp/Kconfig.ssp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_DAI_INTEL_UAOL"></a>

## 73.18 `CONFIG_DAI_INTEL_UAOL`

**提示（Prompt）**：用于 DAI 接口的 Intel USB 音频卸载链路（USB Audio Offload Link，UAOL）驱动支持

**说明（Help）**

启用用于 DAI 接口的 Intel USB 音频卸载链路（USB Audio Offload Link，UAOL）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UAOL && DT_HAS_INTEL_UAOL_DAI_ENABLED && CONFIG_PM_DEVICE_RUNTIME && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dai/intel/uaol/Kconfig.uaol:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/uaol/Kconfig.uaol#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_UAOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UAOL)、[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_MAX_BESPOKE_CFG_SIZE"></a>

## 73.19 `CONFIG_DAI_MAX_BESPOKE_CFG_SIZE`

**提示（Prompt）**：专用配置块（Bespoke Configuration Blob）的最大大小

**说明（Help）**

通过系统调用（Syscall）传给 DAI 驱动的专用配置对象（Bespoke Configuration Object）的最大大小。这些对象会从用户空间（User Space）复制到内核内存进行验证。较小的对象在栈（Stack）上验证；较大的对象复制到临时分配的堆（Heap）内存中，因此此上限不受可用栈大小约束。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_USERSPACE && CONFIG_DAI
```

**默认值（Defaults）**

```text
8192
```

**取值范围（Ranges）**

```text
[256, 65536]
```

**定义位置（Location）**：[`drivers/dai/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → DAI 用户空间（User Space）支持

**配置项引用（Symbol References）**：[`CONFIG_DAI_USERSPACE`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_USERSPACE)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_DAI_NXP_ESAI"></a>

## 73.20 `CONFIG_DAI_NXP_ESAI`

**提示（Prompt）**：NXP 增强型串行音频接口（Enhanced Serial Audio Interface，ESAI）驱动

**说明（Help）**

选择此项，启用 NXP ESAI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DAI_ESAI_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dai/nxp/esai/Kconfig.esai:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/esai/Kconfig.esai#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAI_NXP_MICFIL"></a>

## 73.21 `CONFIG_DAI_NXP_MICFIL`

**提示（Prompt）**：NXP 脉冲密度调制麦克风接口（Pulse Density Modulation Microphone Interface，MICFIL）驱动

**说明（Help）**

选择此项，启用 NXP PDM MICFIL 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DAI_MICFIL_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dai/nxp/micfil/Kconfig.micfil:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/micfil/Kconfig.micfil#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAI_NXP_SAI"></a>

## 73.22 `CONFIG_DAI_NXP_SAI`

**提示（Prompt）**：NXP 同步音频接口（Synchronous Audio Interface，SAI）驱动

**说明（Help）**

选择此项，启用 NXP SAI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DAI_SAI_ENABLED && CONFIG_DAI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dai/nxp/sai/Kconfig.sai:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/sai/Kconfig.sai#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAI_SSP_HAS_POWER_CONTROL"></a>

## 73.23 `CONFIG_DAI_SSP_HAS_POWER_CONTROL`

**提示（Prompt）**：DAI SSP 通过运行时电源管理（pm_runtime）启用或禁用 SSP 电源

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_INTEL_SSP && CONFIG_DAI
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`drivers/dai/intel/ssp/Kconfig.ssp:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/intel/ssp/Kconfig.ssp#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 用于 DAI 接口的 Intel I2S（SSP）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI_INTEL_SSP`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_SSP)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

<a id="CONFIG_DAI_USERSPACE"></a>

## 73.24 `CONFIG_DAI_USERSPACE`

**提示（Prompt）**：DAI 用户空间（User Space）支持

**说明（Help）**

通过系统调用（Syscall）向用户空间线程（User-Space Thread）开放 DAI 接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_DAI
```

**定义位置（Location）**：[`drivers/dai/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_SAI_FIFO_WORD_SIZE"></a>

## 73.25 `CONFIG_SAI_FIFO_WORD_SIZE`

**提示（Prompt）**：FIFO 字（Word）的大小，以字节为单位

**说明（Help）**

用于设置 SAI FIFO 字（Word）的大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_NXP_SAI && CONFIG_DAI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/dai/nxp/sai/Kconfig.sai:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/sai/Kconfig.sai#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → NXP 同步音频接口（Synchronous Audio Interface，SAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI_NXP_SAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_NXP_SAI)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_SAI_HAS_MCLK_CONFIG_OPTION"></a>

## 73.26 `CONFIG_SAI_HAS_MCLK_CONFIG_OPTION`

**提示（Prompt）**：SAI 具备主时钟（MCLK）配置选项时设置此项

**说明（Help）**

如果 SAI IP 支持配置主时钟（Master Clock），则选择此项。主时钟配置包括启用或禁用主时钟、将信号设为输入或输出，以及对主时钟输出分频。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_NXP_SAI && CONFIG_DAI
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/dai/nxp/sai/Kconfig.sai:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/sai/Kconfig.sai#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → NXP 同步音频接口（Synchronous Audio Interface，SAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI_NXP_SAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_NXP_SAI)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<a id="CONFIG_SAI_IMX93_ERRATA_051421"></a>

## 73.27 `CONFIG_SAI_IMX93_ERRATA_051421`

**提示（Prompt）**：SAI IP 版本受 i.MX93 勘误（ERRATA）051421 影响时设置此项

**说明（Help）**

如果所用 SAI IP 版本受 i.MX93 勘误（ERRATA）051421 影响，则选择此项。该勘误说明：当 SAI 是帧同步/位时钟（FSYNC/BCLK）主设备，一个传输方向与另一个方向同步（SYNC），并且异步（ASYNC）方向的 BYP 位发生切换时，同步方向的 BCLK 无法正确生成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAI_NXP_SAI && CONFIG_DAI
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/dai/nxp/sai/Kconfig.sai:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/sai/Kconfig.sai#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → NXP 同步音频接口（Synchronous Audio Interface，SAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAI_NXP_SAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_NXP_SAI)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)。

<!-- kconfig-navigation -->

[上一章](P072_drivers_dac_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P074_drivers_dali_配置项参考.md)
