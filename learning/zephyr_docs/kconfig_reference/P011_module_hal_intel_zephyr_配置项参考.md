---
id: learning.zephyr-docs.kconfig-reference.page-11
title: "`<module:hal_intel>/zephyr`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第11章\_`<module:hal_intel>/zephyr`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:hal_intel>/zephyr` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LOG_BACKEND_I2C"></a>

## 11.1 `CONFIG_LOG_BACKEND_I2C`

**提示（Prompt）**：启用 I2C 日志后端（Log Backend）

**说明（Help）**

启用后，后端（Backend）将使用 I2C 记录日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SEDI && CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && CONFIG_INTEL_HAL
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：`<module:hal_intel>/zephyr/subsys/logging/backends/Kconfig.i2c:9`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration）

**配置项引用（Symbol References）**：[`CONFIG_I2C_SEDI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_SEDI)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_INTEL_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_HAL)、[`CONFIG_LOG_OUTPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_I2C_AUTOSTART"></a>

## 11.2 `CONFIG_LOG_BACKEND_I2C_AUTOSTART`

**提示（Prompt）**：自动启动 I2C 后端（Backend）

**说明（Help）**

启用后，应用程序启动时会自动启动 I2C 日志后端（Logging Backend）。禁用后，应用程序需要使用 `log_backend_enable()` 手动启动后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_I2C && CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && CONFIG_INTEL_HAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_intel>/zephyr/subsys/logging/backends/Kconfig.i2c:18`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C`](P011_module_hal_intel_zephyr_配置项参考.md#CONFIG_LOG_BACKEND_I2C)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_INTEL_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_HAL)。

<a id="CONFIG_LOG_I2C_DEV_ADDR"></a>

## 11.3 `CONFIG_LOG_I2C_DEV_ADDR`

**提示（Prompt）**：I2C 日志设备的 I2C 地址（Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_I2C && CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && CONFIG_INTEL_HAL
```

**默认值（Defaults）**

```text
0x5E
```

**定义位置（Location）**：`<module:hal_intel>/zephyr/subsys/logging/backends/Kconfig.i2c:34`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C`](P011_module_hal_intel_zephyr_配置项参考.md#CONFIG_LOG_BACKEND_I2C)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_INTEL_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_HAL)。

<a id="CONFIG_LOG_I2C_MAX_MSG_LEN"></a>

## 11.4 `CONFIG_LOG_I2C_MAX_MSG_LEN`

**提示（Prompt）**：最大消息长度（Maximum Message Length）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_I2C && CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && CONFIG_INTEL_HAL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：`<module:hal_intel>/zephyr/subsys/logging/backends/Kconfig.i2c:30`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C`](P011_module_hal_intel_zephyr_配置项参考.md#CONFIG_LOG_BACKEND_I2C)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_INTEL_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_HAL)。

<!-- kconfig-navigation -->

[上一章](P010_module_hal_espressif_zephyr_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P012_module_hal_nxp_mcux_配置项参考.md)
