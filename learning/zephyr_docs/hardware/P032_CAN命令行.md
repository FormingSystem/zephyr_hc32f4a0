---
id: learning.zephyr-docs.hardware.periph-can-shell
title: CAN命令行
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/can/shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第32章\_CAN命令行

原文：[CAN Shell](https://docs.zephyrproject.org/latest/hardware/peripherals/can/shell.html)。读取日期：2026-10-13，`latest`。

## 32.1\_启用CAN交互入口

**控制器局域网（Controller Area Network，CAN）**的 **命令解释器（Shell）**提供 `can` 及子命令，用于交互探索 **应用程序编程接口（Application Programming Interface，API）**，无需单独编写测试应用；也可加入已有应用辅助调试。它覆盖控制器检查、配置、收发帧和总线恢复。

必须启用Kconfig配置项 [`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN) 和 [`CONFIG_CAN_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_SHELL)。以下可选项增加能力：

| Kconfig配置项 | 功能 |
| --- | --- |
| [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE) | 启用 **可变数据速率CAN（CAN with Flexible Data-Rate，CAN FD）**的子命令，例如数据阶段时序设置。 |
| [`CONFIG_CAN_RX_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_RX_TIMESTAMP) | 打印接收帧时间戳。 |
| [`CONFIG_CAN_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STATS) | 在 `can show` 中显示控制器统计，还依赖统计子系统配置项 [`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)。 |
| [`CONFIG_CAN_MANUAL_RECOVERY_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MANUAL_RECOVERY_MODE) | 启用手动恢复命令 `can recover`。 |

从Zephyr源码根目录为FRDM-K64F构建带CAN Shell与统计的Hello World示例：

```shell
# From the root of the zephyr repository
west build -b frdm_k64f samples/hello_world -- -DCONFIG_SHELL=y -DCONFIG_CAN=y -DCONFIG_CAN_SHELL=y -DCONFIG_STATS=y -DCONFIG_CAN_STATS=y
```

连接方式见[Shell说明](https://docs.zephyrproject.org/latest/services/shell/index.html#shell-api)。除非禁用Kconfig配置项 [`CONFIG_SHELL_HELP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_HELP)，`can` 及子命令都可用 `-h` / `--help` 显示帮助，参数支持Tab补全。

所有子命令第一个参数都是CAN控制器设备名，也支持补全。启用Kconfig配置项 [`CONFIG_DEVICE_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_SHELL) 后，可用 `device list` 列出设备；下文原例统一用设备名 `can@0`。`uart:~$` 是设备提示符，不是主机命令的一部分。

## 32.2\_检查控制器

`can show` 显示核心时钟、最高位率、接收过滤器数量、能力、当前模式、状态、错误计数和时序范围等。接收/发送在输出中分别缩写为rx/tx；std/ext表示标准/扩展帧；**重同步跳转宽度（Synchronization Jump Width，SJW）**及各时序段见[CAN控制器](P030_CAN控制器.md)。原输出为：

```text
uart:~$ can show can@0
core clock:      144000000 Hz
max bitrate:     5000000 bps
max std filters: 15
max ext filters: 15
capabilities:    normal loopback listen-only fd
mode:            normal
state:           stopped
rx errors:       0
tx errors:       0
timing:          sjw 1..128, prop_seg 0..0, phase_seg1 2..256, phase_seg2 2..128, prescaler 1..512
timing data:     sjw 1..16, prop_seg 0..0, phase_seg1 1..32, phase_seg2 1..16, prescaler 1..32
transceiver:     passive/none
statistics:
  bit errors:    0
    bit0 errors: 0
    bit1 errors: 0
  stuff errors:  0
  crc errors:    0
  form errors:   0
  ack errors:    0
  rx overruns:   0
```

**原文注意：**只有启用 [`CONFIG_CAN_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STATS) 才显示统计。输出中的 `bit errors` 为位错误、`stuff errors` 为填充错误、`crc errors` 为 **循环冗余校验（Cyclic Redundancy Check，CRC）**错误、`form errors` 为格式错误、`ack errors` 为 **确认（Acknowledgement，ACK）**错误、`rx overruns` 为接收溢出。数值是原例，不是当前硬件测量值。

## 32.3\_配置时序与位率

控制器必须处于 **停止状态（Stopped State）**才能修改模式和时序，启动后的初始控制器状态就是停止；初始模式为normal（普通），时序由设备树属性 `bitrate`、`sample-point`、`bitrate-data`、`sample-point-data` 给出。

经典CAN位率或CAN FD仲裁阶段位率由 `can bitrate` 配置，单位为bit/s：

```shell
uart:~$ can bitrate can@0 125000
setting bitrate to 125000 bps
```

启用 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE) 时，可用 `can dbitrate` 设置数据阶段位率，同样以bit/s计：

```shell
uart:~$ can dbitrate can@0 1000000
setting data bitrate to 1000000 bps
```

两者还可用位置参数指定以千分数表示的 **采样点（Sample Point）**和以 **时间量子（Time Quanta）**表示的SJW，具体参数顺序查交互帮助。`can timing` 与 `can dtiming` 可直接设置原始位时序，所需参数也由帮助列出。

## 32.4\_模式、启动与停止

`can mode` 设置控制器模式，原例启用 **回环模式（Loopback Mode）**：

```shell
uart:~$ can mode can@0 loopback
setting mode 0x00000001
```

同一命令可组合多个模式，例如 `can mode can@0 fd loopback` 同时启用CAN FD与回环；厂商专用模式可用十六进制值指定。

时序和模式配置好后，`can start` 启动帧收发：

```shell
uart:~$ can start can@0
starting can@0
```

重新配置前先用 `can stop` 停止：

```shell
uart:~$ can stop can@0
stopping can@0
```

## 32.5\_添加接收过滤器

接收前需配置一个或多个过滤器。`can filter add` 接收十六进制CAN标识符及可选的十六进制掩码，掩码决定哪些位参与匹配，更多参数见命令帮助。

```shell
uart:~$ can filter add can@0 010
adding filter with standard (11-bit) CAN ID 0x010, CAN ID mask 0x7ff, data frames 1, RTR frames 0, CAN FD frames 0
filter ID: 0
```

原例返回过滤器编号0，移除时要使用此编号。日志中的 **远程传输请求（Remote Transmission Request，RTR）**标记区分请求帧和数据帧；默认示例匹配11位标准标识符 `0x010`。

## 32.6\_读取接收输出

匹配过滤器的帧输出到Shell。下列为原页给出的若干格式示例，并非宣称都由上一条单独过滤器接受：

```text
# Dev Flags    ID   Size  Data bytes
can0  --       010   [8]  01 02 03 04 05 06 07 08
can0  B-       010  [08]  01 02 03 04 05 06 07 08
can0  BP       010  [03]  01 aa bb
can0  --  00000010   [0]
can0  --       010   [1]  20
can0  --       010   [8]  remote transmission request
```

各列含义如下：

| 列 | 含义 |
| --- | --- |
| Dev | 接收帧的设备名称。 |
| Flags中的B | CAN FD **位率切换（Bit Rate Switch，BRS）**标志已置位。原文用词为Baud Rate Switch。 |
| Flags中的P | CAN FD **错误状态指示（Error State Indicator，ESI）**已置位，发送节点处于错误被动状态。 |
| Flags中的 `-` | 相应标志未置位。 |
| ID为 `010` | 11位标准标识符的十六进制显示，本例为 `0x10`。 |
| ID为 `00000010` | 29位扩展标识符的十六进制显示，本例也为 `0x10`。 |
| Size为 `[8]` | 十进制数据长度，表示经典CAN的8字节。 |
| Size为 `[08]` | 十进制数据长度，表示CAN FD的8字节。 |
| Data bytes | 十六进制数据字节；`01 ... 08` 表示数值1至8。 |
| `remote transmission request` | RTR帧，不携带数据字节。 |

启用 [`CONFIG_CAN_RX_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_RX_TIMESTAMP) 后，每行前面还有CAN控制器自由运行时间戳计数器的值。

## 32.7\_移除过滤器与抓取全部帧

使用添加时返回的过滤器编号移除：

```shell
uart:~$ can filter remove can@0 0
removing filter with ID 0
```

也可使用 `can dump`：它添加接受全部标准11位和扩展29位接收帧的过滤器，启动控制器，并将收到的帧打印到Shell：

```shell
uart:~$ can dump can@0
dumping CAN RX frames on device can@0, press Ctrl+C to exit
```

按Ctrl+C退出后，自动移除所加过滤器，并再次停止控制器。

## 32.8\_发送帧

`can send` 将帧加入发送队列，参数是十六进制CAN标识符和可选的十六进制数据字节，其他参数见交互帮助：

```shell
uart:~$ can send can@0 010 1 2 3 4 5 6 7 8
enqueuing CAN frame #2 with standard (11-bit) CAN ID 0x010, RTR 0, CAN FD 0, BRS 0, DLC 8
CAN frame #2 successfully sent
```

日志中的DLC是 **数据长度码（Data Length Code）**；帧编号 `#2` 是原例发送跟踪编号，不是CAN标识符。

## 32.9\_总线恢复

`can recover` 从 **总线关闭（Bus-off）**状态发起手动恢复：

```shell
uart:~$ can recover can@0
recovering, no timeout
```

可选恢复超时以毫秒表示；省略时一直等待恢复成功。该子命令仅在启用 [`CONFIG_CAN_MANUAL_RECOVERY_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MANUAL_RECOVERY_MODE) 后可用。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CAN收发器](P031_CAN收发器.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：CRC循环冗余校验](P033_CRC循环冗余校验.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：CAN收发器](P031_CAN收发器.md) · [下一章：CRC循环冗余校验](P033_CRC循环冗余校验.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
