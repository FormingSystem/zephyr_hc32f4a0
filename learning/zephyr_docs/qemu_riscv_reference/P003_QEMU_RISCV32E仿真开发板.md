---
id: learning.zephyr-docs.qemu-riscv-reference.page-3
title: QEMU_RISCV32E仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/riscv32e/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_QEMU\_RISCV32E仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/riscv32e/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_riscv32e"></a>

## 3.1\_开发板概况与概述

名称：`qemu_riscv32e`。厂商：[QEMU，通用开源机器仿真器与虚拟化器](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qemu)。状态：持续维护（Maintained）。架构（Architecture）：[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)；片上系统（System on Chip，SoC）：[qemu_virt_riscv32e](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_virt_riscv32e)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/riscv32e)。

<a id="overview"></a>

此 QEMU 开发板配置用于仿真（Emulation）RISCV32（RV32E） 架构。

<a id="elf-loading-convention"></a>

## 3.2\_ELF加载约定

QEMU 的 RISC-V `virt` 虚拟机器采用与 OpenSBI 的 `fw_dynamic`、`fw_jump`、`fw_payload` 固件以及伯克利引导加载器（Berkeley Boot Loader，BBL）一致的启动行为。ELF 是可执行与可链接格式（Executable and Linkable Format）；SBI 是监管者二进制接口（Supervisor Binary Interface）。原页引用的代码注释如下：

```c
/*
 * NB: Use low address not ELF entry point to ensure that the fw_dynamic
 * behaviour when loading an ELF matches the fw_payload, fw_jump and BBL
 * behaviour, as well as fw_dynamic with a raw binary, all of which jump to
 * the (expected) load address load address. This allows kernels to have
 * separate SBI and ELF entry points (used by FreeBSD, for example).
 */
```

**注释译文：**注意，应使用低地址而非 ELF 入口点，以确保 `fw_dynamic` 加载 ELF 时的行为与 `fw_payload`、`fw_jump`、BBL，以及加载原始二进制的 `fw_dynamic` 一致：它们都跳转到预期的加载地址。这样，内核就可以具有分离的 SBI 入口点和 ELF 入口点，例如 FreeBSD 就使用这种方式。原注释中重复出现的 `load address` 按原样保留。

换言之，通过 `-kernel` 把 ELF 传给 QEMU 时，虚拟中央处理器（Virtual CPU，vCPU）的程序计数器（Program Counter）会被设置为镜像加载到的最低地址，**而不是 ELF 头中 `e_entry` 字段记录的地址**。这使原始二进制（Raw Binary）与 ELF 镜像保持一致的启动行为，也允许内核公开一个与 ELF 入口点不同的 SBI 入口点。

通常，Zephyr 不会感知到这一约定，因为链接脚本（Linker Script）把镜像入口 `CONFIG_KERNEL_ENTRY` 放在只读存储器区域（ROM Region）的最开头，加载地址恰好与入口地址重合。一旦两者分离就会出问题，例如 ROM 区域在 `rom_start` 之前为头部（Header）或填充（Padding）预留空间时，QEMU 会跳到这片预留空间的开头，而不是跳到 `CONFIG_KERNEL_ENTRY`，因此 Zephyr 根本不会运行。

[`CONFIG_QEMU_DEVICE_LOADER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QEMU_DEVICE_LOADER)通过替换 `-kernel` 选项来绕过这一问题：为每个 CPU 添加一项 `-device loader,file=<elf>`，也就是为 [`CONFIG_MP_MAX_NUM_CPUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MP_MAX_NUM_CPUS) 配置的每个核心各添加一项。与 `-kernel` 不同，QEMU 通用加载器设备（Generic Loader Device）遵守 ELF 的实际入口点，因此无论该入口相对于 ROM 基址位于何处，每个 vCPU 都从 `CONFIG_KERNEL_ENTRY` 开始执行。

<a id="programming-and-debugging"></a>

## 3.3\_编程与调试

官方页面在此列出 `qemu_riscv32e` 支持的运行器（Runner）及关联 west 命令。

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

`qemu_riscv32e` 的应用可按仿真开发板通常使用的方式构建和运行，详情见[构建应用](../application/P001_应用开发.md#build-an-application)与[运行应用](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="flashing"></a>

### 3.3.1\_烧写与运行

虽然这是仿真开发板，不能实际“烧写”（Flash），但可以使用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用和内核测试。以下以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，从 Zephyr 仓库根目录执行；代码注释 `From the root of the zephyr repository` 也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_riscv32e samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出（Console Output）：

```text
*** Booting Zephyr OS build v3.1.0-rc1-59-g0d66cc1f6645  ***
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

> 译注：输出及版本号是官方页面给出的原始示例，本次翻译没有运行固件或重新生成这些输出。

<a id="debugging"></a>

### 3.3.2\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

---

[上一章](P002_QEMU_RISCV32_XIP仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P004_QEMU_RISCV64仿真开发板.md)
