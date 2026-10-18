---
id: learning.zephyr-docs.llext.page-10
title: Shell加载器示例
kind: reference
status: maintained
domains: [zephyr, llext, development]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/llext/shell_loader/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Shell加载器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/llext/shell_loader/README.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

<a id="llext-shell-loader"></a>

<a id="overview"></a>

## 10.1\_概述（Overview）

本例通过Shell访问可链接加载扩展（Linkable Loadable Extensions，LLEXT）系统，在Shell中管理可加载代码扩展。

<a id="requirements"></a>

## 10.2\_要求（Requirements）

需要架构受LLEXT支持、且有支持Shell的控制台（Console）的开发板。下面以ARMv7目标为例；其他LLEXT支持的架构流程相同，但工具链前缀（Toolchain Prefix）和生成的十六进制载荷（Hex Payload）不同。

<a id="building"></a>

## 10.3\_构建（Building）

以下命令构建主Shell应用。

译注：主机命令在已配置Zephyr环境的Bash中执行，当前位置为Zephyr源码根目录。主机`$`与设备`uart:~$`是不同提示符，复制命令时不输入提示符。以下保留官方目标和输出，不表示本次已运行或烧录。

```sh
west build -b robokit1 samples/subsys/llext/shell_loader
```

> 注意：可能需要禁用内存保护才能运行此示例，例如ARM上的`CONFIG_ARM_MPU=n`、Xtensa上的`CONFIG_XTENSA_MMU=n`／`CONFIG_XTENSA_MPU=n`，或RISC-V上的`CONFIG_RISCV_PMP=n`。类似选项的完整列表见[`tests/subsys/llext/no_mem_protection.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/llext/no_mem_protection.conf)。

本例还包含一个很简单的扩展源码[`samples/subsys/llext/shell_loader/hello_world.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/llext/shell_loader/hello_world.c)，可用来测试LLEXT功能。通过Zephyr构建系统，可将其编译为`build/hello_world.llext`：

```sh
$ ninja -C build -vvv hello_world_ext
```

如果主机安装了Zephyr SDK，并且匹配的工具链已在`PATH`中，也可直接生成同一个目标文件。选择匹配目标的前缀，例如ARM用`arm-zephyr-eabi-`，Xtensa用`xtensa-<soc>_zephyr-elf-`，RISC-V用`riscv64-zephyr-elf-`：

```sh
$ <toolchain-prefix>gcc -mlong-calls -c -o build/hello_world.llext samples/subsys/llext/shell_loader/hello_world.c
```

> 译注：`<toolchain-prefix>`和`<soc>`是占位符，执行时替换为实际值。此命令中的`-mlong-calls`保留原例，不表示每种架构都接受相同选项；目标CPU、ABI和其他编译选项应与主应用相匹配，见[构建扩展](P002_构建扩展.md)。

> 注意：每种目标架构都必须重新构建扩展。ARM扩展不能在Xtensa或RISC-V上运行，反之亦然。加载器可能接受十六进制字符串，但调用扩展时，CPU会因不识别指令流而触发异常（Trap）。

