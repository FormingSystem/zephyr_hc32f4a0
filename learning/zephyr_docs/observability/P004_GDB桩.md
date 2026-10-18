---
id: learning.zephyr-docs.observability.gdbstub
title: GDB桩
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/services/debugging/gdbstub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第4章\_GDB桩

原文：[GDB stub](https://docs.zephyrproject.org/latest/services/debugging/gdbstub.html)。读取日期：2026-10-12，`latest`。

GDB stub（GDB 桩）实现 GDB 远程串行协议（Remote Serial Protocol，RSP），使 GDB 可以远程调试 Zephyr。协议本身支持串口、UDP/IP、TCP/IP 等连接；本文所述 Zephyr 实现目前只支持串口设备通信。

GDB 作为客户端，Zephyr gdbstub 作为服务器。启用后，`gdb_init()` 启动服务，Zephyr 暂停执行并等待 GDB 连接；连接建立后可以同步交互，目前不能异步向目标发送命令。

## 4.1\_支持的功能与配置

支持添加和移除断点、继续执行、单步、打印回溯、读写通用寄存器以及读写内存。通过 Kconfig 配置项 `CONFIG_GDBSTUB` 启用，串口后端另启用 `CONFIG_GDBSTUB_SERIAL_BACKEND`。

串口后端通过 **通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）** 收发 GDB 命令。板上有空闲 UART 时，在设备树 `/chosen` 的 `zephyr,gdbstub-uart` 属性中指定它，使 `printk()` 和日志不与 GDB 共用同一端口。如果只有一个 UART，且打印和日志也使用该端口，应关闭它们，通常禁用 `CONFIG_PRINTK` 与 `CONFIG_LOG` 即可；否则 GDB 数据和日志交错可能导致意外结果。

## 4.2\_串口调试步骤

启用 GDB stub 和串口后端后构建，将镜像烧入开发板并复位。程序应暂停在 `gdb_init()`。在开发机启动 GDB，连接串口：

```text
target remote <serial device>
```

例如：

```text
target remote /dev/ttyUSB1
```

之后即可使用 GDB 命令调试。

## 4.3\_QEMU完整示例

[tests/subsys/debug/gdbstub](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/debug/gdbstub) 的 `debug.gdbstub.breakpoints` 用例演示 Zephyr GDB stub。测试还包含连接 QEMU 自带 GDB stub 的参考用例，使用自定义端口 `tcp:1235`，用于验证测试脚本。

从 `ZEPHYR_BASE` 目录运行：

```shell
west twister -p qemu_x86 -T tests/subsys/debug/gdbstub
```

原文预期测试成功，下面再以手工步骤展示相同类型的交互。`<SDK install directory>`、`<build directory>`、`<ZEPHYR_BASE>` 应替换为实际目录。

### 4.3.1\_启动目标与调试器

打开两个终端，在第一个构建并运行：

```shell
# From the root of the zephyr repository
west build -b qemu_x86 tests/subsys/debug/gdbstub -- '-DCONFIG_QEMU_EXTRA_FLAGS="-serial tcp:localhost:5678,server"'
west build -t run
```

这里用 `CONFIG_QEMU_EXTRA_FLAGS` 将 QEMU 串口重定向到本机 TCP 5678，等待接下来 GDB 的远程连接。

> 译注：TCP 是 QEMU 对串口的主机侧转接；目标内仍使用串口后端，不与前文“Zephyr 仅支持串口通信”矛盾。参考用例的 QEMU 原生 GDB 端口 1235 与这里转接的 5678 也不是同一服务。

第二个终端启动 GDB：

```shell
<SDK install directory>/x86_64-zephyr-elf/bin/x86_64-zephyr-elf-gdb
```

告诉 GDB 已构建 **可执行与可链接格式（Executable and Linkable Format，ELF）** 的位置：

```text
(gdb) symbol-file <build directory>/zephyr/zephyr.elf
```

原例响应：

```text
Reading symbols from <build directory>/zephyr/zephyr.elf...
```

连接 QEMU 暴露的串口后端：

```text
(gdb) target remote localhost:5678
```

原例响应：

```text
Remote debugging using localhost:5678
arch_gdb_init () at <ZEPHYR_BASE>/arch/x86/core/ia32/gdbstub.c:252
252     }
```

GDB 同时显示暂停位置，本例为 `arch/x86/core/ia32/gdbstub.c` 第 252 行。

### 4.3.2\_回溯、源码与单步

用 `bt` 或 `backtrace` 查看栈帧回溯：

```text
(gdb) bt
#0  arch_gdb_init () at <ZEPHYR_BASE>/arch/x86/core/ia32/gdbstub.c:252
#1  0x00104140 in gdb_init () at <ZEPHYR_BASE>/zephyr/subsys/debug/gdbstub.c:852
#2  0x00109c13 in z_sys_init_run_level (level=INIT_LEVEL_PRE_KERNEL_2) at <ZEPHYR_BASE>/kernel/init.c:360
#3  0x00109e73 in z_cstart () at <ZEPHYR_BASE>/kernel/init.c:630
#4  0x00104422 in z_prep_c (arg=0x1245bc <x86_cpu_boot_arg>) at <ZEPHYR_BASE>/arch/x86/core/prep_c.c:80
#5  0x001000c9 in __csSet () at <ZEPHYR_BASE>/arch/x86/core/ia32/crt0.S:290
#6  0x001245bc in uart_dev ()
#7  0x00134988 in z_interrupt_stacks ()
#8  0x00000000 in ?? ()
```

用 `list` 查看当前暂停位置附近源码：

```text
(gdb) list
247             __asm__ volatile ("int3");
248
249     #ifdef CONFIG_GDBSTUB_TRACE
250             printk("gdbstub:%s GDB is connected\n", __func__);
251     #endif
252     }
253
254     /* Hook current IDT. */
255     _EXCEPTION_CONNECT_NOCODE(z_gdb_debug_isr, IV_DEBUG, 3);
256     _EXCEPTION_CONNECT_NOCODE(z_gdb_break_isr, IV_BREAKPOINT, 3);
```

用 `s` 或 `step` 执行到不同源码行。本例从 `arch_gdb_init()` 返回，继续到 `gdb_init()`：

```text
(gdb) s
gdb_init () at <ZEPHYR_BASE>/subsys/debug/gdbstub.c:857
857     return 0;
```

查看附近代码：

```text
(gdb) list
852             arch_gdb_init();
853
854     #ifdef CONFIG_GDBSTUB_TRACE
855             printk("gdbstub:%s exit\n", __func__);
856     #endif
857             return 0;
858     }
859
860     #ifdef CONFIG_XTENSA
861     /*
```

### 4.3.3\_断点与变量

用 `br` 或 `break` 设置断点。本例在 `main()` 下断点，然后用 `c` 或 `continue` 继续：

```text
(gdb) break main
Breakpoint 1 at 0x10064d: file <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c, line 27.
```

```text
(gdb) continue
Continuing.
```

到达 `main()` 后停止并返回 GDB 提示符：

```text
Breakpoint 1, main () at <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c:27
27              printk("%s():enter\n", __func__);
```

查看主函数开头：

```text
(gdb) list
22
23      int main(void)
24      {
25              int ret;
26
27              printk("%s():enter\n", __func__);
28              ret = test();
29              printk("ret=%d\n", ret);
30              return 0;
31      }
```

用 `p` 或 `print` 查看 `ret`：

```text
(gdb) p ret
$1 = 1273788
```

此时变量未初始化，因此显示的是未定义的初始内容，不能解释为函数计算结果。

### 4.3.4\_进入函数与返回值赋值

原文指出，在该例中使用 `step` 会略过 `test()` 内部。若需检查函数内部，可以在 `test()` 设置断点，或用 `si`/`stepi` 逐机器指令执行，借此进入函数。`finish` 则继续执行直到当前函数返回：

```text
(gdb) finish
Run till exit from #0  test () at <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c:17
0x00100667 in main () at <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c:28
28              ret = test();
Value returned is $2 = 30
```

再次检查 `ret`。有时函数返回后还需再单步一次，才完成返回值赋值，因为工具链生成的赋值机器指令位于返回之后，不会作为独立的 C 源码语句显示：

```text
(gdb) p ret
$3 = 1273788
(gdb) step
29              printk("ret=%d\n", ret);
(gdb) p ret
$4 = 30
```

> 译注：`step` 通常尝试进入有调试信息的函数；原文所述略过行为取决于该例代码、调试信息与优化，不能当作 `step` 的普遍定义。`stepi` 只执行一条机器指令，必须走到相应调用指令才会进入函数，或直接为 `test` 下断点。

### 4.3.5\_结束运行

若此时继续，且之后没有可命中的断点，程序会一直运行。本文所述 Zephyr gdbstub 尚不支持 GDB 通过 `Ctrl-C` 异步暂停；应切到运行 QEMU 的第一个终端，按 `Ctrl+a` 后按 `x` 退出。Twister 运行同一测试时会自动停止 QEMU。

> 译注：以上交互记录、地址、行号和变量示例值来自原文，未在本轮执行。实际输出随构建版本和优化而变化，串口设备名和终端命令也需与使用的主机系统对应。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：线程分析器](P003_线程分析器.md) · [本模块主线目录](../reading/observability.md) · [全部主线](../reading/README.md) · [下一篇：Cortex-M调试监视器](P005_Cortex-M调试监视器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：线程分析器](P003_线程分析器.md) · [下一章：Cortex-M调试监视器](P005_Cortex-M调试监视器.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
