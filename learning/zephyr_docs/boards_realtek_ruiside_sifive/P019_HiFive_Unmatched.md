---
id: learning.zephyr-docs.boards-realtek-ruiside-sifive.page-19
title: HiFive Unmatched
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/sifive/hifive_unmatched/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="hifive_unmatched"></a>

# 第19章\_HiFive Unmatched

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/sifive/hifive_unmatched/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/hifive_unmatched.jpg](images/hifive_unmatched.jpg)](images/hifive_unmatched.jpg)

HiFive Unmatched

名称（Name）：

`hifive_unmatched`

厂商（Vendor）：

[SiFive, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=sifive)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[fu740](https://docs.zephyrproject.org/latest/boards/index.html#soc=fu740)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sifive/hifive_unmatched/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

HiFive Unmatched是一款采用SiFive FU740-C000多核64位RISC-V SoC的开发板。

<a id="programming-and-debugging"></a>

## 编程与调试（Programming and Debugging）

`hifive_unmatched`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="building"></a>

### 构建（Building）

hifive_unmatched板级配置的应用可使用对应开发板名称按常规方式构建，见“构建应用”：（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

<a id="tab-0-Uzc="></a>

<a id="tab-0-VTc0"></a>

<a id="panel-0-Uzc="></a>

**S7**

```text
# From the root of the zephyr repository
west build -b hifive_unmatched/fu740/s7 samples/hello_world
```

<a id="panel-0-VTc0"></a>

**U74**

```text
# From the root of the zephyr repository
west build -b hifive_unmatched/fu740/u74 samples/hello_world
```

<a id="flashing"></a>

### 烧录（Flashing）

当前版本尚不支持将二进制文件烧录到板载Flash ROM。

该板具有USB-JTAG接口，可配合OpenOCD使用。按以下步骤将应用加载到DDR并运行：

<a id="tab-1-Uzc="></a>

<a id="tab-1-VTc0"></a>

<a id="panel-1-Uzc="></a>

**S7**

```text
# From the root of the zephyr repository
west build -b hifive_unmatched//s7 samples/hello_world
west flash
```

<a id="panel-1-VTc0"></a>

**U74**

```text
# From the root of the zephyr repository
west build -b hifive_unmatched//u74 samples/hello_world
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

详细概述见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

## 译注

HiFive Unmatched为FU740-C000，当前页面不支持写入板载Flash ROM，示例通过USB-JTAG及OpenOCD加载到DDR运行。

---

[上一章](P018_HiFive_Unleashed.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_SiFive.md)
