---
id: learning.zephyr-docs.boards-waveshare-tail.page-50
title: ARMv8 Xen Virtual Machine Example
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/xen/xenvm/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="xenvm"></a>

# 第50章\_ARMv8 Xen虚拟机示例

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/xen/xenvm/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`xenvm`

厂商（Vendor）：

[Xen虚拟机监控器（Hypervisor）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=xen)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[`xenvm`](https://docs.zephyrproject.org/latest/boards/index.html#soc=xenvm)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/xen/xenvm/doc/index.rst/../..)<a id="armv8-xen-virtual-machine-example"></a>

## ARMv8 Xen虚拟机示例

<a id="overview"></a>

### 概述（Overview）

此板级配置允许Zephyr作为Xen客户机（Guest）运行在支持ARM虚拟化扩展的ARMv8板卡上。它只是示例配置，因为各虚拟机的配置通常有诸多差异。

提供以下最小设备集：


- ARM通用定时器（Generic Timer）
- GICv2/GICv3

<a id="hardware"></a>

### 硬件（Hardware）

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`xenvm`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="xenvm-hw-features"></a>

<a id="xenvm-xenvm/xenvm-hw-features-section"></a>

##### `xenvm/xenvm`目标（Target）

<a id="xenvm-xenvm/xenvm-hw-features-panel"></a>

<a id="xenvm-xenvm/xenvm-hw-features-memory"></a>

此目标可用存储：16 MiB RAM，闪存不适用。

<a id="xenvm-xenvm/xenvm-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>通用ARMv8-A处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P004_arm_armv8.md#std-dtcompatible-arm-armv8"><code>arm,armv8</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L58">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L48">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>Xen平台HVC UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L81">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P009_xen_hvc-uart.md#std-dtcompatible-xen-hvc-uart"><code>xen,hvc-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L66">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>Xen域看门狗（Domain Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L86">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P010_xen_watchdog.md#std-dtcompatible-xen-watchdog"><code>xen,watchdog</code></a></td>
</tr>
<tr>
<td rowspan="1">Xen 虚拟机监控器（Xen）</td>
<td>板载（On-Board）</td>
<td>Xen平台控制寄存器（Platform Control Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L74">已启用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P013_xen_xen.md#std-dtcompatible-xen-xen"><code>xen,xen</code></a></td>
</tr>
</table>

<a id="xenvm-xenvm/xenvm/gicv3-hw-features-section"></a>

##### `xenvm/xenvm/gicv3`目标（Target）

<a id="xenvm-xenvm/xenvm/gicv3-hw-features-panel"></a>

<a id="xenvm-xenvm/xenvm/gicv3-hw-features-memory"></a>

此目标可用存储：16 MiB RAM，闪存不适用。

<a id="xenvm-xenvm/xenvm/gicv3-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>通用ARMv8-A处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L40">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P004_arm_armv8.md#std-dtcompatible-arm-armv8"><code>arm,armv8</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L58">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L48">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>Xen平台HVC UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L81">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P009_xen_hvc-uart.md#std-dtcompatible-xen-hvc-uart"><code>xen,hvc-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L66">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>Xen域看门狗（Domain Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L86">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P010_xen_watchdog.md#std-dtcompatible-xen-watchdog"><code>xen,watchdog</code></a></td>
</tr>
<tr>
<td rowspan="1">Xen 虚拟机监控器（Xen）</td>
<td>板载（On-Board）</td>
<td>Xen平台控制寄存器（Platform Control Registers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xen/xenvm/xenvm.dts?plain=1#L74">已启用：1</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P013_xen_xen.md#std-dtcompatible-xen-xen"><code>xen,xen</code></a></td>
</tr>
</table>

<a id="devices"></a>

#### 设备（Devices）

<a id="system-clock"></a>

##### 系统时钟（System Clock）

此配置默认系统时钟8.32 MHz，须按实际硬件修正。

可从Xen启动日志确定ARM通用定时器频率：

```text
(XEN) [    0.147541] Generic Timer IRQ: phys=30 hyp=26 virt=27 Freq: 8320 KHz
```

<a id="interrupt-controller"></a>

##### 中断控制器（Interrupt Controller）

根据硬件通用中断控制器（GIC）的版本选择配置变体：


- xenvm选择GICv2
- xenvm//gicv3选择GICv3

<a id="cpu-core-type"></a>

##### CPU内核类型（CPU Core Type）

默认内核为Cortex-A72。可根据实际硬件，采用与中断控制器配置类似的方式修改。

<a id="known-problems-or-limitations"></a>

#### 已知问题或限制（Known Problems or Limitations）

Xen在运行时通过设备树描述并配置客户机环境，而Zephyr依赖构建时已知的静态配置，因此默认镜像可能无法在实际硬件上启动。此时须修改设备树及Kconfig，方法见下一节。

原文说明多数Xen专用功能尚不支持，包括：


- XenBus，开发中
- Xen半虚拟化（Paravirtualization，PV）驱动

当前仅支持以下功能：


- Xen Enlighten内存页
- Xen事件通道（Event Channels）
- Xen PV控制台，两种版本：DomU使用普通环形缓冲区，Dom0使用consoleio
- Xen早期console_io接口，主要用于调试，需要调试版Xen
- Xen授权表（Grant Tables），可授予对本域内存的访问权限，并映射／取消映射其他域的授权内存
- Xen域看门狗（Domain Watchdog）

<a id="watchdog"></a>

##### 看门狗（Watchdog）

板级设备树将Xen域看门狗描述为Zephyr看门狗设备。定时器归Xen所有，超时时按该域的Xen on_watchdog策略处理整个客户机域。Zephyr应用可使用标准看门狗API安装、设置及喂狗。

<a id="building-and-running"></a>

### 构建与运行（Building and Running）

可通过此配置以Xen客户机运行基础Zephyr应用及内核测试，例如基本同步（[Basic Synchronization](../basic_samples/P029_基本同步示例.md#synchronization)）示例：


- 硬件使用GICv2时：

```text
$ west build -b xenvm samples/synchronization
```


- 硬件使用GICv3时：

```text
$ west build -b xenvm//gicv3 samples/synchronization
```

上述命令生成同步示例镜像。接着创建客户机配置文件zephyr.conf，例如：

```text
kernel="zephyr.bin"
name="zephyr"
vcpus=1
memory=16
gic_version="v2"
on_crash="preserve"
```

使用xenvm//gicv3时，须删除gic_version参数，或将其设为v3。

将zephyr.bin和zephyr.conf上传至Dom0，然后运行以下命令启动Zephyr：

```text
$ xl create zephyr.conf
```

随后连接PV控制台：

```text
$ xl console zephyr
```

也可用单条命令完成：

```text
$ xl create -c zephyr.conf
```

应看到Zephyr输出：

```text
*** Booting Zephyr OS build zephyr-v2.4.0-1137-g5803ee1e8183  ***
thread_a: Hello World from cpu 0 on xenvm!
thread_b: Hello World from cpu 0 on xenvm!
thread_a: Hello World from cpu 0 on xenvm!
thread_b: Hello World from cpu 0 on xenvm!
thread_a: Hello World from cpu 0 on xenvm!
```

按CTRL+]退出Xen虚拟控制台。

<a id="updating-configuration"></a>

### 更新配置（Updating Configuration）

Xen使用设备树描述硬件，预期客户机在运行时解析，而Zephyr仅支持构建时静态配置。所提供配置应适用于大多数以aarch64模式运行的ARMv8主机，但不能保证Xen未来不会改变RAM基地址等值。

系统定时器频率也随板卡变化，在新硬件上运行Zephyr xenvm镜像时须更新。

可通过LIBXL_DEBUG_DUMP_DTB环境变量让Xen转储生成的设备树二进制（DTB）：

```text
$ LIBXL_DEBUG_DUMP_DTB=domu-libxl.dtb xl create zephyr.conf
```

然后使用设备树编译器dtc反编译生成的domu-libxl.dtb。

根据反编译DTB中的信息更新xenvm.dts相关条目。若内存布局改变，可能还需修改CONFIG_SRAM_BASE_ADDRESS。

<a id="references"></a>

### 参考资料（References）

[具有虚拟化扩展的Xen ARM](https://wiki.xenproject.org/wiki/Xen_ARM_with_Virtualization_Extensions)

[xl.conf客户机配置文件手册](https://xenbits.xen.org/docs/unstable/man/xl.cfg.5.html)

## 译注

Xen客户机配置必须匹配运行时提供的设备树；默认8.32 MHz、Cortex-A72及GIC版本均需依实际主机调整。Xen域看门狗超时作用于整个客户机域。

---

[上一章](P049_Xen_Hypervisor.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P051_Shenzhen_Xunlong_Software_Co._Limited.md)
