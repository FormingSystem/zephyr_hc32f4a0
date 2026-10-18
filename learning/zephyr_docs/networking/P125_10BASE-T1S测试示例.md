---
id: learning.zephyr-docs.networking.page-125
title: 10BASE-T1S测试示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ethernet/t1s/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_10BASE-T1S测试示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ethernet/t1s/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 10BASE-T1S 网络测试概述（10BASE-T1S Network / OA_TC6 Tests）

本测试设置用于检查 T1S 通信是否能够长期保持稳定并正常运行。可[在 GitHub 查看官方说明源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ethernet/t1s/README.rst/..)。

## 2. 硬件前提（Hardware Prerequisites）

- 一台安装 Debian 11.9、使用 6.1 内核的 [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)，连接 [LAN8670-USB 转接器](https://www.microchip.com/en-us/development-tool/ev08l38a)，配置为 10BASE-T1S 主节点，作为主机（HOST）。
- 一个或多个 [Nucleo G474RE](https://docs.zephyrproject.org/latest/boards/st/nucleo_g474re/doc/index.html#nucleo_g474re)，各自连接 [mikroe.com 的 LAN8651 “micro BUS” 模块](https://www.mikroe.com/two-wire-eth-click?srsltid=AfmBOoouUPjUzmLu19iA8wRez6GyJp5Mf_mMjckgRcvtqrBA9INjaKQe)，作为被测设备（Device Under Test，DUT）。

原文注记：`lan867x-linux-driver-2v2/linux-v6.1.21-support` 在 PC 的 Debian 12 上不能正常使用 IPv6，因此建议改用 RPI4。

> 译注——版本边界：这是官方测试说明记录的特定驱动、内核和主机组合，不能扩展成“Debian 12 本身不支持 IPv6”的结论。

### 2.1 连接和输入／输出（Connections and IOs）

下表保留官方 [Nucleo G474RE](https://docs.zephyrproject.org/latest/boards/st/nucleo_g474re/doc/index.html#nucleo_g474re) 与 [LAN8651 模块](https://www.mikroe.com/two-wire-eth-click?srsltid=AfmBOoouUPjUzmLu19iA8wRez6GyJp5Mf_mMjckgRcvtqrBA9INjaKQe)之间的接线关系：

| Nucleo G474RE | microe-lan8651 |
| --- | --- |
| 3V3 (CN 6) | 3V3 |
| GND (CN 6) | GND |
| SCK/D13 (CN 5) | SCK |
| MISO/D12 (CN 5) | SDO |
| PWM/MOSI/D11 (CN 5) | SDI |
| PWM/CS/D10 (CN 5) | CS |
| D8 (CN 5) | RST |
| D7 (CN 9) | IRQ |

## 3. 软件前提（Software Prerequisites）

为主机和 DUT 分别编译 [udp-perf](https://gitlab.com/network851614/udp-perf/-/tree/main/zephyr?ref_type=heads) 程序。原文要求把 [udp-perf 的 Zephyr 源码](https://gitlab.com/network851614/udp-perf/-/tree/main/zephyr?ref_type=heads)放在 `modules/udp-perf/zephyr`，并扩展 `west.yml`：

```yaml
- name: udp-perf
  path: modules/udp-perf
```

> 译注——外部模块边界：这是官方页面给出的清单片段，不是完整可用的 west 清单。它没有给出 `url` 或远端解析配置，应先按上述项目来源确定仓库地址、版本和实际清单结构；`modules/udp-perf/zephyr` 是外部项目中 Zephyr 集成部分的位置，不是此测试目录自带的代码。已有工作区先核对正在使用的清单，再决定如何加入依赖，不应把片段直接覆盖根清单，也不必重新初始化工作区。

在 `echo_server` 或 `zperf` 使用的配置文件中启用 `UDPPERF`。根据各套测试设置，在 `boards/nucleo_g474re.conf` 中补充 IP 配置：

```kconfig
CONFIG_NET_CONFIG_MY_IPV4_ADDR="192.0.2.1"
CONFIG_NET_CONFIG_PEER_IPV4_ADDR="192.0.2.3"
CONFIG_NET_CONFIG_MY_IPV6_ADDR="2001:db8::1"
CONFIG_NET_CONFIG_PEER_IPV6_ADDR="2001:db8::3"
```

> 译注——文件位置与来源：这里的 `boards/nucleo_g474re.conf` 相对于所选应用目录。例如 [echo_server 的板配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_server/boards/nucleo_g474re.conf) 和 [zperf 的板配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/boards/nucleo_g474re.conf) 是不同文件。当前官方 `samples/net/ethernet/t1s` 目录只有说明文档，实际构建的是下文两个应用；`UDPPERF` 来自外部模块，模块尚未加入时不能把该符号当作 Zephyr 树内固有配置。

## 4. 使用高级回显服务器测试（Echo Server with udp-perf）

使用[高级回显服务器（Echo Server）](P047_高级回显服务器示例.md#sockets-echo-server)和 [udp-perf](https://gitlab.com/network851614/udp-perf/-/tree/main/zephyr?ref_type=heads)。

### 4.1 构建 Nucleo 应用

从已经准备好工具链、依赖及上述配置的 Zephyr 源码根目录，为 Nucleo G474RE 构建：

```sh
west build -p always -b nucleo_g474re samples/net/sockets/echo_server/
```

默认网络配置如下：

```text
Nucleo ip:  192.0.2.1      RPI4: 192.0.2.3
Nucleo ipv6 2001:db8::1      RPI4: 2001:db8::3
```

即 Nucleo 使用 IPv4 `192.0.2.1`、IPv6 `2001:db8::1`；RPI4 使用 IPv4 `192.0.2.3`、IPv6 `2001:db8::3`。构建后的烧录和启动按该板说明执行。

### 4.2 准备 RPI4 主机

将 USB ↔ T1S 转接器插入 RPI4 的 USB 2.0 端口，按原文检查内核并加载驱动：

```sh
uname -a # Linux raspberrypi 6.1.21
cd ~/work/Zephyr/lan867x-linux-driver-2v2/linux-v6.1.21-support
./load.sh
```

> 译注——可移植目录说明：块中的 `~/work/Zephyr/...` 是官方原例的摆放位置，不要求读者建立相同目录。实际操作在 RPI4 的 Linux Bash 中进行，先进入自行取得的 LAN867x 驱动版本目录，再执行其中已有的 `load.sh`；加载驱动需要相应主机权限。`uname -a` 后的内核版本是原例注释，不是本次检测结果。

原文要求在 RPI4 添加通往 Nucleo 的路由，给出的命令为：

```sh
ip -6 route add 2001:db8::1 dev eth0
```

> 译注——路由与接口：原文把它称为默认路由，但命令实际指定目标 `2001:db8::1`，不是 `default`。它使用 `eth0`，下方回显命令却使用 `eth1`；复现时应确认哪一个实际接口连接 T1S 网络，并使地址、路由和命令的接口选择一致。这一配置属于 Linux 主机网络，不是仓库文件。

### 4.3 运行持续测试

在 RPI4 通过 SSH 打开多个独立终端，每个 `while` 循环分别占用一个终端：

```sh
cd ~/work/Zephyr/net-tools $
while :; do ./echo-client -r -i eth1 192.0.2.1; sleep 1; ping -c 3 192.0.2.1; done
while :; do ./echo-client -r -i eth1 2001:db8::1; sleep 1; ping -6 -c 3 2001:db8::1; done
cd ~/work/Zephyr/udp-perf $
while :; do ./target/armv7-unknown-linux-gnueabihf/release/udp-perf client --ip 192.0.2.1 --packets 100 --mode reduced --runs 5; [ $? -ne 0 ] && echo "Error!"; done
```

> 译注——目录和复制修正：上面两条 `cd` 行末的 `$` 是原文遗留的提示符，应在实际执行时去掉。`net-tools` 与 [`udp-perf`](https://gitlab.com/network851614/udp-perf/-/tree/main/zephyr?ref_type=heads) 均为外部工具目录，用读者实际保存的位置替代原例 `~/work/Zephyr/...`。开始循环前应已生成 `echo-client` 和面向 RPI4 的 [`udp-perf`](https://gitlab.com/network851614/udp-perf/-/tree/main/zephyr?ref_type=heads) 可执行文件；`target/armv7-unknown-linux-gnueabihf/release/udp-perf` 指向原例的 ARMv7 Linux 构建产物，并非其他主机架构通用路径。循环持续运行，按 Ctrl+C 结束当前终端中的测试。应观察回显、ping 和程序返回状态，出现 `Error!` 时回查链路、地址与工具构建，不把持续循环本身当作验证通过。

## 5. 使用 zperf 网络流量生成器（zperf Network Traffic Generator）

对应说明见[zperf 网络流量生成器](P097_zperf网络流量生成器示例.md#zperf)。

从 Zephyr 源码根目录为 Nucleo G474RE 构建：

```sh
west build -p always -b nucleo_g474re samples/net/zperf/
```

### 5.1 Zephyr 作为客户端（Client）

下面第一条命令在 Nucleo 的 Zephyr Shell 中执行，第二条在 RPI4 的 Linux Bash 中执行：

```text
zperf udp upload 192.0.2.3 5001 10 1460 10M # -> nucleo shell
iperf -s -l 1460 -u -B 192.0.2.3 -i 1 # -> RPI4
```

> 译注——启动顺序：测试前先让 RPI4 的 iPerf 服务端监听，再从 Nucleo 发起 UDP 上传。原块按设备列举命令，不代表先发客户端、后启动服务端的操作顺序。

### 5.2 Zephyr 作为服务器（Server）

下面第一条命令在 Nucleo 的 Zephyr Shell 中启动下载服务，第二条在 RPI4 的 Linux Bash 中发起客户端传输：

```text
zperf udp download 5001 # -> nucleo shell
iperf -l 1460 -u -c 192.0.2.1 -i 1 -b 10M -p 5001 # -> RPI4
```

通过两端输出检查传输情况。这里的 `iperf` 是原文指定的命令，不能不核对协议版本就直接替换为其他工具。

## 6. 运行多个被测设备（Running More Device Instances）

可以同时使用多个 DUT：

- 调整各设备 `nucleo_g474re.conf` 中的 IP 地址。
- 在对应应用的 `boards/nucleo_g474re.overlay` 中调整 `local-mac-address` 和 `plca-node-id`。

> 译注——源码跟踪：官方 [echo_server 板级 overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_server/boards/nucleo_g474re.overlay) 和 [zperf 板级 overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/boards/nucleo_g474re.overlay) 给出了 LAN865x 连接及物理层冲突避免（Physical Layer Collision Avoidance，PLCA）配置。多节点时分别配置设备身份；这些是官方特定测试板的参数，不能直接作为本仓库其他芯片的接线或驱动结论。


<a id="t1s"></a>
<a id="base-t1s-network-oa-tc6-tests"></a>
<a id="overview"></a>
<a id="prerequisites"></a>
<a id="hw-prerequisites"></a>
<a id="connections-and-ios"></a>
<a id="software-prerequisites"></a>
<a id="testing-and-validation"></a>
<a id="sockets-echo-server-with-udp-perf"></a>
<a id="zperf"></a>
<a id="running-more-device-instances"></a>

[上一章](P124_TSN交换机示例.md) · [返回大纲](大纲.md) · [下一章](P126_DSA分布式交换机架构.md)
