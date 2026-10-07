---
id: hc32-usb-stdio
title: USB1 标准输入输出实验
kind: lab
status: maintained
domains: [zephyr, usb, libc, hc32]
---

<!-- SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_USB1\_标准输入输出实验

## 1.1\_从 USB 字符收发到 printf 和 scanf

本例用于已完成 HC32 USB 适配的工程，目标为 `uyup_rpi_a/hc32f4a0pitb`。硬件、时钟、DAP 切换和 USB 端口依据沿用 [USB 日志实验](../usb_console/README.md)。USB1 是主芯片的 CDC ACM 虚拟串口；USB2/DAP 用于烧录。两个示例分别构建，烧录哪个就运行哪个。

```mermaid
flowchart LR
    A[电脑串口终端] --> B[USB1 CDC ACM 接收]
    B --> C[Zephyr console_getchar]
    C --> D[本例接入 Picolibc stdin]
    D --> E[scanf 或 getchar 或 fgets]
    E --> F[应用处理]
    F --> G[printf 或 puts 或 fprintf]
    G --> H[Zephyr stdout 控制台]
    H --> A
```

`printf()` 格式化输出到 `stdout`，`scanf()` 从 `stdin` 读取并转换输入。它们本身不决定使用 USB 还是硬件串口。本例的接线分成三部分：

| 层次 | 原生配置或实现 | 作用 |
| --- | --- | --- |
| USB 控制台 | Zephyr `cdc-acm-console` snippet | 初始化新 USB 栈，将 `zephyr,console` 选为 CDC ACM |
| 标准输出 | `CONFIG_PICOLIBC=y`、`CONFIG_STDOUT_CONSOLE=y` | `printf`、`puts`、`stderr` 经 Zephyr 控制台发往 USB1 |
| 标准输入 | `CONFIG_CONSOLE_SUBSYS=y`、`CONFIG_CONSOLE_GETCHAR=y` 加本例 `usb_stdio_init()` | Zephyr 提供可阻塞的字符接收；应用把它接到 Picolibc 的 `stdin` |

**`usb_stdio_init()` 是本例定义的函数，声明在 `src/usb_stdio.h`，实现在 `src/usb_stdio.c`，不是 Zephyr 原生 API。** 它调用 `console_init()`，再使用 Picolibc 的 `FDEV_SETUP_STREAM` 初始化现有 `stdin` 的读取回调。接入代码限定使用 Picolibc；更换 Newlib 等 C 库时必须按对应接口调整。无需改动 USB 驱动、板级 DTS、系统安装的库或定义不存在的 `CONFIG_STDIN_CONSOLE`。

源码依据为本仓库的 `lib/libc/picolibc/stdio.c`、`drivers/console/uart_console.c`、`subsys/console/getchar.c` 和当前 SDK 的 `stdio.h`；通用背景见 [Zephyr Picolibc 文档](https://docs.zephyrproject.org/latest/develop/languages/c/picolibc.html)及 [Zephyr 字符控制台示例](https://docs.zephyrproject.org/latest/samples/subsys/console/getchar/README.html)。在线文档可能跟随上游变化，本工程行为以实际源码和生成配置为准。

## 1.2\_构建、下载和打开终端

以下命令在**已集成移植的工程根目录、MSYS2 UCRT64 Bash** 执行。Windows 文件管理器路径不能原样作为 Bash 路径；复制后可用 `cygpath -u` 转换，或使用 UCRT64 的 `/盘符/目录` 形式。先进入自己的工程根目录并完成 SDK/根 `.venv` 配置；`scripts/project_env.py` 是本工程已有工具入口。

```bash
source .venv/Scripts/activate
python scripts/project_env.py exec cmake -S samples/usb_stdio -B build/usb-stdio -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb
python scripts/project_env.py exec cmake --build build/usb-stdio
python scripts/verify_hc32_image.py --build-dir build/usb-stdio
python -m pyocd list
python -m pyocd flash --project . --config debug/pyocd.yaml --erase sector build/usb-stdio/zephyr/zephyr.hex
python -m serial.tools.list_ports -v
```

仅连接一个 DAP 时可直接使用上述下载命令；多个探针时按查询结果加 `--uid`。固件会替换板上原有应用。使用 USB1 的 `VID:PID=2FE3:0004` 端口，本机本轮枚举为 COM8，编号以实际结果为准。保持 USB2/DAP 为已验证的 2.x 模式，恢复切换见硬件说明。

在工程根目录已激活的 UCRT64 环境打开串口：

```bash
python -m serial.tools.miniterm COM8 115200 --raw --echo --eol LF
```

miniterm 默认置 DTR，`--echo` 在电脑上显示自己输入的字符，`--eol LF` 将回车发送为 LF，Ctrl+] 退出。本例设备端不重复回显输入。其他串口工具选择 115200、8N1、无硬件流控、DTR 打开，并启用本地回显；CR、LF、CRLF 均可作为行尾。这里的 115200 是 CDC 线路编码，不是 USB 总线速率。