> 注意：LLEXT默认只导入扩展通过[`EXPORT_SYMBOL`](P015_导出符号API.md#ga0188531646d69e784eccf85bd4fb34aa)宏显式导出的符号。使用该宏编译需要完整Zephyr构建系统，或至少使用LLEXT EDK。为简化本例，应用启用[`CONFIG_LLEXT_IMPORT_ALL_GLOBALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT_IMPORT_ALL_GLOBALS)，使用扩展ELF中定义的全部全局符号。大型扩展不建议这样做，因为内存占用会显著增加。

可用常规binutils工具检查已编译扩展的符号、节和重定位（Relocations），再用其他工具转换为`llext load_hex`命令可用的十六进制字符串。下面的输出由ARM工具链产生；其他架构的重定位类型和指令列表不同，但流程相同。

```text
$ <toolchain-prefix>objdump -r -d -x build/hello_world.llext

      hello_world.elf:     file format elf32-littlearm
      hello_world.elf
      architecture: armv4t, flags 0x00000011:
      HAS_RELOC, HAS_SYMS
      start address 0x00000000
      private flags = 0x5000000: [Version5 EABI]

      Sections:
      Idx Name          Size      VMA       LMA       File off  Algn
        0 .text         00000038  00000000  00000000  00000034  2**2
                        CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
        1 .data         00000000  00000000  00000000  0000006c  2**0
                        CONTENTS, ALLOC, LOAD, DATA
        2 .bss          00000000  00000000  00000000  0000006c  2**0
                        ALLOC
        3 .rodata       00000025  00000000  00000000  0000006c  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        4 .comment      00000021  00000000  00000000  00000091  2**0
                        CONTENTS, READONLY
        5 .ARM.attributes 0000002a  00000000  00000000  000000b2  2**0
                        CONTENTS, READONLY
      SYMBOL TABLE:
      00000000 l    df *ABS*  00000000 hello_world.c
      00000000 l    d  .text  00000000 .text
      00000000 l    d  .data  00000000 .data
      00000000 l    d  .bss   00000000 .bss
      00000000 l    d  .rodata        00000000 .rodata
      00000000 l     O .rodata        00000004 number
      00000000 l    d  .comment       00000000 .comment
      00000000 l    d  .ARM.attributes        00000000 .ARM.attributes
      00000000 g     F .text  00000034 hello_world
      00000000         *UND*  00000000 printk



      Disassembly of section .text:

      00000000 <hello_world>:
         0:   b580            push    {r7, lr}
         2:   af00            add     r7, sp, #0
         4:   4b08            ldr     r3, [pc, #32]   ; (28 <hello_world+0x28>)
         6:   0018            movs    r0, r3
         8:   4b08            ldr     r3, [pc, #32]   ; (2c <hello_world+0x2c>)
         a:   f000 f813       bl      34 <hello_world+0x34>
         e:   222a            movs    r2, #42 ; 0x2a
        10:   4b07            ldr     r3, [pc, #28]   ; (30 <hello_world+0x30>)
        12:   0011            movs    r1, r2
        14:   0018            movs    r0, r3
        16:   4b05            ldr     r3, [pc, #20]   ; (2c <hello_world+0x2c>)
        18:   f000 f80c       bl      34 <hello_world+0x34>
        1c:   46c0            nop                     ; (mov r8, r8)
        1e:   46bd            mov     sp, r7
        20:   bc80            pop     {r7}
        22:   bc01            pop     {r0}
        24:   4700            bx      r0
        26:   46c0            nop                     ; (mov r8, r8)
        28:   00000004        .word   0x00000004
                              28: R_ARM_ABS32 .rodata
        2c:   00000000        .word   0x00000000
                              2c: R_ARM_ABS32 printk
        30:   00000014        .word   0x00000014
                              30: R_ARM_ABS32 .rodata
        34:   4718            bx      r3
        36:   46c0            nop                     ; (mov r8, r8)

$ xxd -p -c 99999 build/hello_world.llext
7f454c4601010100000000000000000001002800010000000000000000000000680200000000000534000000000028000b000a0080b500af084b1800084b00f013f82a22074b11001800054b00f00cf8c046bd4680bc01bc0047c0460400000000000000140000001847c0462a00000068656c6c6f20776f726c640a0000000041206e756d62657220697320256c750a00004743433a20285a65706879722053444b20302e31362e31292031322e322e30004129000000616561626900011f000000053454000602080109011204140115011703180119011a011e06000000000000000000000000000000000100000000000000000000000400f1ff000000000000000000000000030001000000000000000000000000000300030000000000000000000000000003000400000000000000000000000000030005000f00000000000000000000000000050012000000000000000400000001000500190000000000000000000000000001000f0000002800000000000000000001001900000034000000000000000000010000000000000000000000000003000600000000000000000000000000030007001c000000010000003400000012000100280000000000000000000000100000000068656c6c6f5f776f726c642e63002464006e756d6265720024740068656c6c6f5f776f726c64007072696e746b000028000000020500002c000000020e00003000000002050000002e73796d746162002e737472746162002e7368737472746162002e72656c2e74657874002e64617461002e627373002e726f64617461002e636f6d6d656e74002e41524d2e6174747269627574657300000000000000000000000000000000000000000000000000000000000000000000000000000000000000001f0000000100000006000000000000003400000038000000000000000000000004000000000000001b000000090000004000000000000000fc0100001800000008000000010000000400000008000000250000000100000003000000000000006c00000000000000000000000000000001000000000000002b0000000800000003000000000000006c0000000000000000000000000000000100000000000000300000000100000002000000000000006c00000025000000000000000000000004000000000000003800000001000000300000000000000091000000210000000000000000000000010000000100000041000000030000700000000000000000b20000002a0000000000000000000000010000000000000001000000020000000000000000000000dc000000f0000000090000000d000000040000001000000009000000030000000000000000000000cc0100002f0000000000000000000000010000000000000011000000030000000000000000000000140200005100000000000000000000000100000000000000
```

本例有3处绝对重定位（Absolute Relocation）`R_ARM_ABS32`，其中两处应保存字符串所在`.rodata`节内的地址，另一处保存`printk`函数符号的地址。加载时，LLEXT将`.text`节内相应值替换为真实内存地址，使`printk`能够正确使用示例中的字符串。

> 译注：输出中的`hello_world.elf`与命令中的`build/hello_world.llext`名称不同，原记录按原样保留。十六进制字符串是官方ARM二进制示例，不是通用架构的扩展文件；为其他目标加载时，应使用自己实际生成的文件与载荷。

<a id="running"></a>

## 10.4\_运行（Running）

开发板启动后会显示Shell提示符。LLEXT相关命令都位于`llext`子命令下，可通过`llext help`查看：

```text
uart:~$ llext help
llext - Loadable extension commands
Subcommands:
  list          :List loaded extensions and their size in memory
  load_hex      :Load an elf file encoded in hex directly from the shell input.
                 Syntax:
                 <ext_name> <ext_hex_string>
  unload        :Unload an extension by name. Syntax:
                 <ext_name>
  list_symbols  :List extension symbols. Syntax:
                 <ext_name>
  call_fn       :Call extension function with prototype void fn(void). Syntax:
                 <ext_name> <function_name>
```

命令说明的中文对应如下：

| 子命令 | 用途与参数 |
| --- | --- |
| `list` | 列出已加载扩展及其内存大小。 |
| `load_hex` | 从Shell输入直接加载十六进制编码的ELF文件；参数为`<ext_name> <ext_hex_string>`。 |
| `unload` | 按名称卸载扩展；参数为`<ext_name>`。 |
| `list_symbols` | 列出扩展符号；参数为`<ext_name>`。 |
| `call_fn` | 调用原型为`void fn(void)`的扩展函数；参数为`<ext_name> <function_name>`。 |

使用上面生成的十六进制字符串加载扩展：

```text
uart:~$ llext load_hex hello_world 7f454c4601010100000000000000000001002800010000000000000000000000680200000000000534000000000028000b000a0080b500af084b1800084b00f013f82a22074b11001800054b00f00cf8c046bd4680bc01bc0047c0460400000000000000140000001847c0462a00000068656c6c6f20776f726c640a0000000041206e756d62657220697320256c750a00004743433a20285a65706879722053444b20302e31362e31292031322e322e30004129000000616561626900011f000000053454000602080109011204140115011703180119011a011e06000000000000000000000000000000000100000000000000000000000400f1ff000000000000000000000000030001000000000000000000000000000300030000000000000000000000000003000400000000000000000000000000030005000f00000000000000000000000000050012000000000000000400000001000500190000000000000000000000000001000f0000002800000000000000000001001900000034000000000000000000010000000000000000000000000003000600000000000000000000000000030007001c000000010000003400000012000100280000000000000000000000100000000068656c6c6f5f776f726c642e63002464006e756d6265720024740068656c6c6f5f776f726c64007072696e746b000028000000020500002c000000020e00003000000002050000002e73796d746162002e737472746162002e7368737472746162002e72656c2e74657874002e64617461002e627373002e726f64617461002e636f6d6d656e74002e41524d2e6174747269627574657300000000000000000000000000000000000000000000000000000000000000000000000000000000000000001f0000000100000006000000000000003400000038000000000000000000000004000000000000001b000000090000004000000000000000fc0100001800000008000000010000000400000008000000250000000100000003000000000000006c00000000000000000000000000000001000000000000002b0000000800000003000000000000006c0000000000000000000000000000000100000000000000300000000100000002000000000000006c00000025000000000000000000000004000000000000003800000001000000300000000000000091000000210000000000000000000000010000000100000041000000030000700000000000000000b20000002a0000000000000000000000010000000000000001000000020000000000000000000000dc000000f0000000090000000d000000040000001000000009000000030000000000000000000000cc0100002f0000000000000000000000010000000000000011000000030000000000000000000000140200005100000000000000000000000100000000000000
```

随后可用`list`查看已加载扩展，用`list_symbols`打印其符号，并通过`call_fn`执行扩展导出的`hello_world`函数：

```text
uart:~$ llext call_fn hello_world hello_world
hello world
```

<a id="loading-multiple-extensions"></a>

## 10.5\_加载多个扩展（Loading Multiple Extensions）

每次`load_hex`调用都会分配自己的ELF缓冲区，并按扩展名称跟踪。针对该名称调用`unload`时释放缓冲区，因此多个扩展可以同时保持加载状态，并分别调用：

```text
uart:~$ llext load_hex hello_world <hex>
uart:~$ llext load_hex worker <hex>
uart:~$ llext list
| Name             | Size         |
|      hello_world |          ... |
|           worker |          ... |
uart:~$ llext call_fn hello_world hello_world
uart:~$ llext call_fn worker run
uart:~$ llext unload worker
```

同时加载的扩展数量受[`subsys/llext/shell.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/shell.c)中的`LLEXT_SHELL_MAX_LOADED`槽位数量（Slot Count）限制，默认值为4。若需要更多并发扩展，可在该处调整。

<a id="see-also"></a>

## 10.6\_另请参阅（See Also）

- [LLEXT API入口](P006_扩展API入口.md)。
- [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/llext/shell_loader)。
- 译注：[扩展源码](../../../samples/subsys/llext/shell_loader/hello_world.c)、[内存保护配置](../../../tests/subsys/llext/no_mem_protection.conf)与[Shell实现](../../../subsys/llext/shell.c)为仓库相对源码引用；实际版本可能与官网不同。


[上一章](P009_模块式扩展示例.md) · [返回大纲](大纲.md) · [下一章](P011_扩展管理API.md)
