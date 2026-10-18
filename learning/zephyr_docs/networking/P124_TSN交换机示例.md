---
id: learning.zephyr-docs.networking.page-124
title: TSN交换机示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ethernet/tsn-switch/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_TSN交换机示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ethernet/tsn-switch/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例用于测试和调试时间敏感网络交换机（Time-Sensitive Networking Switch，TSN Switch）。

Zephyr 通过分布式交换机架构（Distributed Switch Architecture，DSA）驱动支持交换机设备。建立在 DSA 用户端口上的以太网桥将作为配置交换机的途径，例如配置转发表（Forwarding Database，FDB）、VLAN 等；原文同时说明，这些功能尚未支持。

对于 TSN 协议，目前可以在 DSA 用户端口上启用 gPTP 协议栈，使交换机成为时间感知中继（Time-aware Relay）；Qbv 可以通过管理 API 配置。后续还将支持更多 TSN 协议，并在此示例中启用。

源码位于 [`samples/net/ethernet/tsn-switch`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/tsn-switch)，可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ethernet/tsn-switch/README.rst/..)。

## 2. 前提条件（Requirements）

验证 TSN 交换机至少需要两台支持 TSN、且至少支持 gPTP 的 Linux 主机，分别连接到交换机。

> 译注——环境与结果边界：下文是官方硬件验证示例。Zephyr 构建命令从源码根目录执行；主机侧命令在对应 Linux 主机的 Bash 中执行，需要相应的网络管理、抓包和内核模块权限。块中的 `#` 是原文 root 提示符，输出行也一起保留，不应把整个终端记录当作可执行脚本。接口、IP、MAC 和配置文件按实际测试拓扑确定；本次翻译没有执行这些网络操作。

## 3. 构建、连接与时钟同步（Building, Connecting and Synchronizing）

构建并运行示例：

```sh
west build -b <board to use> samples/net/ethernet/tsn-switch
```

> 译注——目标选择：`<board to use>` 是实际板目标占位符，须选择支持所需 DSA、PTP 时钟及 Qbv 能力的目标。命令完成构建，启动和烧录仍按对应板的说明执行。

把 Linux 主机连接到 TSN 交换机。原文以 NXP i.MX943 EVK 为例：

```text
                      i.MX943 EVK
                  +-----------------+
                  |     bridge0     | gPTP bridge as Master
                  |  IP: 192.0.2.1  |    priority1 246
                  |                 |
                  | swp0(Qbv)  swp1 |
                  +--+----------+---+
                     |          |
             +-------+          +-------+
             |                          |
+------------+-----------+  +-----------+------------+
|          eth0          |  |          eth0          |
| IP:  192.0.2.2         |  | IP:  192.0.2.3         |
| MAC: fa:fa:62:fe:a2:11 |  | MAC: a6:10:52:1d:cb:6d |
+------------------------+  +------------------------+
      Linux Host A                Linux Host B
 gPTP Slave priority1 248    gPTP slave priority1 248
```

拓扑中，交换机的网桥 `bridge0` 地址为 `192.0.2.1`，gPTP 主时钟的 `priority1` 为 `246`。Linux 主机 A、B 分别连接 `swp0`、`swp1`，两台主机的 gPTP 从时钟 `priority1` 都为 `248`。第一块 DSA 用户端口 `swp0` 配置 Qbv 演示功能。

Qbv 的演示门控计划如下：

```text
time cycle 10ms   gate7 6 5 4 3 2 1 0
-----------------------------------------
slot 1 - 2ms:         1 1 1 1 0 1 0 1
slot 2 - 8ms:         1 1 1 1 1 0 0 1
```

> 译注——门控含义：每周期 10 ms，第一时隙 2 ms，第二时隙 8 ms。门（Gate）0 始终打开，门 1 始终关闭，门 2 只在前 2 ms 打开，门 3 只在后 8 ms 打开，其他门始终打开。官方 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/tsn-switch/src/main.c) 中的 `qbv_init()` 设置对应门控列表，并用读取到的 PTP 秒值加 `3` 设置基准时间的秒字段；小于一秒的字段为 `0`。因此这是未来整秒基准，并非精确地从读取时刻再延后 3 秒。

在 Linux 主机配置好 IP 后，可以用 ping 验证三台设备之间的基本通信。

在两台 Linux 主机运行 gPTP，即使用 gPTP 配置文件的 ptp4l，使它们的时间基准与交换机同步：

