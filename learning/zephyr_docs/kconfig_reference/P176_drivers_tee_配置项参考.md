---
id: learning.zephyr-docs.kconfig-reference.page-176
title: "`drivers/tee`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第176章\_`drivers/tee`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/tee` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OPTEE"></a>

## 176.1 `CONFIG_OPTEE`

**提示（Prompt）**：OP-TEE 驱动

**说明（Help）**

实现对作为 BL32 镜像加载的 OP-TEE 固件的支持。OP-TEE 是一种 TrustZone 操作系统（OS），依赖 ARM TrustZone 技术实现硬件隔离机制（Hardware Isolation）。驱动向 OP-TEE 请求功能，并实现 OP-TEE 运行服务所需的远程过程调用（RPC）机制。更多信息请参阅 [OP-TEE 官方网站](https://www.op-tee.org)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_ARM64 && CONFIG_ARMV8_A_NS && CONFIG_HAS_ARM_SMCCC) || CONFIG_ZTEST) && CONFIG_TEE
```

**定义位置（Location）**：[`drivers/tee/optee/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/tee/optee/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 可信环境驱动（Trusted Environment Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARMV8_A_NS`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A_NS)、[`CONFIG_HAS_ARM_SMCCC`](P031_arch_arm64_配置项参考.md#CONFIG_HAS_ARM_SMCCC)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_TEE`](P176_drivers_tee_配置项参考.md#CONFIG_TEE)。

<a id="CONFIG_OPTEE_MAX_NOTIF"></a>

## 176.2 `CONFIG_OPTEE_MAX_NOTIF`

**提示（Prompt）**：OP-TEE 通知（Notifications）的最大数量

**说明（Help）**

设置 OP-TEE 向普通世界（Normal World）发送通知的最大数量。OP-TEE 使用此机制进行同步（Synchronization）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPTEE && CONFIG_TEE
```

**默认值（Defaults）**

```text
255
```

**定义位置（Location）**：[`drivers/tee/optee/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/tee/optee/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 可信环境驱动（Trusted Environment Drivers） → OP-TEE 驱动

**配置项引用（Symbol References）**：[`CONFIG_OPTEE`](P176_drivers_tee_配置项参考.md#CONFIG_OPTEE)、[`CONFIG_TEE`](P176_drivers_tee_配置项参考.md#CONFIG_TEE)。

<a id="CONFIG_TEE"></a>

## 176.3 `CONFIG_TEE`

**提示（Prompt）**：可信环境驱动（Trusted Environment Drivers）

**说明（Help）**

在系统配置中包含可信执行环境（TEE）驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/tee/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/tee/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<!-- kconfig-navigation -->

[上一章](P175_drivers_syscon_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P177_drivers_timeaware_gpio_配置项参考.md)