Ubuntu 22.04 使用 `source .venv/bin/activate`，并把 COM8 换为查询到的 `/dev/ttyACM*`；本轮实际硬件验收在 Windows 完成。关闭并重新打开串口后，可直接输入数字；启动提示只打印一次，不会因为重开串口而重播。

输入 `123` 后按回车：

```text
number> 123
value=123, twice=246
number>
```

输入 `abc` 或 `12abc` 会报告格式错误，然后可以继续输入 `-7`。示例一次接受一个十进制整数，最多 9 个字符（包含正负号），剩余内容仅允许空白。位宽限制保证转换及乘二在当前 32 位 `int` 范围内；它不是任意整数输入校验器。

## 1.3\_在自己的应用中使用

保留本例 `prj.conf`、CMake 中的 snippet 和 `src/usb_stdio.c`，将业务代码放在 `src/main.c`。初始化一次后便可调用标准库函数：

```c
#include <stdio.h>
#include "usb\_stdio.h" /* 本例头文件，不是 Zephyr 标准头文件 */

/* main 中先调用 usb_stdio_init()，检查结果并等待 USB 主机 DTR。 */
int value;

printf("number> ");
fflush(stdout);
if (scanf("%9d", &value) == 1) {
    printf("value=%d\n", value);
}
```

上段只展示标准调用关系；完整错误处理见 `src/main.c` 的循环和 `finish_line()`，不要删除后直接用于反复交互。`scanf` 遇到不能匹配的字符会将其留在输入中，不清理会让后续调用反复失败。格式串末尾不要加 `\n`（如 `"%d\n"`），否则它会继续等待下一个非空白字符。

字符串使用数组和长度限制，例如 `char name[32]; scanf("%31s", name);`，并检查返回值；读取含空格的整行可用 `fgets()`。切换数字读取与行读取时要处理残留换行。面向不受控的复杂输入，优先 `fgets()` 获取有限长度的一整行，再用 `strtol()` 检查范围、结束位置和错误。

本例显式选择 `CONFIG_PICOLIBC_IO_FLOAT=y`，库具有浮点格式化和扫描能力。浮点输入使用 `float` 对应 `%f`、`double` 对应 `%lf`；硬件验收记录以实际测试过的整数用例为准。

## 1.4\_阻塞、回显与使用边界

`scanf()` 没有输入时会阻塞**调用它的线程**。本例接收采用中断缓冲和等待事件，蓝灯由独立的系统工作队列每 500 ms 翻转，所以等待输入时蓝灯仍能运行。不要在中断、系统工作队列处理函数或有实时期限的控制线程里调用阻塞输入。

当前 `stdin` 只有主线程一个消费者，不要同时启动 shell、`console_getline` 或另一段 `uart_poll_in` 去抢同一 USB 控制台的数据。串口断开不等于标准文件 EOF，等待中的读取可能继续阻塞；本例不实现会话取消、自动清空半行或串口重连通知。

本例关闭异步日志，避免提示符被日志穿插。它展示标准输入输出，不提供 shell 的历史记录、方向键及退格编辑。使用终端本地回显时，在按回车前输入的字符已陆续发送到板端；要编辑复杂命令可改用整行发送工具或另做 shell 实验。接收缓冲为 128 字节，不用于无限量高速粘贴。

构建、下载回读和实板交互的实际结果统一记录于[移植状态](../../project-docs/porting-status.md)。