```text
# ptp4l -i eth0 -m -f gPTP-slave.cfg > /tmp/ptp.log &
# tail -f /tmp/ptp.log
ptp4l[186.753]: rms   25 max   51 freq  -8579 +/-  32 delay  1311 +/-   0
ptp4l[187.752]: rms   19 max   39 freq  -8575 +/-  26 delay  1311 +/-   0
ptp4l[188.752]: rms   30 max   59 freq  -8592 +/-  41 delay  1311 +/-   0
ptp4l[189.752]: rms   17 max   28 freq  -8570 +/-  22 delay  1311 +/-   0
ptp4l[190.752]: rms   23 max   37 freq  -8600 +/-  25 delay  1314 +/-   0
ptp4l[191.752]: rms   24 max   42 freq  -8600 +/-  32 delay  1310 +/-   0
ptp4l[192.752]: rms   30 max   54 freq  -8574 +/-  38 delay  1310 +/-   0
ptp4l[193.753]: rms   25 max   35 freq  -8587 +/-  35 delay  1314 +/-   0
ptp4l[194.752]: rms   27 max   48 freq  -8598 +/-  35 delay  1314 +/-   0
ptp4l[195.752]: rms   26 max   42 freq  -8602 +/-  35 delay  1314 +/-   0
ptp4l[196.752]: rms   25 max   42 freq  -8588 +/-  34 delay  1318 +/-   0
```

> 译注——配置与日志：原文叙述称 `gPTP.cfg`，命令实际读取 `gPTP-slave.cfg`；执行前应准备与命令同名的实际配置文件。`/tmp/ptp.log` 是 Linux 临时日志路径，不是仓库位置。日志中的 `rms`、`max`、`freq`、`delay` 分别对应同步统计中的均方根、最大偏差、频率修正与链路延迟。基本 ping 成功不能替代时间同步状态检查。

## 4. 验证 Qbv 门控功能（Verifying Qbv Function）

使用 Linux 数据包生成器（pktgen）从主机 B 向主机 A 发包，验证 Qbv 功能。

### 4.1 PCP 0：门始终打开

在主机 B 每秒发送一个 VLAN 100、优先级代码点（Priority Code Point，PCP）为 `0` 的包：

```text
# modprobe pktgen
# cd /proc/net/pktgen
# echo "add_device eth0"           > kpktgend_0
# echo "count 0"                   > eth0
# echo "clone_skb 0"               > eth0
# echo "pkt_size 64"               > eth0
# echo "dst_mac fa:fa:62:fe:a2:11" > eth0
# echo "vlan_id 100"               > eth0
# echo "vlan_p 0"                  > eth0
# echo "delay 1000000000"          > eth0
# echo "start" > pgctrl
```

> 译注——执行位置：加载 `pktgen` 后，相关写入在 Linux 提供的 `/proc/net/pktgen` 控制目录中进行；这里不是需要创建的仓库文件夹。`dst_mac` 对应主机 A 的实际接口 MAC。`count 0` 用于连续生成流量，切换到下一组参数前需先停止当前发送。主机 A 的抓包在另一终端执行。

主机 A 捕获数据包。门 0 始终打开，因此可以收到数据：

```text
# tcpdump -i eth0 -e vlan
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:56:12.259668 a6:10:52:1d:cb:6d (oui Unknown) > fa:fa:62:fe:a2:11 (oui Unknown), ethertype 802.1Q (0x8100), length 64: vlan 100, p 0, ethertype IPv4, 169.254.153.102.9 > 0.0.0.0.9: UDP, length 18
13:56:13.259696 a6:10:52:1d:cb:6d (oui Unknown) > fa:fa:62:fe:a2:11 (oui Unknown), ethertype 802.1Q (0x8100), length 64: vlan 100, p 0, ethertype IPv4, 169.254.153.102.9 > 0.0.0.0.9: UDP, length 18
13:56:14.259714 a6:10:52:1d:cb:6d (oui Unknown) > fa:fa:62:fe:a2:11 (oui Unknown), ethertype 802.1Q (0x8100), length 64: vlan 100, p 0, ethertype IPv4, 169.254.153.102.9 > 0.0.0.0.9: UDP, length 18
```

### 4.2 PCP 1：门始终关闭

在主机 B 改为每秒发送一个 VLAN 100、PCP 为 `1` 的包：

```text
# echo "vlan_p 1" > eth0
# echo "start" > pgctrl
```

主机 A 再次抓包。因为门 1 始终关闭，所以收不到这些包：

```text
# tcpdump -i eth0 -e vlan
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
```

> 译注——结果定位：应先确认上一组 PCP 0 测试连通，再判断 PCP 1 被门控阻止；若两组都收不到，应回查接口、目的 MAC、交换机转发和 Qbv 配置，不能把普通链路不通解释为门控正确。

## 5. 验证 Qbv 时间窗口（Verifying Qbv Performance）

继续使用 pktgen 从主机 B 向主机 A 发包，观察接收时间是否落在指定窗口。

### 5.1 PCP 2：2 ms 窗口

在主机 B 每 100 μs 发送一个 VLAN 100、PCP 为 `2` 的包：

