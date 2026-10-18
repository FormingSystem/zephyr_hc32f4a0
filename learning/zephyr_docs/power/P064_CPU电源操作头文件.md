---
id: learning.zephyr-docs.power.pmheader-0
title: CPU电源操作头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第64章\_CPU电源操作头文件

原文：[pm__cpu__ops_8h](https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/pm_cpu_ops.h`：中央处理器（Central Processing Unit，CPU）电源管理（Power Management，PM）的公共应用程序编程接口（Application Programming Interface，API）。

## 64.1\_包含关系与源文件

```c
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
```

[查看官方源码](https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h_source.html)。

## 64.2\_类型与宏

复位类型常量如下，均用作 [`pm_system_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#ga65dfe4b0c47af092c50c0022227ac8eb) 的参数：

```c
#define SYS_WARM_RESET 0
#define SYS_COLD_RESET 1
```

[`SYS_WARM_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h.html#a98f079e56ab5b320bb52e1ebaa873d9b) 表示系统热复位（Warm Reset），[`SYS_COLD_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h.html#a92747266cafef3783fcfb550e08ce132) 表示系统冷复位（Cold Reset）。

## 64.3\_函数声明与用途

```c
int pm_cpu_off (void);
int pm_cpu_on (unsigned long cpuid, uintptr_t entry_point);
int pm_system_reset (unsigned char reset);
```

| 函数 | 原页用途 |
| --- | --- |
| [`pm_cpu_off()`](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#gaa6de91e837b262f432b4a80ef5e2b781) | 关闭调用核心。 |
| [`pm_cpu_on()`](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#ga68c37acfc53eee990c34398ca0f1a3f5) | 为核心上电。 |
| [`pm_system_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#ga65dfe4b0c47af092c50c0022227ac8eb) | 执行系统复位。 |

参数、返回值和调用约束见[对应接口说明](P061_CPU电源管理接口.md)。

---

[上一章：系统关机接口](P063_系统关机接口.md) · [下一章：挂起到RAM头文件](P065_挂起到RAM头文件.md) · [返回大纲](大纲.md)
