---
id: learning.zephyr-docs.power.pmheader-1
title: 挂起到RAM头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pm__s2ram_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第65章\_挂起到RAM头文件

原文：[pm__s2ram_8h](https://docs.zephyrproject.org/latest/doxygen/html/pm__s2ram_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/arch/common/pm_s2ram.h`：挂起到随机存取存储器（Suspend to RAM，S2RAM；RAM为Random Access Memory）的公共应用程序编程接口（Application Programming Interface，API）。CPU表示中央处理器（Central Processing Unit）。

## 65.1\_包含关系与源文件

原页未列出头文件包含项。

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/pm__s2ram_8h_source.html)。

## 65.2\_类型与宏

关机函数类型（System Off Function）：

```c
typedef int (*pm_s2ram_system_off_fn_t)(void);
```

## 65.3\_函数声明与用途

```c
int arch_pm_s2ram_suspend (pm_s2ram_system_off_fn_t system_off);
void pm_s2ram_mark_set (void);
bool pm_s2ram_mark_check_and_clear (void);
```

| 函数 | 原页用途 |
| --- | --- |
| [`arch_pm_s2ram_suspend()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga6b82cf263c595b0d5cb353759000615c) | 挂起时保存CPU上下文。 |
| [`pm_s2ram_mark_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga88bb5cb4d2eb2c6014f0bad0e891ae1f) | 标记核心正在进入挂起到RAM状态。 |
| [`pm_s2ram_mark_check_and_clear()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga93f351a7dafa34ccdffd7e97763ab34b) | 检查挂起到RAM标记并清除它。 |

参数、返回值和调用约束见[对应接口说明](P062_挂起到RAM接口.md)。

---

[上一章：CPU电源操作头文件](P064_CPU电源操作头文件.md) · [下一章：系统关机头文件](P066_系统关机头文件.md) · [返回大纲](大纲.md)
