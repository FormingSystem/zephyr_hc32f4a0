---
id: learning.zephyr-docs.userspace-sync-reference.page-1
title: Futex公共接口
kind: reference
status: maintained
domains: [zephyr, kernel, synchronization, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__futex__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Futex公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__futex__apis.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本册覆盖快速用户空间互斥量（Fast Userspace Mutex，Futex）、用户模式互斥量（User Mode Mutex）和用户模式信号量（User Mode Semaphore）。[本册大纲](大纲.md)连接基础指南和内核同步参考；原始接口、展开与示例保留，CONFIG_USERSPACE分支及源码差异另作译注。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.1\_函数（Functions）

<a id="r_ga596bfa265f88567ad9e80fd38cd433d3"></a>

```c
int k_futex_wait (struct k_futex *futex, int expected, k_timeout_t timeout)
```

相关声明：[k_futex_wait](#ga596bfa265f88567ad9e80fd38cd433d3)、[k_futex](P002_Futex结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

让当前线程在快速用户空间互斥量（Fast Userspace Mutex，Futex）上挂起等待。

<a id="r_ga62de1aeb7c5c273aed20d0e05336d7a0"></a>

```c
int k_futex_wake (struct k_futex *futex, bool wake_all)
```

相关声明：[k_futex_wake](#ga62de1aeb7c5c273aed20d0e05336d7a0)、[k_futex](P002_Futex结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

唤醒在Futex上等待的一个或全部线程。

## 1.2\_详细说明（Detailed Documentation）

<a id="ga596bfa265f88567ad9e80fd38cd433d3"></a>

### `k_futex_wait()`

```c
int k_futex_wait ( struct k_futex * futex, int expected, k_timeout_t timeout )
```

```c
#include <zephyr/kernel.h>
```

让当前线程在快速用户空间互斥量（Fast Userspace Mutex，Futex）上挂起等待。

检查给定Futex是否包含预期值；如果相等，就休眠，直到另一个线程对它调用k_futex_wake()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `futex` | Futex的地址。 |
| `expected` | Futex的预期值；如果实际值不同，调用者不会在其上等待。 |
| `timeout` | 等待Futex的时长，或特殊值K_NO_WAIT、K_FOREVER之一。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EACCES` | 调用者没有对该Futex地址的写访问权限。 |
| `-EAGAIN` | Futex的值与expected参数不匹配。 |
| `-ETIMEDOUT` | 线程因为超时而恢复，而非被Futex唤醒操作唤醒。 |
| `0` | 调用者进入休眠后被唤醒。调用者应在唤醒后检查Futex的值，以判断是否需要再次阻塞。 |

> 译注——源码核对：此操作只比较值并等待，不会把futex->val自动改成“已锁定”。当前实现先在锁保护下原子读取val，不等于expected时立即返回-EAGAIN；真正等待路径的超时返回-ETIMEDOUT。唤醒返回0后，调用者仍须按自身协议重新检查或原子争取状态。

<a id="ga62de1aeb7c5c273aed20d0e05336d7a0"></a>

### `k_futex_wake()`

```c
int k_futex_wake ( struct k_futex * futex, bool wake_all )
```

```c
#include <zephyr/kernel.h>
```

唤醒在Futex上等待的一个或全部线程。

唤醒给定Futex上优先级最高的等待线程，或唤醒其上的全部等待线程；具体行为取决于wake_all。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `futex` | 要唤醒其等待线程的Futex。 |
| `wake_all` | true表示唤醒全部等待线程；false表示唤醒优先级最高的等待线程。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EACCES` | 调用者没有该Futex地址的访问权限。 |
| `>=0` | 被唤醒的线程数。 |

> 译注——源码核对：当前实现按Futex地址匹配等待者，wake_all为false时选择匹配者中优先级最高的线程。它不修改val，也不把一次无人等待的wake保存为后续可消费的通知；返回0可表示当前没有匹配等待者。

## 1.3\_源码定位与版本边界

> 译注——阅读与源码边界：Futex的wait／wake是等待与唤醒接口，不提供完整的锁拥有者协议；无竞争时的共享状态操作由使用者通过原子API实现。当前官方futex.c使用一个全局等待队列，按地址筛选线程；它不要求像sys_mutex那样查询K_OBJ_SYS_MUTEX对象元数据。接口位于用户模式配置内，内存访问权限仍必须满足。

仓库相对定位：[include/zephyr/kernel.h](../../../include/zephyr/kernel.h)与[kernel/userspace/futex.c](../../../kernel/userspace/futex.c)；本次核对[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel.h)和[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/futex.c)。

官方源码摘要见[来源记录](../SOURCES.md)；仓库源码、滚动更新的main和latest网页不能自动视为同一版本。本批完成文档与源码核对，未构建或运行用户模式、并发及实板实验。

## 1.4\_原页交叉引用（Cross References）

- [k_futex](P002_Futex结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Futex结构.md)
