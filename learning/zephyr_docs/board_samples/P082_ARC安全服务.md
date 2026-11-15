---
id: learning.zephyr-docs.board-samples.page-82
title: ARC安全服务
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/arc_secure_services/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="arc-secure-service"></a>

<a id="id1"></a>

# 第82章\_ARC 安全服务（ARC Secure Service）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/arc_secure_services/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 82.1 概述（Overview）

本示例基于 ARC SecureShield 实现一个简单的安全服务，演示安全 Zephyr 应用如何与普通 Zephyr 应用共同运行。

> 译注——适用架构：这是 ARC SecureShield 的安全／普通双执行环境示例，不是 ARM TrustZone 的配置方法。安全中断和线程的优先关系由该架构的执行环境决定，不能只用普通 Zephyr 线程优先级数字推导。

本示例中：

- 安全应用位于 `arc_mpu_regions.c` 定义的安全内存空间。RAM 和 ROM 各有一半分给安全世界（Secure world），另一半分给普通世界（Normal world）。

- 未分配给安全应用的内存分配给普通应用。

- 默认情况下，整个外设地址空间都可由普通模式访问，也就是安全模式与普通模式共享外设。如果安全世界需要独占某些外设，可在 `arc_mpu_regions.c` 中添加静态 MPU 条目。

- 两个内部定时器的中断被配置为普通中断，使普通 Zephyr 应用的内核节拍（Kernel tick）正常工作。

- 优先级关系为：安全中断 > 安全线程 > 普通中断 > 普通线程。

<a id="requirements"></a>

## 82.2 前提条件（Requirements）

使用本示例要求 ARC 处理器具备 ARC SecureShield。原文列出以下 Zephyr 开发板配置：

- em_starterkit_em7d：安全应用使用 em_starterkit_em7d_secure；普通应用使用 em_starterkit_em7d_normal。

- nsim_sem：安全应用使用 nsim_sem；普通应用使用 nsim_sem_normal。

<a id="building-and-running"></a>

## 82.3 构建与运行（Building and Running）

> 译注——执行前提：主机 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链和具体板。调试器、双镜像及外部下载工具的目录要求分别按本页说明处理。本次未构建、烧录或执行硬件实验。

<a id="building"></a>

### 82.3.1 构建（Building）

<a id="secure-application"></a>

#### 82.3.1.1 安全应用（Secure application）

首先构建安全应用。

> 译注——旧命令与板目标：下面原文把 em_starterkit_em7d_secure 与 nsim_sem 同时写在一条 west build 中；普通应用命令也列出两个板名。-b 只接受一个板目标，不能原样将两个配置当作同时构建。本次 tests.yaml 使用 nsim/nsim_sem、em_starterkit/emsk_em7d，且标记 build_only；旧的 normal DTS／defconfig 文件需结合当前板模型与内存布局检查，不能把旧名称直接视为现成可运行目标。

```text
west build -b em_starterkit_em7d_secure nsim_sem samples/boards/arc_secure_services
```

<a id="normal-application"></a>

#### 82.3.1.2 普通应用（Normal application）

当前普通应用不能访问内存保护单元（Memory Protection Unit，MPU），因此不支持用户空间（User space）及基于 MPU 的栈检查。请将对应的 dts 和 def_config 文件复制到相应开发板目录，以构建普通应用。

此处以[哲学家就餐（Dining Philosophers）](../basic_samples/P030_哲学家就餐示例.md#dining-philosophers)作为普通应用示例。

```text
west build -b em_starterkit_em7d_normal nsim_sem_normal samples/philosophers
```

<a id="running"></a>

### 82.3.2 运行（Running）

- 使用引导程序运行（Run using the bootloader）

引导程序应把安全应用和普通应用加载到正确位置，再跳到安全应用入口。普通应用入口在安全应用中硬编码，随后由安全应用启动普通应用。

> 译注——入口细节：本次安全应用对 NSIM 使用 NORMAL_FIRMWARE_ENTRY=0x40000，对 EMSK 使用 0x20000；随后读取该地址处的 32 位值传给 arc_go_to_normal()，不是直接跳到常量地址。普通镜像的向量内容和链接地址必须与此约定一致。

- 使用调试器运行，原文推荐此方式（Run using the debugger）

使用 GDB 调试器加载并运行两个应用。

对于 EM Starter Kit，运行以下命令：

> 译注——命令执行位置：原文假定两个应用各自的 build 目录位于应用目录内；若前面从源码根使用 west 的默认 build，这些 cd 和相对 ELF 路径不会自动成立。应给两个应用分别指定构建目录，再按实际产物位置调整。$ 是示意提示符；cd、west 在主机终端执行，monitor、load、target remote、c 是 GDB 命令，不能全部粘贴进同一个 Shell。

```text
# load secure application first
$ cd samples/boards/arc_secure_services/build
$ west debug
# load normal application
$ monitor load_image ../../../philosophers/build/zephyr/zephyr.elf
$ c
```

对于 nsim SEM，需要两个控制台：一个显示应用输出，另一个用于调试器。

> 译注——加载顺序：原文调试器步骤先加载普通镜像、再加载安全镜像并继续执行；secure／normal 的地址空间不同。debugserver 终端需保持运行，另一个终端连接 :3333；端口和 ELF 路径均须与实际会话对应。本次只核对文档，未启动调试器。

在输出控制台执行：

```text
# open debug server
$ cd samples/boards/arc_secure_services/build
$ west debugserver
```

在调试器控制台执行：

```text
# open debug server
$ cd samples/boards/arc_secure_services/build
$ arc-elf32-gdb zephyr/zephyr.elf
$ target remote :3333
# load normal application
$ load ../../../philosophers/build/zephyr/zephyr.elf
# load secure application
$ load
$ c
```

> 译注——源码入口：[src/main.c](../../../samples/boards/arc_secure_services/src/main.c)；[tests.yaml](../../../samples/boards/arc_secure_services/tests.yaml)；[nsim_sem_normal.dts](../../../samples/boards/arc_secure_services/nsim_sem_normal.dts)；[nsim_sem_normal_defconfig](../../../samples/boards/arc_secure_services/nsim_sem_normal_defconfig)。仓库参照使用相对路径，版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/arc_secure_services/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/arc_secure_services/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/arc_secure_services/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P081_NXP示例目录.md) · [返回大纲](大纲.md) · [下一章](P083_USB电力传输分析器.md)
