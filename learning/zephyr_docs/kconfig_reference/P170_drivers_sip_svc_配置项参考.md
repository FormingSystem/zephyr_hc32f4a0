---
id: learning.zephyr-docs.kconfig-reference.page-170
title: "`drivers/sip_svc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第170章\_`drivers/sip_svc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/sip_svc` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARM_SIP_SVC_DRIVER"></a>

## 170.1 `CONFIG_ARM_SIP_SVC_DRIVER`

**提示（Prompt）**：ARM SiP 服务调用（SIP SVC）驱动

**说明（Help）**

ARM 监督调用（Supervisory Call）驱动，用于与异常级别 EL2 或 EL3 的固件通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**定义位置（Location）**：[`drivers/sip_svc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sip_svc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_INIT_PRIORITY"></a>

## 170.2 `CONFIG_ARM_SIP_SVC_DRIVER_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_DRIVER
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/sip_svc/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sip_svc/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_DRIVER)。

<a id="CONFIG_ARM_SIP_SVC_EL3_MAILBOX_RESPONSE_SIZE"></a>

## 170.3 `CONFIG_ARM_SIP_SVC_EL3_MAILBOX_RESPONSE_SIZE`

**提示（Prompt）**：异步（ASYNC）事务使用的响应缓冲区大小

**说明（Help）**

异步（ASYNC）事务使用的响应缓冲区大小。对于 Intel Agilex 平台，响应缓冲区最大为 4096 字节，最小为 4 字节，而且必须是 4 字节的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO && CONFIG_ARM_SIP_SVC_DRIVER
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/sip_svc/Kconfig.sip_smc_agilex:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sip_svc/Kconfig.sip_smc_agilex#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO)、[`CONFIG_ARM_SIP_SVC_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_DRIVER)。

<a id="CONFIG_ARM_SIP_SVC_EL3_MAX_ALLOWED_TRANSACTIONS"></a>

## 170.4 `CONFIG_ARM_SIP_SVC_EL3_MAX_ALLOWED_TRANSACTIONS`

**提示（Prompt）**：允许同时进行的最大事务数

**说明（Help）**

此驱动在 `sip_svc` 子系统中允许的活动事务（Active Transaction）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO && CONFIG_ARM_SIP_SVC_DRIVER
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/sip_svc/Kconfig.sip_smc_agilex:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sip_svc/Kconfig.sip_smc_agilex#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO)、[`CONFIG_ARM_SIP_SVC_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_DRIVER)。

<a id="CONFIG_ARM_SIP_SVC_HAS_DRIVER"></a>

## 170.5 `CONFIG_ARM_SIP_SVC_HAS_DRIVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

各个 SiP 服务调用（SiP SVC）驱动启用此选项，以表明存在 SiP SVC 驱动。其他依赖 SiP SVC 驱动的模块使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_DRIVER
```

**被弱选择（Implied by）**

```text
CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO
```

**定义位置（Location）**：[`drivers/sip_svc/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sip_svc/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_DRIVER)、[`CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO)。

<a id="CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO"></a>

## 170.6 `CONFIG_ARM_SIP_SVC_HAS_INTEL_SDM_MAILBOX_FIFO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过安全监控调用（SMC），支持 Intel SoC FPGA Agilex 中的 SDM 邮箱 FIFO（Mailbox FIFO）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SOCFPGA_AGILEX_SIP_SMC_ENABLED && CONFIG_ARM_SIP_SVC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_ARM_SIP_SVC_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/sip_svc/Kconfig.sip_smc_agilex:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sip_svc/Kconfig.sip_smc_agilex#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_DRIVER)、[`CONFIG_ARM_SIP_SVC_HAS_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_HAS_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P169_drivers_serial_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P171_drivers_smbus_配置项参考.md)
