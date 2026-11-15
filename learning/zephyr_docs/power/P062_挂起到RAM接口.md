---
id: learning.zephyr-docs.power.pmlow-1
title: 挂起到RAM接口
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第62章\_挂起到RAM接口

原文：[group__pm__s2ram](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html)。读取日期：2026-10-13，`latest`。

挂起到随机存取存储器（Suspend to RAM，S2RAM；RAM为Random Access Memory）接口使用头文件 `zephyr/arch/common/pm_s2ram.h`。

## 62.1\_关机函数类型

```c
typedef int (*pm_s2ram_system_off_fn_t)(void);
```

此关机函数作为参数传给 [`arch_pm_s2ram_suspend()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga6b82cf263c595b0d5cb353759000615c)，在中央处理器（Central Processing Unit，CPU）上下文（Context）保存后由它调用，以关闭系统。

系统成功关闭时，该函数不返回。如果操作无法完成，则返回合适的错误值；**返回之前，代码必须负责将系统恢复为完全可运行状态。**系统忙、暂时不能关机时返回 `-EBUSY`（Busy），其他错误返回相应负错误码 `-errno`。

## 62.2\_保存CPU上下文并挂起

```c
int arch_pm_s2ram_suspend(pm_s2ram_system_off_fn_t system_off);
```

执行S2RAM时，将CPU上下文保存到保持供电的RAM，然后使用 `system_off` 指定的函数关闭系统。通常由电源管理（Power Management，PM）子系统或钩子（Hook）调用。

CPU上下文通常是恢复时必须恢复的最小寄存器集合，使平台从挂起前停下的位置继续执行。

| 返回值 | 含义 |
| --- | --- |
| `0` | CPU上下文已成功保存并恢复 |
| `-EBUSY` | 系统忙，当前不能挂起 |
| 其他负错误码 | 操作失败 |

## 62.3\_设置挂起标记

```c
void pm_s2ram_mark_set(void);
```

标记核心正在进入S2RAM。在系统状态已保存到RAM、即将关机之前调用。

未启用 Kconfig 配置选项 `CONFIG_HAS_PM_S2RAM_CUSTOM_MARKING` 时，默认实现向RAM写入魔数（Magic Word）作为标记。

## 62.4\_检查并清除标记

```c
bool pm_s2ram_mark_check_and_clear(void);
```

检查S2RAM标记并清除其状态，用于决定执行挂起后的恢复流程，还是标准启动代码。

未启用 `CONFIG_HAS_PM_S2RAM_CUSTOM_MARKING` 时，默认实现检查RAM中的魔数。找到标记返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，表示应从S2RAM恢复；未找到返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)，表示执行标准启动。

---

[上一章：CPU电源管理接口](P061_CPU电源管理接口.md) · [下一章：系统关机接口](P063_系统关机接口.md) · [返回大纲](大纲.md)
