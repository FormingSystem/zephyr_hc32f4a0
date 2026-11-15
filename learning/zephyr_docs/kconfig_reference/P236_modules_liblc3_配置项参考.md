---
id: learning.zephyr-docs.kconfig-reference.page-236
title: "`modules/liblc3`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第236章\_`modules/liblc3`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/liblc3` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LIBLC3"></a>

## 236.1 `CONFIG_LIBLC3`

**提示（Prompt）**：liblc3 支持（Support）

**说明（Help）**

启用低复杂度通信编解码器（Low Complexity Communication Codec，LC3）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU
```

**主动选择（Selects）**

```text
CONFIG_REQUIRES_FULL_LIBC
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y if CONFIG_BT_NXP_NW612 && CONFIG_BT_AUDIO && CONFIG_FPU
```

**定义位置（Location）**：[`modules/liblc3/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/liblc3/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → liblc3（模块路径 `modules/lib/liblc3`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_REQUIRES_FULL_LIBC`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FULL_LIBC)、[`CONFIG_BT_NXP_NW612`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP_NW612)、[`CONFIG_BT_AUDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO)。

<a id="CONFIG_LIBLC3_PLUS"></a>

## 236.2 `CONFIG_LIBLC3_PLUS`

**提示（Prompt）**：LC3plus 支持［实验性，EXPERIMENTAL］

**说明（Help）**

启用 2.5 ms 和 5 ms 帧时长（frame durations）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/liblc3/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/liblc3/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → liblc3（模块路径 `modules/lib/liblc3`，相对于 west 工作区顶层目录） → liblc3 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LIBLC3_PLUS_HR"></a>

## 236.3 `CONFIG_LIBLC3_PLUS_HR`

**提示（Prompt）**：LC3plus 高分辨率支持（High Resolution Support）［实验性，EXPERIMENTAL］

**说明（Help）**

启用高分辨率模式（High-Resolution mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBLC3
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/liblc3/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/liblc3/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → liblc3（模块路径 `modules/lib/liblc3`，相对于 west 工作区顶层目录） → liblc3 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<!-- kconfig-navigation -->

[上一章](P235_modules_hostap_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P237_modules_libsbc_配置项参考.md)
