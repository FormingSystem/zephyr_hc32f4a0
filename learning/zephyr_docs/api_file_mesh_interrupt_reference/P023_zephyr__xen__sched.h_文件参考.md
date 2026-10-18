---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-23
title: zephyr__xen__sched.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_xen\_\_sched.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xen_2sched_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen调度器操作（Scheduler Operation）的辅助接口。

<a id="details"></a>

```c
#include <xen/public/sched.h>
```

查看此文件的源码。

Xen调度器操作（Scheduler Operation）的辅助接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_ae35f7ea4d4b340ea35fdb10bbea977f0"></a>

```c
int xen_sched_yield (void)
```

相关声明：[xen_sched_yield](#ae35f7ea4d4b340ea35fdb10bbea977f0)。

当前虚拟 CPU（VCPU）主动让出执行权（Yield）。

<a id="r_afb585cc82ac5851d5ad82de7a15d81f0"></a>

```c
int xen_sched_block (void)
```

相关声明：[xen_sched_block](#afb585cc82ac5851d5ad82de7a15d81f0)。

阻塞当前虚拟 CPU（VCPU），直到有事件可处理。

<a id="r_a7d2814d9797a0f1f65819fd774a87bad"></a>

```c
int xen_sched_poll (evtchn_port_t *ports, unsigned int nr_ports, uint64_t timeout)
```

相关声明：[xen_sched_poll](#a7d2814d9797a0f1f65819fd774a87bad)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

轮询事件通道端口（Event-channel Ports），直到某个端口有待处理事件或超时。

<a id="r_a3450b645f99cb336c24ef2835911f1fd"></a>

```c
int xen_sched_shutdown (unsigned int reason)
```

相关声明：[xen_sched_shutdown](#a3450b645f99cb336c24ef2835911f1fd)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使用给定的关闭原因（Shutdown Reason）关闭当前域（Domain）。

<a id="r_a0222b5101cec4a985cec20219fdab238"></a>

```c
int xen_sched_remote_shutdown (domid_t domid, unsigned int reason)
```

相关声明：[xen_sched_remote_shutdown](#a0222b5101cec4a985cec20219fdab238)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

请求关闭另一个域（Domain）。

<a id="r_afe72a62c01c49764514ad62400f19d36"></a>

```c
int xen_sched_shutdown_code (unsigned int reason)
```

相关声明：[xen_sched_shutdown_code](#afe72a62c01c49764514ad62400f19d36)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

保存关闭原因（Shutdown Reason），供后续报告域关闭情况时使用。

<a id="r_ad487cde3d2523420a468bbdbd074382a"></a>

```c
int xen_sched_pin_override (int32_t pcpu)
```

相关声明：[xen_sched_pin_override](#ad487cde3d2523420a468bbdbd074382a)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

覆盖或恢复当前虚拟 CPU（VCPU）到物理 CPU 的固定绑定（Pinning）。

<a id="r_a354226bfab2b158b1b7a597ad8336432"></a>

```c
int xen_sched_watchdog (uint32_t *id, uint32_t timeout)
```

相关声明：[xen_sched_watchdog](#a354226bfab2b158b1b7a597ad8336432)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

创建、更新或销毁 Xen 域看门狗定时器（Domain Watchdog Timer）。

## 23.2\_详细说明（Detailed Documentation）

<a id="afb585cc82ac5851d5ad82de7a15d81f0"></a>

### `xen_sched_block()`

```c
int xen_sched_block ( void )
```

阻塞当前虚拟 CPU（VCPU），直到有事件可处理。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ad487cde3d2523420a468bbdbd074382a"></a>

### `xen_sched_pin_override()`

```c
int xen_sched_pin_override ( int32_t pcpu)
```

覆盖或恢复当前虚拟 CPU（VCPU）到物理 CPU 的固定绑定（Pinning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pcpu` | 要固定绑定（Pin）到的物理 CPU；传入 -1 则恢复正常的固定绑定行为。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a7d2814d9797a0f1f65819fd774a87bad"></a>

### `xen_sched_poll()`

```c
int xen_sched_poll ( evtchn_port_t * ports, unsigned int nr_ports, uint64_t timeout )
```

轮询事件通道端口（Event-channel Ports），直到某个端口有待处理事件或超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ports` | 要轮询的事件通道端口（Event-channel Ports）。 |
| `nr_ports` | `ports` 中的条目数（Number of Entries）。 |
| `timeout` | 以 Xen 系统绝对时间（Absolute Xen System Time）表示的超时期限；传入 0 则不设超时地轮询。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a0222b5101cec4a985cec20219fdab238"></a>

### `xen_sched_remote_shutdown()`

```c
int xen_sched_remote_shutdown ( domid_t domid, unsigned int reason )
```

请求关闭另一个域（Domain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要关闭的域 ID（Domain ID）。 |
| `reason` | `SHUTDOWN_*` 原因码（Reason Code）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a3450b645f99cb336c24ef2835911f1fd"></a>

### `xen_sched_shutdown()`

```c
int xen_sched_shutdown ( unsigned int reason)
```

使用给定的关闭原因（Shutdown Reason）关闭当前域（Domain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reason` | `SHUTDOWN_*` 原因码（Reason Code）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="afe72a62c01c49764514ad62400f19d36"></a>

### `xen_sched_shutdown_code()`

```c
int xen_sched_shutdown_code ( unsigned int reason)
```

保存关闭原因（Shutdown Reason），供后续报告域关闭情况时使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reason` | `SHUTDOWN_*` 原因码（Reason Code）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a354226bfab2b158b1b7a597ad8336432"></a>

### `xen_sched_watchdog()`

```c
int xen_sched_watchdog ( uint32_t * id, uint32_t timeout )
```

创建、更新或销毁 Xen 域看门狗定时器（Domain Watchdog Timer）。

当 `id` 指向的值为 0 时，Xen 创建超时为 `timeout` 的看门狗（Watchdog），并将新看门狗 ID 作为超级调用（Hypercall）的返回值。此封装函数将新 ID 写入 `id` 指向的位置。当 `id` 指向非零值时，`timeout` 用于更新该看门狗；若 `timeout` 为 0，则销毁它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] id` | 看门狗标识符（Watchdog Identifier）。 |
| ` timeout` | 传给 Xen 的看门狗超时值（Watchdog Timeout），单位为秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `id` 为 `NULL`，或 `id` 指向的值为 0 且 `timeout` 也为 0。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ae35f7ea4d4b340ea35fdb10bbea977f0"></a>

### `xen_sched_yield()`

```c
int xen_sched_yield ( void )
```

当前虚拟 CPU（VCPU）主动让出执行权（Yield）。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 23.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P932_sched.h_源码浏览.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_zephyr__sw_isr_table.h_文件参考.md) · [返回大纲](大纲.md)
