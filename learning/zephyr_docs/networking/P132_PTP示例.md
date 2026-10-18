---
id: learning.zephyr-docs.networking.page-132
title: PTP示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ptp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_PTP示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ptp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 的精确时间协议（Precision Time Protocol，PTP）示例启用 IEEE 1588-2019 支持。

源码位于 [`samples/net/ptp`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ptp)，可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ptp/README.rst/..)。

## 2. 前提条件（Requirements）

用于调试的通用主机连接方法见[native_sim 板联网](P008_native_sim联网.md#networking-with-native-sim)。

测试嵌入式设备时，必须使用支持时间戳的以太网 PHY。原文说明，曾在 [Nucleo H563ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#nucleo_h563zi) 的以太网 PHY 上，与 ptp4l 守护进程、GPS 时钟直连、支持 PTP 的交换机以及 GPS 时钟加 PTP 交换机的组合进行测试。

## 3. 构建和运行（Building and Running）

可按联网文档在[原生模拟器 native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 中运行此应用，也可使用 [Nucleo H563ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#nucleo_h563zi)、[Nucleo H743ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html#nucleo_h743zi)、[Nucleo H745ZI-Q](https://docs.zephyrproject.org/latest/boards/st/nucleo_h745zi_q/doc/index.html#nucleo_h745zi_q)、[Nucleo F767ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_f767zi/doc/index.html#nucleo_f767zi) 或 [FRDM-MCXN947](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#frdm_mcxn947) 等嵌入式设备。

PTP 仅支持具备以太网端口、且支持采集已发送和已接收帧时间戳的开发板。

从工具链和依赖已准备好的 Zephyr 源码根目录构建，替换原文的板目标占位符：

```sh
west build -b <board to use> samples/net/ptp
```

## 4. 解读 net ptp 输出（Interpreting net ptp Output）

Shell 提供两种互补视图：

- `net ptp`：实例级摘要，包括时钟标识、当前／父数据集、最佳外部时间发送端，以及各端口状态表。
- `net ptp <port>`，例如 `net ptp 1`：指定端口的详细视图，包括配置、运行计数器和定时器。

### 4.1 作为最高主时钟（Grandmaster）

`net ptp` 的原文输出示例：

```text
uart:~$ net ptp
PTP Instance:
Clock ID      : 02:00:00:FF:FE:00:00:01
Clock Type    : ORDINARY
Protocol      : UDP/IPv4
Domain        : 0
Priorities    : 128 / 128
Time source   : INTERNAL_OSCILLATOR (0xa0)
Ports         : 1
TR only       : no
PHC now       : 95.703698720

Current dataset:
steps_rm      : 0
offset_from_tt: 0 ns
mean_delay    : 0 ns
sync status   : stable

Parent/GM dataset:
grandmaster   : 02:00:00:FF:FE:00:00:01 (p1=128 p2=128 class=248 acc=0xfe)
parent port   : 02:00:00:FF:FE:00:00:01-0
UTC offset    : 37

Best foreign transmitter : none

Port  Interface  State
   1          1  GRAND_MASTER
```

`net ptp 1` 的原文输出示例：

```text
uart:~$ net ptp 1
PTP Port 1:
interface            : 1
port identity        : 02:00:00:FF:FE:00:00:01-1

Configuration:
state                : GRAND_MASTER
enabled              : yes
protocol             : UDP/IPv4
time transmitter only: no
announce log itv     : 1
announce timeout     : 5
sync log itv         : 0
min delay_req log itv: 0
delay mechanism      : E2E
delay asymmetry      : 0 ns
mean link delay      : 0 ns

Runtime:
seq announce/delay/signaling/sync: 66 / 0 / 0 / 132
timeouts bits      : announce=0 delay=0 sync=0 qualification=0
timer remaining ms : announce=1677 delay=0 sync=677 qualification=0
PHC now            : 145.138244620
best foreign       : none
```

### 4.2 作为时间接收端（Time Receiver）

`net ptp` 的原文输出示例：

```text
uart:~$ net ptp
PTP Instance:
Clock ID      : 02:00:00:FF:FE:00:00:01
Clock Type    : ORDINARY
Protocol      : UDP/IPv4
Domain        : 0
Priorities    : 128 / 128
Time source   : INTERNAL_OSCILLATOR (0xa0)
Ports         : 1
TR only       : no
PHC now       : 1774472701.341945363

Current dataset:
steps_rm      : 2
offset_from_tt: 22 ns
mean_delay    : 639 ns
sync status   : stable

Parent/GM dataset:
grandmaster   : 02:00:00:FF:FE:00:00:10 (p1=128 p2=128 class=6 acc=0x21)
parent port   : 02:00:00:FF:FE:00:00:20-2
UTC offset    : 37

Best foreign transmitter : 02:00:00:FF:FE:00:00:20-2 (records=2)
Dataset                : p1=128 p2=128 steps_rm=1 receiver=02:00:00:FF:FE:00:00:01-1

Port  Interface  State
   1          1  TIME_RECEIVER
```

`net ptp 1` 的原文输出示例：

```text
uart:~$ net ptp 1
PTP Port 1:
interface            : 1
port identity        : 02:00:00:FF:FE:00:00:01-1

Configuration:
state                : TIME_RECEIVER
enabled              : yes
protocol             : UDP/IPv4
time transmitter only: no
announce log itv     : 1
announce timeout     : 5
sync log itv         : 0
min delay_req log itv: 0
delay mechanism      : E2E
delay asymmetry      : 0 ns
mean link delay      : 0 ns

Runtime:
seq announce/delay/signaling/sync: 0 / 1268 / 0 / 0
timeouts bits      : announce=0 delay=0 sync=0 qualification=0
timer remaining ms : announce=9459 delay=539 sync=4408 qualification=0
PHC now            : 1774472701.764088663
best foreign       : 02:00:00:FF:FE:00:00:20-2 (p1=128 p2=128 steps_rm=1)
```

### 4.3 字段含义与角色判断

| 字段 | 含义 |
| --- | --- |
| `TR only` | 是否启用了 [`CONFIG_PTP_TIME_RECEIVER_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_TIME_RECEIVER_ONLY)，即仅作为时间接收端。 |
| `PHC now` | 从以太网 PTP 硬件时钟（PTP Hardware Clock，PHC）读取的当前时间。 |
| `steps_rm` | 到选定最高主时钟的网络步数。 |
| `offset_from_tt` | 当前相对于时间发送端的同步偏移。 |
| `mean_delay` | 当前路径延迟估计。 |
| `Best foreign transmitter` | 从网络收到的最佳 Announce 候选，用于最佳主时钟算法（Best Master Clock Algorithm，BMCA）和状态决策。 |

当状态为 `GRAND_MASTER` 且 `best foreign : none` 时，表示尚未选中符合条件的外部时间发送端，本地时钟正在充当最高主时钟。收到并选中有效 Announce 后，状态通常根据 BMCA 结果转为 `TIME_RECEIVER` 或 `PASSIVE`。

> 译注——其他输出术语：`Clock ID/Type` 是时钟标识／类型，`Protocol` 是传输协议，`Domain` 是时间域，`Priorities` 是时钟优先级，`Time source` 是时间源。`Current dataset` 为当前数据集，`Parent/GM dataset` 为父时钟／最高主时钟数据集，`UTC offset` 为 UTC 偏移。端口视图的 `Configuration` 是配置，`Runtime` 是运行状态，`seq` 为消息序号，`timeouts bits` 为超时标志，`timer remaining ms` 为定时器剩余毫秒数；这些原输出完整保留，不能当作本次执行记录。

## 5. Linux 主机准备（Setting up Linux Host）

默认情况下，Zephyr 的 PTP 不输出调试日志。可在应用配置中启用 [`CONFIG_PTP_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_LOG_LEVEL_DBG)。

首先，在 Linux Bash 中从选定的外部项目存放目录获取并构建 linuxptp：

```sh
git clone http://git.code.sf.net/p/linuxptp/code linuxptp
cd linuxptp
make
```

> 译注——文件来源：`linuxptp` 是这条克隆命令取得的外部工具目录，不是本示例自行生成的 Zephyr 源码。编译需要该项目要求的主机工具与依赖；成功生成 `ptp4l` 后，再从其所在目录启动以下守护进程。

## 6. Linux 主机连接嵌入式设备（Use Linux Host with an Embedded Device）

### 6.1 端到端时延机制（E2E）

创建 ptp4l 配置文件，例如 `e2e.cfg`，内容如下：

```ini
[global]
# Delay mechanism must match your configuration
delay_mechanism        E2E

# Use hardware timestamping if your NIC supports it
time_stamping          hardware

# Choose the transport that matches your network:
# - L2 = EtherType 0x88f7 (typical in TSN/industrial, needs L2 reachability)
# - UDPv4 = common in IT networks / routed segments
network_transport      UDPv4

# Must match switch domain
domainNumber           0

# Message rates (adjust as needed)
logSyncInterval        -3
logMinDelayReqInterval -3

# Quality-of-life
tx_timestamp_timeout   20
summary_interval       1
```

> 译注——配置注释对照：时延机制必须与 Zephyr 配置一致；网卡支持时使用硬件时间戳。传输协议按网络选择，`L2` 使用 EtherType `0x88f7`，常见于 TSN／工业网络并要求二层可达；`UDPv4` 常用于 IT 网络或路由网段。`domainNumber` 必须与交换机时间域一致；消息速率按需调整。末尾参数设置发送时间戳等待超时及摘要输出间隔。

按以下方式启动 E2E 配置：

```sh
sudo ./ptp4l -i zeth -f /path/to/config/e2e.cfg -m
```

> 译注——可移植位置：`/path/to/config/e2e.cfg` 是官方原文的配置文件占位路径。若按本节把文件创建在当前 linuxptp 目录中，实际参数可用 `-f ./e2e.cfg`。`zeth` 同样须换成连接设备的实际接口；硬件时间戳配置需要所选网卡具备对应能力。

### 6.2 对等时延机制（P2P）

如果 Zephyr 使用 [`CONFIG_PTP_DELAY_MECHANISM_P2P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_DELAY_MECHANISM_P2P)，则另建 `p2p.cfg`，在 Linux 主机也使用 P2P：

```ini
[global]
delay_mechanism         P2P
time_stamping           hardware
network_transport       UDPv4
domainNumber            0
logSyncInterval         -3
logMinPdelayReqInterval -3
tx_timestamp_timeout    20
summary_interval        1
```

Zephyr 当前支持两步式（Two-step）P2P 时延测量。一步式 `Pdelay_Resp` 会被拒绝并记录日志。

启动 P2P 配置：

```sh
sudo ./ptp4l -i zeth -f /path/to/config/p2p.cfg -m
```

这里的路径同样是原例占位符；配置文件在当前目录时使用 `-f ./p2p.cfg`。两端必须选用一致的时延机制、传输协议和时间域，不能只修改其中一端。

## 7. Linux 主机连接 native_sim（Use Linux Host with native_sim）

此流程使用三个或四个终端：

- 终端 1：在 `tools/net-tools` 中准备主机网络。
- 终端 2：运行 ptp4l。
- 终端 3：运行 Zephyr `native_sim` 进程。
- 可选终端 4：连接 Zephyr Shell 的 UART 伪终端（PTY）。

> 译注——目录约定：`tools/net-tools` 是原文的外部工具布局，具体获取方法见前面的主机联网文档。以下步骤分别说明当前位置，各终端均按读者实际工作区进入目录，不要求复刻作者的机器路径。

### 7.1 构建 Zephyr 应用

在具备 native_sim 构建环境的 Linux 终端，从 Zephyr 源码根目录执行：

```sh
west build -b native_sim/native/64 samples/net/ptp
```

### 7.2 创建主机 TAP 接口

终端 1 进入外部 `tools/net-tools` 目录，执行：

```sh
sudo ./net-setup.sh start
```

示例运行期间保持该接口。结束后，在同一工具目录执行清理命令：

```sh
sudo ./net-setup.sh stop
```

### 7.3 启动 ptp4l

终端 2 进入已构建 linuxptp 的目录，执行：

```sh
sudo ./ptp4l -4 -i zeth -m -q -l 6 -S
```

如果 ptp4l 先于 Zephyr 启动，暂时出现 `link down` 和 `FAULTY` 是预期情况。Zephyr 建立并启用 `zeth` 后，ptp4l 转回 `LISTENING`，继续正常 BMCA 操作。

### 7.4 启动 native_sim 镜像

终端 3 从 Zephyr 源码根目录执行构建产物：

```sh
build/zephyr/zephyr.exe
```

预期启动输出包含：

```text
uart connected to pseudotty: /dev/pts/<N>
*** Booting Zephyr OS build ... ***
<inf> net_ptp_sample: Runs forever
```

`Runs forever` 是预期输出，因为示例配置为 `CONFIG_NET_SAMPLE_RUN_DURATION=0`。

若希望自动打开终端连接 Zephyr Shell UART PTY，改用带 `-attach_uart` 的启动命令：

```sh
build/zephyr/zephyr.exe -attach_uart
```

自动连接命令由 [`CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD) 选择，它可以是任意带单个 `%s` 占位符的 Shell 命令，该占位符用于 PTY 路径。例如，在 gnome-terminal 中打开 screen，可在应用配置中设置：

```kconfig
CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD="gnome-terminal -- screen %s"
```

> 译注——前提和生效：配置值写入应用使用的配置文件并重新构建后生效。主机需要已安装且可调用 `gnome-terminal` 和 `screen`；`%s` 是运行时替换项，不应预先写死某次启动的设备节点。

### 7.5 连接 Zephyr Shell

若没有使用 `-attach_uart`，根据启动时打印的 `/dev/pts/<N>` 手动连接。已安装 screen 时，在终端 4 的 Linux Bash 中执行：

```sh
screen /dev/pts/<N>
```

未安装 screen 时可使用 socat：

```sh
socat -,rawer,echo=0,escape=0x1d /dev/pts/<N>,rawer,echo=0
```

按 Ctrl-] 退出 socat。

> 译注——PTY 路径：`<N>` 要替换为当前进程打印的实际编号；这是 Linux 动态生成的设备节点，不是仓库内文件，也不应固定为作者的编号。连接命令执行目录不限，但必须使用仍在运行的模拟进程所对应的节点。

### 7.6 查看 PTP 状态

在已连接的 Zephyr Shell 中执行：

```text
uart:~$ net ptp
uart:~$ net ptp 1
```

在 `native_sim` 上，同时看到主机和 Zephyr 发送 Announce／Sync 流量是正常情况。根据 BMCA 数据，即使存在 `best foreign`，Zephyr 仍可能保持 `GRAND_MASTER`。

示例还启用 `ptp_clock` Shell，可独立于协议状态机检查 PTP 时钟：

| 命令 | 用途 |
| --- | --- |
| `ptp_clock get <device>` | 读取 PHC 时间。 |
| `ptp_clock set <device> <seconds>` | 设置时钟时间。 |
| `ptp_clock adj <device> <seconds>` | 调整时钟时间。 |
| `ptp_clock freq <device> <ppb>` | 以十亿分之一（Parts Per Billion，ppb）为单位调整频率。 |
| `ptp_clock selftest <device> <time> <freq> <delay> <adj>` | 快速检查驱动基本行为。 |

> 译注——检查层次：`get` 用于读取；设置、调整和自测命令会作用于所选时钟。时钟驱动可读写不代表 PTP 协议已经同步成功，仍需结合端口角色、偏移与延迟等状态判断；模拟环境也不替代硬件精度验证。

## 8. 另请参阅（See Also）

[PTP 支持接口（PTP Support）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html)。


<a id="ptp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="interpreting-net-ptp-output"></a>
<a id="setting-up-linux-host"></a>
<a id="use-linux-host-with-an-embedded-device"></a>
<a id="use-linux-host-with-native-sim"></a>
<a id="step-1-build-zephyr-application"></a>
<a id="step-2-create-host-tap-interface"></a>
<a id="step-3-start-ptp4l"></a>
<a id="step-4-start-zephyr-native-sim-image"></a>
<a id="step-5-attach-to-zephyr-shell"></a>
<a id="step-6-check-ptp-state-in-zephyr-shell"></a>
<a id="see-also"></a>

[上一章](P131_网络超时.md) · [返回大纲](大纲.md) · [下一章](P133_数据包套接字示例.md)
