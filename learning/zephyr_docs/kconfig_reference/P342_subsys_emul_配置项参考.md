---
id: learning.zephyr-docs.kconfig-reference.page-342
title: "`subsys/emul`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第342章\_`subsys/emul`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/emul` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EMUL"></a>

## 342.1 `CONFIG_EMUL`

**提示（Prompt）**：仿真驱动（Emulation drivers）

**说明（Help）**

启用仿真驱动配置（Emulation Driver Configuration）。这些驱动模拟硬件设备，以支持各种子系统的测试。例如，可以为 I2C 罗盘编写仿真器（emulator），使其呈现在 I2C 总线上，并像真实硬件一样使用。

仿真器通常实现专用于测试的功能。例如，罗盘可在 I2C 总线速度过高时返回错误数据，或在校准尚未完成时返回无效测量值。这样便可测试上层代码是否正确处理这些情况。若模拟了所有故障条件，测试覆盖率（test coverage）就有可能接近 100%。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SENSOR_GENERIC_EMUL
```

**定义位置（Location）**：[`subsys/emul/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/emul/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_GENERIC_EMUL`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_GENERIC_EMUL)。

<a id="CONFIG_EMUL_ESPI_HOST"></a>

## 342.2 `CONFIG_EMUL_ESPI_HOST`

**提示（Prompt）**：仿真 eSPI 主机（host）

**说明（Help）**

这是通用 eSPI 主机的仿真器（emulator），支持基本主机操作，包括虚拟线（virtual wires）和向端口 80 写入数据，并可扩展。

注意：该仿真器不绑定特定的设备树（DT）节点，因此不使用 `DT_HAS_<compat>_ENABLED` 宏。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL
```

**定义位置（Location）**：[`subsys/emul/espi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/emul/espi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](P342_subsys_emul_配置项参考.md#CONFIG_EMUL)。

<a id="CONFIG_EMUL_ESPI_HOST_ACPI_SHM_REGION_SIZE"></a>

## 342.3 `CONFIG_EMUL_ESPI_HOST_ACPI_SHM_REGION_SIZE`

**提示（Prompt）**：仿真器共享内存的主机 I/O 外设端口大小

**说明（Help）**

此端口大小用于模拟主机（Host）与嵌入式控制器（EC）通过共享内存区域进行的通信，该区域返回 ACPI 响应数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION && CONFIG_EMUL_ESPI_HOST && CONFIG_EMUL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/emul/espi/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/emul/espi/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真 eSPI 主机（host）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)、[`CONFIG_EMUL_ESPI_HOST`](P342_subsys_emul_配置项参考.md#CONFIG_EMUL_ESPI_HOST)、[`CONFIG_EMUL`](P342_subsys_emul_配置项参考.md#CONFIG_EMUL)。

<a id="CONFIG_EMUL_INIT_PRIORITY"></a>

## 342.4 `CONFIG_EMUL_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

仿真设备驱动的初始化优先级（initialisation priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`subsys/emul/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/emul/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](P342_subsys_emul_配置项参考.md#CONFIG_EMUL)。

<!-- kconfig-navigation -->

[上一章](P341_subsys_dsp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P343_subsys_fb_配置项参考.md)