```text
# modprobe pktgen
# cd /proc/net/pktgen
# echo "add_device eth0"           > kpktgend_0
# echo "count 0"                   > eth0
# echo "clone_skb 0"               > eth0
# echo "pkt_size 64"               > eth0
# echo "dst_mac fa:fa:62:fe:a2:11" > eth0
# echo "vlan_id 100"               > eth0
# echo "vlan_p 2"                  > eth0
# echo "delay 100000"              > eth0
# echo "start" > pgctrl
```

在主机 A 捕获 100000 个包，检查它们是否落在 2 ms 窗口内。门 2 的时隙为 2 ms，所以数据包只能在此窗口内接收。原文示例结果考虑到一些临界情况，有 `99.98%` 的包位于该窗口：

```text
# tcpdump -i eth0 -j adapter_unsynced --time-stamp-precision nano -tt -e vlan -c 100000 -w pcp2.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
100000 packets captured
101793 packets received by filter
0 packets dropped by kernel
#
#
# tcpdump -r pcp2.pcap --time-stamp-precision nano -tt -n 2>/dev/null | \
awk '
BEGIN{
  period=10000000; win=2000000; off=0;
  win_in=0; win_out=0; total=0;
}
$1 ~ /^[0-9]+\.[0-9]+$/ {
  split($1,a,"."); t=a[1]*1000000000 + (a[2]+0);
  phase = ((t - off) % period + period) % period;
  if (phase < win) win_in++; else win_out++;
  total++;
}
END{
  pct = (total ? (win_in*100.0/total) : 0);
  printf("period=10ms win=2ms off=%dns\n", off);
  printf("total=%d win_in=%d win_out=%d in_win=%.2f%%\n",
         total, win_in, win_out, pct);
}'
period=10ms win=2ms off=0ns
total=100000 win_in=99977 win_out=23 in_win=99.98%
```

### 5.2 PCP 3：8 ms 窗口

在主机 B 改为每 100 μs 发送一个 VLAN 100、PCP 为 `3` 的包：

```text
# echo "vlan_p 3" > eth0
# echo "start" > pgctrl
```

在主机 A 捕获 100000 个包，检查它们是否落在 8 ms 窗口内。门 3 的时隙为 8 ms，数据包只能在该窗口内接收。原文示例结果考虑到一些临界情况，也有 `99.98%` 的包位于窗口内：

```text
# tcpdump -i eth0 -j adapter_unsynced --time-stamp-precision nano -tt -e vlan -c 100000 -w pcp2.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
100000 packets captured
101793 packets received by filter
0 packets dropped by kernel
#
#
# tcpdump -r pcp3.pcap --time-stamp-precision nano -tt -n 2>/dev/null | \
awk '
BEGIN{
  period=10000000; win=8000000; off=2000000;
  win_in=0; win_out=0; total=0;
}
$1 ~ /^[0-9]+\.[0-9]+$/ {
  split($1,a,"."); t=a[1]*1000000000 + (a[2]+0);
  phase = ((t - off) % period + period) % period;
  if (phase < win) win_in++; else win_out++;
  total++;
}
END{
  pct = (total ? (win_in*100.0/total) : 0);
  printf("period=10ms win=8ms off=%dns\n", off);
  printf("total=%d win_in=%d win_out=%d in_win=%.2f%%\n",
         total, win_in, win_out, pct);
}'
period=10ms win=8ms off=2000000ns
total=100000 win_in=99976 win_out=24 in_win=99.98%
```

> 译注——原命令文件名不一致：上一块 PCP 3 的抓包命令仍写 `-w pcp2.pcap`，后面的分析却读取 `pcp3.pcap`。这里为便于对照完整保留原文；实际复现该组测试时，应把写入文件名改为 `pcp3.pcap`，使生成和读取一致，避免读到不存在的文件或旧结果。

> 译注——时间分析条件：两段 awk 按 10 ms 周期取相位，PCP 2 使用起点 `0`、宽度 2 ms，PCP 3 使用起点 2 ms、宽度 8 ms。`adapter_unsynced` 选择网卡提供的时间戳类型，并不自动保证其时间基准与门控基准已经对齐。应先确认设备支持相应时间戳并完成所需同步。原抓包表达式 `vlan` 没有限定 PCP 或目的 MAC，测试中还需排除无关 VLAN 流量。原文的 `99.98%` 只属于所示设置与数据，不能当作任意硬件的保证值。

## 6. 另请参阅（See Also）

- [以太网桥接 API（Ethernet Bridging API）](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html)。
- [PTP 时钟（PTP Clock）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html)。
- [以太网管理库（Ethernet Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html)。


<a id="tsn-switch"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P123_DSA分布式交换机示例.md) · [返回大纲](大纲.md) · [下一章](P125_10BASE-T1S测试示例.md)
