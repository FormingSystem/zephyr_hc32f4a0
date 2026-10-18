---
id: learning.zephyr-docs.kconfig-reference.page-251
title: "`modules/trusted-firmware-a`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第251章\_`modules/trusted-firmware-a`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/trusted-firmware-a` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUILD_WITH_TFA"></a>

## 251.1 `CONFIG_BUILD_WITH_TFA`

**提示（Prompt）**：构建时使用 TF-A 作为安全执行环境（Secure Execution Environment）

**说明（Help）**

启用后，此选项指示 Zephyr 构建过程在生成 Zephyr 镜像的同时，额外生成用于安全执行环境（Secure Execution Environment）的 TF-A 镜像。Zephyr 镜像本身将在非安全处理环境（Non-Secure Processing Environment）中执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/trusted-firmware-a/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-a/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-a（模块路径 `modules/tee/tf-a/trusted-firmware-a`，相对于 west 工作区顶层目录）

<a id="CONFIG_TFA_BUILD_FIP"></a>

## 251.2 `CONFIG_TFA_BUILD_FIP`

**提示（Prompt）**：生成固件镜像包（Firmware Image Package，FIP）

**说明（Help）**

生成包含全部启动阶段（boot stage）的 ARM 固件镜像包（Firmware Image Package，FIP）。使用 FIP 的平台应在开发板 defconfig 中显式启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFA
```

**定义位置（Location）**：[`modules/trusted-firmware-a/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-a/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-a（模块路径 `modules/tee/tf-a/trusted-firmware-a`，相对于 west 工作区顶层目录） → 构建时使用 TF-A 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFA`](P251_modules_trusted-firmware-a_配置项参考.md#CONFIG_BUILD_WITH_TFA)。

<a id="CONFIG_TFA_FIP_USE_BL33_ZEPHYR"></a>

## 251.3 `CONFIG_TFA_FIP_USE_BL33_ZEPHYR`

**提示（Prompt）**：生成 TF-A FIP 时将 Zephyr 作为 BL33 包含（Include Zephyr as BL33）

**说明（Help）**

在 TF-A FIP 构建中，将 Zephyr 二进制文件作为 BL33 传入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFA_BUILD_FIP && CONFIG_BUILD_WITH_TFA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-a/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-a/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-a（模块路径 `modules/tee/tf-a/trusted-firmware-a`，相对于 west 工作区顶层目录） → 构建时使用 TF-A 作为安全执行环境（Secure Execution Environment） → 生成固件镜像包（Firmware Image Package，FIP）

**配置项引用（Symbol References）**：[`CONFIG_TFA_BUILD_FIP`](P251_modules_trusted-firmware-a_配置项参考.md#CONFIG_TFA_BUILD_FIP)、[`CONFIG_BUILD_WITH_TFA`](P251_modules_trusted-firmware-a_配置项参考.md#CONFIG_BUILD_WITH_TFA)。

<a id="CONFIG_TFA_MAKE_BUILD_TYPE_DEBUG"></a>

## 251.4 `CONFIG_TFA_MAKE_BUILD_TYPE_DEBUG`

**提示（Prompt）**：调试构建（Debug build）

**说明（Help）**

启用后，TF-A 的构建类型为调试（debug）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFA
```

**定义位置（Location）**：[`modules/trusted-firmware-a/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-a/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-a（模块路径 `modules/tee/tf-a/trusted-firmware-a`，相对于 west 工作区顶层目录） → 构建时使用 TF-A 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFA`](P251_modules_trusted-firmware-a_配置项参考.md#CONFIG_BUILD_WITH_TFA)。

<a id="CONFIG_TFA_PLATFORM"></a>

## 251.5 `CONFIG_TFA_PLATFORM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

TF-A 构建系统使用的平台名称（platform name），即 `PLAT=` 参数。开发板应在其 `Kconfig.defconfig` 文件中设置此值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFA
```

**定义位置（Location）**：[`modules/trusted-firmware-a/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-a/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-a（模块路径 `modules/tee/tf-a/trusted-firmware-a`，相对于 west 工作区顶层目录） → 构建时使用 TF-A 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFA`](P251_modules_trusted-firmware-a_配置项参考.md#CONFIG_BUILD_WITH_TFA)。

<!-- kconfig-navigation -->

[上一章](P250_modules_tflite-micro_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P252_modules_trusted-firmware-m_配置项参考.md)
