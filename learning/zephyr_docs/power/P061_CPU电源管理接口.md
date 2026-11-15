---
id: learning.zephyr-docs.power.pmlow-0
title: CPU电源管理接口
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第61章\_CPU电源管理接口

原文：[group__power__management__cpu__api](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html)。读取日期：2026-10-13，`latest`。

中央处理器（Central Processing Unit，CPU）电源管理（Power Management，PM）接口自 Zephyr 2.6 提供，版本0.8.0。使用头文件 `zephyr/drivers/pm_cpu_ops.h`；原页另列出ARM电源状态协调接口（Power State Coordination Interface，PSCI）专用头文件 [psci.h](P072_Arm电源状态协调接口头文件.md)。

## 61.1\_关闭当前核心

```c
int pm_cpu_off(void);
```

关闭调用本函数的核心，面向处理器热插拔（CPU Hotplug）场景。由 `cpu_off` 关闭的核心，只能响应 `cpu_on` 再次上电。

**成功时不返回。**操作不受支持时返回 `-ENOTSUP`（Not Supported）。

## 61.2\_开启核心

```c
int pm_cpu_on(unsigned long cpuid, uintptr_t entry_point);
```

为尚未启动进入调用方监督软件（Supervisory Software）的核心上电，或重新开启先前通过 `cpu_off` 关闭的核心。

| 参数 | 含义 |
| --- | --- |
| `cpuid` | 要开启的CPU标识 |
| `entry_point` | 核心开始执行的入口地址（Entry Point） |

成功返回 `0`，失败返回负错误码（Errno）；不支持操作时返回 `-ENOTSUP`。

## 61.3\_系统复位

```c
int pm_system_reset(unsigned char reset);
```

执行系统冷复位（Cold Reset）或热复位（Warm Reset）。参数 `reset` 指定复位类型。原页规定成功返回 `0`，失败返回负错误码。

复位类型常量见[CPU电源操作头文件](P064_CPU电源操作头文件.md)。

---

[上一章：STM32唤醒引脚示例](P060_STM32唤醒引脚示例.md) · [下一章：挂起到RAM接口](P062_挂起到RAM接口.md) · [返回大纲](大纲.md)
