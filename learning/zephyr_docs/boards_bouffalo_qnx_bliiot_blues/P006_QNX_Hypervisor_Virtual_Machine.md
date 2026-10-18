---
id: learning.zephyr-docs.boards-bouffalo-qnx-bliiot-blues.page-6
title: QNX Hypervisor Virtual Machine
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/blackberry/qnxhv_vm/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="qnxhv_vm"></a>

# 第6章\_QNX虚拟机监控器虚拟机（QNX Hypervisor Virtual Machine）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/blackberry/qnxhv_vm/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`qnxhv_vm`

厂商（Vendor）：

[黑莓有限公司（BlackBerry Limited）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=blackberry)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[`qnxhv_vm`](https://docs.zephyrproject.org/latest/boards/index.html#soc=qnxhv_vm)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/blackberry/qnxhv_vm/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此开发板配置允许Zephyr作为客户机（Guest）运行于QNX Hypervisor虚拟机。

这是一份示例配置。虚拟机布局通常因产品而异，因此可能需要调整设备树和Kconfig，以匹配实际的内存映射、中断路由、时钟、设备等配置。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`qnxhv_vm`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="qnxhv_vm-hw-features"></a>

<a id="qnxhv_vm-qnxhv_vm/qnxhv_vm-hw-features-section"></a>

#### `qnxhv_vm/qnxhv_vm`目标（Target）

<a id="qnxhv_vm-qnxhv_vm/qnxhv_vm-hw-features-panel"></a>

<a id="qnxhv_vm-qnxhv_vm/qnxhv_vm-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、N/A Flash。

<a id="qnxhv_vm-qnxhv_vm/qnxhv_vm-hw-features-table"></a>

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
<td>通用ARMv8-A处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P004_arm_armv8.md#std-dtcompatible-arm-armv8"><code>arm,armv8</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L36">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L57">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>板载（On-Board）</td>
<td>VIRTIO熵设备（Entropy Device），ID为4（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L104">已启用：1</a>）</td>
<td><a href="../hardware/P586_VirtIO熵源设备绑定.md#dtbinding-virtio-device4"><code>virtio,device4</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L76">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>VIRTIO控制台设备（Console Device）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L92">已启用：1</a>）</td>
<td><a href="../hardware/P591_VirtIO控制台绑定.md#dtbinding-virtio-console"><code>virtio,console</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L52">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L66">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">虚拟输入输出（Virtio）</td>
<td>板载（On-Board）</td>
<td>通过内存映射输入输出（MMIO）访问VIRTIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/blackberry/qnxhv_vm/qnxhv_vm.dts?plain=1#L86">已启用：2</a>）</td>
<td><a href="../hardware/P584_VirtIO_MMIO传输绑定.md#dtbinding-virtio-mmio"><code>virtio,mmio</code></a></td>
</tr>
</table>

<a id="qnx-hypervisor-virtual-machine-configuration"></a>

<a id="qvmconf"></a>

#### QNX Hypervisor虚拟机配置（Virtual Machine Configuration）

客户机可见的虚拟硬件由虚拟机配置文件决定。以下配置支持上述功能。

```text
# Guest name (optional)
system zephyr

# One vCPU
cpu

# Guest RAM base/size
ram 0x80000000,128M

# Virtual interrupt controller
vdev gic version 2

# Load Zephyr image (ELF is supported by qvm)
load ./zephyr.elf

# PL011 UART mapped into the guest at loc, routed to a host device/endpoint
vdev pl011
        hostdev >-        # QVM console (stdout/stderr), keeps early output visible
        loc 0x1c090000
        intr gic:37

# Enable virtio-console
vdev virtio-console
        loc 0x20000000
        intr gic:42

# Enable random number generator
vdev virtio-entropy
        loc 0x1c0e0000
        intr  gic:43
```

<a id="building-and-running"></a>

## 构建与运行（Building and Running）

<a id="build-an-application"></a>

### 构建应用（Build an Application）

使用此配置将基本Zephyr应用作为客户机运行，例如构建[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)示例：

```text
# From the root of the zephyr repository
west build -b qnxhv_vm samples/synchronization
```

这会在构建目录中生成客户机镜像，例如`zephyr/zephyr.elf`。

<a id="create-a-vm-configuration-file"></a>

### 创建虚拟机配置文件（VM Configuration File）

还需创建`.qvmconf`文件来配置虚拟机。“QNX Hypervisor虚拟机配置”一节给出了默认`qnxhv_vm`配置支持的QVM示例。（[QNX Hypervisor虚拟机配置（Virtual Machine Configuration）](#qvmconf)）

此处创建`zephyr.qvmconf`文件，并填入该示例内容。

<a id="running-an-application"></a>

### 运行应用（Running an Application）

将Zephyr镜像及QVM配置文件传到QNX Hypervisor主机，然后启动虚拟机：

```text
qvm @zephyr.qvmconf
```

应看到Zephyr输出：

```text
*** Booting Zephyr OS build v4.3.0-3524-g5c47f098ffc4 ***
thread_a: Hello World from cpu 0 on qnxhv_vm!
thread_b: Hello World from cpu 0 on qnxhv_vm!
thread_a: Hello World from cpu 0 on qnxhv_vm!
thread_b: Hello World from cpu 0 on qnxhv_vm!
thread_a: Hello World from cpu 0 on qnxhv_vm!
```

使用`Ctrl+C`停止虚拟机。

<a id="references"></a>

## 参考资料（References）


- [QNX Hypervisor用户指南：虚拟机配置（VM Configuration）](https://www.qnx.com/developers/docs/8.0/com.qnx.doc.hypervisor.user/topic/vm/vm.html)

## 译注

此页是QNX Hypervisor客户机配置示例，原文明确要求按产品实际VM内存映射、中断、时钟和设备调整DTS及Kconfig，不能直接推定适用于所有QNX虚拟机。

---

[上一章](P005_BlackBerry.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_BLIIoT_ARMxy_BL350_AM62x_M4.md)
