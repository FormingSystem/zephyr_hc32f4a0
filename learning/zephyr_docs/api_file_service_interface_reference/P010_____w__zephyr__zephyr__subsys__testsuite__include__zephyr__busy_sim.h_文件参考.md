---
id: learning.zephyr-docs.api-file-service-interface-reference.page-10
title: ____w__zephyr__zephyr__subsys__testsuite__include__zephyr__busy_sim.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_include\_\_zephyr\_\_busy\_sim.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.1\_类型定义（Typedefs）

<a id="r_a6b09e8372800e740a653f45f10a3501f"></a>

```c
typedef void(* busy_sim_cb_t) (void)
```

相关声明：[busy_sim_cb_t](#a6b09e8372800e740a653f45f10a3501f)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.2\_函数（Functions）

<a id="r_a2bb7c55b7e21ee9e5f927fcecd758705"></a>

```c
void busy_sim_start (uint32_t active_avg, uint32_t active_delta, uint32_t idle_avg, uint32_t idle_delta, busy_sim_cb_t cb)
```

相关声明：[busy_sim_start](#a2bb7c55b7e21ee9e5f927fcecd758705)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[busy_sim_cb_t](#a6b09e8372800e740a653f45f10a3501f)。

启动忙碌模拟器（Busy Simulator）。

<a id="r_ae7f199942b18363936dcb11fca8d0c96"></a>

```c
void busy_sim_stop (void)
```

相关声明：[busy_sim_stop](#ae7f199942b18363936dcb11fca8d0c96)。

停止忙碌模拟器（Busy Simulator）。

## 10.3\_详细说明（Detailed Documentation）

<a id="a6b09e8372800e740a653f45f10a3501f"></a>

### `busy_sim_cb_t`

```c
typedef void(* busy_sim_cb_t) (void)
```

<a id="a2bb7c55b7e21ee9e5f927fcecd758705"></a>

### `busy_sim_start()`

```c
void busy_sim_start ( uint32_t active_avg, uint32_t active_delta, uint32_t idle_avg, uint32_t idle_delta, busy_sim_cb_t cb )
```

启动忙碌模拟器（Busy Simulator）。

启动后，使用计数器设备（Counter Device）以随机间隔生成中断，并在中断中忙循环（Busy Loop）随机时长。中断源和优先级通过设备树（Devicetree）配置。随机数由默认熵源（Entropy Source）提供；系统工作队列（System Work Queue）负责获取随机值并保存在环形缓冲区（Ring Buffer）中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `active_avg` | 计数器回调中忙循环（Busy Loop）的平均时长，单位为微秒。 |
| `active_delta` | 忙循环时长相对平均值的偏差，单位为微秒。 |
| `idle_avg` | 计数器警报（Counter Alarm）超时的平均时长，单位为微秒。 |
| `idle_delta` | 计数器警报时长相对平均值的偏差，单位为微秒。 |
| `cb` | 在忙碌模拟器超时上下文中调用的回调。若模拟器计数器使用零延迟中断（Zero Latency Interrupt，ZLI），此回调中不能使用内核 API。回调在忙等待（Busy Waiting）之前执行。 |

<a id="ae7f199942b18363936dcb11fca8d0c96"></a>

### `busy_sim_stop()`

```c
void busy_sim_stop ( void )
```

停止忙碌模拟器（Busy Simulator）。


## 10.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P080_busy_sim.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_zephyr__bluetooth__mesh__brg_cfg_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__uart__cdc_acm.h_文件参考.md)
