---
id: learning.zephyr-docs.snippets.page-22
title: Xen控制域配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/xen-dom0/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="xen-dom0-universal-snippet-for-xen-control-domain"></a>
<a id="xen-dom0"></a>

# 第22章\_Xen控制域配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/xen-dom0/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 22.1 概述（Overview）

本片段允许把Zephyr构建为Xen初始域（Initial Domain，Dom0）。该功能以配置片段形式实现，以便支持任意兼容的平台。

<a id="how-to-add-support-of-a-new-board"></a>

## 22.2 为新开发板添加支持（How to add support of a new board）

1. 为本片段添加板级设备树覆盖文件，删除UART节点。
2. 在应用的设备树覆盖文件中，根据当前环境里Xen为Domain-0选择的区域，添加正确的内存节点和虚拟机监控器（Hypervisor）节点。

> 译注——删除与禁用：原文使用“删除UART节点”的表述；当前官方QEMU覆盖文件实际将`uart0`的`status`改为`disabled`，并非通过`/delete-node/`删除节点。通用覆盖文件把控制台和Shell串口转到Xen HVC控制台，板级处理应与实际设备树配合。

<a id="programming"></a>

## 22.3 构建配置（Programming）

调用`west build`时必须指定正确的Xen片段名称。例如：

```sh
west build -b qemu_cortex_a53 -S xen-dom0 samples/synchronization
```

<a id="qemu-example-with-xen"></a>

## 22.4 QEMU与Xen示例（QEMU example with Xen）

本片段[snippets/xen-dom0/boards/](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/xen-dom0/boards/)目录中为`qemu_cortex_a53`提供的覆盖文件，是QEMU Xen控制域（Control Domain）示例。

运行这套配置需要：

1. 获取Xen，并为Arm64平台构建，例如使用`RELEASE-4.17.0`。
2. 取出`example/`目录中的示例设备树并编译。
3. 使用`xen-dom0`片段构建Zephyr示例或应用，并将其作为Xen控制域启动。

<a id="important-notice-regarding-device-tree"></a>

### 22.4.1 关于设备树的重要说明（Important notice regarding device tree）

Xen动态分配Dom0镜像、授权表（Grant Table）以及扩展区域（Extended Regions）使用的地址，因此不同环境中的地址可能不同。它们取决于内存Bank的位置与大小、应用镜像大小、引导程序使用的Hypervisor装载地址等因素。由于Zephyr不在运行时解析设备树，也不是位置无关可执行文件（Position-Independent Executable），构建时就需要知道准确数值。

为此，需要构建最终二进制文件，尝试通过Xen启动，然后分析Hypervisor输出，取得当前环境的准确地址。输出类似以下内容。


> 译注——版本范围：上述构建时固定地址的要求描述的是本文这套Dom0片段流程。当前官方[Xen Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/xen/Kconfig)另有依赖`BOARD_XENVM`的`XEN_FDT`选项，用于在早期启动时复制Xen提供的设备树；不能把原文概括成所有Zephyr Xen配置永远不能接收启动设备树，也不能据此省略本示例的静态地址核对。

授权表区域，对应`hypervisor`节点中的第一个`reg`区域：

```text
(XEN) Grant table range: 0x00000088080000-0x000000880c0000
```

扩展区域，对应`hypervisor`节点中第二个及之后的`reg`区域：

```text
(XEN) [    0.928173] d0: extended region 2: 0x40000000->0x47e00000
```

Zephyr Dom0内存：

```text
(XEN) Allocating 1:1 mappings for dom0:
(XEN) BANK[0] 0x00000060000000-0x00000070000000 (256MB)
```

对于所给示例，应用覆盖文件应添加以下设备树节点。该示例基于带扩展区域的R-Car H3ULCB：

```dts
hypervisor: hypervisor@88080000 {
    compatible = "xen,xen";
    reg = <0x0 0x88080000 0x0 0x40000 0x0 0x40000000 0x0 0x7e00000>;
    interrupts = <GIC_PPI 0x0 IRQ_TYPE_EDGE IRQ_DEFAULT_PRIORITY>;
    interrupt-parent = <&gic>;
    status = "okay";
};

ram: memory@60000000 {
    device_type = "mmio-sram";
    reg = <0x00 0x60000000 0x00 DT_SIZE_M(256)>;
};
```

<a id="xen-extended-regions-notice"></a>

### 22.4.2 Xen扩展区域说明（Xen extended regions notice）

默认禁用Xen扩展区域支持。因此，在设备树`hypervisor`节点中指定扩展区域之后，原文还要求在应用覆盖文件中把`XEN_REGIONS`配置设为“yes”。

> 译注——配置文件类型：`XEN_REGIONS`是Kconfig选项，应用配置片段中应写作`CONFIG_XEN_REGIONS=y`，不能把它写成设备树`.overlay`属性。原文这里用“application overlay file”称呼应用覆盖文件，容易与前面的设备树覆盖混淆。设备树负责区域地址，Kconfig负责启用对应功能；两者需要同时匹配。

<a id="start-the-example"></a>

### 22.4.3 启动示例（Start the example）

可以使用Zephyr SDK中的QEMU，按以下命令启动：

```sh
<path to Zephyr SDK>/sysroots/x86_64-pokysdk-linux/usr/bin/qemu-system-aarch64 -cpu cortex-a53 \
-m 6G -nographic -machine virt,gic-version=3,virtualization=true -chardev stdio,id=con,mux=on \
-serial chardev:con -mon chardev=con,mode=readline -pidfile qemu.pid \
-device loader,file=<path to Zephyr app build>/zephyr.bin,addr=0x40600000 \
-dtb <path to DTB>/xen.dtb -kernel <path to Xen build>/xen
```

这将启动Xen Hypervisor，并把应用作为Xen控制域运行。为了使用控制域管理功能，可以将Xen-troops的[zephyr-xenlib](https://github.com/xen-troops/zephyr-xenlib)库加入项目。它提供基本域管理功能，包括创建和配置域。

> 译注——路径与地址：`<path to ...>`是原命令中的路径占位符，应由读者替换为自己的SDK、构建结果和DTB位置；这些位置不固定到作者机器。原命令的装载地址、RAM大小和设备树示例数值也须依据前述Xen输出复核。选择片段不会自动下载或构建Xen，也没有在本批翻译中执行该启动流程。


> 译注——片段源码：[snippet.yml](../../../snippets/xen-dom0/snippet.yml)、[xen-dom0.overlay](../../../snippets/xen-dom0/xen-dom0.overlay)、[xen-dom0.conf](../../../snippets/xen-dom0/xen-dom0.conf)。片段定义中的名称为`xen-dom0`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/xen-dom0/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/xen-dom0/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/xen-dom0/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P021_Silicon_Labs包跟踪接口配置片段.md) · [返回大纲](大纲.md) · [下一章](P023_WiFi配置片段目录.md)
