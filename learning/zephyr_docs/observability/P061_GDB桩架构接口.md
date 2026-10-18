---
id: learning.zephyr-docs.observability.debugaux-6
title: GDB桩架构接口
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第61章\_GDB桩架构接口

原文：[group__arch-gdbstub](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html)。读取日期：2026-10-13，`latest`。

## 61.1\_调试控制

这些接口用于 **GNU调试器桩（GNU Debugger Stub，GDB Stub）**的架构适配。

```c
#include <zephyr/arch/arch_interface.h>
```

```c
void arch_gdb_init(void);
void arch_gdb_continue(void);
void arch_gdb_step(void);
```

[`arch_gdb_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga21c8a32d35c4d267b8306d595ff1d726) 启动架构层调试，由 `gdb_init()` 调用。[`arch_gdb_continue()`](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga9c130421feeee919651828511743b346) 继续程序执行。[`arch_gdb_step()`](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga2aa577d5e55c8b739e2be6187336aaf0) 单步继续，直到下一条语句。

## 61.2\_读取寄存器

以下函数分别读取所有或一个**中央处理器（Central Processing Unit，CPU）**寄存器（Register），输出必须是GDB能够解析的**十六进制字符串（Hexadecimal String）**。

```c
size_t arch_gdb_reg_readall(struct gdb_ctx *ctx, uint8_t *buf, size_t buflen);
size_t arch_gdb_reg_readone(struct gdb_ctx *ctx, uint8_t *buf, size_t buflen,
                          uint32_t regno);
```

| 参数 | 含义 |
| --- | --- |
| `ctx` | GDB上下文（Context） |
| `buf` | 十六进制字符串输出缓冲区 |
| `buflen` | 缓冲区长度 |
| `regno` | 单寄存器版本要读取的寄存器编号 |

两者均返回写入的十六进制字符串长度；发生错误或不支持时返回 `0`。

## 61.3\_写入寄存器

以下函数接收GDB提供的十六进制字符串，分别用新值更新所有或一个CPU寄存器：

```c
size_t arch_gdb_reg_writeall(struct gdb_ctx *ctx, uint8_t *hex, size_t hexlen);
size_t arch_gdb_reg_writeone(struct gdb_ctx *ctx, uint8_t *hex, size_t hexlen,
                           uint32_t regno);
```

| 参数 | 含义 |
| --- | --- |
| `ctx` | GDB上下文 |
| `hex` | 输入十六进制字符串 |
| `hexlen` | 输入字符串长度 |
| `regno` | 单寄存器版本要更新的寄存器编号 |

两者均返回已解析的十六进制字符串长度；发生错误或不支持时返回 `0`。

## 61.4\_断点与观察点

下列接口添加或移除**断点（Breakpoint）**或**观察点（Watchpoint）**：

```c
int arch_gdb_add_breakpoint(struct gdb_ctx *ctx, uint8_t type, uintptr_t addr,
                            uint32_t kind);
int arch_gdb_remove_breakpoint(struct gdb_ctx *ctx, uint8_t type, uintptr_t addr,
                               uint32_t kind);
```

两者参数含义相同：

| 参数 | 含义 |
| --- | --- |
| `ctx` | GDB上下文 |
| `type` | 断点或观察点类型 |
| `addr` | 断点或观察点地址 |
| `kind` | 断点或观察点大小，单位为字节 |

两者均以 `0` 表示成功、`-1` 表示遇到错误、`-2` 表示不支持。

## 61.5\_内存写入后处理

```c
void arch_gdb_post_memory_write(uintptr_t addr, size_t len, uint8_t align);
```

执行内存写入后的处理。三个参数均为输入：`addr` 是内存区域起始地址，`len` 是区域大小，`align` 是该区域的写入对齐（Write Alignment）。

---

[上一章：核心转储架构接口](P060_核心转储架构接口.md) · [下一章：调试示例目录](P062_调试示例目录.md) · [返回大纲](大纲.md)
