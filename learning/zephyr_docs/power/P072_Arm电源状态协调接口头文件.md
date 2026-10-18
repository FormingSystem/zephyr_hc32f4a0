---
id: learning.zephyr-docs.power.pmrest-1
title: Arm电源状态协调接口头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第72章\_Arm电源状态协调接口头文件

原文：[psci_8h](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/pm_cpu_ops/psci.h` 提供 Arm **电源状态协调接口（Power State Coordination Interface，PSCI）**专用的应用程序编程接口（Application Programming Interface，API），用于中央处理器（Central Processing Unit，CPU）的电源管理（Power Management）。

## 72.1\_包含关系与源文件

```c
#include <zephyr/types.h>
#include <zephyr/arch/arm64/arm-smccc.h>
#include <stddef.h>
#include <zephyr/device.h>
```

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h_source.html)。

## 72.2\_版本字段宏

`PSCI_VERSION_MAJOR(ver)` 从PSCI版本值中提取主版本（Major Version）字段。参数 `ver` 是PSCI版本值；宏值为：

```c
(((ver) & PSCI_VERSION_MAJOR_MASK) >> PSCI_VERSION_MAJOR_SHIFT)
```

`PSCI_VERSION_MINOR(ver)` 从PSCI版本值中提取次版本（Minor Version）字段。参数 `ver` 同样是PSCI版本值；宏值为：

```c
((ver) & PSCI_VERSION_MINOR_MASK)
```

## 72.3\_挂起CPU

```c
int psci_cpu_suspend(uint32_t state, uintptr_t entry_point);
```

[`psci_cpu_suspend()`](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html#ac41b706f3b75f2c42689e5c57908903c) 用于发起PSCI的 `CPU_SUSPEND` 调用；原文将其描述为PSCI安全监控调用（Secure Monitor Call，SMC）接口。

| 参数 | 中文说明 |
| --- | --- |
| [`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) | CPU电源状态 |
| `entry_point` | 从挂起状态返回时的入口地址 |

成功进入挂起返回 `0`，其他返回值表示失败。原页未进一步列出失败码。

## 72.4\_查询固件版本

```c
uint32_t psci_version(void);
```

[`psci_version()`](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html#a1964266f31f19eb7e7e0acd4bb660f4c) 返回检测到的PSCI固件版本：**高16位是主版本，低16位是次版本**。使用前述 [`PSCI_VERSION_MAJOR()`](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html#a1e6404a2f880eccc43566b399c1aded7) 和 [`PSCI_VERSION_MINOR()`](https://docs.zephyrproject.org/latest/doxygen/html/psci_8h.html#affdc7b10fe33298091cfbfbd4ef290b0) 解码相应字段。

---

[上一章：电源状态头文件](P071_电源状态头文件.md) · [下一章：稳压器接口](P073_稳压器接口.md) · [返回大纲](大纲.md)
